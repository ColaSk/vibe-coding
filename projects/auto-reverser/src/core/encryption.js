class EncryptionAnalyzer {
    constructor() {
        this.encryptionPatterns = {
            MD5: {
                pattern: /^[a-fA-F0-9]{32}$/,
                description: 'MD5 Hash (32位十六进制)'
            },
            SHA1: {
                pattern: /^[a-fA-F0-9]{40}$/,
                description: 'SHA1 Hash (40位十六进制)'
            },
            SHA256: {
                pattern: /^[a-fA-F0-9]{64}$/,
                description: 'SHA256 Hash (64位十六进制)'
            },
            SHA512: {
                pattern: /^[a-fA-F0-9]{128}$/,
                description: 'SHA512 Hash (128位十六进制)'
            },
            Base64: {
                pattern: /^[A-Za-z0-9+/]+=*$/,
                description: 'Base64编码'
            },
            Base64URL: {
                pattern: /^[A-Za-z0-9_-]+=*$/,
                description: 'Base64URL编码'
            },
            Hex: {
                pattern: /^[a-fA-F0-9]+$/,
                description: '十六进制编码'
            },
            URLEncoded: {
                pattern: /%[0-9A-Fa-f]{2}/,
                description: 'URL编码'
            },
            JWT: {
                pattern: /^eyJ[A-Za-z0-9_-]*\.eyJ[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*$/,
                description: 'JSON Web Token'
            },
            UUID: {
                pattern: /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i,
                description: 'UUID'
            },
            Timestamp: {
                pattern: /^[0-9]{10,13}$/,
                description: '时间戳'
            }
        };

        this.suspiciousParamNames = [
            'sign', 'signature', 'token', 'auth', 'key', 'secret',
            'encrypt', 'cipher', 'hash', 'checksum', 'digest',
            'data', 'params', 'payload', 'body', 'content'
        ];
    }

    async analyze(params) {
        const result = {
            encryptedParams: [],
            suspiciousParams: [],
            analysis: {}
        };

        if (!params) return result;

        const allParams = {
            ...params.queryParams,
            ...params.bodyParams,
            ...params.headers
        };

        for (const [name, value] of Object.entries(allParams)) {
            if (typeof value !== 'string') continue;

            const paramAnalysis = this.analyzeParam(name, value);
            
            if (paramAnalysis.isEncrypted) {
                result.encryptedParams.push(paramAnalysis);
            }

            if (paramAnalysis.isSuspicious) {
                result.suspiciousParams.push(paramAnalysis);
            }

            result.analysis[name] = paramAnalysis;
        }

        return result;
    }

    analyzeParam(name, value) {
        const analysis = {
            name: name,
            value: value,
            length: value.length,
            isEncrypted: false,
            isSuspicious: false,
            encryptionType: null,
            confidence: 0,
            possibleTypes: [],
            decodedValue: null
        };

        const lowerName = name.toLowerCase();
        analysis.isSuspicious = this.suspiciousParamNames.some(
            pattern => lowerName.includes(pattern)
        );

        for (const [type, config] of Object.entries(this.encryptionPatterns)) {
            if (config.pattern.test(value)) {
                analysis.possibleTypes.push(type);
                analysis.confidence += 20;

                if (type === 'Base64' || type === 'Base64URL') {
                    if (value.length % 4 === 0) {
                        analysis.confidence += 10;
                    }
                    analysis.decodedValue = this.tryDecodeBase64(value);
                }

                if (type === 'Hex' && value.length >= 32) {
                    analysis.confidence += 15;
                }

                if (type === 'JWT') {
                    analysis.confidence = 100;
                    analysis.decodedValue = this.decodeJWT(value);
                }
            }
        }

        if (analysis.possibleTypes.includes('MD5')) {
            analysis.encryptionType = 'MD5';
            analysis.isEncrypted = true;
            analysis.confidence = Math.max(analysis.confidence, 80);
        } else if (analysis.possibleTypes.includes('SHA256')) {
            analysis.encryptionType = 'SHA256';
            analysis.isEncrypted = true;
            analysis.confidence = Math.max(analysis.confidence, 85);
        } else if (analysis.possibleTypes.includes('SHA1')) {
            analysis.encryptionType = 'SHA1';
            analysis.isEncrypted = true;
            analysis.confidence = Math.max(analysis.confidence, 80);
        } else if (analysis.possibleTypes.includes('JWT')) {
            analysis.encryptionType = 'JWT';
            analysis.isEncrypted = true;
            analysis.confidence = 100;
        } else if (analysis.possibleTypes.includes('Base64')) {
            if (analysis.decodedValue && this.looksLikeData(analysis.decodedValue)) {
                analysis.encryptionType = 'Base64';
                analysis.isEncrypted = true;
                analysis.confidence = Math.max(analysis.confidence, 70);
            }
        }

        if (analysis.isSuspicious && analysis.confidence > 30) {
            analysis.isEncrypted = true;
        }

        return analysis;
    }

    tryDecodeBase64(value) {
        try {
            const decoded = Buffer.from(value, 'base64').toString('utf-8');
            if (this.isPrintable(decoded)) {
                return decoded;
            }
        } catch (e) {}
        return null;
    }

    decodeJWT(token) {
        try {
            const parts = token.split('.');
            if (parts.length !== 3) return null;

            const header = JSON.parse(Buffer.from(parts[0], 'base64').toString());
            const payload = JSON.parse(Buffer.from(parts[1], 'base64').toString());

            return {
                header: header,
                payload: payload,
                signature: parts[2]
            };
        } catch (e) {
            return null;
        }
    }

    isPrintable(str) {
        for (let i = 0; i < str.length; i++) {
            const code = str.charCodeAt(i);
            if (code < 32 && code !== 9 && code !== 10 && code !== 13) {
                return false;
            }
            if (code > 126 && code < 160) {
                return false;
            }
        }
        return true;
    }

    looksLikeData(str) {
        if (str.startsWith('{') || str.startsWith('[')) {
            try {
                JSON.parse(str);
                return true;
            } catch (e) {}
        }

        if (/^[a-zA-Z0-9_\-&=]+$/.test(str) && str.length > 5) {
            return true;
        }

        return false;
    }

    detectEncryptionCombination(params) {
        const combinations = [];

        const sortedKeys = Object.keys(params).sort();
        
        for (let i = 0; i < sortedKeys.length; i++) {
            for (let j = i + 1; j < sortedKeys.length; j++) {
                const key1 = sortedKeys[i];
                const key2 = sortedKeys[j];
                const value1 = params[key1];
                const value2 = params[key2];

                if (this.looksLikeTimestamp(value1) || this.looksLikeTimestamp(value2)) {
                    combinations.push({
                        type: 'timestamp_signature',
                        params: [key1, key2],
                        confidence: 60
                    });
                }
            }
        }

        return combinations;
    }

    looksLikeTimestamp(value) {
        if (!/^\d+$/.test(value)) return false;
        
        const num = parseInt(value);
        const now = Date.now();
        
        if (value.length === 10) {
            return num > 1000000000 && num < 2000000000;
        }
        if (value.length === 13) {
            return num > 1000000000000 && num < 2000000000000;
        }
        
        return false;
    }

    async locateEncryptionFunction(page, paramName) {
        await page.evaluateOnNewDocument(() => {
            window.__encryptionCalls = [];

            const hookFunction = (obj, fnName, type) => {
                const original = obj[fnName];
                obj[fnName] = function(...args) {
                    window.__encryptionCalls.push({
                        type: type,
                        function: fnName,
                        args: args.map(a => String(a)),
                        timestamp: Date.now(),
                        stack: new Error().stack
                    });
                    return original.apply(this, args);
                };
            };

            hookFunction(window, 'btoa', 'encoding');
            hookFunction(window, 'atob', 'decoding');

            if (window.CryptoJS) {
                ['MD5', 'SHA1', 'SHA256', 'SHA512', 'AES', 'DES', 'HmacSHA256'].forEach(fn => {
                    if (window.CryptoJS[fn]) {
                        hookFunction(window.CryptoJS, fn, 'crypto');
                    }
                });
            }

            if (window.crypto && window.crypto.subtle) {
                const originalDigest = window.crypto.subtle.digest;
                window.crypto.subtle.digest = function(...args) {
                    window.__encryptionCalls.push({
                        type: 'subtle',
                        function: 'digest',
                        args: args.map(a => String(a)),
                        timestamp: Date.now()
                    });
                    return originalDigest.apply(this, args);
                };
            }
        });

        const encryptionCalls = await page.evaluate(() => {
            return window.__encryptionCalls || [];
        });

        return encryptionCalls.filter(call => 
            call.args.some(arg => 
                arg.toLowerCase().includes(paramName.toLowerCase())
            )
        );
    }
}

module.exports = { EncryptionAnalyzer };
