# Auto Reverser — 浏览器自动逆向工具技术文档

## 一、项目概述

### 1.1 项目目标
开发一款桌面级网络请求捕获与逆向分析工具，通过内嵌可交互浏览器实时拦截所有网络请求，帮助安全研究人员和开发者快速理解目标网站的数据交互机制、识别 API 接口及加密参数。

### 1.2 已实现核心功能

| 功能 | 状态 | 说明 |
|------|------|------|
| URL 输入与页面加载 | ✅ | 内嵌 BrowserView，支持完整页面渲染 |
| 实时网络请求捕获 | ✅ | 基于真实 CDP，含请求头、响应头、响应体 |
| 请求列表实时展示 | ✅ | 防抖增量渲染，支持过滤与搜索 |
| 请求详情五标签页 | ✅ | 概览 / 请求头 / 参数 / 响应头 / 响应体 |
| 完整响应体获取 | ✅ | `Network.getResponseBody`，自动格式化 JSON |
| 验证码人工介入 | ✅ | 非阻塞导航，捕获在停止前持续进行 |
| 浏览器面板拖拽缩放 | ✅ | 上下拖拽调整高度，折叠/展开切换 |
| 左右面板拖拽缩放 | ✅ | 拖动分隔条调整请求列表与详情宽度 |
| 内嵌浏览器导航控制 | ✅ | 前进 / 后退 / 刷新 / 开发者工具 |
| 请求数据一键复制 | ✅ | 复制完整请求 JSON 到剪贴板 |
| 加密参数识别模块 | ⚠️ | 模块已实现，界面集成待完善 |
| 导出报告 | ⚠️ | 按钮已占位，功能待实现 |
| 请求重放 | ⚠️ | 按钮已占位，功能待实现 |

---

## 二、技术架构

### 2.1 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                     桌面应用层（Electron）                        │
│                                                                   │
│  ┌─────────────────────────┐  ┌──────────────────────────────┐   │
│  │     主进程 (Main)        │  │    渲染进程 (Renderer)        │   │
│  │  src/main/index.js      │  │  src/renderer/               │   │
│  │                         │  │    index.html                │   │
│  │  · BrowserView 管理     │  │    scripts/renderer.js       │   │
│  │  · IPC 处理             │  │    styles/main.css           │   │
│  │  · 模块初始化           │  │                              │   │
│  └──────────┬──────────────┘  └──────────────┬───────────────┘   │
│             │    IPC (ipcMain / ipcRenderer)  │                   │
│             └────────────────────────────────┘                   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │               内嵌浏览器（BrowserView）                   │     │
│  │  · 独立渲染进程，与主界面叠加显示                          │     │
│  │  · webContents.debugger 挂载 CDP                        │     │
│  └─────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      核心引擎层                                    │
│                                                                   │
│  ┌───────────────────────┐   ┌──────────────────────────────┐    │
│  │  CDPInterceptor        │   │  APIAnalyzer / Encryption     │    │
│  │  src/core/cdp-         │   │  Analyzer / EncryptionCracker│    │
│  │  interceptor.js        │   │  src/core/                   │    │
│  │                        │   │                              │    │
│  │  Chrome DevTools       │   │  src/analysis/               │    │
│  │  Protocol Network      │   │    ast-analyzer.js           │    │
│  │  Domain                │   │    deobfuscator.js           │    │
│  └───────────────────────┘   └──────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 实际技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| 桌面框架 | Electron 39 | 主/渲染双进程架构 |
| 内嵌浏览器 | Electron BrowserView | 嵌入主窗口，支持完整页面渲染与用户交互 |
| 网络拦截 | Electron `webContents.debugger` + CDP | 真实 CDP 协议，可获取完整响应体 |
| 前端界面 | 原生 HTML + CSS + JS | 无框架，Class 组件式写法 |
| JS 静态分析 | `@babel/parser` + `@babel/traverse` | AST 解析与遍历 |
| 加密识别 | `crypto-js` + 自定义规则 | 常见算法特征检测 |
| 配置存储 | `electron-store` | 本地 JSON 持久化配置 |
| 进程通信 | Electron IPC | `ipcMain.handle` / `ipcRenderer.invoke` + 事件推送 |

