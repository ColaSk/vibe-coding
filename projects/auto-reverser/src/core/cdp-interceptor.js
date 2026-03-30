/**
 * 使用 Electron debugger API（真正的 CDP）拦截网络请求并获取完整响应体。
 *
 * session.webRequest 无法获取响应体，必须通过 CDP Network domain：
 *   Network.requestWillBeSent  → 捕获请求
 *   Network.responseReceived   → 捕获响应头/状态码（立即通知渲染进程显示状态）
 *   Network.loadingFinished    → 调用 Network.getResponseBody 获取响应体
 *   Network.loadingFailed      → 记录请求失败
 */
class CDPInterceptor {
    constructor() {
        this.requests = new Map();   // cdpRequestId → requestData
        this.listeners = new Set();
        this.browserView = null;
        this.cdpDebugger = null;
    }

    async attachToBrowserView(browserView) {
        this.browserView = browserView;
        this.clear();

        const webContents = browserView.webContents;
        this.cdpDebugger = webContents.debugger;

        // 挂载 CDP debugger
        try {
            if (!this.cdpDebugger.isAttached()) {
                this.cdpDebugger.attach('1.3');
            }
        } catch (err) {
            console.error('Failed to attach CDP debugger:', err);
            return;
        }

        // 启用 Network domain，设置缓冲区大小以支持响应体读取
        try {
            await this.cdpDebugger.sendCommand('Network.enable', {
                maxTotalBufferSize: 10 * 1024 * 1024,
                maxResourceBufferSize: 5 * 1024 * 1024
            });
        } catch (err) {
            console.error('Failed to enable Network domain:', err);
            return;
        }

        // 监听 CDP 网络事件
        this.cdpDebugger.on('message', async (event, method, params) => {
            try {
                switch (method) {
                    case 'Network.requestWillBeSent':
                        this.handleCDPRequest(params);
                        break;
                    case 'Network.responseReceived':
                        this.handleCDPResponse(params);
                        break;
                    case 'Network.loadingFinished':
                        await this.handleCDPLoadingFinished(params);
                        break;
                    case 'Network.loadingFailed':
                        this.handleCDPLoadingFailed(params);
                        break;
                }
            } catch (err) {
                // 静默处理，避免单条消息错误影响整体
            }
        });

        console.log('CDP interceptor attached successfully');
    }

    // ─── CDP 事件处理 ─────────────────────────────────────────────────────────

    handleCDPRequest(params) {
        const { requestId, request, type } = params;

        const requestData = {
            id: requestId,
            url: request.url,
            method: (request.method || 'GET').toUpperCase(),
            headers: request.headers || {},
            postData: request.postData || null,
            resourceType: (type || 'Other').toLowerCase(),
            timestamp: Date.now(),
            status: 'pending',
            response: null
        };

        this.requests.set(requestId, requestData);
        this.notifyListeners('request', requestData);
    }

    handleCDPResponse(params) {
        const { requestId, response } = params;
        const request = this.requests.get(requestId);
        if (!request) return;

        // 立即用响应头/状态码更新请求，让列表能快速显示状态码
        request.response = {
            id: requestId,
            url: response.url,
            status: response.status,
            statusText: response.statusText || '',
            headers: response.headers || {},
            timestamp: Date.now(),
            body: null,
            bodyType: 'loading'
        };
        request.status = 'completed';

        // 先通知一次，让列表显示状态码（响应体稍后在 loadingFinished 中补充）
        this.notifyListeners('response', { request, response: request.response });
    }

    async handleCDPLoadingFinished(params) {
        const { requestId } = params;
        const request = this.requests.get(requestId);
        if (!request) return;

        if (!request.response) {
            request.response = {
                id: requestId,
                url: request.url,
                status: 0,
                statusText: '',
                headers: {},
                timestamp: Date.now(),
                body: null,
                bodyType: 'unknown'
            };
        }

        // 通过 CDP 获取响应体
        try {
            const result = await this.cdpDebugger.sendCommand(
                'Network.getResponseBody',
                { requestId }
            );

            let bodyText = result.body || '';
            if (result.base64Encoded && bodyText) {
                // 二进制内容转为 UTF-8（如 gzip 解压后的文本）
                bodyText = Buffer.from(bodyText, 'base64').toString('utf8');
            }

            // 先尝试解析为 JSON
            try {
                request.response.body = JSON.parse(bodyText);
                request.response.bodyType = 'json';
            } catch {
                request.response.body = bodyText;
                request.response.bodyType = this.detectBodyType(request.response.headers);
            }
        } catch {
            // 响应体不可用（二进制、资源被取消等）
            const contentType = this.getContentType(request.response.headers);
            if (contentType && /image|video|audio|font|woff|otf/i.test(contentType)) {
                request.response.body = `[Binary: ${contentType}]`;
                request.response.bodyType = 'binary';
            } else {
                request.response.body = null;
                request.response.bodyType = 'unavailable';
            }
        }

        // 补充了响应体后再通知一次，让详情面板刷新
        this.notifyListeners('response', { request, response: request.response });
    }

    handleCDPLoadingFailed(params) {
        const { requestId, errorText, canceled } = params;
        const request = this.requests.get(requestId);
        if (!request) return;

        request.status = 'failed';
        request.error = canceled ? 'Canceled' : (errorText || 'Unknown error');
    }

    // ─── 辅助方法 ─────────────────────────────────────────────────────────────

    detectBodyType(headers) {
        const ct = this.getContentType(headers);
        if (!ct) return 'text';
        if (ct.includes('javascript')) return 'javascript';
        if (ct.includes('html')) return 'html';
        if (ct.includes('css')) return 'css';
        if (ct.includes('xml')) return 'xml';
        return 'text';
    }

    getContentType(headers) {
        if (!headers) return '';
        const entry = Object.entries(headers).find(
            ([k]) => k.toLowerCase() === 'content-type'
        );
        return entry ? entry[1] : '';
    }

    // ─── 公共接口 ─────────────────────────────────────────────────────────────

    getAllRequests() {
        return Array.from(this.requests.values());
    }

    getRequest(id) {
        return this.requests.get(id);
    }

    addListener(callback) {
        this.listeners.add(callback);
        return () => this.listeners.delete(callback);
    }

    clearListeners() {
        this.listeners.clear();
    }

    notifyListeners(type, data) {
        this.listeners.forEach(callback => {
            try {
                callback(type, data);
            } catch (error) {
                console.error('Listener error:', error);
            }
        });
    }

    clear() {
        this.requests.clear();
    }

    detach() {
        if (this.cdpDebugger) {
            try {
                if (this.cdpDebugger.isAttached()) {
                    this.cdpDebugger.detach();
                }
            } catch (err) {
                console.error('Error detaching CDP debugger:', err);
            }
            this.cdpDebugger = null;
        }
        this.browserView = null;
        this.clearListeners();
        this.clear();
    }
}

module.exports = { CDPInterceptor };
