# Auto Reverser - 浏览器自动逆向工具

一款桌面级自动化逆向分析工具，用于自动识别网站API接口、分析请求参数、破解加密参数。

## 功能特性

- **URL输入与页面加载**：支持用户输入任意网站URL，自动加载并渲染页面
- **接口自动识别**：自动捕获并分析页面加载过程中的所有网络请求
- **数据接口定位**：智能识别列表页数据来源接口
- **参数分析**：解析请求参数结构，识别加密参数
- **加密破解**：针对常见加密算法进行自动化破解
- **脚本导出**：支持导出Python和Node.js脚本

## 技术栈

- **桌面框架**: Electron
- **浏览器控制**: Puppeteer / Chrome DevTools Protocol
- **JS分析**: Babel AST
- **加密识别**: CryptoJS

## 安装

```bash
cd projects/auto-reverser
npm install
```

## 运行

```bash
npm start
```

## 开发模式

```bash
npm run dev
```

## 构建

```bash
# macOS
npm run build:mac

# Windows
npm run build:win

# Linux
npm run build:linux
```

## 项目结构

```
auto-reverser/
├── src/
│   ├── main/                 # Electron主进程
│   │   ├── index.js         # 主进程入口
│   │   └── browser.js       # 浏览器控制
│   │
│   ├── renderer/            # 渲染进程（前端）
│   │   ├── index.html       # 主页面
│   │   ├── styles/          # 样式文件
│   │   └── scripts/         # 前端脚本
│   │
│   ├── core/                # 核心引擎
│   │   ├── interceptor.js   # 请求拦截器
│   │   ├── cdp.js           # CDP协议控制
│   │   ├── analyzer.js      # 接口分析器
│   │   ├── encryption.js    # 加密分析
│   │   └── cracker.js       # 加密破解
│   │
│   ├── analysis/            # 分析模块
│   │   ├── ast-analyzer.js  # AST分析
│   │   └── deobfuscator.js  # 反混淆
│   │
│   └── utils/               # 工具函数
│       ├── crypto.js        # 加密工具
│       └── storage.js       # 存储工具
│
├── docs/                    # 文档
├── package.json
└── README.md
```

## 支持的加密算法

| 算法 | 特征 | 破解方式 |
|------|------|---------|
| MD5 | 32位十六进制 | 彩虹表、字典攻击 |
| SHA1 | 40位十六进制 | 字典攻击 |
| SHA256 | 64位十六进制 | 字典攻击 |
| Base64 | 字母数字+/= | 直接解码 |
| JWT | 三段式Base64 | 弱密钥破解 |
| AES | Base64/Hex | 已知密钥解密 |

## 使用说明

1. 输入要分析的网站URL
2. 点击"开始分析"按钮
3. 等待页面加载完成
4. 查看捕获的请求列表
5. 选择请求查看详情
6. 分析加密参数
7. 导出破解脚本

## 注意事项

- 本工具仅供合法的安全研究和授权测试使用
- 不得用于获取和存储用户隐私数据
- 不得用于破解商业软件和受保护内容

## License

MIT
