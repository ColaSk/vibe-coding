const { app, BrowserWindow, BrowserView, ipcMain } = require('electron');
const path = require('path');
const { RequestInterceptor } = require('../core/interceptor');
const { CDPInterceptor } = require('../core/cdp-interceptor');
const { APIAnalyzer } = require('../core/analyzer');
const { EncryptionAnalyzer } = require('../core/encryption');
const { EncryptionCracker } = require('../core/cracker');
const { OllamaProvider } = require('../core/ollama-provider');
const { ToolRegistry }   = require('../core/tool-registry');
const { LLMAgent }       = require('../core/llm-agent');
const Store = require('electron-store');

const store = new Store();
let mainWindow = null;
let browserView = null;
let requestInterceptor = null;
let cdpInterceptor = null;
let apiAnalyzer = null;
let encryptionAnalyzer = null;
let encryptionCracker = null;
let currentAgent = null;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1400,
        height: 900,
        minWidth: 1000,
        minHeight: 700,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            webSecurity: false,
            webviewTag: true
        },
        titleBarStyle: 'hiddenInset',
        backgroundColor: '#1a1a2e'
    });

    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));

    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    mainWindow.on('resize', () => {
        if (browserView) {
            updateBrowserViewBounds();
        }
    });

}

function createBrowserView() {
    if (browserView) {
        browserView.webContents.destroy();
        browserView = null;
    }

    browserView = new BrowserView({
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            webSecurity: false,
            preload: path.join(__dirname, '../preload/browser-preload.js')
        }
    });

    mainWindow.setBrowserView(browserView);
    updateBrowserViewBounds();

    browserView.webContents.on('did-navigate', (event, url) => {
        mainWindow.webContents.send('browser-url-changed', url);
    });

    browserView.webContents.on('did-navigate-in-page', (event, url) => {
        mainWindow.webContents.send('browser-url-changed', url);
    });

    browserView.webContents.on('did-start-loading', () => {
        mainWindow.webContents.send('browser-loading', true);
    });

    browserView.webContents.on('did-stop-loading', () => {
        mainWindow.webContents.send('browser-loading', false);
    });

    browserView.webContents.on('new-window', (event, url) => {
        event.preventDefault();
        browserView.webContents.loadURL(url);
    });

    return browserView;
}

function updateBrowserViewBounds() {
    if (!browserView || !mainWindow) return;

    const contentBounds = mainWindow.getContentBounds();
    
    // 先设置一个默认边界
    browserView.setBounds({
        x: 0,
        y: 0,
        width: contentBounds.width,
        height: 400
    });
    
    // 然后获取精确位置
    mainWindow.webContents.executeJavaScript(`
        (function() {
            const container = document.getElementById('browser-container');
            if (!container) return null;
            const rect = container.getBoundingClientRect();
            return {
                x: Math.round(rect.left),
                y: Math.round(rect.top),
                width: Math.round(rect.width),
                height: Math.round(rect.height)
            };
        })()
    `).then(bounds => {
        if (bounds && bounds.width > 0 && bounds.height > 0) {
            browserView.setBounds(bounds);
        }
    }).catch(err => {
        console.error('Failed to get browser container bounds:', err);
    });
}

function initializeModules() {
    requestInterceptor = new RequestInterceptor();
    cdpInterceptor = new CDPInterceptor();
    apiAnalyzer = new APIAnalyzer();
    encryptionAnalyzer = new EncryptionAnalyzer();
    encryptionCracker = new EncryptionCracker();
}