---

## 三、核心模块详解

### 3.1 CDPInterceptor（`src/core/cdp-interceptor.js`）

这是请求捕获的核心，通过 Electron 的 `webContents.debugger` API 接入真实的 Chrome DevTools Protocol。

#### 为什么必须使用 CDP 而非 `session.webRequest`

`session.webRequest` 是 Electron 的请求过滤 API，只提供 URL、方法、请求头、响应头和状态码，**从设计上不提供响应体**。要获取完整响应体，必须使用 CDP 的 `Network.getResponseBody` 命令。

#### 初始化流程

```javascript
async attachToBrowserView(browserView) {
    this.cdpDebugger = browserView.webContents.debugger;
    this.cdpDebugger.attach('1.3');

    // 启用 Network domain，配置缓冲区
    await this.cdpDebugger.sendCommand('Network.enable', {
        maxTotalBufferSize: 10 * 1024 * 1024,   // 10MB 总缓冲
        maxResourceBufferSize: 5 * 1024 * 1024   // 5MB 单资源缓冲
    });

    // 监听 CDP 网络事件
    this.cdpDebugger.on('message', async (event, method, params) => {
        switch (method) {
            case 'Network.requestWillBeSent':  // 捕获请求
            case 'Network.responseReceived':   // 获取响应头/状态码
            case 'Network.loadingFinished':    // 获取响应体
            case 'Network.loadingFailed':      // 记录失败
        }
    });
}
```

#### 两阶段响应通知机制

```
Network.responseReceived
  → 立即通知渲染进程（携带状态码和响应头）
  → 请求列表快速显示状态码

Network.loadingFinished
  → 调用 Network.getResponseBody 获取响应体
  → 再次通知渲染进程（携带完整响应体）
  → 详情面板刷新显示响应内容
```

#### 响应体处理逻辑

```javascript
async handleCDPLoadingFinished({ requestId }) {
    const result = await this.cdpDebugger.sendCommand(
        'Network.getResponseBody', { requestId }
    );

    let bodyText = result.body || '';
    if (result.base64Encoded && bodyText) {
        // Base64 解码（处理 gzip 等压缩内容）
        bodyText = Buffer.from(bodyText, 'base64').toString('utf8');
    }

    // 优先解析为 JSON，失败则按 Content-Type 归类
    try {
        request.response.body = JSON.parse(bodyText);
        request.response.bodyType = 'json';
    } catch {
        request.response.body = bodyText;
        request.response.bodyType = detectBodyType(headers); // html/js/css/xml/text
    }
}
```

---

### 3.2 实时流式请求捕获架构

#### 设计背景

旧版采用"一次性批量"模式：等待页面加载完成 → 返回全部请求。这导致：
- 遇到验证码时，页面加载"完成"后返回，之后用户过验证码产生的请求全部丢失
- 用户手动交互产生的请求无法被捕获

#### 当前架构：事件驱动流式推送

```
用户点击"开始分析"
  ↓
主进程：创建 BrowserView，挂载 CDP，立即返回 success
  ↓
主进程注册 CDP 监听器：
  每条新请求 → ipcMain.webContents.send('request-captured', {type:'request', data})
  每条新响应 → ipcMain.webContents.send('request-captured', {type:'response', data})
  ↓
渲染进程：
  ipcRenderer.on('request-captured') → addOrUpdateRequest() → 防抖重绘列表
  ↓
遇到验证码 → 用户手动操作 → 后续请求继续推送 ✅
  ↓
用户点击"停止" → isAnalyzing = false → 停止接收 → 显示总计数
```

#### 增量更新与防抖渲染

