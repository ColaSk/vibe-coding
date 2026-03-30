const { ipcRenderer } = require('electron');

class App {
    constructor() {
        this.requests = [];
        this.selectedRequest = null;
        this.isAnalyzing = false;
        this.currentUrl = 'about:blank';
        this.currentFilter = 'all';
        this.searchQuery = '';
        this.activeDetailTab = 'overview';
        this.browserHeight = 300;
        this.browserCollapsed = false;
        this._renderDebounceTimer = null;
        this.theme = localStorage.getItem('theme') || 'dark';

        this.init();
    }

    init() {
        this.bindElements();
        this.bindEvents();
        this.setupBrowserListeners();
        this.setupBrowserResize();
        this.setupPanelsResize();
        this.applyTheme(this.theme, false);
        this.updateStatus('就绪');
    }

    bindElements() {
        this.urlInput = document.getElementById('url-input');
        this.btnStart = document.getElementById('btn-start');
        this.btnStop = document.getElementById('btn-stop');
        this.btnExport = document.getElementById('btn-export');
        this.btnTheme = document.getElementById('btn-theme');
        this.requestsList = document.getElementById('requests-list');
        this.requestDetail = document.getElementById('request-detail');
        this.statusText = document.getElementById('status-text');
        this.statusStats = document.getElementById('status-stats');
        this.modalContainer = document.getElementById('modal-container');
        this.modalTitle = document.getElementById('modal-title');
        this.modalContent = document.getElementById('modal-content');
        this.browserContainer = document.getElementById('browser-container');
        this.browserCurrentUrl = document.getElementById('browser-current-url');
        this.btnBack = document.getElementById('btn-back');
        this.btnForward = document.getElementById('btn-forward');
        this.btnRefresh = document.getElementById('btn-refresh');
        this.btnDevtools = document.getElementById('btn-devtools');
        this.btnToggleBrowser = document.getElementById('btn-toggle-browser');
        this.browserSection = document.getElementById('browser-section');
        this.browserResizeHandle = document.getElementById('browser-resize-handle');
        this.requestCount = document.getElementById('request-count');
        this.requestSearch = document.getElementById('request-search');
        this.detailTabsContainer = document.getElementById('detail-tabs-container');
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

        this.requestSearch.addEventListener('input', (e) => {
            this.searchQuery = e.target.value.toLowerCase().trim();
            this.renderRequests();
        });

        document.getElementById('btn-copy-request').addEventListener('click', () => this.copyRequest());
        document.getElementById('btn-replay-request').addEventListener('click', () => this.replayRequest());

        document.querySelector('.modal-overlay').addEventListener('click', () => this.hideModal());
        document.querySelector('.modal-cancel').addEventListener('click', () => this.hideModal());
        document.querySelector('.modal-close').addEventListener('click', () => this.hideModal());

        this.btnBack.addEventListener('click', () => this.browserBack());
        this.btnForward.addEventListener('click', () => this.browserForward());
        this.btnRefresh.addEventListener('click', () => this.browserRefresh());
        this.btnDevtools.addEventListener('click', () => this.openDevtools());
        this.btnToggleBrowser.addEventListener('click', () => this.toggleBrowser());
        this.btnTheme.addEventListener('click', () => this.toggleTheme());
    }

    // ─── 主题切换 ─────────────────────────────────────────────────────────────

    toggleTheme() {
        const next = this.theme === 'dark' ? 'light' : 'dark';
        this.applyTheme(next, true);
    }

    applyTheme(theme, save = true) {
        this.theme = theme;
        document.documentElement.setAttribute('data-theme', theme);

        const icon  = this.btnTheme.querySelector('.theme-icon');
        const label = this.btnTheme.querySelector('.theme-label');
        if (theme === 'dark') {
            icon.textContent  = '🌙';
            label.textContent = '深色';
        } else {
            icon.textContent  = '☀️';
            label.textContent = '浅色';
        }

        if (save) localStorage.setItem('theme', theme);
    }

