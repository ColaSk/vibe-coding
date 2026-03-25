# 谷歌浏览器自动逆向工具技术方案

## 一、项目概述

### 1.1 项目目标
开发一款桌面级自动化逆向分析工具，用于自动识别网站API接口、分析请求参数、破解加密参数，帮助安全研究人员和开发者快速理解网站的数据交互机制。

### 1.2 核心功能
- **URL输入与页面加载**：支持用户输入任意网站URL，自动加载并渲染页面
- **接口自动识别**：自动捕获并分析页面加载过程中的所有网络请求
- **数据接口定位**：智能识别列表页数据来源接口
- **参数分析**：解析请求参数结构，识别加密参数
- **加密破解**：针对常见加密算法进行自动化破解

---

## 二、技术架构

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                      桌面应用层 (Electron)                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  URL输入界面  │  │  结果展示界面 │  │  参数配置界面        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      核心引擎层                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Chrome DevTools Protocol                │   │
│  │  (Network、Page、Runtime、Debugger 协议)              │   │
│  └─────────────────────────────────────────────────────┘   │
│                              │                              │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐   │
│  │ 请求拦截引擎  │  │ JS执行引擎   │  │  加密分析引擎   │   │
│  └──────────────┘  └──────────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      分析处理层                              │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐   │
│  │ 接口分类器    │  │ 参数解析器   │  │  加密破解器     │   │
│  └──────────────┘  └──────────────┘  └────────────────┘   │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐   │
│  │ AST分析器    │  │ 混淆还原器   │  │  算法识别器     │   │
│  └──────────────┘  └──────────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      数据存储层                              │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────┐   │
│  │ SQLite数据库 │  │ 文件缓存     │  │  配置存储       │   │
│  └──────────────┘  └──────────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 技术栈选型

| 层级 | 技术选型 | 说明 |
|------|---------|------|
| 桌面框架 | Electron + React/Vue | 跨平台桌面应用，界面开发效率高 |
| 浏览器控制 | Puppeteer / CDP | Chrome DevTools Protocol 协议控制 |
| 网络分析 | Chrome DevTools Protocol Network | 拦截和分析所有网络请求 |
| JS分析 | Babel + AST | JavaScript代码静态分析 |
| 加密识别 | CryptoJS + 自定义规则库 | 常见加密算法识别与破解 |
| 反混淆 | javascript-obfuscator + de4js | JavaScript代码反混淆 |
| 数据存储 | SQLite + LevelDB | 本地数据持久化 |
| 调试器 | Chrome Debugger Protocol | 支持断点调试和变量追踪 |

---

## 三、功能模块详细设计

### 3.1 模块一：URL输入与页面加载

#### 3.1.1 功能描述
用户在主页输入目标网站URL，工具自动启动无头浏览器加载页面。

#### 3.1.2 实现方案

```javascript
// 核心实现伪代码
const puppeteer = require('puppeteer');

async function loadPage(url) {
    const browser = await puppeteer.launch({
        headless: false,
        devtools: true,
        args: ['--auto-open-devtools-for-tabs']
    });
    
    const page = await browser.newPage();
    
    // 启用网络请求监控
    await page.setRequestInterception(true);
    
    // 监听所有网络请求
    page.on('request', request => {
        captureRequest(request);
        request.continue();
    });
    
    // 监听响应
    page.on('response', response => {
        captureResponse(response);
    });
    
    await page.goto(url, { waitUntil: 'networkidle2' });
    
    return { browser, page };
}
```

#### 3.1.3 关键配置
- User-Agent伪装
- Cookie管理
- 代理设置
- 请求头自定义

---

### 3.2 模块二：接口自动识别与分类

#### 3.2.1 功能描述
自动捕获页面加载过程中的所有网络请求，智能识别数据接口。

#### 3.2.2 接口识别策略