```javascript
addOrUpdateRequest({ type, data }) {
    if (type === 'request') {
        // 去重后追加到列表
        if (!this.requests.find(r => String(r.id) === String(data.id))) {
            this.requests.push(data);
        }
    } else if (type === 'response') {
        // 更新对应请求的响应数据
        const idx = this.requests.findIndex(r => String(r.id) === String(data.request.id));
        if (idx >= 0) this.requests[idx] = data.request;
        // 若当前正查看该请求，同步刷新详情面板
        if (this.selectedRequest?.id === data.request.id) {
            this.selectedRequest = data.request;
            this.renderRequestDetail();
        }
    }

    // 立即更新计数徽标
    this.requestCount.textContent = this.requests.length;

    // 200ms 防抖整体重绘列表（避免高频请求连续重绘）
    clearTimeout(this._renderDebounceTimer);
    this._renderDebounceTimer = setTimeout(() => this.renderRequests(), 200);
}
```

---

### 3.3 IPC 通信接口

#### 主进程暴露的 Handle（请求-响应型）

| Channel | 参数 | 返回 | 说明 |
|---------|------|------|------|
| `start-analysis` | `url: string` | `{success, data: {url}}` | 启动分析，立即返回 |
| `stop-analysis` | — | `{success}` | 停止分析，销毁 BrowserView |
| `get-requests` | — | `Request[]` | 获取当前所有请求 |
| `analyze-api` | `requestId` | `AnalysisResult` | 分析指定请求 |
| `analyze-encryption` | `params` | `EncryptionResult` | 分析加密参数 |
| `crack-encryption` | `data, type` | `CrackResult` | 尝试破解加密 |
| `export-script` | `type, data` | `string` | 导出破解脚本 |
| `browser-navigate` | `url` | — | 导航到指定 URL |
| `browser-back` | — | — | 后退 |
| `browser-forward` | — | — | 前进 |
| `browser-refresh` | — | — | 刷新 |
| `browser-devtools` | — | — | 打开 DevTools |
| `show-browser` | — | — | 更新 BrowserView 边界 |

#### 主进程主动推送的事件（单向推送）

| Channel | 数据 | 触发时机 |
|---------|------|---------|
| `request-captured` | `{type: 'request'\|'response', data}` | 每条请求或响应到达时 |
| `browser-url-changed` | `url: string` | 页面导航完成 |
| `browser-loading` | `isLoading: boolean` | 页面开始/停止加载 |
| `browser-load-error` | `message: string` | 导航发生错误 |

---

### 3.4 界面模块（`src/renderer/`）

渲染进程采用单文件 `App` 类管理所有 UI 状态和交互。

#### 请求列表

每个列表项展示三列：
```
[METHOD]  [路径 + 域名 + 类型标签]  [状态码 + 时间]
```

支持功能：
- **类型过滤**：全部 / API（XHR+Fetch）/ XHR / 加密
- **URL 搜索**：实时过滤
- **点击选中**：仅切换 `active` 类，不重绘整个列表

#### 请求详情（五标签页）

| 标签页 | 内容 |
|--------|------|
| 概览 | 完整 URL、方法、状态码、资源类型、域名、路径、时间戳、加密标记 |
| 请求头 | 所有请求头的 KV 表格 |
| 参数 | Query 参数 KV 表格 + POST 请求体（格式化展示） |
| 响应头 | 所有响应头的 KV 表格 |
| 响应体 | 格式化 JSON / 文本代码块，带一键复制按钮 |

响应体的 `bodyType` 状态流转：
```
请求进行中：null
responseReceived 后：'loading'（显示"正在获取..."）
loadingFinished 后：'json' / 'html' / 'javascript' / 'css' / 'xml' / 'text'
不可用时：'unavailable' 或 'binary'
```

#### 可拖拽布局

| 操作 | 效果 |
|------|------|
| 拖动浏览器区域底部手柄 | 上下调整浏览器面板高度（最小 44px，最大 72%） |
| 点击浏览器 toolbar 的 ▼/▶ 按钮 | 折叠/展开浏览器面板 |
| 拖动两面板中间分隔条 | 左右调整请求列表与详情面板宽度（两侧最小 180px） |

---

## 四、项目结构

