# 知乎 PC 作者主页 —— zse-ck / unhuman 验证结论

> 验证日期：2026-10-21
> 样本 URL：`https://www.zhihu.com/people/yunhanfantuo`（页面标题「安邑生 - 知乎」）
> 运行时：Python 3.12、`curl_cffi==0.10.0`（最高 impersonate `chrome133a`）、`playwright==1.61.0`
>
> 时效性：知乎会轮换 `zse-ck/v4/<hash>.js` 与评分模型。脚本地址必须从 403 页现取，不要写死。超过约一个月或看到新的挑战形态，按下节流程重跑对照。
>
> 本文只记录公开站点行为与可复现步骤，不含任何内部仓库、模块或机器路径。

---

## 目录

1. 结论速览
2. 验证范围
3. 两道独立的门
4. 为什么只有 Chrome Blink 算出的 ck 可用
5. 环境准备
6. 复现流程（逐步）
7. 通过判定
8. 实测对照表
9. 被证伪的方案
10. 未完成项

---

## 1. 结论速览

**作者详情主页可以不登录打开。** HTTP 走 `curl_cffi` impersonate `chrome133a`；浏览器只用来执行官方 `zse-ck/v4` WASM，算出 `__zse_ck`。不要用浏览器去拉业务 HTML。

2026-10-21 对 `yunhanfantuo` 的通过快照：

| 项 | 值 |
|---|---|
| HTTP | `200` |
| `<title>` | `安邑生 - 知乎` |
| 是否跳转 unhuman | 否 |
| `d_c0` cookie | 已下发 |
| `followerCount` | 10634 |
| `voteupCount` | 114820 |
| `favoritedCount` | 27115 |
| `zvideoCount` | 0 |
| `answerCount` | 616 |
| `articlesCount` | 39 |

| 维度 | 结论 |
|---|---|
| 数据入口 | people HTML 的 `script#js-initialData`，不是 `/api/v4/members/` |
| 第一道门 | 403 HTML：`meta#zh-zse-ck` + `static.zhihu.com/zse-ck/v4/<hash>.js` |
| `__zse_ck` 形态 | 成功值 `005_` + 128 字符（总长 132）；浏览器 cookie 完整值再拼 `'-'+meta`，约 261 |
| 第二道门 | 形态合法后 302 `/account/unhuman?type=U4E3Z1` |
| U4E3Z1 | 登录墙诱饵，不是验证码；服务端校验 Blink 环境摘要 |
| 过第二道门 | 必须在 **Google Chrome 或 Playwright Chrome for Testing** 里跑官方 WASM |
| 开源 Chromium / Node / jsdom / sdenv | 能写出 `005_`，随后一定 U4E3Z1 |
| HTTP 指纹 | `chrome133a` + UA `Chrome/133.0.0.0`；`chrome131` / `chrome124` 会 JSON 40362 |
| Playwright 职责 | 只算 ck，路由拦截，不访问外网 |
| 部署约束 | 无系统 Chrome、无 Node 时，安装 Playwright 的 **chrome**（Chrome for Testing），不要只装 chromium |
| `zse-ck/v4` ≠ `x-zse-96` | 前者写 cookie；后者是 web API 签名，前缀 `2.0_` |
| 动态接口 | `/api/v3/moments/.../activities` 仍 10003，与主页开门无关 |

**一句话**：知乎把「cookie 长得像」和「digest 是不是 Chrome Blink 算出来的」拆成两道门。Node 和开源 Chromium 只能开第一道。

---

## 2. 验证范围

只验证 PC 作者详情首页：

| 做 | 不做 |
|---|---|
| `GET https://www.zhihu.com/people/{token}` | 回答 / 文章 / 想法等 tab 列表 |
| 解析 SSR `js-initialData` | 把 `/api/v4/members/{token}` 当产品路径 |
| 不登录 | 用浏览器当 HTTP 客户端去拉页面 |

`/api/v4/members/` 返回 REST JSON，字段是 snake_case（`follower_count`）。页面 SSR 字段是 camelCase（`followerCount`）。两条链路不是同一份数据。真实 Chrome 无痕窗口可以不登录打开该主页。

