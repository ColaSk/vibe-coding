const CDP = require('chrome-remote-interface');

class CDPController {
    constructor() {
        this.client = null;
        this.Network = null;
        this.Page = null;
        this.Debugger = null;
        this.Runtime = null;
    }

    async connect(port = 9222) {
        this.client = await CDP({ port });
        
        this.Network = this.client.Network;
        this.Page = this.client.Page;
        this.Debugger = this.client.Debugger;
        this.Runtime = this.client.Runtime;

        await this.Network.enable();
        await this.Page.enable();
        await this.Debugger.enable();
        await this.Runtime.enable();

        return this.client;
    }

    async enableNetworkMonitoring(callbacks = {}) {
        this.Network.requestWillBeSent((params) => {
            if (callbacks.onRequest) {
                callbacks.onRequest({
                    requestId: params.requestId,
                    url: params.request.url,
                    method: params.request.method,
                    headers: params.request.headers,
                    postData: params.request.postData,
                    timestamp: params.wallTime
                });
            }
        });

        this.Network.responseReceived(async (params) => {
            if (callbacks.onResponse) {
                let body = null;
                try {
                    const responseBody = await this.Network.getResponseBody({
                        requestId: params.requestId
                    });
                    body = responseBody;
                } catch (e) {}

                callbacks.onResponse({
                    requestId: params.requestId,
                    url: params.response.url,
                    status: params.response.status,
                    headers: params.response.headers,
                    body: body
                });
            }
        });

        this.Network.loadingFailed((params) => {
            if (callbacks.onFailed) {
                callbacks.onFailed({
                    requestId: params.requestId,
                    error: params.errorText
                });
            }
        });
    }

    async setBreakpoint(url, lineNumber) {
        return await this.Debugger.setBreakpointByUrl({
            url: url,
            lineNumber: lineNumber
        });
    }

    async setBreakpointByUrl(urlRegex, lineNumber) {
        return await this.Debugger.setBreakpointByUrl({
            urlRegex: urlRegex,
            lineNumber: lineNumber
        });
    }

    async pauseOnExceptions() {
        await this.Debugger.setPauseOnExceptions({ state: 'all' });
    }

    async resume() {
        await this.Debugger.resume();
    }

    async stepOver() {
        await this.Debugger.stepOver();
    }

    async stepInto() {
        await this.Debugger.stepInto();
    }

    async stepOut() {
        await this.Debugger.stepOut();
    }

    async evaluateOnCallFrame(callFrameId, expression) {
        return await this.Debugger.evaluateOnCallFrame({
            callFrameId: callFrameId,
            expression: expression
        });
    }

    async getProperties(objectId) {
        return await this.Runtime.getProperties({
            objectId: objectId,
            ownProperties: true
        });
    }

    async evaluate(expression) {
        return await this.Runtime.evaluate({
            expression: expression,
            returnByValue: true
        });
    }

    async getCookies() {
        return await this.Network.getCookies();
    }

    async setCookie(name, value, options = {}) {
        return await this.Network.setCookie({
            name: name,
            value: value,
            ...options
        });
    }

    async deleteCookies(name, url) {
        return await this.Network.deleteCookies({
            name: name,
            url: url
        });
    }

    async disconnect() {
        if (this.client) {
            await this.client.close();
            this.client = null;
        }
    }
}

module.exports = { CDPController };