    // ─── 浏览器面板拖拽缩放 ───────────────────────────────────────────────────

    setupBrowserResize() {
        const handle = this.browserResizeHandle;
        const section = this.browserSection;
        const MIN_HEIGHT = 44;   // 只露出 toolbar
        const MAX_RATIO = 0.72;  // 最多占可用高度的 72%

        let startY = 0;
        let startH = 0;
        let dragging = false;

        const onMouseMove = (e) => {
            if (!dragging) return;
            const mainH = document.querySelector('.main-content').clientHeight;
            const maxH = Math.floor(mainH * MAX_RATIO);
            let newH = startH + (e.clientY - startY);
            newH = Math.max(MIN_HEIGHT, Math.min(maxH, newH));

            this.browserHeight = newH;
            section.style.height = newH + 'px';

            // 展开时同步取消折叠状态
            if (newH > MIN_HEIGHT) {
                this.browserCollapsed = false;
                section.classList.remove('collapsed');
                this.btnToggleBrowser.textContent = '▼';
                this.showBrowserPlaceholder(false);
            }
        };

        const onMouseUp = () => {
            if (!dragging) return;
            dragging = false;
            section.classList.remove('resizing');
            handle.classList.remove('active');
            document.body.style.cursor = '';
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);
            // 通知主进程更新 BrowserView 边界
            ipcRenderer.invoke('show-browser');
        };