H5 侧已验证、PC 同样成立的 Client Hints 规则：`User-Agent`、`sec-ch-ua-mobile`、`sec-ch-ua-platform` 必须一致。PC 用桌面 UA + `sec-ch-ua-mobile: ?0` + `sec-ch-ua-platform: "macOS"`。不要把 Android UA 和 macOS Client Hints 混在一起。`curl_cffi` impersonate 会自己带这些头，**不要再手动覆盖**。

---

## 3. 两道独立的门

### 3.1 第一道：zse-ck/v4

无 `__zse_ck` 或 ck 非法时，people 返回 **403 HTML**，页面里有：

```html
<meta id="zh-zse-ck" content="<挑战盐>">
<script src="https://static.zhihu.com/zse-ck/v4/<hash>.js"></script>
```

脚本是 TinyGo 0.31.2 编出的 WASM + 嵌套 JSVMP。跑成功后写 cookie `__zse_ck`，前缀必须是 `005_`。

这一层只认 **形态**。Node、MiniRacer、开源 Chromium 都能做出 `005_`。

### 3.2 第二道：U4E3Z1

带上形态合法的 `005_` 再打 people。若 digest 不是 Chrome Blink 环境：

```
HTTP/1.1 302
Location: https://www.zhihu.com/account/unhuman?type=U4E3Z1&need_login=true&session=<hex>&next=/signin
```

页面文案像登录墙（前端有 `requireVerified:!1`），不是 captcha。

```
GET /api/v4/anticrawl/new_captcha_appeal?session=<hex>
```

可以返回 `block_level: 0`，**不能**清掉 people 的 302。

### 3.3 错误码

| 现象 | 含义 |
|---|---|
| HTML 403，正文含 `zse-ck` | 缺合法 `__zse_ck` |
| cookie 以 `001_` 开头 | 环境不完整，WASM 没跑出成功态 |
| 302 `type=U4E3Z1` | ck 形态对，Blink digest 不对 |
| JSON `error.code = 40362` | TLS/JA3 或请求头与 impersonate 不一致 |
| JSON `error.code = 40353` | 后续接口仍落在 unhuman 会话 |
| JSON `error.code = 10003` | 缺 `x-zse-93` / `x-zse-96` |
| `ImpersonateError`（`chrome150`） | `curl_cffi` 0.10.0 最高只到 `chrome133a` |

---

## 4. 为什么只有 Chrome Blink 算出的 ck 可用

官方 WASM 会采集宿主特征做 digest，至少包括：

- canvas / WebGL / Audio
- `Error.stack` 形态
- `window === globalThis`
- 有无 Node 全局（`process` / `fs` / `Buffer`）
- 浏览器品牌：`Google Chrome` 或 Chrome for Testing，不是开源 Chromium

因此：

| 算 ck 的宿主 | 第一道门 | 第二道门 |
|---|---|---|
| 系统 Google Chrome | 过 | 过 |
| Playwright `install chrome`（Chrome for Testing） | 过 | 过 |
| Playwright `install chromium`（开源 Chromium） | 过 | U4E3Z1 |
| `chromium_headless_shell` | 过或启动失败 | U4E3Z1 |
| Node / MiniRacer / JSDOM / happy-dom / sdenv | 过 | U4E3Z1 |

没有现成 npm/pip 包能完整模仿这套 Blink 宿主。`sdenv` 面向瑞数；Camoufox 是 Gecko。

`zse-ck/v4` **不生成** `x-zse-96`。Web API 签名是另一套：

```
zse93   = "101_3_3.0"
source  = [zse93, pathname + search, d_c0].filter(Boolean).join("+")
x-zse-93 = zse93
x-zse-96 = "2.0_" + encrypt(md5(source))
```

移动端常见的 `1.0_` 签名不能签 PC web 接口。主页开门不需要 `x-zse-96`。

---

## 5. 环境准备

### 5.1 Python 包

```bash
pip install 'curl_cffi==0.10.0' 'playwright==1.61.0'
python -m playwright install chrome
```

必须装 **chrome**（Chrome for Testing）。只执行 `playwright install chromium` 会得到开源 Chromium，后续一定 U4E3Z1。

Playwright ≥ 1.49 在 `launch(headless=True)` 时默认找 `chromium_headless_shell`。线上通常没装这个变体，会报 `Executable doesn't exist`。复现时用 `executable_path` 指向完整 Chrome for Testing，并加 `--headless=new`。