**策略一：响应内容分析**
```javascript
// 识别数据接口的特征
function isDataAPI(response) {
    const contentType = response.headers()['content-type'];
    const url = response.url();
    
    // 特征1: JSON响应
    if (contentType && contentType.includes('application/json')) {
        return true;
    }
    
    // 特征2: API路径特征
    const apiPatterns = [
        /\/api\//i,
        /\/v\d+\//i,
        /\/graphql/i,
        /\/query/i,
        /\/list/i,
        /\/data/i
    ];
    
    if (apiPatterns.some(pattern => pattern.test(url))) {
        return true;
    }
    
    return false;
}
```

**策略二：请求参数分析**
```javascript
// 分析请求参数
function analyzeRequestParams(request) {
    const method = request.method();
    const url = new URL(request.url());
    const postData = request.postData();
    
    const params = {
        queryParams: Object.fromEntries(url.searchParams),
        bodyParams: postData ? parsePostData(postData) : {},
        headers: request.headers()
    };
    
    return params;
}
```

**策略三：列表页数据识别**
```javascript
// 识别列表数据接口
async function identifyListAPI(responses) {
    const candidates = [];
    
    for (const response of responses) {
        try {
            const data = await response.json();
            
            // 检查是否包含列表特征
            if (isListData(data)) {
                candidates.push({
                    url: response.url(),
                    data: data,
                    confidence: calculateConfidence(data)
                });
            }
        } catch (e) {}
    }
    
    // 按置信度排序
    return candidates.sort((a, b) => b.confidence - a.confidence);
}

function isListData(data) {
    // 特征1: 数组结构
    if (Array.isArray(data)) return true;
    
    // 特征2: 分页结构
    if (data.list || data.items || data.data) {
        const listField = data.list || data.items || data.data;
        if (Array.isArray(listField)) return true;
    }
    
    // 特征3: 分页参数
    if (data.page || data.pageSize || data.total) return true;
    
    return false;
}
```

#### 3.2.3 接口分类结果

| 分类 | 特征 | 示例 |
|------|------|------|
| 数据接口 | JSON响应，包含列表/分页结构 | /api/list, /graphql |
| 静态资源 | JS/CSS/图片 | .js, .css, .png |
| 认证接口 | 登录/注册相关 | /login, /auth |
| 追踪接口 | 统计/埋点 | /track, /analytics |

---

### 3.3 模块三：加密参数分析

#### 3.3.1 功能描述
识别请求中的加密参数，分析加密算法和加密位置。

#### 3.3.2 加密参数识别

```javascript
// 识别加密参数
function identifyEncryptedParams(params) {
    const encryptedParams = [];
    
    for (const [key, value] of Object.entries(params)) {
        if (isLikelyEncrypted(value)) {
            encryptedParams.push({
                param: key,
                value: value,
                type: detectEncryptionType(value)
            });
        }
    }
    
    return encryptedParams;
}

function isLikelyEncrypted(value) {
    if (typeof value !== 'string') return false;
    
    // Base64特征
    if (/^[A-Za-z0-9+/]+=*$/.test(value) && value.length % 4 === 0) {
        return true;
    }
    
    // Hex特征
    if (/^[a-fA-F0-9]+$/.test(value) && value.length % 2 === 0) {
        return true;
    }
    
    // URL编码特征
    if (/%[0-9A-Fa-f]{2}/.test(value)) {
        return true;
    }
    
    // 长度异常
    if (value.length > 32 && !/\s/.test(value)) {
        return true;
    }
    
    return false;
}

function detectEncryptionType(value) {
    // MD5: 32位hex
    if (/^[a-fA-F0-9]{32}$/.test(value)) return 'MD5';
    
    // SHA1: 40位hex
    if (/^[a-fA-F0-9]{40}$/.test(value)) return 'SHA1';
    
    // SHA256: 64位hex
    if (/^[a-fA-F0-9]{64}$/.test(value)) return 'SHA256';
    
    // Base64
    if (/^[A-Za-z0-9+/]+=*$/.test(value)) return 'Base64';
    
    // AES (通常较长)
    if (value.length > 32 && value.length % 16 === 0) return 'AES';
    
    return 'Unknown';
}
```

#### 3.3.3 加密位置定位