function setupIPC() {
    ipcMain.handle('start-analysis', async (event, url) => {
        try {
            const result = await startAnalysis(url);
            return { success: true, data: result };
        } catch (error) {
            return { success: false, error: error.message };
        }
    });

    ipcMain.handle('stop-analysis', async () => {
        try {
            await stopAnalysis();
            return { success: true };
        } catch (error) {
            return { success: false, error: error.message };
        }
    });

    ipcMain.handle('get-requests', async () => {
        return cdpInterceptor.getAllRequests();
    });

    ipcMain.handle('analyze-api', async (event, requestId) => {
        const request = cdpInterceptor.getRequest(requestId);
        if (request) {
            return await apiAnalyzer.analyze(request);
        }
        return null;
    });

    ipcMain.handle('analyze-encryption', async (event, params) => {
        return await encryptionAnalyzer.analyze(params);
    });

    ipcMain.handle('crack-encryption', async (event, encryptedData, type) => {
        return await encryptionCracker.crack(encryptedData, type);
    });

    ipcMain.handle('export-script', async (event, type, data) => {
        return encryptionCracker.generateScript(type, data);
    });

    ipcMain.handle('browser-navigate', async (event, url) => {
        if (browserView) {
            browserView.webContents.loadURL(url);
        }
    });

    ipcMain.handle('browser-back', async () => {
        if (browserView && browserView.webContents.canGoBack()) {
            browserView.webContents.goBack();
        }
    });

    ipcMain.handle('browser-forward', async () => {
        if (browserView && browserView.webContents.canGoForward()) {
            browserView.webContents.goForward();
        }
    });

    ipcMain.handle('browser-refresh', async () => {
        if (browserView) {
            browserView.webContents.reload();
        }
    });

    ipcMain.handle('browser-devtools', async () => {
        if (browserView) {
            browserView.webContents.openDevTools();
        }
    });

    ipcMain.handle('show-browser', async () => {
        if (browserView) {
            updateBrowserViewBounds();
        }
    });

    // ─── Agent IPC ───────────────────────────────────────────────────────────

    ipcMain.handle('agent-chat', async (event, { message, history }) => {
        try {
            const config = store.get('llmConfig') || {};
            const provider = new OllamaProvider(config);

            const stream = (ev) => {
                if (!mainWindow || mainWindow.isDestroyed()) return;
                mainWindow.webContents.send('agent-stream', ev);
            };

            const registry = new ToolRegistry(
                cdpInterceptor, apiAnalyzer, encryptionAnalyzer, encryptionCracker,
                {
                    // Agent 主动导航：通知渲染进程同步 UI，然后启动抓包
                    navigateCallback: async (url) => {
                        stream({ type: 'capture-started', url });
                        await startAnalysis(url);
                    },
                    // 等待期间实时推送进度给 UI
                    progressCallback: (message, count) => {
                        stream({ type: 'progress', message, count });
                    }
                }
            );

            currentAgent = new LLMAgent(provider, registry, stream);
            // 异步运行，不 await，立即返回让 UI 开始监听流
            currentAgent.chat(message, history || []);
            return { success: true };
        } catch (err) {
            return { success: false, error: err.message };
        }
    });

    ipcMain.handle('agent-stop', () => {
        if (currentAgent) currentAgent.stop();
        return { stopped: true };
    });

    ipcMain.handle('llm-config-save', (event, config) => {
        store.set('llmConfig', config);
        return true;
    });

    ipcMain.handle('llm-config-get', () => {
        const c = store.get('llmConfig') || {};
        return {
            provider:    c.provider    || 'ollama',
            model:       c.model       || 'qwen2.5:7b',
            host:        c.host        || 'http://localhost:11434',
            maxRounds:   c.maxRounds   || 10,
            temperature: c.temperature || 0.2
        };
    });

    ipcMain.handle('llm-verify', async () => {
        try {
            const config   = store.get('llmConfig') || {};
            const provider = new OllamaProvider(config);
            const start    = Date.now();
            const result   = await provider.verify();
            return { ...result, latency_ms: Date.now() - start };
        } catch (err) {
            return { success: false, error: err.message };
        }
    });
}

async function startAnalysis(url) {
    console.log('Starting analysis for:', url);

    createBrowserView();
    cdpInterceptor.attachToBrowserView(browserView);

    // 实时将每条请求/响应推送到渲染进程，不等待页面加载完成
    cdpInterceptor.addListener((type, data) => {
        if (!mainWindow || mainWindow.isDestroyed()) return;
        mainWindow.webContents.send('request-captured', { type, data });
    });

    // 非阻塞导航：不 await，让用户可以在页面加载期间手动操作（过验证码等）
    browserView.webContents.loadURL(url).catch(err => {
        console.error('Navigation error:', err.message);
        if (mainWindow && !mainWindow.isDestroyed()) {
            mainWindow.webContents.send('browser-load-error', err.message);
        }
    });

    // 立即返回，请求通过事件实时推送
    return { url };
}

async function stopAnalysis() {
    if (browserView) {
        if (cdpInterceptor) {
            cdpInterceptor.detach();
        }
        browserView.webContents.destroy();
        browserView = null;
    }
    if (requestInterceptor) {
        requestInterceptor.clear();
    }
}

app.whenReady().then(() => {
    initializeModules();
    setupIPC();
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('before-quit', async () => {
    await stopAnalysis();
});
