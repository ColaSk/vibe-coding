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
        this.setupAgentResize();
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

        // Agent 面板
        this.btnAgent          = document.getElementById('btn-agent');
        this.agentPanel        = document.getElementById('agent-panel');
        this.agentResizeHandle = document.getElementById('agent-resize-handle');
        this.agentMessages     = document.getElementById('agent-messages');
        this.agentInput        = document.getElementById('agent-input');
        this.agentModelInput   = document.getElementById('agent-model');
        this.agentHostInput    = document.getElementById('agent-host');
        this.agentStatusDot    = document.getElementById('agent-status-dot');
        this.btnAgentSend      = document.getElementById('btn-agent-send');
    }

    bindEvents() {
        this.btnStart.addEventListener('click', () => this.startAnalysis());
        this.btnStop.addEventListener('click', () => this.stopAnalysis());

        this.urlInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.startAnalysis();
        });

        document.querySelectorAll('.filter-btn[data-filter]').forEach(btn => {
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

        // Agent 面板事件
        this.btnAgent.addEventListener('click', () => this.openAgentPanel());
        document.getElementById('btn-agent-close').addEventListener('click', () => this.closeAgentPanel());
        this.btnAgentSend.addEventListener('click', () => this.sendAgentMessage());
        document.getElementById('btn-agent-verify').addEventListener('click', () => this.verifyOllama());

        // Ctrl/Cmd + Enter 发送
        this.agentInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
                e.preventDefault();
                this.sendAgentMessage();
            }
        });

        // 监听 Agent 流式事件
        ipcRenderer.on('agent-stream', (_, ev) => this.handleAgentStream(ev));

        // 初始化：读取保存的模型配置
        ipcRenderer.invoke('llm-config-get').then(cfg => {
            if (cfg && cfg.model) this.agentModelInput.value = cfg.model;
            if (cfg && cfg.host && cfg.host !== 'http://localhost:11434') {
                this.agentHostInput.value = cfg.host;
            }
        });
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
        const MIN_HEIGHT     = 44;   // 只露出 toolbar
        const MIN_ANALYSIS_H = 180;  // 请求/详情面板最低高度
        const GAP            = 20;   // main-content 的 gap
        const HANDLE_H       = 8;    // browser-resize-handle 高度
        const PADDING_V      = 40;   // main-content 上下 padding 合计

        let startY = 0;
        let startH = 0;
        let dragging = false;

        const onMouseMove = (e) => {
            if (!dragging) return;
            const col = document.querySelector('.main-col');
            const urlSection = document.querySelector('.url-input-section');
            // 真实可分配给浏览器的最大高度：总高减去 padding、URL区、间距、手柄、最小分析区
            const mainH = col.clientHeight;
            const urlH  = urlSection ? urlSection.offsetHeight : 100;
            const maxH  = mainH - PADDING_V - urlH - GAP * 3 - HANDLE_H - MIN_ANALYSIS_H;
            let newH = startH + (e.clientY - startY);
            newH = Math.max(MIN_HEIGHT, Math.min(Math.max(MIN_HEIGHT, maxH), newH));

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

    setupAgentResize() {
        const handle = this.agentResizeHandle;
        const panel  = this.agentPanel;
        const MIN_WIDTH = 260;
        const MAX_WIDTH = 720;

        let startX = 0;
        let startW = 0;
        let dragging = false;

        const onMouseMove = (e) => {
            if (!dragging) return;
            // 手柄在面板左侧：鼠标左移(负 delta) → 面板变宽
            let newW = startW - (e.clientX - startX);
            newW = Math.max(MIN_WIDTH, Math.min(MAX_WIDTH, newW));
            panel.style.width = newW + 'px';
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
            startW = panel.offsetWidth;
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
        this.updateAgentButton();
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
            this.updateAgentButton();
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

    // ─── Agent 面板 ────────────────────────────────────────────────────────────

    /** 更新 Agent 发送按钮的可用状态（需要有已捕获请求） */
    updateAgentButton() {
        if (!this.btnAgentSend) return;
        // 发送按钮：有请求数据且面板已打开时才可用
        const panelOpen = !this.agentPanel.classList.contains('hidden');
        this.btnAgentSend.disabled = !(this.requests.length > 0 && panelOpen);
    }

    /** 展开 Agent 面板 */
    openAgentPanel() {
        this.agentPanel.classList.remove('hidden');
        this.agentResizeHandle.classList.remove('hidden');
        this.btnAgent.classList.add('active');
        this.btnAgentSend.disabled = this.requests.length === 0;
    }

    /** 收起 Agent 面板 */
    closeAgentPanel() {
        this.agentPanel.classList.add('hidden');
        this.agentResizeHandle.classList.add('hidden');
        this.btnAgent.classList.remove('active');
        this.btnAgentSend.disabled = true;
    }

    /** 验证 Ollama 连接 */
    async verifyOllama() {
        const model = this.agentModelInput.value.trim();
        const host  = this.agentHostInput.value.trim() || 'http://localhost:11434';

        // 保存配置
        await ipcRenderer.invoke('llm-config-save', {
            provider: 'ollama',
            model:    model || 'qwen2.5:7b',
            host:     host
        });

        // 更新状态圆点为检测中
        this.agentStatusDot.className = 'agent-status-dot checking';
        this.agentStatusDot.title = '连接中...';

        // 清除首次空状态提示
        const emptyState = this.agentMessages.querySelector('.empty-state');
        if (emptyState) emptyState.remove();

        // 在消息区显示检测提示
        const checkingBubble = this._appendBubble('assistant',
            `正在连接 Ollama...\n地址：${host}\n模型：${model || 'qwen2.5:7b'}`
        );

        const result = await ipcRenderer.invoke('llm-verify');

        // 移除检测提示，换成结果
        if (checkingBubble.parentNode) checkingBubble.remove();

        if (result.success) {
            this.agentStatusDot.className = 'agent-status-dot connected';
            const modelList = (result.models || []);
            const modelStr  = modelList.length
                ? modelList.map(m => `• ${m}`).join('\n')
                : '（未发现已下载模型，请先在服务端执行 ollama pull <模型名>）';

            this._appendBubble('assistant',
                `✅ 连接成功（${result.latency_ms}ms）\n\n` +
                `地址：${host}\n` +
                `当前模型：${model || 'qwen2.5:7b'}\n\n` +
                `服务端已有模型：\n${modelStr}\n\n` +
                `捕获请求后即可点击「发送」开始分析。`
            );
            this.agentStatusDot.title = `已连接 · ${result.latency_ms}ms`;
        } else {
            this.agentStatusDot.className = 'agent-status-dot disconnected';
            this._appendBubble('error',
                `❌ 连接失败：${result.error}\n\n` +
                `地址：${host}\n\n` +
                `请检查：\n• 远端 Ollama 服务是否正在运行\n• 地址和端口是否正确\n• 防火墙是否放通了该端口`
            );
            this.agentStatusDot.title = '连接失败';
        }
    }

    /** 发送用户消息，启动 Agent 推理循环 */
    async sendAgentMessage() {
        const text = this.agentInput.value.trim();
        if (!text) return;
        if (this.requests.length === 0) {
            this._appendBubble('error', '请先捕获页面请求再进行 Agent 分析。');
            return;
        }

        // 清空输入框，禁用发送按钮
        this.agentInput.value = '';
        this.btnAgentSend.disabled = true;

        // 清除首次空状态提示
        const emptyState = this.agentMessages.querySelector('.empty-state');
        if (emptyState) emptyState.remove();

        // 追加用户气泡
        this._appendBubble('user', text);

        // 追加"思考中"动画
        const thinkingEl = this._appendThinking();

        // 保存当前模型配置
        const model = this.agentModelInput.value.trim();
        const host  = this.agentHostInput.value.trim() || 'http://localhost:11434';
        if (model) {
            await ipcRenderer.invoke('llm-config-save', {
                provider: 'ollama',
                model:    model,
                host:     host
            });
        }

        // 构建历史（只取气泡内容，最近 10 条，避免 context 过长）
        const history = this._buildMessageHistory();

        await ipcRenderer.invoke('agent-chat', { message: text, history });

        // 移除思考动画（会在 handleAgentStream done/error 时处理）
        thinkingEl._remove = () => {
            if (thinkingEl.parentNode) thinkingEl.remove();
        };
    }

    /** 处理主进程推送的流式事件 */
    handleAgentStream(ev) {
        // 移除已有的思考动画
        const removeThinking = () => {
            const el = this.agentMessages.querySelector('.agent-thinking');
            if (el) el.remove();
        };

        switch (ev.type) {
            case 'capture-started':
                // Agent 主动触发导航：同步渲染进程 UI 状态
                removeThinking();
                this.isAnalyzing = true;
                this.clearResults();
                this.urlInput.value = ev.url;
                this.showBrowserPlaceholder(false);
                if (this.browserCollapsed) this.toggleBrowser();
                this.updateUI();
                this.updateStatus('Agent 正在抓包中...');
                this._removeProgressBubble();
                this._appendBubble('assistant', `🌐 正在打开 ${ev.url}`);
                break;

            case 'progress':
                // 抓包等待期间的实时进度（复用同一个进度气泡，避免刷屏）
                this._upsertProgressBubble(ev.message);
                this.updateStatus(`抓包中：${ev.message}`);
                break;

            case 'thinking':
                // 每轮 LLM 推理开始前：清理进度气泡，显示思考动画
                this._removeProgressBubble();
                removeThinking();
                this._appendThinking(ev.round);
                break;

            case 'text':
                removeThinking();
                if (ev.content && ev.content.trim()) {
                    this._appendBubble('assistant', ev.content);
                }
                break;

            case 'tool_step':
                removeThinking();
                this._appendToolCard(ev);
                break;

            case 'done':
                removeThinking();
                this._removeProgressBubble();
                // 若是 Agent 触发的抓包会话，分析完成后自动停止抓包
                if (this.isAnalyzing) {
                    this.isAnalyzing = false;
                    this.updateUI();
                    this.updateStatus(`分析完成，共捕获 ${this.requests.length} 条请求`);
                }
                this.btnAgentSend.disabled = false;
                this.agentInput.focus();
                break;

            case 'error':
                removeThinking();
                this._removeProgressBubble();
                this._appendBubble('error', ev.message || '发生未知错误');
                if (this.isAnalyzing) {
                    this.isAnalyzing = false;
                    this.updateUI();
                }
                this.btnAgentSend.disabled = false;
                break;
        }
    }

    /** 创建或更新进度气泡（保持单一，避免刷屏） */
    _upsertProgressBubble(message) {
        let el = this.agentMessages.querySelector('.agent-progress-bubble');
        if (!el) {
            el = document.createElement('div');
            el.className = 'agent-bubble assistant agent-progress-bubble';
            this.agentMessages.appendChild(el);
        }
        el.textContent = `⏳ ${message}`;
        this._scrollAgentToBottom();
    }

    /** 移除进度气泡 */
    _removeProgressBubble() {
        const el = this.agentMessages.querySelector('.agent-progress-bubble');
        if (el) el.remove();
    }

    /** 追加文本气泡 */
    _appendBubble(role, content) {
        const div = document.createElement('div');
        div.className = `agent-bubble ${role}`;
        div.textContent = content;
        this.agentMessages.appendChild(div);
        this._scrollAgentToBottom();
        return div;
    }

    /** 追加工具调用卡片（可折叠 details） */
    _appendToolCard(ev) {
        const toolLabels = {
            navigate_and_capture:      '打开页面并抓包',
            identify_list_apis:        '识别列表接口',
            analyze_encryption_params: '检测加密参数',
            get_request_detail:        '获取请求详情',
            get_js_sources:            '列举 JS 文件',
            generate_solution_script:  '生成复现脚本'
        };
        const label = toolLabels[ev.toolName] || ev.toolName;

        const details = document.createElement('details');
        details.className = 'agent-tool-card';

        // 结果摘要（一行文字）
        let summary1Line = '';
        if (ev.result && !ev.result.error) {
            if (ev.toolName === 'navigate_and_capture') {
                summary1Line = `捕获 ${ev.result.captured} 条请求`;
            } else if (ev.toolName === 'identify_list_apis') {
                summary1Line = `找到 ${ev.result.count} 个候选接口`;
            } else if (ev.toolName === 'analyze_encryption_params') {
                summary1Line = `检测到 ${(ev.result.encrypted_params || []).length} 个加密参数`;
            } else if (ev.toolName === 'get_js_sources') {
                summary1Line = `共 ${ev.result.count} 个 JS 文件`;
            } else if (ev.toolName === 'generate_solution_script') {
                summary1Line = '脚本生成成功';
            } else {
                summary1Line = '完成';
            }
        } else if (ev.result?.error) {
            summary1Line = `错误: ${ev.result.error}`;
        }

        details.innerHTML = `
            <summary>
                <span>🔧</span>
                <span class="tool-name">${this.escapeHtml(label)}</span>
                <span style="color:var(--text-muted);font-size:11px;flex:1;margin-left:4px">${this.escapeHtml(summary1Line)}</span>
                <span class="tool-elapsed">${ev.elapsed_ms}ms</span>
            </summary>
            <div class="agent-tool-body">
                <div class="agent-tool-section-label">输入参数</div>
                <pre>${this.escapeHtml(JSON.stringify(ev.input, null, 2))}</pre>
                <div class="agent-tool-section-label" style="margin-top:6px">返回结果</div>
                <pre>${this.escapeHtml(JSON.stringify(ev.result, null, 2))}</pre>
            </div>
        `;

        this.agentMessages.appendChild(details);
        this._scrollAgentToBottom();
        return details;
    }

    /** 追加"思考中"动画，round 为当前推理轮次（可选） */
    _appendThinking(round) {
        const div = document.createElement('div');
        div.className = 'agent-thinking';
        const label = round && round > 1 ? `第 ${round} 轮推理中...` : '思考中...';
        div.innerHTML = `
            <div class="agent-thinking-dot"></div>
            <div class="agent-thinking-dot"></div>
            <div class="agent-thinking-dot"></div>
            <span style="margin-left:4px;font-size:11px">${label}</span>
        `;
        this.agentMessages.appendChild(div);
        this._scrollAgentToBottom();
        return div;
    }

    /** 滚动消息区到底部 */
    _scrollAgentToBottom() {
        this.agentMessages.scrollTop = this.agentMessages.scrollHeight;
    }

    /**
     * 从 DOM 中提取最近的对话历史（最多 10 条），
     * 用于多轮对话时向主进程传递上下文
     */
    _buildMessageHistory() {
        const bubbles = this.agentMessages.querySelectorAll('.agent-bubble:not(.error)');
        const history = [];
        bubbles.forEach(b => {
            const role = b.classList.contains('user') ? 'user' : 'assistant';
            const content = b.textContent.trim();
            if (content) history.push({ role, content });
        });
        // 只保留最近 10 条（避免 context 过长）
        return history.slice(-10);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
