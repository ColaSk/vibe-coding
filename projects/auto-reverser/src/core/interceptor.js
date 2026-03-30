const { v4: uuidv4 } = require('uuid');
const { session } = require('electron');

class RequestInterceptor {
    constructor() {
        this.requests = new Map();
        this.responses = new Map();
        this.listeners = new Set();
        this.page = null;
        this.browserView = null;
    }

    attach(page) {
        this.page = page;
        this.clear();

        page.on('request', (request) => {
            this.handleRequest(request);
            request.continue();
        });

        page.on('response', (response) => {
            this.handleResponse(response);
        });

        page.on('requestfailed', (request) => {
            this.handleRequestFailed(request);
        });
    }

    attachToBrowserView(browserView) {
        this.browserView = browserView;
        this.clear();

        const webContents = browserView.webContents;

        webContents.on('before-input-event', (event, input) => {
            if (input.key === 'F5' || (input.control && input.key === 'r')) {
                webContents.reload();
            }
        });

        webContents.session.webRequest.onBeforeRequest(
            { urls: ['*://*/*'] },
            (details, callback) => {
                this.handleWebRequest(details);
                callback({});
            }
        );

        webContents.session.webRequest.onCompleted(
            { urls: ['*://*/*'] },
            (details) => {
                this.handleWebResponse(details);
            }
        );

        webContents.session.webRequest.onErrorOccurred(
            { urls: ['*://*/*'] },
            (details) => {
                this.handleWebError(details);
            }
        );
    }

    handleWebRequest(details) {
        const requestId = details.id || uuidv4();
        const requestData = {
            id: requestId,
            url: details.url,
            method: details.method,
            headers: details.requestHeaders || {},
            postData: details.uploadData ? details.uploadData.map(d => d.bytes?.toString()).join('') : null,
            resourceType: details.resourceType,
            timestamp: Date.now(),
            status: 'pending'
        };

        this.requests.set(requestId, requestData);
        this.notifyListeners('request', requestData);
    }

    handleWebResponse(details) {
        const requestId = details.id;
        if (!requestId) return;

        const responseData = {
            id: requestId,
            url: details.url,
            status: details.statusCode,
            statusText: details.statusLine,
            headers: details.responseHeaders || {},
            timestamp: Date.now()
        };

        this.responses.set(requestId, responseData);

        const originalRequest = this.requests.get(requestId);
        if (originalRequest) {
            originalRequest.status = 'completed';
            originalRequest.response = responseData;
        }

        this.notifyListeners('response', {
            request: originalRequest,
            response: responseData
        });
    }

    handleWebError(details) {
        const requestId = details.id;
        if (!requestId) return;

        const originalRequest = this.requests.get(requestId);
        if (originalRequest) {
            originalRequest.status = 'failed';
            originalRequest.error = details.error || 'Unknown error';
        }
    }

    handleRequest(request) {
        const requestId = uuidv4();
        const requestData = {
            id: requestId,
            url: request.url(),
            method: request.method(),
            headers: request.headers(),
            postData: request.postData(),
            resourceType: request.resourceType(),
            timestamp: Date.now(),
            status: 'pending'
        };

        this.requests.set(requestId, requestData);
        this.notifyListeners('request', requestData);
    }

    async handleResponse(response) {
        const request = response.request();
        const requestId = this.findRequestIdByUrl(request.url());
        
        if (!requestId) return;

        const responseData = {
            id: requestId,
            url: response.url(),
            status: response.status(),
            statusText: response.statusText(),
            headers: response.headers(),
            timestamp: Date.now()
        };

        try {
            const contentType = response.headers()['content-type'] || '';
            
            if (contentType.includes('application/json')) {
                responseData.body = await response.json();
                responseData.bodyType = 'json';
            } else if (contentType.includes('text/') || contentType.includes('javascript')) {
                responseData.body = await response.text();
                responseData.bodyType = 'text';
            } else {
                responseData.body = '[Binary Data]';
                responseData.bodyType = 'binary';
            }
        } catch (error) {
            responseData.body = null;
            responseData.bodyType = 'error';
            responseData.error = error.message;
        }

        this.responses.set(requestId, responseData);

        const originalRequest = this.requests.get(requestId);
        if (originalRequest) {
            originalRequest.status = 'completed';
            originalRequest.response = responseData;
        }

        this.notifyListeners('response', {
            request: originalRequest,
            response: responseData
        });
    }

    handleRequestFailed(request) {
        const requestId = this.findRequestIdByUrl(request.url());
        
        if (requestId) {
            const originalRequest = this.requests.get(requestId);
            if (originalRequest) {
                originalRequest.status = 'failed';
                originalRequest.error = request.failure()?.errorText || 'Unknown error';
            }
        }
    }

    findRequestIdByUrl(url) {
        for (const [id, request] of this.requests) {
            if (request.url === url) {
                return id;
            }
        }
        return null;
    }

    getAllRequests() {
        return Array.from(this.requests.values());
    }

    getRequest(id) {
        return this.requests.get(id);
    }

    getResponse(id) {
        return this.responses.get(id);
    }

    getAPIRequests() {
        return this.getAllRequests().filter(req => 
            req.resourceType === 'xhr' || 
            req.resourceType === 'fetch' ||
            this.isAPIUrl(req.url)
        );
    }

    isAPIUrl(url) {
        const apiPatterns = [
            /\/api\//i,
            /\/v\d+\//i,
            /\/graphql/i,
            /\/query/i,
            /\.json$/i
        ];

        return apiPatterns.some(pattern => pattern.test(url));
    }

    addListener(callback) {
        this.listeners.add(callback);
        return () => this.listeners.delete(callback);
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
        this.responses.clear();
    }

    detach() {
        if (this.page) {
            this.page.removeAllListeners('request');
            this.page.removeAllListeners('response');
            this.page.removeAllListeners('requestfailed');
            this.page = null;
        }
        if (this.browserView) {
            const webContents = this.browserView.webContents;
            webContents.session.webRequest.onBeforeRequest(null);
            webContents.session.webRequest.onCompleted(null);
            webContents.session.webRequest.onErrorOccurred(null);
            this.browserView = null;
        }
        this.clear();
    }
}

module.exports = { RequestInterceptor };