**方法一：全局搜索加密函数**
```javascript
async function locateEncryptionFunction(page, paramName) {
    // 注入监控代码
    await page.evaluateOnNewDocument(() => {
        // Hook常见加密函数
        const originalBtoa = window.btoa;
        window.btoa = function(str) {
            console.log('[ENCRYPT] btoa called with:', str);
            return originalBtoa.call(this, str);
        };
        
        // Hook CryptoJS
        if (window.CryptoJS) {
            const methods = ['MD5', 'SHA1', 'SHA256', 'AES', 'DES'];
            methods.forEach(method => {
                if (window.CryptoJS[method]) {
                    const original = window.CryptoJS[method];
                    window.CryptoJS[method] = function(...args) {
                        console.log(`[ENCRYPT] CryptoJS.${method} called:`, args);
                        return original.apply(this, args);
                    };
                }
            });
        }
    });
}
```

**方法二：断点调试追踪**
```javascript
async function traceEncryption(page, paramName) {
    // 获取所有JS文件
    const scripts = await page.evaluate(() => {
        return Array.from(document.scripts).map(s => s.src);
    });
    
    // 下载并分析JS文件
    for (const scriptUrl of scripts) {
        const scriptContent = await fetchScript(scriptUrl);
        const encryptPatterns = findEncryptionPatterns(scriptContent);
        
        if (encryptPatterns.length > 0) {
            // 设置断点
            await setBreakpoint(page, scriptUrl, encryptPatterns);
        }
    }
}
```

**方法三：AST静态分析**
```javascript
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;

function analyzeEncryptionInJS(code) {
    const ast = parser.parse(code, {
        sourceType: 'module',
        plugins: ['jsx']
    });
    
    const encryptionCalls = [];
    
    traverse(ast, {
        CallExpression(path) {
            const callee = path.node.callee;
            
            // 检测加密函数调用
            if (isEncryptionCall(callee)) {
                encryptionCalls.push({
                    type: 'CallExpression',
                    function: getFunctionName(callee),
                    arguments: path.node.arguments,
                    location: path.node.loc
                });
            }
        },
        
        AssignmentExpression(path) {
            // 检测参数赋值
            if (isParamAssignment(path.node)) {
                encryptionCalls.push({
                    type: 'Assignment',
                    param: getParamName(path.node.left),
                    value: path.node.right,
                    location: path.node.loc
                });
            }
        }
    });
    
    return encryptionCalls;
}
```

---

### 3.4 模块四：加密参数破解

#### 3.4.1 功能描述
根据识别的加密类型，尝试自动破解或提供破解方案。

#### 3.4.2 破解策略

**策略一：已知算法破解**

```javascript
const crypto = require('crypto');

class EncryptionBreaker {
    // Base64解码
    static decodeBase64(str) {
        try {
            return Buffer.from(str, 'base64').toString('utf-8');
        } catch (e) {
            return null;
        }
    }
    
    // MD5破解（彩虹表）
    static async crackMD5(hash) {
        // 常见密码字典
        const commonPasswords = ['123456', 'password', 'admin', ...];
        
        for (const pwd of commonPasswords) {
            const md5 = crypto.createHash('md5').update(pwd).digest('hex');
            if (md5 === hash) {
                return pwd;
            }
        }
        
        // 调用在线彩虹表API
        return await queryOnlineRainbowTable(hash);
    }
    
    // AES解密（需要密钥）
    static decryptAES(encrypted, key, iv) {
        try {
            const decipher = crypto.createDecipheriv('aes-128-cbc', key, iv);
            let decrypted = decipher.update(encrypted, 'base64', 'utf8');
            decrypted += decipher.final('utf8');
            return decrypted;
        } catch (e) {
            return null;
        }
    }
    
    // 时间戳签名破解
    static crackTimestampSignature(params, encrypted) {
        const timestamp = Date.now();
        
        // 尝试不同的签名组合
        const combinations = [
            `${params}&timestamp=${timestamp}`,
            `${timestamp}${params}`,
            `${params}${timestamp}`
        ];
        
        for (const combo of combinations) {
            const hash = crypto.createHash('md5').update(combo).digest('hex');
            if (hash === encrypted) {
                return { algorithm: 'MD5', pattern: combo };
            }
        }
        
        return null;
    }
}
```

