"""Debug capture proxy for Cursor official API traffic."""

from __future__ import annotations

import base64
import json
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

from tools.protocol_capture.store import CaptureStore

OFFICIAL = "https://api2.cursor.sh"

UI = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <title>cursor-switch protocol capture</title>
  <style>
    body { font-family: ui-sans-serif, system-ui; margin: 24px; background: #111; color: #eee; }
    a { color: #9cf; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border-bottom: 1px solid #333; padding: 8px; text-align: left; font-size: 14px; }
    pre { background: #1b1b1b; padding: 12px; overflow: auto; }
  </style>
</head>
<body>
  <h1>protocol capture</h1>
  <p>把 Cursor 代理指到本服务，或对本机控制面路径做对照抓包。固定上游：api2.cursor.sh</p>
  <div id="list">loading…</div>
  <h2>详情</h2>
  <pre id="detail">选择一行查看</pre>
  <script>
    async function load() {
      const rows = await fetch('/api/exchanges').then(r => r.json());
      const root = document.getElementById('list');
      if (!rows.length) { root.textContent = '暂无记录'; return; }
      root.innerHTML = '<table><thead><tr><th>id</th><th>method</th><th>path</th><th>status</th></tr></thead><tbody>' +
        rows.map(r => `<tr data-id="${r.id}"><td>${r.id}</td><td>${r.method}</td><td>${r.path}</td><td>${r.status_code}</td></tr>`).join('') +
        '</tbody></table>';
      root.querySelectorAll('tr[data-id]').forEach(tr => tr.onclick = async () => {
        const detail = await fetch('/api/exchanges/' + tr.dataset.id).then(r => r.json());
        document.getElementById('detail').textContent = JSON.stringify(detail, null, 2);
      });
    }
    load();
    setInterval(load, 3000);
  </script>
</body>
</html>
"""


def create_capture_app(db_path: Path) -> FastAPI:
    store = CaptureStore(db_path)

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        try:
            yield
        finally:
            store.close()

    app = FastAPI(title="cursor-switch-protocol-capture", lifespan=lifespan)

    @app.get("/", response_class=HTMLResponse)
    async def index() -> str:
        return UI

    @app.get("/api/exchanges")
    async def list_exchanges() -> list[dict[str, object]]:
        return [
            {
                "id": item.id,
                "created_at": item.created_at,
                "method": item.method,
                "path": item.path,
                "status_code": item.status_code,
            }
            for item in store.list()
        ]

    @app.get("/api/exchanges/{exchange_id}")
    async def get_exchange(exchange_id: int) -> dict[str, object]:
        item = store.get(exchange_id)
        if item is None:
            return {"error": "not found"}
        return {
            "id": item.id,
            "created_at": item.created_at,
            "method": item.method,
            "path": item.path,
            "status_code": item.status_code,
            "request_headers": item.request_headers,
            "request_body_b64": base64.b64encode(item.request_body).decode("ascii"),
            "response_headers": item.response_headers,
            "response_body_b64": base64.b64encode(item.response_body).decode("ascii"),
        }

    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
    async def forward(full_path: str, request: Request) -> Response:
        body = await request.body()
        headers = {
            key: value
            for key, value in request.headers.items()
            if key.lower() not in {"host", "content-length", "transfer-encoding"}
        }
        path = "/" + full_path
        if request.url.query:
            path = f"{path}?{request.url.query}"
        target = f"{OFFICIAL}{path}"
        async with httpx.AsyncClient(timeout=60.0, follow_redirects=False) as client:
            upstream = await client.request(
                request.method,
                target,
                headers=headers,
                content=body,
            )
        store.add(
            method=request.method,
            path=path,
            request_headers=json.dumps(dict(request.headers)),
            request_body=body,
            status_code=upstream.status_code,
            response_headers=json.dumps(dict(upstream.headers)),
            response_body=upstream.content,
        )
        return Response(
            content=upstream.content,
            status_code=upstream.status_code,
            headers={
                key: value
                for key, value in upstream.headers.items()
                if key.lower() not in {"transfer-encoding", "content-encoding", "content-length"}
            },
            media_type=upstream.headers.get("content-type"),
        )

    return app