### 5.2 如何找到 Chrome for Testing

按下面优先级挑可执行文件，**不要**用系统安装的 Google Chrome，也**不要**用 `headless_shell`：

1. 二进制文件名是 `Google Chrome for Testing`
2. 路径中含 `chrome-linux64` / `chrome-mac-arm64` / `chrome-win64`
3. Playwright 缓存目录下 `chrome-*` 频道的 `chrome` / `chrome.exe`
4. 开源 `Chromium` 仅作对照（预期 U4E3Z1）

缓存根目录（Playwright 官方约定，按操作系统取其一）：

- 环境变量 `PLAYWRIGHT_BROWSERS_PATH`
- macOS：`$HOME/Library/Caches/ms-playwright`
- Linux：`$HOME/.cache/ms-playwright`
- 部分容器镜像：`/ms-playwright`

### 5.3 固定指纹（必须一致）

```
User-Agent:
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36

curl_cffi impersonate: chrome133a
视口: 1440 × 900
locale: zh-CN
timezone: Asia/Shanghai
```

不要再手动设置 `sec-ch-ua*`，交给 impersonate。

---

## 6. 复现流程（逐步）

全程同一个 `curl_cffi.requests.Session`。浏览器进程不算业务请求。

### 第 1 步：打开 people（hop1）

```python
from curl_cffi import requests as cf

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
)
TOKEN = "yunhanfantuo"
URL = f"https://www.zhihu.com/people/{TOKEN}"

session = cf.Session(impersonate="chrome133a", timeout=20)
hop1 = session.get(URL, allow_redirects=False)
html = hop1.text or ""
print(hop1.status_code, hop1.headers.get("Location") or hop1.headers.get("location") or "")
```

预期：`403`，正文含 `zh-zse-ck` 和 `zse-ck/v4`。若已经是 `200` 且有 `js-initialData`，跳到第 6 步。

### 第 2 步：从 403 页取出挑战

```python
import re

meta = re.search(
    r'<meta[^>]+id=["\']zh-zse-ck["\'][^>]+content=["\']([^"\']+)["\']',
    html, re.I,
) or re.search(
    r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+id=["\']zh-zse-ck["\']',
    html, re.I,
)
script = re.search(
    r'src=["\'](https://static\.zhihu\.com/zse-ck/v4/[^"\']+)["\']',
    html, re.I,
)
assert meta and script, "403 页缺少挑战 meta 或脚本"
js = session.get(script.group(1), allow_redirects=False)
script_bytes = js.content
print("meta_len", len(meta.group(1)), "script_bytes", len(script_bytes))
```

脚本体积约 500KB 量级。hash 每次以页面为准。

### 第 3 步：用 Chrome for Testing 执行官方 WASM

浏览器 **不得**访问知乎外网。用 `page.route("**/*")`：

- URL 含 `zhihu.com/people/` → fulfill hop1 的 403 HTML
- URL 含 `zse-ck/v4` → fulfill 第 2 步下载的 JS 字节
- 其余 → `abort()`