**策略二：动态执行获取加密逻辑**

```javascript
async function extractEncryptionLogic(page, paramName) {
    // 方法1: 直接调用加密函数
    const encryptionResult = await page.evaluate((param) => {
        // 尝试找到加密函数
        const encryptFunctions = [
            'encrypt', 'sign', 'signature', 'getToken',
            'generateSign', 'calcSign', 'getSign'
        ];
        
        for (const funcName of encryptFunctions) {
            if (typeof window[funcName] === 'function') {
                return {
                    found: true,
                    functionName: funcName,
                    result: window[funcName](param)
                };
            }
        }
        
        return { found: false };
    }, 'test_param');
    
    return encryptionResult;
}
```

**策略三：JS逆向还原**

```javascript
async function reverseEncryption(jsCode) {
    // 1. 反混淆
    const deobfuscated = await deobfuscateJS(jsCode);
    
    // 2. 提取加密函数
    const encryptFunction = extractEncryptFunction(deobfuscated);
    
    // 3. 分析加密逻辑
    const logic = analyzeEncryptionLogic(encryptFunction);
    
    // 4. 生成Python实现
    const pythonCode = generatePythonCode(logic);
    
    return {
        deobfuscatedCode: deobfuscated,
        encryptFunction: encryptFunction,
        logic: logic,
        pythonImplementation: pythonCode
    };
}

function deobfuscateJS(code) {
    // 常见混淆模式还原
    const patterns = [
        // 十六进制字符串还原
        [/'\\x[0-9a-fA-F]{2}'/g, match => eval(match)],
        // Unicode还原
        [/\\u[0-9a-fA-F]{4}/g, match => eval(`"${match}"`)],
        // 数组混淆还原
        [/_0x[a-fA-F0-9]+\[/g, match => /* 还原数组访问 */]
    ];
    
    let deobfuscated = code;
    patterns.forEach(([pattern, replacement]) => {
        deobfuscated = deobfuscated.replace(pattern, replacement);
    });
    
    return deobfuscated;
}
```

---

## 四、工作流程设计

### 4.1 主流程图

```
┌─────────────┐
│  输入URL    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  加载页面   │◄─────────────┐
└──────┬──────┘              │
       │                     │
       ▼                     │
┌─────────────┐              │
│  拦截请求   │              │
└──────┬──────┘              │
       │                     │
       ▼                     │
┌─────────────┐              │
│  分类请求   │              │
└──────┬──────┘              │
       │                     │
       ▼                     │
┌─────────────┐      ┌───────┴───────┐
│ 是否数据接口│──否──►│  继续监听    │
└──────┬──────┘      └───────────────┘
       │是
       ▼
┌─────────────┐
│  分析参数   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 识别加密参数│
└──────┬──────┘
       │
       ▼
┌─────────────┐      ┌───────┬───────┐
│ 是否有加密  │──否──►│ 输出结果      │
└──────┬──────┘      └───────────────┘
       │是
       ▼
┌─────────────┐
│  定位加密   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  分析算法   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  尝试破解   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  输出结果   │
└─────────────┘
```

### 4.2 详细步骤

#### 步骤1：初始化环境
```javascript
async function initialize() {
    // 1. 启动浏览器
    const browser = await launchBrowser();
    
    // 2. 配置请求拦截
    const page = await configurePage(browser);
    
    // 3. 注入监控脚本
    await injectMonitorScripts(page);
    
    // 4. 初始化数据存储
    const storage = await initStorage();
    
    return { browser, page, storage };
}
```

#### 步骤2：加载并分析页面
```javascript
async function analyzePage(page, url) {
    // 1. 导航到目标页面
    await page.goto(url, { waitUntil: 'networkidle0' });
    
    // 2. 等待动态内容加载
    await page.waitForTimeout(2000);
    
    // 3. 触发滚动加载更多数据
    await autoScroll(page);
    
    // 4. 收集所有请求
    const requests = collectRequests();
    
    return requests;
}
```

