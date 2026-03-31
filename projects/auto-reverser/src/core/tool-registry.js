/**
 * ToolRegistry — 注册分析工具，为 LLM Agent 提供 Tool Schema 和执行函数
 *
 * 5 个 MVP 工具：
 *   1. identify_list_apis       — 识别列表型数据接口
 *   2. analyze_encryption_params — 检测加密参数
 *   3. get_request_detail        — 获取单条请求完整信息
 *   4. get_js_sources            — 列举已捕获的 JS 文件
 *   5. generate_solution_script  — 生成签名复现代码
 */
class ToolRegistry {
    /**
     * @param {object} cdpInterceptor
     * @param {object} apiAnalyzer
     * @param {object} encryptionAnalyzer
     * @param {object} encryptionCracker
     * @param {object} options
     * @param {function} options.navigateCallback  - async (url: string) => void，触发浏览器导航
     * @param {function} options.progressCallback  - (message: string, count: number) => void，实时推送进度
     */
    constructor(cdpInterceptor, apiAnalyzer, encryptionAnalyzer, encryptionCracker, options = {}) {
        this.cdpInterceptor      = cdpInterceptor;
        this.apiAnalyzer         = apiAnalyzer;
        this.encryptionAnalyzer  = encryptionAnalyzer;
        this.encryptionCracker   = encryptionCracker;
        this.navigateCallback    = options.navigateCallback  || null;
        this.progressCallback    = options.progressCallback  || (() => {});

        this._tools = this._buildTools();
    }

    // ─── 公共接口 ─────────────────────────────────────────────────────────────

    /** 返回传给 LLM 的 tool schema 数组 */
    getSchemas() {
        return this._tools.map(t => t.schema);
    }

    /** 根据名称执行工具，返回结果对象 */
    async execute(name, args) {
        const tool = this._tools.find(t => t.schema.name === name);
        if (!tool) {
            return { error: `Unknown tool: ${name}` };
        }
        try {
            return await tool.execute(args || {});
        } catch (err) {
            return { error: err.message };
        }
    }

    // ─── 工具定义 ─────────────────────────────────────────────────────────────

    _buildTools() {
        return [
            this._navigateAndCapture(),
            this._identifyListApis(),
            this._analyzeEncryptionParams(),
            this._getRequestDetail(),
            this._getJsSources(),
            this._generateSolutionScript()
        ];
    }

    // 0. navigate_and_capture
    _navigateAndCapture() {
        return {
            schema: {
                name: 'navigate_and_capture',
                description:
                    '在内置浏览器中打开指定 URL，自动等待页面加载并捕获所有网络请求。' +
                    '当用户提供目标网站 URL 时，必须首先调用此工具完成数据采集，再进行后续分析。' +
                    '工具会等待网络空闲（连续 2 秒无新请求）或达到最大等待时间后返回。',
                parameters: {
                    type: 'object',
                    properties: {
                        url: {
                            type: 'string',
                            description: '要访问的目标页面 URL，必须包含协议前缀（https://）'
                        },
                        wait_seconds: {
                            type: 'number',
                            description: '最长等待时间（秒），范围 5-30，默认 15'
                        }
                    },
                    required: ['url']
                }
            },
            execute: async ({ url, wait_seconds = 15 } = {}) => {
                if (!this.navigateCallback) {
                    return { error: '导航功能未初始化，请通过正常流程使用 Agent。' };
                }
                if (!url || !url.startsWith('http')) {
                    return { error: '无效的 URL，必须以 http:// 或 https:// 开头。' };
                }

                // 触发浏览器导航（同时通知渲染进程更新 UI）
                await this.navigateCallback(url);

                // 等待网络空闲或超时
                const maxWait      = Math.min(Math.max(wait_seconds, 5), 30) * 1000;
                const idleThreshold = 2500;   // 连续 2.5s 无新请求视为空闲
                const pollInterval  = 800;
                const start         = Date.now();
                let lastCount       = 0;
                let idleSince       = Date.now();

                while (Date.now() - start < maxWait) {
                    await new Promise(r => setTimeout(r, pollInterval));
                    const count = this.cdpInterceptor.getAllRequests().length;

                    if (count !== lastCount) {
                        lastCount = count;
                        idleSince = Date.now();
                        this.progressCallback(`已捕获 ${count} 条请求...`, count);
                    } else if (Date.now() - idleSince >= idleThreshold) {
                        this.progressCallback(`网络空闲，捕获完成（${count} 条）`, count);
                        break;
                    }
                }

                const allRequests = this.cdpInterceptor.getAllRequests();
                const typeStats   = {};
                for (const r of allRequests) {
                    typeStats[r.resourceType] = (typeStats[r.resourceType] || 0) + 1;
                }

                return {
                    url,
                    captured:       allRequests.length,
                    resource_types: typeStats,
                    message:        `成功捕获 ${allRequests.length} 条请求，可继续调用 identify_list_apis 进行分析。`
                };
            }
        };
    }

