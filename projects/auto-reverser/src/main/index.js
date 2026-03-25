const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { BrowserController } = require('./browser');
const { RequestInterceptor } = require('../core/interceptor');
const { APIAnalyzer } = require('../core/analyzer');
const { EncryptionAnalyzer } = require('../core/encryption');
const { EncryptionCracker } = require('../core/cracker');
const Store = require('electron-store');

const store = new Store();
let mainWindow = null;
let browserController = null;
let requestInterceptor = null;
let apiAnalyzer = null;
let encryptionAnalyzer = null;
let encryptionCracker = null;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1400,
        height: 900,
        minWidth: 1000,
        minHeight: 700,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            webSecurity: false
        },
        titleBarStyle: 'hiddenInset',
        backgroundColor: '#1a1a2e'
    });

    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));

    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    mainWindow.webContents.openDevTools();
}

function initializeModules() {
    browserController = new BrowserController();
    requestInterceptor = new RequestInterceptor();
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
        return requestInterceptor.getAllRequests();
    });

    ipcMain.handle('analyze-api', async (event, requestId) => {
        const request = requestInterceptor.getRequest(requestId);
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
}

async function startAnalysis(url) {
    const page = await browserController.launch(url);
    
    requestInterceptor.attach(page);
    
    await page.goto(url, { 
        waitUntil: 'domcontentloaded',
        timeout: 60000 
    });
    
    await browserController.autoScroll();
    
    const requests = requestInterceptor.getAllRequests();
    const apiRequests = await apiAnalyzer.identifyAPIs(requests);
    
    return {
        url: url,
        requests: requests,
        apiRequests: apiRequests
    };
}

async function stopAnalysis() {
    if (browserController) {
        await browserController.close();
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