#### 步骤3：智能识别数据接口
```javascript
async function identifyDataInterface(requests) {
    // 1. 过滤非数据请求
    const dataRequests = requests.filter(r => isDataAPI(r));
    
    // 2. 分析响应内容
    for (const request of dataRequests) {
        const response = await request.response();
        const data = await response.json();
        
        // 3. 计算数据特征得分
        const score = calculateDataScore(data);
        
        request.dataScore = score;
    }
    
    // 4. 排序并返回最可能的数据接口
    return dataRequests.sort((a, b) => b.dataScore - a.dataScore);
}
```

#### 步骤4：加密参数深度分析
```javascript
async function deepAnalyzeEncryption(page, request) {
    // 1. 提取所有JS文件
    const jsFiles = await extractJSFiles(page);
    
    // 2. 分析每个JS文件
    const analysisResults = [];
    for (const jsFile of jsFiles) {
        const content = await fetchJS(jsFile);
        const analysis = await analyzeJS(content, request);
        analysisResults.push(analysis);
    }
    
    // 3. 合并分析结果
    const encryptionInfo = mergeAnalysisResults(analysisResults);
    
    // 4. 尝试破解
    const crackResult = await attemptCrack(encryptionInfo);
    
    return crackResult;
}
```

---

## 五、关键技术实现

### 5.1 Chrome DevTools Protocol 应用

```javascript
const CDP = require('chrome-remote-interface');

async function useCDP() {
    const client = await CDP();
    const { Network, Page, Debugger, Runtime } = client;
    
    // 启用网络监控
    await Network.enable();
    
    // 启用页面监控
    await Page.enable();
    
    // 启用调试器
    await Debugger.enable();
    
    // 监听网络请求
    Network.requestWillBeSent((params) => {
        console.log('Request:', params.request.url);
        console.log('Method:', params.request.method);
        console.log('Headers:', params.request.headers);
        console.log('PostData:', params.request.postData);
    });
    
    // 监听响应
    Network.responseReceived(async (params) => {
        const { response } = params;
        console.log('Response:', response.url);
        console.log('Status:', response.status);
        console.log('Headers:', response.headers);
        
        // 获取响应体
        const body = await Network.getResponseBody({
            requestId: params.requestId
        });
        console.log('Body:', body);
    });
    
    // 设置断点
    await Debugger.setBreakpointByUrl({
        lineNumber: 100,
        urlRegex: '.*\\.js'
    });
    
    // 监听断点
    Debugger.paused((params) => {
        console.log('Paused at:', params.callFrames[0]);
        // 获取变量值
        Runtime.evaluate({
            expression: 'Object.keys(window)'
        });
    });
}
```

### 5.2 JavaScript AST分析

