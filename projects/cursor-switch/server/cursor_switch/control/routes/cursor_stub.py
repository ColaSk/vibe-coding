"""Minimal Cursor-facing stubs until the full gateway lands."""

from __future__ import annotations

from fastapi import APIRouter, Response

router = APIRouter(tags=["cursor-stub"])


@router.post("/aiserver.v1.NetworkService/IsConnected")
async def is_connected() -> Response:
    # Empty protobuf body is enough for Cursor's connectivity probe.
    return Response(content=b"", media_type="application/proto")


@router.post("/aiserver.v1.AnalyticsService/BootstrapStatsig")
async def bootstrap_statsig() -> Response:
    return Response(content=b"{}", media_type="application/json")
