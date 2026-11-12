"""Local CA and routing rules."""

import asyncio
from pathlib import Path

import pytest

from cursor_switch.adapters.local_access.ca import CaManager, CaState
from cursor_switch.adapters.local_access.proxy import CursorProxy, ProxyTrafficMode
from cursor_switch.adapters.local_access.routing import (
    is_cursor_host,
    should_route_locally,
)


def test_ca_generate_and_load(tmp_path: Path) -> None:
    manager = CaManager(tmp_path / "ca")
    assert manager.state() is CaState.MISSING
    assert manager.initialize() in {CaState.UNTRUSTED, CaState.READY}
    loaded = manager.load()
    assert b"BEGIN CERTIFICATE" in loaded.cert_pem
    leaf_cert, leaf_key = manager.issue_server_cert("api2.cursor.sh")
    assert b"BEGIN CERTIFICATE" in leaf_cert
    assert b"BEGIN RSA PRIVATE KEY" in leaf_key or b"BEGIN PRIVATE KEY" in leaf_key
    assert manager.install_command()


def test_cursor_host_and_local_routing() -> None:
    assert is_cursor_host("api2.cursor.sh")
    assert is_cursor_host("repo42.cursor.sh")
    assert not is_cursor_host("example.com")
    assert should_route_locally("/aiserver.v1.NetworkService/IsConnected")
    assert should_route_locally("/aiserver.v1.BidiService/BidiAppend")
    assert not should_route_locally("/aiserver.v1.AiService/StreamCpp")
    assert not should_route_locally("/unknown")


def test_passthrough_is_default_mode(tmp_path: Path) -> None:
    proxy = CursorProxy(CaManager(tmp_path / "ca"))
    assert proxy.mode is ProxyTrafficMode.PASSTHROUGH
    proxy.set_mode(ProxyTrafficMode.INTERCEPT)
    assert proxy.status.mode is ProxyTrafficMode.INTERCEPT


def test_traffic_ring_buffer(tmp_path: Path) -> None:
    from cursor_switch.adapters.local_access.proxy import TrafficEvent

    proxy = CursorProxy(CaManager(tmp_path / "ca"), traffic_limit=2)
    proxy.record(
        TrafficEvent(
            ts=1.0,
            event="connect_open",
            host="api2.cursor.sh",
            port=443,
            mode="passthrough",
            cursor_host=True,
        )
    )
    proxy.record(
        TrafficEvent(
            ts=2.0,
            event="connect_close",
            host="api2.cursor.sh",
            port=443,
            mode="passthrough",
            cursor_host=True,
            bytes_up=10,
            bytes_down=20,
        )
    )
    proxy.record(
        TrafficEvent(
            ts=3.0,
            event="connect_open",
            host="example.com",
            port=443,
            mode="passthrough",
            cursor_host=False,
        )
    )
    events = proxy.traffic(limit=10)
    assert len(events) == 2
    assert events[0]["host"] == "api2.cursor.sh"
    assert events[1]["host"] == "example.com"


@pytest.mark.asyncio
async def test_proxy_reads_chunked_request_body(tmp_path: Path) -> None:
    proxy = CursorProxy(CaManager(tmp_path / "ca"))
    raw = (
        b"POST /aiserver.v1.BidiService/BidiAppend HTTP/1.1\r\n"
        b"Host: api2.cursor.sh\r\n"
        b"Transfer-Encoding: chunked\r\n"
        b"\r\n"
        b"5\r\nhello\r\n"
        b"6\r\n world\r\n"
        b"0\r\n\r\n"
    )
    reader = asyncio.StreamReader()
    reader.feed_data(raw)
    reader.feed_eof()
    method, path, headers, body = await proxy._read_http_request(reader)
    assert method == "POST"
    assert path.endswith("/BidiAppend")
    assert headers.get("transfer-encoding") == "chunked"
    assert body == b"hello world"