```python
import os
from playwright.sync_api import sync_playwright

def pick_chrome_for_testing() -> str:
    roots = [
        os.environ.get("PLAYWRIGHT_BROWSERS_PATH") or "",
        os.path.expanduser("~/Library/Caches/ms-playwright"),
        os.path.expanduser("~/.cache/ms-playwright"),
        "/ms-playwright",
    ]
    found = []
    for root in roots:
        if not root or not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [n for n in dirnames if n not in {
                "Frameworks", "Helpers", "Libraries", "resources", "Resources",
            }]
            for name in filenames:
                path = os.path.join(dirpath, name)
                if name == "Google Chrome for Testing" and os.access(path, os.X_OK):
                    return path
                if name in {"chrome", "chrome.exe"} and "headless_shell" not in path:
                    if any(tag in path for tag in (
                        "chrome-linux64", "chrome-mac-arm64", "chrome-win64",
                    )):
                        found.append(path)
    if found:
        return found[0]
    raise RuntimeError("未找到 Chrome for Testing，请先 python -m playwright install chrome")

chrome = pick_chrome_for_testing()
print("browser", chrome)

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=chrome,
        headless=True,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--headless=new",
        ],
        ignore_default_args=["--enable-automation"],
    )
    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        locale="zh-CN",
        timezone_id="Asia/Shanghai",
        user_agent=UA,
    )
    page = context.new_page()
    page.add_init_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        "window.chrome = window.chrome || { runtime: {} };"
    )

    def on_route(route):
        url = route.request.url
        if "zhihu.com/people/" in url:
            route.fulfill(
                status=200,
                content_type="text/html; charset=utf-8",
                body=html.encode("utf-8"),
            )
            return
        if "zse-ck/v4" in url:
            route.fulfill(
                status=200,
                content_type="application/javascript",
                body=script_bytes,
            )
            return
        route.abort()

    page.route("**/*", on_route)
    try:
        page.goto(URL, wait_until="domcontentloaded", timeout=20000)
    except Exception:
        pass
    ck = ""
    for _ in range(50):
        jar = {c["name"]: c["value"] for c in context.cookies()}
        ck = jar.get("__zse_ck") or ""
        if ck.startswith("005_"):
            break
        page.wait_for_timeout(100)
    browser.close()

assert ck.startswith("005_"), ck
print("ck_prefix", ck[:12], "ck_len", len(ck))
```

预期：`ck_len` 为 132 或约 261（含 `'-'+meta`）。前缀必须 `005_`。`001_` 表示 WASM 没跑成功。

对照实验：把 `executable_path` 换成开源 Chromium，后面第 4 步会变成 U4E3Z1。

### 第 4 步：同一 Session 带 ck 再打开（hop2）

```python
session.cookies.set("__zse_ck", ck, domain=".zhihu.com")
hop2 = session.get(URL, allow_redirects=False)
html2 = hop2.text or ""
loc = hop2.headers.get("Location") or hop2.headers.get("location") or ""
print(hop2.status_code, loc[:180], "d_c0", bool(session.cookies.get("d_c0")))
```

预期：`200`，`Location` 为空，`d_c0` 为真。  
失败：`302` 且 `unhuman?type=U4E3Z1`。

### 第 5 步：解析 `js-initialData`

```python
import json

title_m = re.search(r"<title[^>]*>([^<]+)</title>", html2, re.I)
title = title_m.group(1).strip() if title_m else ""
data_m = re.search(
    r'<script id="js-initialData"[^>]*>(.*?)</script>',
    html2, re.S,
)
payload = json.loads(data_m.group(1)) if data_m else {}
users = payload.get("initialState", {}).get("entities", {}).get("users", {})
user = next(iter(users.values())) if users else {}
print({
    "title": title,
    "name": user.get("name"),
    "followerCount": user.get("followerCount"),
    "voteupCount": user.get("voteupCount"),
    "favoritedCount": user.get("favoritedCount"),
    "zvideoCount": user.get("zvideoCount"),
    "answerCount": user.get("answerCount"),
    "articlesCount": user.get("articlesCount"),
    "avatarUrl": bool(user.get("avatarUrl")),
    "gender": user.get("gender"),   # 0 女 / 1 男
    "ipInfo": user.get("ipInfo"),
})
```

页面字段是 camelCase。members REST 的 `follower_count` 不能拿来解析这份 HTML。

### 第 6 步（可选，预期失败）：动态接口

```python
path = f"/api/v3/moments/{TOKEN}/activities?limit=7&desktop=true&ws_qiangzhisafe=0"
resp = session.get("https://www.zhihu.com" + path, allow_redirects=False)
print(resp.status_code, (resp.text or "")[:200])
```

2026-10-21 预期：JSON `error.code = 10003`（缺 web `x-zse-96`）。这不否定主页成功。

---

## 7. 通过判定

同时满足才算主页复现成功：

1. hop2 状态码 `200`（不是 302）
2. `Location` 不含 `unhuman`
3. `<title>` 为 `安邑生 - 知乎`（换 token 则为该作者名 + ` - 知乎`）
4. `js-initialData` 能取出 `name`
5. Session 中有 `d_c0`
6. `__zse_ck` 以 `005_` 开头

样本 `yunhanfantuo` 的数量级应接近第 1 节快照（粉丝、点赞会随时间变，名称不应变）。

