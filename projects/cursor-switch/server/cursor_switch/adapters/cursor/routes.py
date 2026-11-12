"""HTTP routes that Cursor hits through the local TLS proxy."""

from __future__ import annotations

import asyncio
import json
import logging
from pathlib import Path

from fastapi import APIRouter, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse

from cursor_switch.adapters.cursor.connect import (
    ConnectCode,
    ConnectStreamError,
    decode_frames,
    decode_unary,
    encode_message,
)
from cursor_switch.adapters.cursor.envelope import decode_agent_client_message
from cursor_switch.adapters.cursor.proto_min import (
    BidiAppendRequest,
    decode_bidi_append_request,
    decode_bidi_request_id,
    encode_bidi_append_response,
)
from cursor_switch.adapters.cursor.transport import TransportRoute
from cursor_switch.control.deps import AppServices
import logging
from pathlib import Path

logger = logging.getLogger("cursor_switch.agent_ws")

router = APIRouter(tags=["cursor-gateway"])


def _services(request: Request | WebSocket) -> AppServices:
    return request.app.state.services


def _proto(body: bytes, *, media: str = "application/proto") -> Response:
    return Response(content=body, media_type=media)


@router.post("/aiserver.v1.NetworkService/IsConnected")
async def is_connected() -> Response:
    return _proto(b"")