```javascript
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const t = require('@babel/types');
const generate = require('@babel/generator').default;

class JSAnalyzer {
    constructor(code) {
        this.ast = parser.parse(code, {
            sourceType: 'module',
            plugins: ['jsx', 'typescript']
        });
        this.encryptionFunctions = [];
        this.apiCalls = [];
    }
    
    // 查找加密函数
    findEncryptionFunctions() {
        traverse(this.ast, {
            FunctionDeclaration(path) {
                const name = path.node.id?.name;
                if (this.isEncryptionFunction(name)) {
                    this.encryptionFunctions.push({
                        name: name,
                        params: path.node.params,
                        body: path.node.body,
                        loc: path.node.loc
                    });
                }
            },
            
            VariableDeclarator(path) {
                if (t.isFunctionExpression(path.node.init)) {
                    const name = path.node.id?.name;
                    if (this.isEncryptionFunction(name)) {
                        this.encryptionFunctions.push({
                            name: name,
                            params: path.node.init.params,
                            body: path.node.init.body,
                            loc: path.node.loc
                        });
                    }
                }
            }
        });
        
        return this.encryptionFunctions;
    }
    
    // 查找API调用
    findAPICalls() {
        traverse(this.ast, {
            CallExpression(path) {
                const callee = path.node.callee;
                
                // fetch调用
                if (t.isIdentifier(callee, { name: 'fetch' })) {
                    this.apiCalls.push({
                        type: 'fetch',
                        arguments: path.node.arguments,
                        loc: path.node.loc
                    });
                }
                
                // axios调用
                if (t.isMemberExpression(callee)) {
                    if (callee.object.name === 'axios') {
                        this.apiCalls.push({
                            type: 'axios',
                            method: callee.property.name,
                            arguments: path.node.arguments,
                            loc: path.node.loc
                        });
                    }
                }
                
                // XMLHttpRequest
                if (t.isMemberExpression(callee)) {
                    if (callee.property.name === 'open' || callee.property.name === 'send') {
                        this.apiCalls.push({
                            type: 'xhr',
                            method: callee.property.name,
                            arguments: path.node.arguments,
                            loc: path.node.loc
                        });
                    }
                }
            }
        });
        
        return this.apiCalls;
    }
    
    // 判断是否为加密函数
    isEncryptionFunction(name) {
        const patterns = [
            /encrypt/i, /decrypt/i, /sign/i, /signature/i,
            /hash/i, /encode/i, /decode/i, /cipher/i,
            /crypto/i, /md5/i, /sha/i, /aes/i, /rsa/i
        ];
        
        return patterns.some(pattern => pattern.test(name));
    }
    
    // 提取函数调用关系
    extractCallGraph() {
        const callGraph = new Map();
        
        traverse(this.ast, {
            FunctionDeclaration(path) {
                const functionName = path.node.id?.name;
                const calls = [];
                
                path.traverse({
                    CallExpression(innerPath) {
                        const callee = innerPath.node.callee;
                        if (t.isIdentifier(callee)) {
                            calls.push(callee.name);
                        }
                    }
                });
                
                callGraph.set(functionName, calls);
            }
        });
        
        return callGraph;
    }
}
```

### 5.3 反混淆处理

```javascript
class Deobfuscator {
    constructor(code) {
        this.code = code;
    }
    
    // 字符串数组还原
    decodeStringArray() {
        // 匹配字符串数组定义
        const arrayPattern = /var\s+_0x[a-f0-9]+\s*=\s*\[([^\]]+)\]/;
        const match = this.code.match(arrayPattern);
        
        if (match) {
            const array = eval(`[${match[1]}]`);
            return array;
        }
        
        return null;
    }
    
    // 十六进制字符串还原
    decodeHexStrings() {
        return this.code.replace(
            /'\\x([0-9a-fA-F]{2})'/g,
            (match, hex) => String.fromCharCode(parseInt(hex, 16))
        );
    }
    
    // Unicode转义还原
    decodeUnicode() {
        return this.code.replace(
            /\\u([0-9a-fA-F]{4})/g,
            (match, hex) => String.fromCharCode(parseInt(hex, 16))
        );
    }
    
    // 控制流平坦化还原
    deflattenControlFlow() {
        const ast = parser.parse(this.code);
        
        traverse(ast, {
            WhileStatement(path) {
                // 检测控制流平坦化模式
                const test = path.node.test;
                const body = path.node.body;
                
                if (t.isLiteral(test, { value: true }) || 
                    t.isStringLiteral(test)) {
                    // 提取switch语句
                    const switchStmt = body.body.find(t.isSwitchStatement);
                    if (switchStmt) {
                        // 还原控制流
                        this.reorderStatements(switchStmt);
                    }
                }
            }
        });
        
        return generate(ast).code;
    }
    
    // 完整反混淆流程
    deobfuscate() {
        let result = this.code;
        
        // 1. 十六进制还原
        result = this.decodeHexStrings();
        
        // 2. Unicode还原
        result = this.decodeUnicode();
        
        // 3. 字符串数组还原
        const stringArray = this.decodeStringArray();
        if (stringArray) {
            result = this.replaceStringArrayCalls(result, stringArray);
        }
        
        // 4. 控制流还原
        result = this.deflattenControlFlow();
        
        // 5. 变量重命名
        result = this.renameVariables(result);
        
        return result;
    }
}
```