        handle.addEventListener('mousedown', (e) => {
            if (this.browserCollapsed) return;
            dragging = true;
            startY = e.clientY;
            startH = section.offsetHeight;
            section.classList.add('resizing');
            handle.classList.add('active');
            document.body.style.cursor = 'row-resize';
            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
            e.preventDefault();
        });
    }

    setupPanelsResize() {
        const handle = document.getElementById('panels-resize-handle');
        const leftPanel = document.getElementById('requests-panel');
        const container = document.getElementById('panel-container');
        const MIN_WIDTH = 180;

        let startX = 0;
        let startW = 0;
        let dragging = false;

        const onMouseMove = (e) => {
            if (!dragging) return;
            const containerW = container.clientWidth;
            const maxW = containerW - MIN_WIDTH - handle.offsetWidth;
            let newW = startW + (e.clientX - startX);
            newW = Math.max(MIN_WIDTH, Math.min(maxW, newW));
            leftPanel.style.width = newW + 'px';
        };

        const onMouseUp = () => {
            if (!dragging) return;
            dragging = false;
            handle.classList.remove('active');
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);
        };

        handle.addEventListener('mousedown', (e) => {
            dragging = true;
            startX = e.clientX;
            startW = leftPanel.offsetWidth;
            handle.classList.add('active');
            document.body.style.cursor = 'col-resize';
            document.body.style.userSelect = 'none';
            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
            e.preventDefault();
        });
    }

    toggleBrowser() {
        if (this.browserCollapsed) {
            // 展开
            this.browserCollapsed = false;
            this.browserSection.classList.remove('collapsed');
            this.browserSection.style.height = this.browserHeight + 'px';
            this.btnToggleBrowser.textContent = '▼';
            setTimeout(() => ipcRenderer.invoke('show-browser'), 160);
        } else {
            // 折叠
            this.browserCollapsed = true;
            this.browserSection.classList.add('collapsed');
            this.btnToggleBrowser.textContent = '▶';
        }
    }

    setupBrowserListeners() {
        ipcRenderer.on('browser-url-changed', (event, url) => {
            this.currentUrl = url;
            this.browserCurrentUrl.textContent = url;
        });

        ipcRenderer.on('browser-loading', (event, isLoading) => {
            this.btnRefresh.textContent = isLoading ? '⏳' : '🔄';
        });

        // 实时接收主进程推送的请求/响应事件
        ipcRenderer.on('request-captured', (event, payload) => {
            if (!this.isAnalyzing) return;
            this.addOrUpdateRequest(payload);
        });

        ipcRenderer.on('browser-load-error', (event, message) => {
            this.updateStatus(`加载出错: ${message}`);
        });
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
        this.showBrowserPlaceholder(false);

        // 若浏览器面板已折叠则自动展开
        if (this.browserCollapsed) this.toggleBrowser();

        try {
            const result = await ipcRenderer.invoke('start-analysis', url);

            if (result.success) {
                // 浏览器已启动，请求将通过 request-captured 事件实时推送
                this.updateStatus('正在捕获请求，遇到验证码请手动通过后继续...');
            } else {
                this.showError(result.error);
                this.updateStatus('启动失败');
                this.isAnalyzing = false;
                this.updateUI();
            }
        } catch (error) {
            this.showError(error.message);
            this.updateStatus('启动失败');
            this.isAnalyzing = false;
            this.updateUI();
        }
        // 注意：不在这里设置 isAnalyzing = false
        // 捕获会持续进行，直到用户点击"停止"
    }

    async stopAnalysis() {
        await ipcRenderer.invoke('stop-analysis');
        this.isAnalyzing = false;
        clearTimeout(this._renderDebounceTimer);
        this.updateUI();
        this.updateStatus(`已停止，共捕获 ${this.requests.length} 条请求`);
        this.showBrowserPlaceholder(true);
    }

    // ─── 实时请求增量更新 ──────────────────────────────────────────────────────

    addOrUpdateRequest(payload) {
        const { type, data } = payload;

        if (type === 'request') {
            // 新请求进来：加入列表（去重）
            if (!this.requests.find(r => String(r.id) === String(data.id))) {
                this.requests.push(data);
            }
        } else if (type === 'response') {
            // 响应回来：更新对应请求的状态和响应数据
            const updated = data.request;
            if (!updated) return;
            const idx = this.requests.findIndex(r => String(r.id) === String(updated.id));
            if (idx >= 0) {
                this.requests[idx] = updated;
                // 若当前正在查看该请求的详情，同步刷新详情面板
                if (this.selectedRequest && String(this.selectedRequest.id) === String(updated.id)) {
                    this.selectedRequest = updated;
                    this.renderRequestDetail();
                }
            }
        }

        // 立即更新计数徽标
        if (this.requestCount) this.requestCount.textContent = this.requests.length;

        // 防抖重绘列表（避免高频请求时频繁整体重绘）
        clearTimeout(this._renderDebounceTimer);
        this._renderDebounceTimer = setTimeout(() => {
            this.renderRequests();
            this.statusStats.innerHTML = `
                <span class="stat-item">请求: ${this.requests.length}</span>
            `;
        }, 200);
    }

    async browserBack() { await ipcRenderer.invoke('browser-back'); }
    async browserForward() { await ipcRenderer.invoke('browser-forward'); }
    async browserRefresh() { await ipcRenderer.invoke('browser-refresh'); }
    async openDevtools() { await ipcRenderer.invoke('browser-devtools'); }

    showBrowserPlaceholder(show) {
        const placeholder = this.browserContainer.querySelector('.browser-placeholder');
        if (placeholder) placeholder.style.display = show ? 'flex' : 'none';
    }

    isValidUrl(string) {
        try { new URL(string); return true; } catch (_) { return false; }
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
        this.statusStats.innerHTML = `
            <span class="stat-item">请求: ${this.requests.length}</span>
            <span class="stat-item">API: ${apiCount}</span>
        `;
    }

    clearResults() {
        this.requests = [];
        this.selectedRequest = null;
        this.searchQuery = '';
        if (this.requestSearch) this.requestSearch.value = '';
        this.requestsList.innerHTML = `<div class="empty-state"><p>正在捕获网络请求...</p></div>`;
        this.requestDetail.innerHTML = `<div class="empty-state"><p>选择一个请求查看详情</p></div>`;
        if (this.requestCount) this.requestCount.textContent = '0';
        if (this.detailTabsContainer) {
            this.detailTabsContainer.innerHTML = '';
            this.detailTabsContainer.classList.add('hidden');
        }
    }

    // ─── 请求列表 ────────────────────────────────────────────────────────────

    filterRequests(filter) {
        this.currentFilter = filter;
        // 只对带 data-filter 的按钮切换 active，避免影响详情 Tab 按钮
        document.querySelectorAll('.filter-btn[data-filter]').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
        this.renderRequests();
    }

    renderRequests() {
        let filtered = this.requests;

        switch (this.currentFilter) {
            case 'api':
                filtered = filtered.filter(r => r.resourceType === 'xhr' || r.resourceType === 'fetch');
                break;
            case 'xhr':
                filtered = filtered.filter(r => r.resourceType === 'xhr');
                break;
            case 'encrypted':
                filtered = filtered.filter(r => r.hasEncryption === true);
                break;
        }

        if (this.searchQuery) {
            filtered = filtered.filter(r => r.url.toLowerCase().includes(this.searchQuery));
        }

        if (this.requestCount) this.requestCount.textContent = this.requests.length;

        if (filtered.length === 0) {
            this.requestsList.innerHTML = `<div class="empty-state"><p>没有找到匹配的请求</p></div>`;
            return;
        }

        this.requestsList.innerHTML = filtered.map(req => {
            const isActive = String(this.selectedRequest?.id) === String(req.id);
            let urlObj = null;
            try { urlObj = new URL(req.url); } catch (_) {}

            const path = urlObj ? (urlObj.pathname + (urlObj.search || '')) : req.url;
            const host = urlObj ? urlObj.hostname : '';
            const method = (req.method || 'GET').toUpperCase();
            const statusCode = req.response?.status;
            const statusClass = this.getStatusClass(statusCode);
            const statusLabel = statusCode || (req.status === 'pending' ? '···' : req.status || '···');
            const resType = req.resourceType || 'other';

            return `
                <div class="request-item ${isActive ? 'active' : ''}" data-id="${req.id}">
                    <div class="request-item-method">
                        <span class="request-method method-${method.toLowerCase()}">${method}</span>
                    </div>
                    <div class="request-item-info">
                        <div class="request-path" title="${this.escapeHtml(req.url)}">${this.escapeHtml(this.truncateUrl(path, 52))}</div>
                        <div class="request-meta">
                            <span class="request-host">${this.escapeHtml(host)}</span>
                            <span class="request-type-tag">${resType}</span>
                            ${req.hasEncryption ? '<span class="has-encryption" title="检测到加密参数">🔐</span>' : ''}
                        </div>
                    </div>
                    <div class="request-item-right">
                        <span class="request-status status-${statusClass}">${statusLabel}</span>
                        <span class="request-time">${this.formatTime(req.timestamp)}</span>
                    </div>
                </div>
            `;
        }).join('');

        this.requestsList.querySelectorAll('.request-item').forEach(item => {
            item.addEventListener('click', () => this.selectRequest(item.dataset.id));
        });
    }

    selectRequest(id) {
        this.selectedRequest = this.requests.find(r => String(r.id) === String(id));
        if (!this.selectedRequest) return;

        // 只更新 active 状态，不重新渲染整个列表
        this.requestsList.querySelectorAll('.request-item').forEach(item => {
            item.classList.toggle('active', item.dataset.id === String(id));
        });

        this.activeDetailTab = 'overview';
        this.renderRequestDetail();

        document.getElementById('btn-copy-request').disabled = false;
        document.getElementById('btn-replay-request').disabled = false;
    }

    // ─── 请求详情（Tab 式） ───────────────────────────────────────────────────

    renderRequestDetail() {
        if (!this.selectedRequest) return;

        const tabs = [
            { id: 'overview',    label: '概览' },
            { id: 'req-headers', label: '请求头' },
            { id: 'req-params',  label: '参数' },
            { id: 'res-headers', label: '响应头' },
            { id: 'res-body',    label: '响应体' },
        ];

        // 将 Tab 渲染到 panel-header 的第二行，复用 filter-btn 样式
        this.detailTabsContainer.innerHTML = tabs.map(t => `
            <button class="filter-btn ${this.activeDetailTab === t.id ? 'active' : ''}"
                    data-tab="${t.id}">${t.label}</button>
        `).join('');
        this.detailTabsContainer.classList.remove('hidden');

        this.detailTabsContainer.querySelectorAll('.filter-btn[data-tab]').forEach(btn => {
            btn.addEventListener('click', () => {
                this.activeDetailTab = btn.dataset.tab;
                this.detailTabsContainer.querySelectorAll('.filter-btn[data-tab]').forEach(b => {
                    b.classList.toggle('active', b.dataset.tab === this.activeDetailTab);
                });
                this.renderDetailTabContent();
            });
        });

        // 内容区只放内容容器
        this.requestDetail.innerHTML = '<div class="detail-tab-content" id="detail-tab-content"></div>';

        this.renderDetailTabContent();
    }

    renderDetailTabContent() {
        const req = this.selectedRequest;
        const content = document.getElementById('detail-tab-content');
        if (!content || !req) return;

        switch (this.activeDetailTab) {
            case 'overview':
                content.innerHTML = this.buildOverviewTab(req);
                break;
            case 'req-headers':
                content.innerHTML = this.buildHeadersTable(req.headers || {}, '无请求头信息');
                break;
            case 'req-params':
                content.innerHTML = this.buildParamsTab(req);
                break;
            case 'res-headers':
                content.innerHTML = req.response
                    ? this.buildHeadersTable(req.response.headers || {}, '无响应头信息')
                    : '<div class="empty-state"><p>暂无响应数据</p></div>';
                break;
            case 'res-body':
                content.innerHTML = req.response
                    ? this.buildResponseBody(req.response)
                    : '<div class="empty-state"><p>暂无响应数据</p></div>';
                break;
        }

        // 绑定响应体复制按钮
        const copyCodeBtn = content.querySelector('.btn-copy-code');
        if (copyCodeBtn) {
            copyCodeBtn.addEventListener('click', () => {
                const body = req.response?.body;
                if (body != null) {
                    navigator.clipboard.writeText(typeof body === 'string' ? body : JSON.stringify(body, null, 2));
                    this.updateStatus('已复制到剪贴板');
                }
            });
        }
    }

    buildOverviewTab(req) {
        let urlObj = null;
        try { urlObj = new URL(req.url); } catch (_) {}

        const method = (req.method || 'GET').toUpperCase();
        const statusCode = req.response?.status;
        const statusClass = this.getStatusClass(statusCode);

        const statusHtml = statusCode
            ? `<span class="request-status status-${statusClass}">${statusCode}</span> <span class="text-muted">${this.escapeHtml(req.response.statusText || '')}</span>`
            : `<span class="text-muted">${req.status || 'pending'}</span>`;

        return `
            <div class="overview-url">${this.escapeHtml(req.url)}</div>
            <div class="kv-table">
                <div class="kv-row">
                    <span class="kv-key">方法</span>
                    <span class="kv-val"><span class="request-method method-${method.toLowerCase()}">${method}</span></span>
                </div>
                <div class="kv-row">
                    <span class="kv-key">状态</span>
                    <span class="kv-val">${statusHtml}</span>
                </div>
                <div class="kv-row">
                    <span class="kv-key">类型</span>
                    <span class="kv-val">${this.escapeHtml(req.resourceType || 'other')}</span>
                </div>
                ${urlObj ? `
                <div class="kv-row">
                    <span class="kv-key">域名</span>
                    <span class="kv-val">${this.escapeHtml(urlObj.hostname)}</span>
                </div>
                <div class="kv-row">
                    <span class="kv-key">路径</span>
                    <span class="kv-val">${this.escapeHtml(urlObj.pathname)}</span>
                </div>
                ` : ''}
                <div class="kv-row">
                    <span class="kv-key">时间</span>
                    <span class="kv-val">${req.timestamp ? new Date(req.timestamp).toLocaleString() : '-'}</span>
                </div>
                ${req.hasEncryption ? `
                <div class="kv-row">
                    <span class="kv-key">加密</span>
                    <span class="kv-val"><span class="encryption-badge">🔐 检测到加密参数</span></span>
                </div>
                ` : ''}
            </div>
        `;
    }

    buildHeadersTable(headers, emptyMsg = '无数据') {
        const entries = Object.entries(headers);
        if (entries.length === 0) {
            return `<div class="empty-state"><p>${emptyMsg}</p></div>`;
        }
        return `
            <div class="kv-table">
                ${entries.map(([key, value]) => `
                    <div class="kv-row">
                        <span class="kv-key">${this.escapeHtml(key)}</span>
                        <span class="kv-val">${this.escapeHtml(String(value))}</span>
                    </div>
                `).join('')}
            </div>
        `;
    }

    buildParamsTab(req) {
        let urlObj = null;
        try { urlObj = new URL(req.url); } catch (_) {}

        const queryParams = urlObj ? Array.from(urlObj.searchParams.entries()) : [];
        let html = '';

        if (queryParams.length > 0) {
            html += `
                <div class="params-section-title">Query 参数</div>
                <div class="kv-table">
                    ${queryParams.map(([k, v]) => `
                        <div class="kv-row">
                            <span class="kv-key">${this.escapeHtml(k)}</span>
                            <span class="kv-val">${this.escapeHtml(v)}</span>
                        </div>
                    `).join('')}
                </div>
            `;
        }

        if (req.postData) {
            html += `
                <div class="params-section-title" style="margin-top:14px;">请求体</div>
                <div class="code-block">
                    <pre>${this.escapeHtml(this.formatJSON(req.postData))}</pre>
                </div>
            `;
        }

        return html || '<div class="empty-state"><p>无请求参数</p></div>';
    }

    buildResponseBody(response) {
        const bodyType = response.bodyType || 'text';

        if (bodyType === 'loading') {
            return '<div class="empty-state"><p>正在获取响应体...</p></div>';
        }
        if (bodyType === 'unavailable') {
            return '<div class="empty-state"><p>响应体不可用（可能为流式或已被丢弃）</p></div>';
        }
        if (bodyType === 'binary') {
            return `<div class="empty-state"><p>${this.escapeHtml(String(response.body || '[Binary]'))}</p></div>`;
        }
        if (response.body == null || response.body === '') {
            return '<div class="empty-state"><p>响应体为空</p></div>';
        }

        return `
            <div class="code-block">
                <div class="code-block-header">
                    <span class="code-type">${this.escapeHtml(bodyType)}</span>
                    <button class="btn-copy-code">复制</button>
                </div>
                <pre>${this.escapeHtml(this.formatJSON(response.body))}</pre>
            </div>
        `;
    }

    // ─── 工具方法 ─────────────────────────────────────────────────────────────

    copyRequest() {
        if (!this.selectedRequest) return;
        navigator.clipboard.writeText(JSON.stringify(this.selectedRequest, null, 2));
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

    escapeHtml(str) {
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    truncateUrl(url, maxLength = 60) {
        if (url.length <= maxLength) return url;
        return url.substring(0, maxLength) + '…';
    }

    formatTime(timestamp) {
        if (!timestamp) return '';
        return new Date(timestamp).toLocaleTimeString();
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
        if (data == null) return '';
        try {
            if (typeof data === 'string') {
                return JSON.stringify(JSON.parse(data), null, 2);
            }
            return JSON.stringify(data, null, 2);
        } catch (_) {
            return String(data);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