```
auto-reverser/
├── package.json
├── src/
│   ├── main/
│   │   └── index.js              # 主进程：窗口、BrowserView、IPC、生命周期
│   │
│   ├── renderer/                 # 渲染进程（主界面）
│   │   ├── index.html            # 页面结构
│   │   ├── scripts/
│   │   │   └── renderer.js       # App 类：全部 UI 逻辑
│   │   └── styles/
│   │       └── main.css          # 深色主题样式
│   │
│   ├── core/                     # 核心引擎
│   │   ├── cdp-interceptor.js    # CDP 拦截器（主要使用）
│   │   ├── interceptor.js        # 旧版 webRequest 拦截器（保留备用）
│   │   ├── analyzer.js           # API 接口分析器
│   │   ├── encryption.js         # 加密参数分析
│   │   └── cracker.js            # 加密破解器
│   │
│   ├── analysis/                 # 静态分析模块
│   │   ├── ast-analyzer.js       # Babel AST 分析
│   │   └── deobfuscator.js       # JS 反混淆
│   │
│   └── preload/
│       └── browser-preload.js    # BrowserView 预加载脚本
│
└── docs/
    └── API逆向分析项目文档.md
```

---

## 五、界面布局

```
┌───────────────────────────────────────────────────────────────┐
│  🔍 Auto Reverser                        [导出报告] [⚙️]       │
├───────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────┐    │
│  │  https://example.com/...         [开始分析] / [停止]   │    │
│  │  ☑ 拦截XHR/Fetch请求   ☑ 自动分析加密参数              │    │
│  └───────────────────────────────────────────────────────┘    │
├── 浏览器区域（可上下拖拽调整高度，可折叠）─────────────────────┤
│  ◀ ▶ 🔄  │  https://example.com/...  │  [开发者工具] [▼]      │
│  ┌──────────────────────────────────────────────────────┐     │
│  │                  BrowserView（内嵌浏览器）              │     │
│  └──────────────────────────────────────────────────────┘     │
├── 拖拽手柄 ────────────────────────────────────────────────────┤
│  ┌──────────────────────────┬─┬──────────────────────────┐    │
│  │ 请求列表  [0]             │ │ 请求详情                  │    │
│  │ [全部][API][XHR][加密]   │║│ [概览][请求头][参数]       │    │
│  │ [搜索 URL...]            │ │ [响应头][响应体]            │    │
│  ├──────────────────────────┤ │ [复制][重放]              │    │
│  │ GET  /api/data   200     │ ├───────────────────────────┤    │
│  │      example.com fetch   │ │ URL: https://...          │    │
│  │ POST /api/login  401     │ │ 方法: POST                 │    │
│  │      example.com xhr     │ │ 状态: 200 OK               │    │
│  │ GET  /static/js  200     │ │ 类型: fetch               │    │
│  │  ...                     │ │ 域名: example.com          │    │
│  └──────────────────────────┘ └───────────────────────────┘    │
│    ↑可左右拖拽分隔条↑                                           │
├───────────────────────────────────────────────────────────────┤
│  正在捕获请求，遇到验证码请手动通过后继续...    请求: 42        │
└───────────────────────────────────────────────────────────────┘
```

---

## 六、关键设计决策

### 6.1 使用 Electron BrowserView 而非 Puppeteer

| 方案 | 优点 | 缺点 |
|------|------|------|
| Puppeteer | 控制能力强，接口完善 | 独立进程，无法嵌入界面；用户无法直接操作页面 |
| BrowserView | 嵌入主窗口，用户可直接交互（过验证码、手动操作） | 控制接口较少 |

选择 BrowserView 的核心原因：**支持用户手动干预**（过验证码、登录、触发交互），这对逆向分析场景至关重要。

### 6.2 非阻塞导航设计

```javascript
// ❌ 旧设计：等待页面加载完再返回
await browserView.webContents.loadURL(url, { timeout: 60000 });
await autoScroll(browserView);
return { requests: cdpInterceptor.getAllRequests() }; // 一次性返回

// ✅ 新设计：立即返回，请求持续推送
browserView.webContents.loadURL(url).catch(handleError); // 不 await
return { url }; // 立即返回，请求通过事件实时推送
```