---

## 六、界面设计

### 6.1 主界面布局

```
┌────────────────────────────────────────────────────────────────┐
│  🔍 谷歌浏览器自动逆向工具                          [—][□][×] │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  URL: https://weibo.com/...                    [开始分析]│  │
│  └──────────────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────────────┤
│  ┌─────────────┬──────────────────────────────────────────┐   │
│  │ 请求列表    │  详情面板                                 │   │
│  ├─────────────┤  ┌────────────────────────────────────┐  │   │
│  │ ○ API请求1  │  │ 请求URL: /api/list                 │  │   │
│  │ ● API请求2  │  │ 请求方法: POST                     │  │   │
│  │ ○ API请求3  │  │ ─────────────────────────────────  │  │   │
│  │ ○ 静态资源  │  │ 请求参数:                          │  │   │
│  │ ○ 静态资源  │  │   page: 1                          │  │   │
│  │ ○ 追踪请求  │  │   size: 20                         │  │   │
│  │             │  │   sign: a1b2c3d4... [加密]         │  │   │
│  │             │  │ ─────────────────────────────────  │  │   │
│  │             │  │ 响应数据:                          │  │   │
│  │             │  │   {                                │  │   │
│  │             │  │     "code": 200,                   │  │   │
│  │             │  │     "data": [...]                  │  │   │
│  │             │  │   }                                │  │   │
│  │             │  └────────────────────────────────────┘  │   │
│  └─────────────┴──────────────────────────────────────────┘   │
├────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 加密分析结果                                              │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │ 参数名: sign                                             │  │
│  │ 加密类型: MD5                                            │  │
│  │ 加密位置: https://example.com/static/js/main.js:1234     │  │
│  │ 加密函数: function calcSign(params) { ... }              │  │
│  │ 破解状态: ✅ 已破解                                       │  │
│  │ 破解方案: MD5(page + size + timestamp + secret)          │  │
│  │ [查看详细代码]  [导出Python脚本]  [导出Node.js脚本]       │  │
│  └──────────────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────────────┤
│  状态: 分析完成 | 发现 3 个数据接口 | 识别 1 个加密参数        │
└────────────────────────────────────────────────────────────────┘
```

### 6.2 功能按钮说明

| 按钮 | 功能 |
|------|------|
| 开始分析 | 启动页面加载和请求拦截 |
| 停止分析 | 停止当前分析过程 |
| 导出报告 | 导出分析结果为PDF/HTML |
| 导出脚本 | 导出破解脚本（Python/Node.js） |
| 查看源码 | 查看JS源码和反混淆结果 |
| 重放请求 | 重新发送请求验证破解结果 |

---

## 七、项目结构

```
browser-reverse-tool/
├── package.json
├── electron.config.js
├── src/
│   ├── main/                    # Electron主进程
│   │   ├── index.js
│   │   ├── browser.js          # 浏览器控制
│   │   └── ipc.js              # 进程通信
│   │
│   ├── renderer/               # 渲染进程（前端）
│   │   ├── index.html
│   │   ├── App.vue
│   │   ├── components/
│   │   │   ├── URLInput.vue
│   │   │   ├── RequestList.vue
│   │   │   ├── DetailPanel.vue
│   │   │   └── EncryptionResult.vue
│   │   └── store/
│   │       └── index.js
│   │
│   ├── core/                   # 核心引擎
│   │   ├── interceptor.js      # 请求拦截器
│   │   ├── analyzer.js         # 接口分析器
│   │   ├── encryption.js       # 加密分析
│   │   └── cracker.js          # 加密破解
│   │
│   ├── analysis/               # 分析模块
│   │   ├── ast-analyzer.js     # AST分析
│   │   ├── deobfuscator.js     # 反混淆
│   │   ├── pattern-matcher.js  # 模式匹配
│   │   └── crypto-detector.js  # 加密检测
│   │
│   ├── utils/                  # 工具函数
│   │   ├── crypto.js
│   │   ├── network.js
│   │   └── storage.js
│   │
│   └── assets/                 # 静态资源
│       ├── icons/
│       └── styles/
│
├── tests/                      # 测试
│   ├── unit/
│   └── e2e/
│
└── docs/                       # 文档
    ├── API.md
    └── GUIDE.md
```

