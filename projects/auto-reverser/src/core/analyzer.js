class APIAnalyzer {
    constructor() {
        this.apiPatterns = [
            /\/api\//i,
            /\/v\d+\//i,
            /\/graphql/i,
            /\/query/i,
            /\/list/i,
            /\/data/i,
            /\/search/i,
            /\/get/i,
            /\/post/i,
            /\.json$/i
        ];

        this.listDataPatterns = [
            'list', 'items', 'data', 'results', 'records',
            'entries', 'rows', 'content', 'payload'
        ];

        this.paginationPatterns = [
            'page', 'pageSize', 'limit', 'offset', 'total',
            'count', 'size', 'per_page', 'page_size'
        ];
    }

    async analyze(request) {
        if (!request) return null;

        const analysis = {
            id: request.id,
            url: request.url,
            method: request.method,
            isAPI: false,
            apiType: null,
            confidence: 0,
            params: {},
            response: null,
            dataStructure: null
        };

        analysis.isAPI = this.isDataAPI(request);
        
        if (analysis.isAPI) {
            analysis.apiType = this.getAPIType(request);
            analysis.confidence = this.calculateConfidence(request);
            analysis.params = this.extractParams(request);
            
            if (request.response) {
                analysis.response = request.response;
                analysis.dataStructure = this.analyzeDataStructure(request.response.body);
            }
        }

        return analysis;
    }

    async identifyAPIs(requests) {
        const apiRequests = [];

        for (const request of requests) {
            if (this.isDataAPI(request)) {
                const analysis = await this.analyze(request);
                apiRequests.push(analysis);
            }
        }

        return apiRequests.sort((a, b) => b.confidence - a.confidence);
    }

    isDataAPI(request) {
        const url = request.url;
        const resourceType = request.resourceType;

        if (resourceType === 'xhr' || resourceType === 'fetch') {
            return true;
        }

        if (this.apiPatterns.some(pattern => pattern.test(url))) {
            return true;
        }

        if (request.response) {
            const contentType = request.response.headers?.['content-type'] || '';
            if (contentType.includes('application/json')) {
                return true;
            }
        }

        return false;
    }

    getAPIType(request) {
        const url = request.url.toLowerCase();
        const method = request.method.toLowerCase();

        if (url.includes('/graphql')) return 'graphql';
        if (url.includes('/auth') || url.includes('/login') || url.includes('/token')) return 'auth';
        if (url.includes('/track') || url.includes('/analytics') || url.includes('/log')) return 'tracking';
        if (url.includes('/upload') || url.includes('/file')) return 'upload';
        
        if (this.isListAPI(request)) return 'list';
        
        if (method === 'get') return 'read';
        if (method === 'post') return 'create';
        if (method === 'put' || method === 'patch') return 'update';
        if (method === 'delete') return 'delete';

        return 'unknown';
    }

    isListAPI(request) {
        if (request.response?.body) {
            const body = request.response.body;
            
            if (this.hasListStructure(body)) {
                return true;
            }
        }

        const url = request.url.toLowerCase();
        if (url.includes('list') || url.includes('search') || url.includes('query')) {
            return true;
        }

        const params = this.extractParams(request);
        if (params.queryParams) {
            const queryKeys = Object.keys(params.queryParams).map(k => k.toLowerCase());
            const hasPagination = queryKeys.some(key => 
                this.paginationPatterns.includes(key)
            );
            if (hasPagination) return true;
        }

        return false;
    }

    hasListStructure(data) {
        if (Array.isArray(data)) return true;

        if (typeof data === 'object' && data !== null) {
            for (const pattern of this.listDataPatterns) {
                if (Array.isArray(data[pattern])) {
                    return true;
                }
            }

            for (const pattern of this.paginationPatterns) {
                if (data[pattern] !== undefined) {
                    return true;
                }
            }
        }

        return false;
    }

    analyzeDataStructure(data) {
        if (!data) return null;

        const structure = {
            type: Array.isArray(data) ? 'array' : 'object',
            fields: [],
            isArray: false,
            itemCount: 0,
            hasPagination: false,
            paginationInfo: null
        };

        if (Array.isArray(data)) {
            structure.isArray = true;
            structure.itemCount = data.length;
            
            if (data.length > 0) {
                structure.fields = this.extractFields(data[0]);
            }
        } else if (typeof data === 'object') {
            for (const pattern of this.listDataPatterns) {
                if (Array.isArray(data[pattern])) {
                    structure.isArray = true;
                    structure.itemCount = data[pattern].length;
                    structure.dataField = pattern;
                    
                    if (data[pattern].length > 0) {
                        structure.fields = this.extractFields(data[pattern][0]);
                    }
                    break;
                }
            }

            const paginationInfo = {};
            for (const pattern of this.paginationPatterns) {
                if (data[pattern] !== undefined) {
                    paginationInfo[pattern] = data[pattern];
                    structure.hasPagination = true;
                }
            }
            if (structure.hasPagination) {
                structure.paginationInfo = paginationInfo;
            }
        }

        return structure;
    }

    extractFields(obj, prefix = '') {
        const fields = [];

        if (!obj || typeof obj !== 'object') return fields;

        for (const [key, value] of Object.entries(obj)) {
            const fieldPath = prefix ? `${prefix}.${key}` : key;
            
            const field = {
                name: key,
                path: fieldPath,
                type: this.getValueType(value)
            };

            if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
                field.nested = this.extractFields(value, fieldPath);
            }

            fields.push(field);
        }

        return fields;
    }

    getValueType(value) {
        if (value === null) return 'null';
        if (value === undefined) return 'undefined';
        if (Array.isArray(value)) return 'array';
        if (typeof value === 'object') return 'object';
        if (typeof value === 'string') {
            if (/^\d{4}-\d{2}-\d{2}/.test(value)) return 'date';
            if (/^https?:\/\//.test(value)) return 'url';
            return 'string';
        }
        if (typeof value === 'number') return 'number';
        if (typeof value === 'boolean') return 'boolean';
        return 'unknown';
    }

    extractParams(request) {
        const params = {
            queryParams: {},
            bodyParams: {},
            headers: {},
            pathParams: {}
        };

        try {
            const url = new URL(request.url);
            params.queryParams = Object.fromEntries(url.searchParams);
        } catch (e) {}

        if (request.postData) {
            try {
                if (typeof request.postData === 'string') {
                    if (request.postData.startsWith('{') || request.postData.startsWith('[')) {
                        params.bodyParams = JSON.parse(request.postData);
                    } else {
                        const searchParams = new URLSearchParams(request.postData);
                        params.bodyParams = Object.fromEntries(searchParams);
                    }
                } else {
                    params.bodyParams = request.postData;
                }
            } catch (e) {
                params.bodyParams = { raw: request.postData };
            }
        }

        params.headers = request.headers || {};

        return params;
    }

    calculateConfidence(request) {
        let score = 0;

        if (request.resourceType === 'xhr' || request.resourceType === 'fetch') {
            score += 30;
        }

        if (request.response?.headers?.['content-type']?.includes('application/json')) {
            score += 20;
        }

        if (this.apiPatterns.some(pattern => pattern.test(request.url))) {
            score += 20;
        }

        if (request.response?.body) {
            if (this.hasListStructure(request.response.body)) {
                score += 30;
            }
        }

        const params = this.extractParams(request);
        const allParams = {
            ...params.queryParams,
            ...params.bodyParams
        };

        const paramKeys = Object.keys(allParams).map(k => k.toLowerCase());
        if (paramKeys.some(key => this.paginationPatterns.includes(key))) {
            score += 10;
        }

        return Math.min(score, 100);
    }

    async findListAPI(requests) {
        const apiRequests = await this.identifyAPIs(requests);
        
        return apiRequests.filter(req => 
            req.apiType === 'list' || 
            req.dataStructure?.hasPagination ||
            req.dataStructure?.isArray
        );
    }
}

module.exports = { APIAnalyzer };