@router.post("/aiserver.v1.AnalyticsService/BootstrapStatsig")
async def bootstrap_statsig(request: Request) -> Response:
    return Response(
        content=_services(request).telemetry.bootstrap_statsig(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.AiService/AvailableModels")
async def available_models(request: Request) -> Response:
    body = await _services(request).model_catalog.available_models_proto()
    return _proto(body)


@router.post("/agent.v1.AgentService/GetUsableModels")
@router.post("/aiserver.v1.AiService/GetUsableModels")
async def usable_models(request: Request) -> Response:
    body = await _services(request).model_catalog.usable_models_proto()
    return _proto(body)


@router.post("/aiserver.v1.AiService/GetDefaultModel")
async def default_model(request: Request) -> Response:
    body = await _services(request).model_catalog.default_model_proto()
    return _proto(body)


@router.post("/aiserver.v1.AiService/GetDefaultModelForCli")
@router.post("/agent.v1.AgentService/GetDefaultModelForCli")
async def default_model_for_cli(request: Request) -> Response:
    body = await _services(request).model_catalog.default_model_for_cli_proto()
    return _proto(body)


@router.post("/aiserver.v1.AiService/GetDefaultModelNudgeData")
async def default_model_nudge(request: Request) -> Response:
    body = await _services(request).model_catalog.default_model_nudge_proto()
    return _proto(body)


@router.post("/aiserver.v1.AuthService/GetEmail")
async def get_email(request: Request) -> Response:
    return Response(content=_services(request).account.email_json(), media_type="application/json")


@router.post("/aiserver.v1.AuthService/GetUserMeta")
@router.post("/aiserver.v1.DashboardService/GetMe")
@router.post("/aiserver.v1.DashboardService/GetUserProfile")
async def get_me(request: Request) -> Response:
    return Response(content=_services(request).account.me_json(), media_type="application/json")


@router.post("/aiserver.v1.DashboardService/GetTeams")
async def get_teams() -> Response:
    return Response(content=b'{"teams":[]}', media_type="application/json")


@router.post("/aiserver.v1.DashboardService/GetCurrentPeriodUsage")
@router.post("/aiserver.v1.DashboardService/GetUsageLimitStatusAndActiveGrants")
async def usage(request: Request) -> Response:
    return Response(content=_services(request).account.usage_json(), media_type="application/json")


@router.post("/auth/full_stripe_profile")
@router.post("/auth/stripe_profile")
async def stripe_profile(request: Request) -> Response:
    return Response(
        content=_services(request).account.stripe_profile_json(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.AiService/GetServerConfig")
@router.post("/aiserver.v1.ServerConfigService/GetServerConfig")
async def server_config(request: Request) -> Response:
    return Response(
        content=_services(request).account.server_config_json(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.DashboardService/GetUserPrivacyMode")
async def privacy_mode(request: Request) -> Response:
    return Response(
        content=_services(request).account.privacy_mode_json(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.DashboardService/GetEffectiveUserPlugins")
async def plugins(request: Request) -> Response:
    return Response(
        content=_services(request).account.plugins_json(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.AiService/AvailableDocs")
async def docs(request: Request) -> Response:
    return Response(content=_services(request).account.docs_json(), media_type="application/json")


@router.post("/agent.v1.AgentService/UpdateConversationMetadata")
async def update_metadata() -> Response:
    return Response(content=b"{}", media_type="application/json")


@router.post("/aiserver.v1.AiService/KnowledgeBaseList")
async def knowledge_list(request: Request) -> Response:
    return Response(
        content=_services(request).knowledge.list_json(),
        media_type="application/json",
    )


@router.post("/aiserver.v1.AiService/KnowledgeBaseAdd")
async def knowledge_add(request: Request) -> Response:
    raw = await request.body()
    try:
        payload = json.loads(raw.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        payload = {}
    body = _services(request).knowledge.add(
        str(payload.get("title") or "untitled"),
        str(payload.get("content") or ""),
    )
    return Response(content=body, media_type="application/json")


@router.post("/aiserver.v1.AiService/KnowledgeBaseUpdate")
async def knowledge_update(request: Request) -> Response:
    raw = await request.body()
    try:
        payload = json.loads(raw.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        payload = {}
    body = _services(request).knowledge.update(
        str(payload.get("id") or ""),
        str(payload.get("title") or ""),
        str(payload.get("content") or ""),
    )
    return Response(content=body, media_type="application/json")


@router.post("/aiserver.v1.AiService/KnowledgeBaseRemove")
async def knowledge_remove(request: Request) -> Response:
    raw = await request.body()
    try:
        payload = json.loads(raw.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        payload = {}
    body = _services(request).knowledge.remove(str(payload.get("id") or ""))
    return Response(content=body, media_type="application/json")


@router.post("/aiserver.v1.AiService/WriteGitCommitMessage")
async def write_commit_message() -> Response:
    return Response(
        content=json.dumps({"commitMessage": "chore: update"}).encode("utf-8"),
        media_type="application/json",
    )


@router.post("/aiserver.v1.BidiService/BidiAppend")
async def bidi_append(request: Request) -> Response:
    services = _services(request)
    await services.model_index.refresh()
    body = await request.body()
    Path("/tmp/cursor-switch-bidi-last.bin").write_bytes(body)
    try:
        raw = decode_unary(body)
        append_req = decode_bidi_append_request(raw)
    except Exception as exc:  # noqa: BLE001 — keep the live frame for diagnosis
        logging.getLogger("cursor_switch.bidi").exception(
            "BidiAppend decode failed: %s body_len=%s head=%s",
            exc,
            len(body),
            body[:16].hex(),
        )
        return Response(content=str(exc), status_code=400, media_type="text/plain")
    if append_req.data:
        Path("/tmp/cursor-switch-bidi-last.hex").write_text(append_req.data, encoding="utf-8")
    elif append_req.data_binary:
        Path("/tmp/cursor-switch-bidi-last-msg.bin").write_bytes(append_req.data_binary)
    try:
        await services.gateway.handle_bidi_append(append_req)
    except Exception as exc:  # noqa: BLE001 — dump real Cursor failures for diagnosis
        dump = Path("/tmp/cursor-switch-bidi-last-400.bin")
        dump.write_bytes(body)
        logging.getLogger("cursor_switch.bidi").error(
            "BidiAppend 400: %s | data_len=%s data_binary_len=%s request_id=%s seq=%s dump=%s",
            exc,
            len(append_req.data),
            len(append_req.data_binary),
            append_req.request_id,
            append_req.append_seqno,
            dump,
        )
        return Response(content=str(exc), status_code=400, media_type="text/plain")
    return _proto(encode_message(encode_bidi_append_response()))


async def _sse_for_request(request: Request, *, timeout: float = 30.0) -> StreamingResponse:
    services = _services(request)
    raw = decode_unary(await request.body())
    req = decode_bidi_request_id(raw)
    connect_media = "application/connect+proto"
    if not req.request_id:
        return StreamingResponse(
            _error_stream("request_id is required"),
            media_type=connect_media,
            status_code=400,
        )

    handle = await services.gateway.transport.get_or_create(req.request_id)
    route = await handle.wait_route(timeout=timeout)
    if route is TransportRoute.UPSTREAM:
        return StreamingResponse(
            _error_stream("upstream route should be handled by proxy"),
            media_type=connect_media,
            status_code=502,
        )
    if route is TransportRoute.UNKNOWN:
        return StreamingResponse(
            _error_stream("route not ready"),
            media_type=connect_media,
            status_code=504,
        )

    if handle.protocol == "run_inference":
        await services.gateway.transport.ensure_run_ready(req.request_id)

    queue = handle.subscribe()

    async def event_gen():
        while True:
            chunk = await queue.get()
            if chunk is None:
                break
            yield chunk

    return StreamingResponse(
        event_gen(),
        media_type=connect_media,
        headers={
            "Cache-Control": "no-cache",
            "connect-protocol-version": "1",
        },
    )


@router.post("/agent.v1.AgentService/RunSSE")
async def run_sse(request: Request) -> StreamingResponse:
    return await _sse_for_request(request)


@router.post("/aiserver.v1.InferenceService/RunInferenceSSE")
async def run_inference_sse(request: Request) -> StreamingResponse:
    return await _sse_for_request(request, timeout=60.0)


@router.websocket("/agent/v1/run")
async def agent_run_websocket(websocket: WebSocket) -> None:
    """Agent / RunInference WebSocket: hello handshake, then run frames."""
    from cursor_switch.adapters.cursor.agent_ws_frames import (
        WsRunIdentity,
        decode_client_frame,
        encode_hello_frame,
        encode_run_accepted,
        encode_run_end,
        encode_server_message,
    )

    services = _services(websocket)
    await services.model_index.refresh()
    request_id = (
        websocket.headers.get("x-original-request-id")
        or websocket.headers.get("x-request-id")
        or ""
    )
    subprotocols = websocket.headers.get("sec-websocket-protocol", "")
    accepted = None
    if subprotocols:
        accepted = subprotocols.split(",")[0].strip()
    await websocket.accept(subprotocol=accepted or None)
    is_run_inference = "run-inference" in (accepted or "")
    logger.info(
        "agent ws open request_id=%s protocol=%s",
        request_id,
        accepted,
    )
    Path("/tmp/cursor-switch-agent-ws-last.txt").write_text(
        f"request_id={request_id}\nheaders={dict(websocket.headers)}\n",
        encoding="utf-8",
    )

    run_id = ""
    active_request_id = request_id
    seqno = 0
    outbound_task: asyncio.Task[None] | None = None
    ws_out_seq = 0

    async def pump_outbound(handle_request_id: str) -> None:
        nonlocal ws_out_seq
        handle = await services.gateway.transport.get_or_create(handle_request_id)
        queue = handle.subscribe()
        try:
            while True:
                chunk = await queue.get()
                if chunk is None:
                    if run_id:
                        await websocket.send_bytes(
                            encode_run_end(
                                WsRunIdentity(run_id=run_id, request_id=handle_request_id)
                            )
                        )
                    break
                # Strip Connect frame wrapper if present; WS carries raw proto.
                payload = chunk
                frames = decode_frames(chunk)
                if frames and not (frames[0][0] & 0x02):
                    payload = frames[0][1]
                elif frames and (frames[0][0] & 0x02):
                    continue
                # Client SequenceValidator starts at 0.
                seq = ws_out_seq
                ws_out_seq += 1
                out = encode_server_message(
                    run_id=run_id or handle_request_id,
                    sequence=seq,
                    message=payload,
                )
                Path("/tmp/cursor-switch-agent-ws-out.bin").write_bytes(out)
                logger.info(
                    "agent ws out seq=%s bytes=%s head=%s",
                    seq,
                    len(out),
                    out[:24].hex(),
                )
                await websocket.send_bytes(out)
        except Exception:  # noqa: BLE001
            logger.exception("agent ws outbound pump failed")
            return

    try:
        while True:
            message = await websocket.receive()
            if message.get("type") == "websocket.disconnect":
                break
            data = message.get("bytes")
            if data is None and message.get("text") is not None:
                data = str(message["text"]).encode("utf-8")
            if not data:
                continue
            Path("/tmp/cursor-switch-agent-ws-frame.bin").write_bytes(data)
            frame = decode_client_frame(data)
            logger.info(
                "agent ws frame kind=%s request_id=%s bytes=%s head=%s",
                frame.kind,
                active_request_id,
                len(data),
                data[:24].hex(),
            )
            if frame.kind == "hello":
                await websocket.send_bytes(encode_hello_frame())
                continue
            if frame.kind == "run_start":
                identity = frame.identity
                if identity is not None:
                    run_id = identity.run_id
                    if identity.request_id:
                        active_request_id = identity.request_id
                if not active_request_id:
                    await websocket.close(code=1008)
                    return
                handle = await services.gateway.transport.get_or_create(active_request_id)
                if is_run_inference:
                    handle.protocol = "run_inference"
                await services.gateway.transport.mark_local(active_request_id)
                await websocket.send_bytes(
                    encode_run_accepted(
                        identity
                        or WsRunIdentity(run_id=run_id, request_id=active_request_id)
                    )
                )
                if outbound_task is None:
                    outbound_task = asyncio.create_task(pump_outbound(active_request_id))
                continue
            if frame.kind in {"half_close", "cancel_run"}:
                if active_request_id:
                    await services.gateway.transport.close(active_request_id)
                break
            if frame.kind == "client_message" and frame.message:
                if not active_request_id:
                    continue
                seqno += 1
                try:
                    append = decode_agent_client_message(
                        frame.message, request_id=active_request_id, seqno=seqno
                    )
                    logger.info(
                        "agent ws decoded action=%s model=%r text_len=%s",
                        append.action.value,
                        append.model_id,
                        len(append.text),
                    )
                    await services.gateway.handle_bidi_append(
                        BidiAppendRequest(
                            data="",
                            request_id=active_request_id,
                            append_seqno=seqno,
                            data_binary=frame.message,
                        )
                    )
                except Exception as exc:  # noqa: BLE001
                    logger.exception("agent ws client_message error: %s", exc)
    except WebSocketDisconnect:
        pass
    finally:
        if outbound_task is not None:
            outbound_task.cancel()
            try:
                await outbound_task
            except asyncio.CancelledError:
                pass
            except Exception:  # noqa: BLE001
                pass
        logger.info("agent ws close request_id=%s", active_request_id)


async def _error_stream(message: str):
    from cursor_switch.adapters.cursor.connect import encode_error_end_stream

    yield encode_error_end_stream(
        ConnectStreamError(code=ConnectCode.INVALID_ARGUMENT, message=message)
    )
    await asyncio.sleep(0)
