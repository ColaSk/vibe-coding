const { ipcRenderer } = require('electron');

class App {
    constructor() {
        this.requests = [];
        this.selectedRequest = null;
        this.encryptionResults = [];
        this.isAnalyzing = false;
        
        this.init();
    }

    init() {
        this.bindElements();
        this.bindEvents();
        this.updateStatus('就绪');
    }

    bindElements() {
        this.urlInput = document.getElementById('url-input');
        this.btnStart = document.getElementById('btn-start');
        this.btnStop = document.getElementById('btn-stop');
        this.btnExport = document.getElementById('btn-export');
        this.requestsList = document.getElementById('requests-list');
        this.requestDetail = document.getElementById('request-detail');
        this.encryptionResults = document.getElementById('encryption-results');
        this.statusText = document.getElementById('status-text');
        this.statusStats = document.getElementById('status-stats');
        this.modalContainer = document.getElementById('modal-container');
        this.modalTitle = document.getElementById('modal-title');
        this.modalContent = document.getElementById('modal-content');
    }

    bindEvents() {
        this.btnStart.addEventListener('click', () => this.startAnalysis());
        this.btnStop.addEventListener('click', () => this.stopAnalysis());
        
        this.urlInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.startAnalysis();
        });

        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.filterRequests(e.target.dataset.filter));
        });

        document.getElementById('btn-export-python').addEventListener('click', () => this.exportScript('python'));
        document.getElementById('btn-export-nodejs').addEventListener('click', () => this.exportScript('nodejs'));
        document.getElementById('btn-copy-request').addEventListener('click', () => this.copyRequest());
        document.getElementById('btn-replay-request').addEventListener('click', () => this.replayRequest());

        document.querySelector('.modal-overlay').addEventListener('click', () => this.hideModal());
        document.querySelector('.modal-cancel').addEventListener('click', () => this.hideModal());
        document.querySelector('.modal-close').addEventListener('click', () => this.hideModal());
    }

    async startAnalysis() {
        const url = this.urlInput.value.trim();
        
        if (!url) {
            this.showError('请输入要分析的URL');
            return;
        }

        if (!this.isValidUrl(url)) {
            this.showError('请输入有效的URL');
            return;
        }

        this.isAnalyzing = true;
        this.updateUI();
        this.updateStatus('正在启动浏览器...');
        this.clearResults();

        try {
            const result = await ipcRenderer.invoke('start-analysis', url);
            
            if (result.success) {
                this.requests = result.data.requests || [];
                this.renderRequests();
                this.updateStatus('分析完成');
                this.updateStats(result.data);
            } else {
                this.showError(result.error);
                this.updateStatus('分析失败');
            }
        } catch (error) {
            this.showError(error.message);
            this.updateStatus('分析失败');
        } finally {
            this.isAnalyzing = false;
            this.updateUI();
        }
    }

    async stopAnalysis() {
        await ipcRenderer.invoke('stop-analysis');
        this.isAnalyzing = false;
        this.updateUI();
        this.updateStatus('已停止');
    }

    isValidUrl(string) {
        try {
            new URL(string);
            return true;
        } catch (_) {
            return false;
        }
    }

    updateUI() {
        this.btnStart.classList.toggle('hidden', this.isAnalyzing);
        this.btnStop.classList.toggle('hidden', !this.isAnalyzing);
        this.urlInput.disabled = this.isAnalyzing;
        this.btnExport.disabled = this.requests.length === 0;
    }

    updateStatus(text) {
        this.statusText.textContent = text;
    }

    updateStats(data) {
        const apiCount = data.apiRequests?.length || 0;
        const encryptedCount = this.encryptionResults.length;
        
        this.statusStats.innerHTML = `
            <span class="stat-item">请求: ${this.requests.length}</span>
            <span class="stat-item">API: ${apiCount}</span>
            <span class="stat-item">加密参数: ${encryptedCount}</span>
        `;
    }

    clearResults() {
        this.requests = [];
        this.selectedRequest = null;
        this.encryptionResults = [];
        this.requestsList.innerHTML = `
            <div class="empty-state">
                <p>正在捕获网络请求...</p>
            </div>
        `;
        this.requestDetail.innerHTML = `
            <div class="empty-state">
                <p>选择一个请求查看详情</p>
            </div>
        `;
        this.encryptionResults.innerHTML = `
            <div class="empty-state">
                <p>分析完成后，加密参数将显示在这里</p>
            </div>
        `;
    }

    renderRequests(filter = 'all') {
        let filteredRequests = this.requests;

        switch (filter) {
            case 'api':
                filteredRequests = this.requests.filter(r => 
                    r.resourceType === 'xhr' || r.resourceType === 'fetch'
                );
                break;
            case 'xhr':
                filteredRequests = this.requests.filter(r => 
                    r.resourceType === 'xhr'
                );
                break;
            case 'encrypted':
                filteredRequests = this.requests.filter(r => 
                    r.hasEncryption === true
                );
                break;
        }

        if (filteredRequests.length === 0) {
            this.requestsList.innerHTML = `
                <div class="empty-state">
                    <p>没有找到匹配的请求</p>
                </div>
            `;
            return;
        }

        this.requestsList.innerHTML = filteredRequests.map(req => `
            <div class="request-item ${this.selectedRequest?.id === req.id ? 'active' : ''}" 
                 data-id="${req.id}">
                <div class="request-item-header">
                    <span class="request-method method-${req.method.toLowerCase()}">${req.method}</span>
                    ${req.hasEncryption ? '<span class="has-encryption">🔐</span>' : ''}
                </div>
                <div class="request-url" title="${req.url}">${this.truncateUrl(req.url)}</div>
                <div class="request-item-footer">
                    <span class="request-status status-${this.getStatusClass(req.response?.status)}">
                        ${req.response?.status || req.status}
                    </span>
                    <span>${this.formatTime(req.timestamp)}</span>
                </div>
            </div>
        `).join('');

        this.requestsList.querySelectorAll('.request-item').forEach(item => {
            item.addEventListener('click', () => this.selectRequest(item.dataset.id));
        });
    }

    filterRequests(filter) {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
        this.renderRequests(filter);
    }

    async selectRequest(id) {
        this.selectedRequest = this.requests.find(r => r.id === id);
        
        if (!this.selectedRequest) return;

        this.renderRequests();
        this.renderRequestDetail();

        document.getElementById('btn-copy-request').disabled = false;
        document.getElementById('btn-replay-request').disabled = false;

        const analysis = await ipcRenderer.invoke('analyze-api', id);
        if (analysis?.params) {
            const encryptionResult = await ipcRenderer.invoke('analyze-encryption', analysis.params);
            if (encryptionResult?.encryptedParams?.length > 0) {
                this.selectedRequest.hasEncryption = true;
                this.renderEncryptionResults(encryptionResult.encryptedParams);
            }
        }
    }

    renderRequestDetail() {
        if (!this.selectedRequest) return;

        const req = this.selectedRequest;
        const url = new URL(req.url);

        let html = `
            <div class="detail-section">
                <div class="detail-section-title">请求信息</div>
                <div class="detail-content">
                    <div class="param-item">
                        <span class="param-name">URL</span>
                        <span class="param-value">${req.url}</span>
                    </div>
                    <div class="param-item">
                        <span class="param-name">方法</span>
                        <span class="param-value">${req.method}</span>
                    </div>
                    <div class="param-item">
                        <span class="param-name">类型</span>
                        <span class="param-value">${req.resourceType}</span>
                    </div>
                </div>
            </div>
        `;

        if (url.search) {
            html += `
                <div class="detail-section">
                    <div class="detail-section-title">查询参数</div>
                    <div class="detail-content">
                        ${Array.from(url.searchParams.entries()).map(([key, value]) => `
                            <div class="param-item">
                                <span class="param-name">${key}</span>
                                <span class="param-value">${value}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }

        if (req.postData) {
            html += `
                <div class="detail-section">
                    <div class="detail-section-title">请求体</div>
                    <div class="detail-content">
                        <pre>${this.formatJSON(req.postData)}</pre>
                    </div>
                </div>
            `;
        }

        if (req.response) {
            html += `
                <div class="detail-section">
                    <div class="detail-section-title">响应 (${req.response.status})</div>
                    <div class="detail-content">
                        <pre>${this.formatJSON(req.response.body)}</pre>
                    </div>
                </div>
            `;
        }

        this.requestDetail.innerHTML = html;
    }

    async renderEncryptionResults(encryptedParams) {
        if (!encryptedParams || encryptedParams.length === 0) return;

        this.encryptionResults.innerHTML = encryptedParams.map(param => `
            <div class="encryption-item">
                <div class="encryption-item-header">
                    <span class="encryption-param-name">${param.name}</span>
                    <span class="encryption-type">${param.encryptionType || 'Unknown'}</span>
                </div>
                <div class="encryption-item-body">
                    <div class="encryption-field">
                        <span class="encryption-field-label">原始值</span>
                        <span class="encryption-field-value">${this.truncate(param.value, 50)}</span>
                    </div>
                    <div class="encryption-field">
                        <span class="encryption-field-label">置信度</span>
                        <span class="encryption-field-value">${param.confidence}%</span>
                    </div>
                    <div class="encryption-field">
                        <span class="encryption-field-label">解码值</span>
                        <span class="encryption-field-value">${param.decodedValue || '无法解码'}</span>
                    </div>
                    <div class="encryption-field">
                        <span class="encryption-field-label">状态</span>
                        <span class="encryption-field-value">
                            <span class="encryption-status status-pending">待破解</span>
                        </span>
                    </div>
                </div>
            </div>
        `).join('');

        document.getElementById('btn-export-python').disabled = false;
        document.getElementById('btn-export-nodejs').disabled = false;
    }

    async exportScript(type) {
        if (!this.selectedRequest) return;

        const result = await ipcRenderer.invoke('export-script', type, {
            params: this.selectedRequest.params || {},
            value: this.selectedRequest.value
        });

        this.showModal(`导出 ${type === 'python' ? 'Python' : 'Node.js'} 脚本`, 
            `<pre style="white-space: pre-wrap; word-break: break-all;">${result[type]}</pre>`
        );
    }

    copyRequest() {
        if (!this.selectedRequest) return;
        
        const data = JSON.stringify(this.selectedRequest, null, 2);
        navigator.clipboard.writeText(data);
        this.updateStatus('已复制到剪贴板');
    }

    replayRequest() {
        if (!this.selectedRequest) return;
        this.showModal('重放请求', '功能开发中...');
    }

    showModal(title, content) {
        this.modalTitle.textContent = title;
        this.modalContent.innerHTML = content;
        this.modalContainer.classList.remove('hidden');
    }

    hideModal() {
        this.modalContainer.classList.add('hidden');
    }

    showError(message) {
        this.showModal('错误', `<p style="color: var(--accent-primary);">${message}</p>`);
    }

    truncateUrl(url, maxLength = 60) {
        if (url.length <= maxLength) return url;
        return url.substring(0, maxLength) + '...';
    }

    truncate(str, maxLength = 50) {
        if (!str) return '';
        if (str.length <= maxLength) return str;
        return str.substring(0, maxLength) + '...';
    }

    formatTime(timestamp) {
        if (!timestamp) return '';
        const date = new Date(timestamp);
        return date.toLocaleTimeString();
    }

    getStatusClass(status) {
        if (!status) return 'pending';
        if (status >= 200 && status < 300) return '2xx';
        if (status >= 300 && status < 400) return '3xx';
        if (status >= 400 && status < 500) return '4xx';
        if (status >= 500) return '5xx';
        return 'pending';
    }

    formatJSON(data) {
        if (!data) return '';
        
        try {
            if (typeof data === 'string') {
                const parsed = JSON.parse(data);
                return JSON.stringify(parsed, null, 2);
            }
            return JSON.stringify(data, null, 2);
        } catch (e) {
            return String(data);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