    // 1. identify_list_apis
    _identifyListApis() {
        return {
            schema: {
                name: 'identify_list_apis',
                description:
                    '扫描所有已捕获的网络请求，识别返回列表型数据（JSON 数组、分页结构）的 API 接口，' +
                    '按置信度评分从高到低排序返回候选列表。分析开始时应首先调用此工具。',
                parameters: {
                    type: 'object',
                    properties: {
                        min_confidence: {
                            type: 'number',
                            description: '最低置信度过滤阈值（0-100），默认 30'
                        },
                        limit: {
                            type: 'integer',
                            description: '最多返回几条候选接口，默认 10'
                        }
                    }
                }
            },
            execute: async ({ min_confidence = 30, limit = 10 } = {}) => {
                const allRequests = this.cdpInterceptor.getAllRequests();
                if (!allRequests.length) {
                    return {
                        count: 0,
                        apis: [],
                        message: '未捕获到任何请求。请在左上角输入目标 URL 后点击「分析」按钮开始捕获，待页面加载完成后再发送问题。'
                    };
                }

                const listApis = await this.apiAnalyzer.findListAPI(allRequests);
                const filtered = listApis
                    .filter(a => a.confidence >= min_confidence)
                    .slice(0, limit);

                return {
                    count: filtered.length,
                    total_captured: allRequests.length,
                    apis: filtered.map(a => ({
                        id:            a.id,
                        url:           a.url,
                        method:        a.method,
                        api_type:      a.apiType,
                        confidence:    a.confidence,
                        has_pagination: a.dataStructure?.hasPagination || false,
                        item_count:    a.dataStructure?.itemCount || 0,
                        fields:        (a.dataStructure?.fields || []).slice(0, 10).map(f => f.name)
                    }))
                };
            }
        };
    }

    // 2. analyze_encryption_params
    _analyzeEncryptionParams() {
        return {
            schema: {
                name: 'analyze_encryption_params',
                description:
                    '分析指定请求的 Query 参数、POST Body 和关键 Headers，检测是否存在加密或签名参数，' +
                    '识别加密类型（MD5/SHA/JWT/Base64 等）及置信度。在发现候选接口后调用此工具。',
                parameters: {
                    type: 'object',
                    properties: {
                        request_id: {
                            type: 'string',
                            description: '要分析的请求 ID（来自 identify_list_apis 结果）'
                        }
                    },
                    required: ['request_id']
                }
            },
            execute: async ({ request_id } = {}) => {
                const req = this.cdpInterceptor.getRequest(request_id);
                if (!req) return { error: `未找到请求 ID: ${request_id}` };

                const apiInfo = await this.apiAnalyzer.analyze(req);
                const params  = apiInfo?.params || {};
                const result  = await this.encryptionAnalyzer.analyze(params);

                return {
                    request_url:       req.url,
                    request_method:    req.method,
                    encrypted_params:  result.encryptedParams.map(p => ({
                        name:            p.name,
                        value_preview:   String(p.value).slice(0, 60) + (p.value.length > 60 ? '...' : ''),
                        encryption_type: p.encryptionType,
                        confidence:      p.confidence,
                        decoded_value:   p.decodedValue
                    })),
                    suspicious_params: result.suspiciousParams.map(p => p.name),
                    combinations:      result.combinations || [],
                    total_params:      Object.keys(params.queryParams || {}).length +
                                       Object.keys(params.bodyParams  || {}).length
                };
            }
        };
    }

