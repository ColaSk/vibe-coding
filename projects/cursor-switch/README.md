# cursor-switch

本机网关：让 Cursor 使用自己配置的第三方模型。

设计文档：

- [设计方案](docs/design.md)
- [模块抽象](docs/modules.md)
- [实现路线](docs/roadmap.md)
- [协议工具](docs/protocol-tools.md)

## 结构

```text
apps/desktop/     Electron 桌面客户端
server/           Python 后端（FastAPI 控制面 + 领域核心 + 适配器）
tools/            协议提取与抓包调试（开发用）
protocols/        Cursor 协议产物
docs/             设计与路线
```

## 环境

- Python：conda 环境 `cursor-switch`（3.12+）
- Node.js：nvm 的 `v26.13.0`

```bash
conda activate cursor-switch
nvm use 26.13.0
```

## 后端

```bash
cd projects/cursor-switch
pip install -e .
pip install pytest pytest-asyncio

cursor-switch-server --host 127.0.0.1 --port 8787
# 或
PYTHONPATH=server python -m cursor_switch.control.main --host 127.0.0.1 --port 8787
```

健康检查：

```bash
curl http://127.0.0.1:8787/healthz
```

测试：

```bash
PYTHONPATH=. pytest
```

## 桌面客户端

默认启动 **Electron 客户端**（不是浏览器页）。主进程会探活/拉起本机控制面。

```bash
cd apps/desktop
nvm use 26.13.0
# 若 electron 二进制下载失败，可用国内镜像：
# ELECTRON_MIRROR=https://cdn.npmmirror.com/binaries/electron/ npm install
npm install
npm start
# 等同于 npm run desktop / npm run dev
```

仅调试 Vite 页面（可选）：

```bash
npm run web
```

## 打包（macOS / Windows）

打包产物 = Electron 壳 + PyInstaller 冻结的控制面 sidecar。

```bash
# 1) 冻结后端（在仓库根目录，需已 conda activate cursor-switch）
bash packaging/build-server.sh
# Windows: powershell -ExecutionPolicy Bypass -File packaging/build-server.ps1

# 2) 打桌面安装包（在 apps/desktop）
cd apps/desktop
npm install
npm run dist:mac   # → release/*.dmg / *.zip
npm run dist:win   # → release/*-setup.exe（需在 Windows 上执行）
```

说明：

- 开发模式仍用本机 Python（`python -m cursor_switch.control.main`）
- 安装包内 sidecar 路径：`resources/cursor-switch-server/cursor-switch-server[.exe]`
- 后端打包在中性目录完成（mac/linux：`/tmp/cursor-switch-build`；Windows：`%SystemDrive%\cursor-switch-build`），并用 micromamba 拉起隔离 Python 3.12，避免二进制嵌入本机用户路径；构建结束会扫描并拒绝含 `/Users/` 或 `/home/` 的产物
- CI：推送 `v*` tag 触发 `.github/workflows/release.yml`（macos + windows 矩阵）
- 当前 CI 产物为未公证/未签名构建；分发前可自行补签名与公证

界面：暗色 VS Code token、左侧导航卡片、标题栏拖拽区、卡片/按钮控件。

## 接入 Cursor

1. 启动桌面客户端（`apps/desktop` 下 `npm start`），确认控制面健康。
2. 打开 **数据概览 / Cursor**，点 **初始化 CA**，再按页面里的命令把证书装进系统信任（macOS 需 `sudo`）。装完后 CA 状态应变为 `ready`。
3. 在 **Cursor** 页添加模型：协议、服务地址、API Key、模型名称；保存后点 **测试**，确认上游可通。
4. 点 **开启接管**。服务会：
   - 启动本机 HTTPS 代理（只劫持 `*.cursor.sh`）
   - 写入 Cursor 的 `User/settings.json`：`http.proxy` / `http.proxySupport=on` 等
5. **完全退出并重启 Cursor**，新开一个对话；在模型列表里手动选你配置的模型（不要用 Auto）。
6. Tab 补全仍转发官方；关掉接管会清掉上述 proxy 设置并停代理。

证书路径默认：`~/.cursor-switch/ca/ca.crt`。