**优势**：
- 验证码出现时用户可以手动通过，后续请求继续被捕获
- 长时间加载页面不会阻塞用户操作
- 用户随时可以手动导航，所有请求均被记录

### 6.3 响应体获取的两阶段通知

`Network.responseReceived` 时只有头部信息，响应体在 `Network.loadingFinished` 后才能通过 `Network.getResponseBody` 获取。设计为两次通知：
1. **第一次**（`responseReceived`）：立即更新状态码，请求列表快速显示响应状态
2. **第二次**（`loadingFinished`）：补充响应体，详情面板自动刷新

---

## 七、依赖说明

### 生产依赖

| 包名 | 版本 | 用途 |
|------|------|------|
| `electron-store` | ^8.1.0 | 本地配置持久化 |
| `uuid` | ^9.0.0 | 生成唯一 ID |
| `@babel/parser` | ^7.23.0 | JS 代码 AST 解析 |
| `@babel/traverse` | ^7.23.0 | AST 遍历 |
| `@babel/types` | ^7.23.0 | AST 节点类型工具 |
| `@babel/generator` | ^7.23.0 | AST 转回代码 |
| `crypto-js` | ^4.2.0 | 加密算法识别与处理 |
| `chrome-remote-interface` | ^0.33.0 | CDP 客户端（分析模块备用） |
| `puppeteer` | ^24.0.0 | 高级浏览器控制（分析模块备用） |

### 开发依赖

| 包名 | 版本 | 用途 |
|------|------|------|
| `electron` | ^39.0.0 | 桌面应用框架 |
| `electron-builder` | ^25.0.0 | 应用打包 |
| `eslint` | ^8.53.0 | 代码规范检查 |
| `jest` | ^29.7.0 | 单元测试 |

---

## 八、待完善功能

### 8.1 导出报告
当前"导出报告"按钮已渲染但处于禁用状态，需实现：
- 将捕获的请求数据导出为 JSON / CSV / HTML 报告
- 调用 `ipcMain.handle('export-script', ...)` 接口已实现，待接入 UI

### 8.2 请求重放
"重放"按钮点击后显示"功能开发中"，需实现：
- 读取选中请求的 URL、方法、请求头、请求体
- 通过 Node.js `https`/`axios` 重新发送请求
- 展示响应结果并与原始响应对比

### 8.3 加密参数 UI 集成
`src/core/encryption.js`、`src/core/cracker.js`、`src/analysis/ast-analyzer.js`、`src/analysis/deobfuscator.js` 已实现核心逻辑，但尚未与界面连接：
- 在请求详情中展示加密参数分析结果
- 提供尝试破解的交互入口
- 导出破解脚本（Python / Node.js）

---

## 九、常见加密特征参考

| 算法 | 特征 | 长度 | 示例 |
|------|------|------|------|
| MD5 | Hex 字符串 | 32 位 | `d41d8cd98f00b204e9800998ecf8427e` |
| SHA1 | Hex 字符串 | 40 位 | `da39a3ee5e6b4b0d3255bfef95601890afd80709` |
| SHA256 | Hex 字符串 | 64 位 | `e3b0c44298fc1c149afbf4c8996fb924...` |
| Base64 | 字母数字 + `/=` | 4 的倍数 | `SGVsbG8gV29ybGQ=` |
| AES | Base64 / Hex | 16/32 字节倍数 | 加密块数据 |
| RSA | Base64 | 128/256 字节 | 公钥加密结果 |

---

## 十、参考资料

- [Chrome DevTools Protocol — Network Domain](https://chromedevtools.github.io/devtools-protocol/tot/Network/)
- [Electron webContents.debugger API](https://www.electronjs.org/docs/latest/api/debugger)
- [Electron BrowserView](https://www.electronjs.org/docs/latest/api/browser-view)
- [Babel AST 文档](https://babeljs.io/docs/en/babel-parser)
- [CryptoJS 文档](https://cryptojs.gitbook.io/docs/)

---

**文档版本**：v2.0  
**创建日期**：2025-03-25  
**最后更新**：2026-03-30