    // 3. get_request_detail
    _getRequestDetail() {
        return {
            schema: {
                name: 'get_request_detail',
                description:
                    '获取指定请求 ID 的完整信息，包括请求 URL、方法、请求头、请求体和响应体结构。' +
                    '用于深入了解某个具体接口的细节。',
                parameters: {
                    type: 'object',
                    properties: {
                        request_id: {
                            type: 'string',
                            description: '请求 ID'
                        }
                    },
                    required: ['request_id']
                }
            },
            execute: async ({ request_id } = {}) => {
                const req = this.cdpInterceptor.getRequest(request_id);
                if (!req) return { error: `未找到请求 ID: ${request_id}` };

                const bodyPreview = req.response?.body;
                let bodyStr = '';
                if (typeof bodyPreview === 'object') {
                    bodyStr = JSON.stringify(bodyPreview).slice(0, 500);
                } else if (typeof bodyPreview === 'string') {
                    bodyStr = bodyPreview.slice(0, 500);
                }

                return {
                    id:              req.id,
                    url:             req.url,
                    method:          req.method,
                    status:          req.response?.status,
                    resource_type:   req.resourceType,
                    request_headers: req.headers || {},
                    post_data:       req.postData || null,
                    response_status: req.response?.status,
                    response_headers: req.response?.headers || {},
                    response_body_preview: bodyStr,
                    response_body_type:    req.response?.bodyType
                };
            }
        };
    }

    // 4. get_js_sources
    _getJsSources() {
        return {
            schema: {
                name: 'get_js_sources',
                description:
                    '列举本次会话中已捕获的所有 JavaScript 文件（URL + 大小），' +
                    '用于选择哪些 JS 文件值得进行源码加密溯源分析。',
                parameters: {
                    type: 'object',
                    properties: {
                        limit: {
                            type: 'integer',
                            description: '最多返回几个 JS 文件，默认 20'
                        }
                    }
                }
            },
            execute: async ({ limit = 20 } = {}) => {
                const allRequests = this.cdpInterceptor.getAllRequests();
                const jsFiles = allRequests
                    .filter(r => r.resourceType === 'javascript' &&
                                 r.response?.bodyType === 'javascript' &&
                                 typeof r.response?.body === 'string')
                    .slice(0, limit)
                    .map(r => ({
                        request_id:  String(r.id),
                        url:         r.url,
                        size_bytes:  r.response?.body?.length || 0,
                        status:      r.response?.status
                    }));

                return {
                    count: jsFiles.length,
                    files: jsFiles,
                    note: jsFiles.length === 0
                        ? '未捕获到 JS 文件，可能因为文件已被浏览器缓存（304）。'
                        : ''
                };
            }
        };
    }

    // 5. generate_solution_script
    _generateSolutionScript() {
        return {
            schema: {
                name: 'generate_solution_script',
                description:
                    '根据已确定的加密类型和请求参数，生成 Python 和 Node.js 格式的签名复现脚本，包含使用示例。' +
                    '这通常是分析流程的最后一步。',
                parameters: {
                    type: 'object',
                    properties: {
                        encryption_type: {
                            type: 'string',
                            description: '加密类型，如 MD5、SHA256、Base64、JWT、AES'
                        },
                        params: {
                            type: 'object',
                            description: '请求参数键值对，作为脚本中的示例数据'
                        },
                        secret: {
                            type: 'string',
                            description: '若已知密钥（HMAC secret / AES key），在此传入'
                        }
                    },
                    required: ['encryption_type', 'params']
                }
            },
            execute: async ({ encryption_type, params = {}, secret = '' } = {}) => {
                const scripts = this.encryptionCracker.generateScript(encryption_type, {
                    params,
                    secret
                });
                return {
                    encryption_type,
                    python:  scripts.python,
                    nodejs:  scripts.nodejs
                };
            }
        };
    }
}

module.exports = { ToolRegistry };
