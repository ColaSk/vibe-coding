# Passthrough proxy (layer 1)

## Goal

Enable Cursor takeover without breaking the IDE: traffic is tunneled as-is.

## Behavior

- Default traffic mode: `passthrough`
- Cursor hosts use CONNECT TCP tunnel (no MITM, no local gateway)
- Fixed default proxy port: `8788`
- Passthrough does not require a trusted CA
- Later `intercept` mode re-enables MITM + local routing for protocol work

## Status fields

- `enabled`, `proxy_url`, `proxy_port`, `mode` (`passthrough` | `intercept`)

## Layer 2 — traffic observation

- Passthrough still tunnels bytes unchanged
- Record CONNECT events: host, port, mode, cursor_host, bytes_up/down, opened/closed
- Expose `GET /api/harness/cursor/traffic` (ring buffer) and log lines on the control process