---

## 八、风险与挑战

### 8.1 技术挑战

| 挑战 | 描述 | 解决方案 |
|------|------|---------|
| 复杂加密算法 | 自定义加密算法难以识别 | 建立加密特征库，机器学习辅助识别 |
| 代码混淆 | 高强度混淆难以还原 | 多层次反混淆，动态执行分析 |
| 反调试机制 | 网站检测调试行为 | 注入反反调试代码 |
| 动态加载 | JS动态加载难以追踪 | MutationObserver监听DOM变化 |
| WebSocket通信 | 实时数据流难以拦截 | WebSocket帧拦截与分析 |

### 8.2 法律风险

- **用途限制**：仅用于合法的安全研究和授权测试
- **数据隐私**：不得获取和存储用户隐私数据
- **知识产权**：不得破解商业软件和受保护内容
- **使用声明**：工具需包含使用免责声明

### 8.3 应对策略

```javascript
// 反反调试代码注入
const antiAntiDebug = `
    // 禁用debugger检测
    const originalDebugger = Object.getOwnPropertyDescriptor(
        Window.prototype, 'debugger'
    );
    
    Object.defineProperty(Window.prototype, 'debugger', {
        get: function() { return undefined; },
        set: function() {}
    });
    
    // 禁用控制台检测
    const originalConsole = window.console;
    Object.defineProperty(window, 'console', {
        get: function() { return originalConsole; },
        set: function() {}
    });
    
    // 禁用DevTools检测
    const originalToString = Function.prototype.toString;
    Function.prototype.toString = function() {
        if (this === originalDebugger?.get) {
            return 'function getter() { [native code] }';
        }
        return originalToString.call(this);
    };
`;
```

---

## 九、开发计划

### 9.1 阶段划分

| 阶段 | 时间 | 任务 | 交付物 |
|------|------|------|--------|
| 第一阶段 | 2周 | 基础框架搭建 | Electron框架、基础UI |
| 第二阶段 | 2周 | 请求拦截与分类 | 网络监控模块 |
| 第三阶段 | 3周 | 加密参数识别 | 加密检测引擎 |
| 第四阶段 | 3周 | 加密破解实现 | 破解算法库 |
| 第五阶段 | 2周 | 界面优化与测试 | 完整应用 |
| 第六阶段 | 1周 | 文档与发布 | 用户手册、API文档 |

### 9.2 里程碑

- **M1**：完成基础UI和浏览器控制
- **M2**：实现请求拦截和接口识别
- **M3**：完成加密参数自动识别
- **M4**：实现常见加密算法破解
- **M5**：完成完整功能测试
- **M6**：正式发布v1.0版本

---

## 十、附录

### 10.1 常见加密算法特征

| 算法 | 特征 | 长度 | 示例 |
|------|------|------|------|
| MD5 | Hex字符串 | 32位 | `d41d8cd98f00b204e9800998ecf8427e` |
| SHA1 | Hex字符串 | 40位 | `da39a3ee5e6b4b0d3255bfef95601890afd80709` |
| SHA256 | Hex字符串 | 64位 | `e3b0c44298fc1c149afbf4c8996fb924...` |
| Base64 | 字母数字+/= | 4的倍数 | `SGVsbG8gV29ybGQ=` |
| AES | Base64/Hex | 16/32字节倍数 | 加密数据 |
| RSA | Base64 | 128/256字节 | 公钥加密数据 |

### 10.2 参考资源

- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
- [Puppeteer文档](https://pptr.dev/)
- [Babel AST文档](https://babeljs.io/docs/en/babel-parser)
- [CryptoJS文档](https://cryptojs.gitbook.io/docs/)

---

**文档版本**：v1.0  
**创建日期**：2025-03-25  
**最后更新**：2025-03-25