---

## 8. 实测对照表

样本均为 `yunhanfantuo`，HTTP 侧同一个 `curl_cffi` Session。日期 2026-10-21。

| 算 ck 的环境 | HTTP impersonate | people 结果 |
|---|---|---|
| 无 ck | 任意 | 403 zse-ck，偶发 cookie `001_` |
| Node / MiniRacer / JSDOM / sdenv 的 `005_` | `chrome133a` | 302 U4E3Z1 |
| 开源 Chromium（Playwright 对应构建）headless | `chrome133a` | 302 U4E3Z1 |
| 开源 Chromium headed | `chrome133a` | 302 U4E3Z1 |
| Chrome for Testing，`--headless=new` | `chrome133a` | **200，安邑生** |
| Chrome for Testing headed | `chrome133a` | **200，安邑生** |
| 系统 Google Chrome + Playwright 算 ck | `chrome133a` | **200，安邑生**（部署环境没有系统 Chrome，只作对照） |
| 合法 ck + `chrome131` / `chrome124` | 对应 impersonate | JSON 40362 |
| 合法 ck + 手写文档头覆盖 impersonate | — | Client Hints 与 UA 不一致 |
| `chrome150` impersonate | — | `ImpersonateError` |
| 标准库 `requests` | — | 无 `d_c0`，过不了 |
| Android 指纹对齐的 VM + `chrome131_android` | — | 40362 |
| 不带 `d_c0` 的 unsigned `/api/v4/members/{token}` | — | 200 JSON，但是另一套字段，不能当主页 |
| 先打站点其它页面拿到的 `d_c0`，再配 Node ck | — | 40362 |
| appeal 接口 `block_level=0` | — | people 仍 302 |

Playwright 启动上踩过的坑：

- `headless=True` 且不传 `executable_path` → 找 `chromium_headless_shell` → 未安装则启动失败
- 必须 `ignore_default_args=["--enable-automation"]`
- 必须 `--disable-blink-features=AutomationControlled`
- 算 ck 时禁止浏览器出网，否则会打到真实 403/登录页，污染 cookie

---

## 9. 被证伪的方案

| 方案 | 结果 |
|---|---|
| 只用 `requests` / `httpx` 仿请求 | 过不了 zse-ck，或随后 40362 |
| 只换 JA3 / impersonate，不跑官方 WASM | hop1 永远 403 zse-ck |
| 自建 Node WASM host | `005_` → U4E3Z1 |
| MiniRacer / V8 | 同上 |
| JSDOM / happy-dom | 同上 |
| sdenv | 瑞数方案，知乎无效；`window.crypto` 还会报错 |
| 把真实 Chrome 的 canvas PNG 喂回 Node | 仍 U4E3Z1 |
| 删掉 Node 的 `process` / `fs`，改 `Function` 返回 `this` | Go WASM 假死（十余秒无 ck） |
| Android UA + 仍是 macOS 的 `sec-ch-ua-*` | Client Hints 不一致 |
| 用 members REST 代替打开页面 | 字段集不同，页面请求链上没有这条接口 |
| 用 appeal 接口清 U4E3Z1 | `block_level=0` 不清 people 302 |
| Playwright 开源 Chromium 当算 ck 环境 | 形态过、U4E3Z1 |
| 让浏览器去发业务 HTTP | 与「页面请求走 curl_cffi」不符，且 headless 品牌更容易被打 |

---

## 10. 未完成项

1. **动态接口 10003**  
   主页成功后 Session 里已有 `d_c0` 和可用的 `__zse_ck`，但  
   `GET /api/v3/moments/{token}/activities?limit=7&desktop=true&ws_qiangzhisafe=0`  
   仍返回 `error.code = 10003`。需要 web 侧 `x-zse-96`（`2.0_`）。主页采集不依赖这一步。

2. **浏览器频道**  
   过 unhuman 的是 Chrome for Testing，不是开源 Chromium。部署侧必须能执行 `python -m playwright install chrome`。

3. **脚本 hash 与 digest 模型**  
   `zse-ck/v4/<hash>.js` 从 403 页现取。若官方 WASM 升级采集项，需要重新确认 Chrome for Testing 是否仍过 U4E3Z1。
