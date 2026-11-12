"""Async TLS proxy: passthrough tunnel by default; optional MITM intercept."""

from __future__ import annotations

import asyncio
import logging
import ssl
import time
from collections import deque
from dataclasses import asdict, dataclass
from enum import Enum
from threading import Lock

import httpx

from cursor_switch.adapters.local_access.ca import CaManager
from cursor_switch.adapters.local_access.routing import is_cursor_host, should_route_locally


logger = logging.getLogger("cursor_switch.proxy")


class ProxyTrafficMode(str, Enum):
    PASSTHROUGH = "passthrough"
    INTERCEPT = "intercept"


@dataclass
class ProxyStatus:
    running: bool
    url: str | None
    port: int | None
    mode: ProxyTrafficMode = ProxyTrafficMode.PASSTHROUGH


@dataclass(frozen=True, slots=True)
class TrafficEvent:
    ts: float
    event: str
    host: str
    port: int
    mode: str
    cursor_host: bool
    bytes_up: int = 0
    bytes_down: int = 0
    path: str | None = None
    status: int | None = None
    error: str | None = None


class CursorProxy:
    def __init__(
        self,
        ca: CaManager,
        *,
        backend_host: str = "127.0.0.1",
        backend_port: int = 8787,
        mode: ProxyTrafficMode = ProxyTrafficMode.PASSTHROUGH,
        traffic_limit: int = 500,
    ) -> None:
        self._ca = ca
        self._backend_host = backend_host
        self._backend_port = backend_port
        self._mode = mode
        self._server: asyncio.AbstractServer | None = None
        self._port: int | None = None
        self._cert_cache: dict[str, tuple[str, str]] = {}
        self._traffic: deque[TrafficEvent] = deque(maxlen=traffic_limit)
        self._traffic_lock = Lock()

    @property
    def status(self) -> ProxyStatus:
        running = self._server is not None
        port = self._port
        return ProxyStatus(
            running=running,
            url=None if port is None else f"http://127.0.0.1:{port}",
            port=port,
            mode=self._mode,
        )

    @property
    def mode(self) -> ProxyTrafficMode:
        return self._mode

    def set_mode(self, mode: ProxyTrafficMode) -> None:
        self._mode = mode

    def set_backend(self, host: str, port: int) -> None:
        self._backend_host = host
        self._backend_port = port

    def record(self, event: TrafficEvent) -> None:
        with self._traffic_lock:
            self._traffic.append(event)
        logger.info(
            "proxy %s host=%s:%s mode=%s cursor=%s up=%s down=%s path=%s status=%s err=%s",
            event.event,
            event.host,
            event.port,
            event.mode,
            event.cursor_host,
            event.bytes_up,
            event.bytes_down,
            event.path,
            event.status,
            event.error,
        )

    def traffic(self, *, limit: int = 100) -> list[dict[str, object]]:
        with self._traffic_lock:
            items = list(self._traffic)[-max(0, limit) :]
        return [asdict(item) for item in items]

    def clear_traffic(self) -> None:
        with self._traffic_lock:
            self._traffic.clear()

    async def start(self, requested_port: int = 0) -> ProxyStatus:
        if self._server is not None:
            return self.status
        try:
            self._server = await asyncio.start_server(
                self._handle_client, "127.0.0.1", requested_port
            )
        except OSError:
            if requested_port == 0:
                raise
            logger.warning("proxy port %s unavailable; falling back to ephemeral", requested_port)
            self._server = await asyncio.start_server(self._handle_client, "127.0.0.1", 0)
        sockets = self._server.sockets or []
        self._port = sockets[0].getsockname()[1] if sockets else None
        return self.status

    async def stop(self) -> None:
        if self._server is None:
            return
        self._server.close()
        await self._server.wait_closed()
        self._server = None
        self._port = None

    async def _handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        try:
            request_line = await reader.readline()
            if not request_line:
                return
            line = request_line.decode("latin-1").strip()
            parts = line.split(" ")
            if len(parts) < 2 or parts[0].upper() != "CONNECT":
                writer.write(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
                await writer.drain()
                return
            while True:
                header = await reader.readline()
                if header in {b"\r\n", b"\n", b""}:
                    break

            target = parts[1]
            host, _, port_text = target.partition(":")
            port = int(port_text or "443")
            # Passthrough: byte-for-byte TCP tunnel for every host, including Cursor.
            if self._mode is ProxyTrafficMode.PASSTHROUGH or not is_cursor_host(host):
                await self._tunnel(reader, writer, host, port)
                return

            writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            await writer.drain()
            await self._mitm(reader, writer, host)
        except Exception:
            pass
        finally:
            writer.close()
            try:
                await writer.wait_closed()
            except Exception:
                pass

    async def _tunnel(
        self,
        client_reader: asyncio.StreamReader,
        client_writer: asyncio.StreamWriter,
        host: str,
        port: int,
    ) -> None:
        cursor = is_cursor_host(host)
        self.record(
            TrafficEvent(
                ts=time.time(),
                event="connect_open",
                host=host,
                port=port,
                mode=self._mode.value,
                cursor_host=cursor,
            )
        )
        try:
            remote_reader, remote_writer = await asyncio.open_connection(host, port)
        except Exception as exc:  # noqa: BLE001
            self.record(
                TrafficEvent(
                    ts=time.time(),
                    event="connect_error",
                    host=host,
                    port=port,
                    mode=self._mode.value,
                    cursor_host=cursor,
                    error=str(exc) or type(exc).__name__,
                )
            )
            raise
        client_writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        await client_writer.drain()

        bytes_up = 0
        bytes_down = 0

        async def pipe(
            source: asyncio.StreamReader,
            destination: asyncio.StreamWriter,
            *,
            upward: bool,
        ) -> None:
            nonlocal bytes_up, bytes_down
            try:
                while True:
                    chunk = await source.read(65536)
                    if not chunk:
                        break
                    if upward:
                        bytes_up += len(chunk)
                    else:
                        bytes_down += len(chunk)
                    destination.write(chunk)
                    await destination.drain()
            except Exception:
                pass
            finally:
                destination.close()

        try:
            await asyncio.gather(
                pipe(client_reader, remote_writer, upward=True),
                pipe(remote_reader, client_writer, upward=False),
            )
        finally:
            self.record(
                TrafficEvent(
                    ts=time.time(),
                    event="connect_close",
                    host=host,
                    port=port,
                    mode=self._mode.value,
                    cursor_host=cursor,
                    bytes_up=bytes_up,
                    bytes_down=bytes_down,
                )
            )

    async def _mitm(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        host: str,
    ) -> None:
        cert_file, key_file = self._leaf_paths(host)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        # Cursor may offer h2; our MITM only speaks HTTP/1.1.
        context.set_alpn_protocols(["http/1.1"])
        await writer.start_tls(context)

        # Cursor keeps the CONNECT tunnel open for multiple HTTP/1.1 requests.
        while True:
            request = await self._read_http_request(reader)
            if request is None:
                return
            method, path, headers, body = request
            route_path = path.split("?", 1)[0]
            local = should_route_locally(route_path)
            upgrade = headers.get("upgrade", "").lower() == "websocket"
            if upgrade:
                try:
                    status = await self._forward_websocket(
                        client_reader=reader,
                        client_writer=writer,
                        method=method,
                        path=path,
                        headers=headers,
                        body=body,
                        local=local,
                        host=host,
                    )
                    self.record(
                        TrafficEvent(
                            ts=time.time(),
                            event="websocket",
                            host=host,
                            port=443,
                            mode=self._mode.value,
                            cursor_host=True,
                            bytes_up=len(body),
                            path=f"{method} {route_path}",
                            status=status,
                        )
                    )
                except Exception as exc:  # noqa: BLE001
                    self.record(
                        TrafficEvent(
                            ts=time.time(),
                            event="http_error",
                            host=host,
                            port=443,
                            mode=self._mode.value,
                            cursor_host=True,
                            bytes_up=len(body),
                            path=f"{method} {route_path}",
                            error=str(exc) or type(exc).__name__,
                        )
                    )
                    raise
                return
            if local:
                target = f"http://{self._backend_host}:{self._backend_port}{path}"
            else:
                # Keep the original Cursor host (api2/api3/metrics/…).
                target = f"https://{host}{path}"
            try:
                close_after, status = await self._forward_stream(
                    writer, method, target, headers, body
                )
                self.record(
                    TrafficEvent(
                        ts=time.time(),
                        event="http",
                        host=host,
                        port=443,
                        mode=self._mode.value,
                        cursor_host=True,
                        bytes_up=len(body),
                        path=f"{method} {route_path}",
                        status=status,
                    )
                )
            except Exception as exc:  # noqa: BLE001
                self.record(
                    TrafficEvent(
                        ts=time.time(),
                        event="http_error",
                        host=host,
                        port=443,
                        mode=self._mode.value,
                        cursor_host=True,
                        bytes_up=len(body),
                        path=f"{method} {route_path}",
                        error=str(exc) or type(exc).__name__,
                    )
                )
                raise
            if close_after:
                return

    def _leaf_paths(self, host: str) -> tuple[str, str]:
        cached = self._cert_cache.get(host)
        if cached is not None:
            return cached
        cert_pem, key_pem = self._ca.issue_server_cert(host)
        root = self._ca.dir / "leaf"
        root.mkdir(parents=True, exist_ok=True)
        cert_path = root / f"{host}.crt"
        key_path = root / f"{host}.key"
        cert_path.write_bytes(cert_pem)
        key_path.write_bytes(key_pem)
        paths = (str(cert_path), str(key_path))
        self._cert_cache[host] = paths
        return paths

    async def _read_http_request(
        self, reader: asyncio.StreamReader
    ) -> tuple[str, str, dict[str, str], bytes] | None:
        request_line = await reader.readline()
        if not request_line:
            return None
        method, path, _ = request_line.decode("latin-1").strip().split(" ", 2)
        headers: dict[str, str] = {}
        while True:
            line = await reader.readline()
            if line in {b"\r\n", b"\n", b""}:
                break
            key, _, value = line.decode("latin-1").partition(":")
            headers[key.strip().lower()] = value.strip()
        body = await self._read_body(reader, headers)
        return method, path, headers, body

    async def _read_body(
        self, reader: asyncio.StreamReader, headers: dict[str, str]
    ) -> bytes:
        encoding = headers.get("transfer-encoding", "").lower()
        if "chunked" in encoding:
            chunks: list[bytes] = []
            while True:
                size_line = await reader.readline()
                if not size_line:
                    break
                size_text = size_line.decode("latin-1").strip().split(";", 1)[0]
                if not size_text:
                    continue
                size = int(size_text, 16)
                if size == 0:
                    # Consume trailers until blank line.
                    while True:
                        trailer = await reader.readline()
                        if trailer in {b"\r\n", b"\n", b""}:
                            break
                    break
                chunks.append(await reader.readexactly(size))
                crlf = await reader.readline()
                if crlf not in {b"\r\n", b"\n"}:
                    raise ValueError("invalid chunked body")
            return b"".join(chunks)
        length = int(headers.get("content-length", "0") or "0")
        return await reader.readexactly(length) if length else b""

    async def _forward_websocket(
        self,
        *,
        client_reader: asyncio.StreamReader,
        client_writer: asyncio.StreamWriter,
        method: str,
        path: str,
        headers: dict[str, str],
        body: bytes,
        local: bool,
        host: str,
    ) -> int:
        """Finish a WebSocket upgrade by raw-byte tunneling to local or upstream."""
        if local:
            remote_reader, remote_writer = await asyncio.open_connection(
                self._backend_host, self._backend_port
            )
            host_header = f"{self._backend_host}:{self._backend_port}"
        else:
            context = ssl.create_default_context()
            remote_reader, remote_writer = await asyncio.open_connection(
                host, 443, ssl=context, server_hostname=host
            )
            host_header = host

        request = bytearray()
        request.extend(f"{method} {path} HTTP/1.1\r\n".encode("latin-1"))
        sent_host = False
        for key, value in headers.items():
            if key == "host":
                value = host_header
                sent_host = True
            request.extend(f"{key}: {value}\r\n".encode("latin-1"))
        if not sent_host:
            request.extend(f"host: {host_header}\r\n".encode("latin-1"))
        request.extend(b"\r\n")
        if body:
            request.extend(body)
        remote_writer.write(request)
        await remote_writer.drain()

        status = 101

        async def pipe(
            source: asyncio.StreamReader,
            destination: asyncio.StreamWriter,
            *,
            capture_status: bool = False,
        ) -> None:
            nonlocal status
            try:
                if capture_status:
                    header = await source.readuntil(b"\r\n\r\n")
                    destination.write(header)
                    await destination.drain()
                    first = header.split(b"\r\n", 1)[0].decode("latin-1", errors="replace")
                    parts = first.split(" ", 2)
                    if len(parts) >= 2 and parts[1].isdigit():
                        status = int(parts[1])
                while True:
                    chunk = await source.read(65536)
                    if not chunk:
                        break
                    destination.write(chunk)
                    await destination.drain()
            except Exception:
                pass
            finally:
                destination.close()

        await asyncio.gather(
            pipe(remote_reader, client_writer, capture_status=True),
            pipe(client_reader, remote_writer),
        )
        return status

    async def _forward_stream(
        self,
        writer: asyncio.StreamWriter,
        method: str,
        url: str,
        headers: dict[str, str],
        body: bytes,
    ) -> tuple[bool, int]:
        """Forward one request. Returns (close_after, status_code)."""
        hop_by_hop = {
            "proxy-connection",
            "connection",
            "keep-alive",
            "transfer-encoding",
            "te",
            "trailer",
            "upgrade",
            "host",
            "content-length",
        }
        outbound = {key: value for key, value in headers.items() if key not in hop_by_hop}
        path_only = url.split("?", 1)[0]
        stream_path = path_only.endswith(("/RunSSE", "/RunInferenceSSE"))
        timeout = httpx.Timeout(None if stream_path else 60.0, connect=15.0)
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=False) as client:
            async with client.stream(method, url, headers=outbound, content=body) as response:
                status_code = response.status_code
                status_line = f"HTTP/1.1 {status_code} {response.reason_phrase}\r\n"
                skip = {
                    "transfer-encoding",
                    "content-encoding",
                    "content-length",
                    "connection",
                }
                response_headers = "".join(
                    f"{key}: {value}\r\n"
                    for key, value in response.headers.multi_items()
                    if key.lower() not in skip
                )
                if stream_path:
                    # Chunked streaming so Agent RunSSE is not buffered to completion.
                    head = (
                        status_line
                        + response_headers
                        + "Transfer-Encoding: chunked\r\n"
                        + "Connection: close\r\n\r\n"
                    )
                    writer.write(head.encode("latin-1"))
                    await writer.drain()
                    async for chunk in response.aiter_bytes():
                        if not chunk:
                            continue
                        writer.write(f"{len(chunk):x}\r\n".encode("ascii"))
                        writer.write(chunk)
                        writer.write(b"\r\n")
                        await writer.drain()
                    writer.write(b"0\r\n\r\n")
                    await writer.drain()
                    return True, status_code

                payload = await response.aread()
                head = (
                    status_line
                    + response_headers
                    + f"Content-Length: {len(payload)}\r\n"
                    + "Connection: keep-alive\r\n\r\n"
                )
                writer.write(head.encode("latin-1") + payload)
                await writer.drain()
                return False, status_code

