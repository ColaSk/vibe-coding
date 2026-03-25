const crypto = require('crypto');
const CryptoJS = require('crypto-js');

class EncryptionCracker {
    constructor() {
        this.commonSecrets = [
            'secret', 'key', 'password', 'salt', 'appkey',
            '123456', 'abcdef', 'test', 'api', 'app'
        ];

        this.commonPasswords = [
            '123456', 'password', 'admin', 'root', 'test',
            'guest', 'user', 'demo', 'default', '12345678'
        ];
    }

    async crack(encryptedData, type, options = {}) {
        const result = {
            success: false,
            type: type,
            decrypted: null,
            method: null,
            script: null
        };

        switch (type) {
            case 'Base64':
                return this.crackBase64(encryptedData);
            case 'MD5':
                return this.crackMD5(encryptedData, options);
            case 'SHA1':
                return this.crackSHA1(encryptedData, options);
            case 'SHA256':
                return this.crackSHA256(encryptedData, options);
            case 'JWT':
                return this.crackJWT(encryptedData, options);
            case 'AES':
                return this.crackAES(encryptedData, options);
            default:
                return this.tryAllMethods(encryptedData, options);
        }
    }

    crackBase64(data) {
        const result = {
            success: false,
            type: 'Base64',
            decrypted: null,
            method: 'decode'
        };

        try {
            const decoded = Buffer.from(data, 'base64').toString('utf-8');
            if (this.isPrintable(decoded)) {
                result.success = true;
                result.decrypted = decoded;
            }
        } catch (e) {}

        return result;
    }

    async crackMD5(hash, options = {}) {
        const result = {
            success: false,
            type: 'MD5',
            decrypted: null,
            method: 'rainbow'
        };

        const passwords = [...this.commonPasswords, ...(options.dictionary || [])];

        for (const pwd of passwords) {
            const md5 = crypto.createHash('md5').update(pwd).digest('hex');
            if (md5 === hash.toLowerCase()) {
                result.success = true;
                result.decrypted = pwd;
                return result;
            }
        }

        if (options.params) {
            const combinations = this.generateCombinations(options.params);
            for (const combo of combinations) {
                const md5 = crypto.createHash('md5').update(combo).digest('hex');
                if (md5 === hash.toLowerCase()) {
                    result.success = true;
                    result.decrypted = combo;
                    result.method = 'params_combination';
                    return result;
                }
            }
        }

        return result;
    }

    crackSHA1(hash, options = {}) {
        const result = {
            success: false,
            type: 'SHA1',
            decrypted: null,
            method: 'dictionary'
        };

        const passwords = [...this.commonPasswords, ...(options.dictionary || [])];

        for (const pwd of passwords) {
            const sha1 = crypto.createHash('sha1').update(pwd).digest('hex');
            if (sha1 === hash.toLowerCase()) {
                result.success = true;
                result.decrypted = pwd;
                return result;
            }
        }

        return result;
    }

    crackSHA256(hash, options = {}) {
        const result = {
            success: false,
            type: 'SHA256',
            decrypted: null,
            method: 'dictionary'
        };

        const passwords = [...this.commonPasswords, ...(options.dictionary || [])];

        for (const pwd of passwords) {
            const sha256 = crypto.createHash('sha256').update(pwd).digest('hex');
            if (sha256 === hash.toLowerCase()) {
                result.success = true;
                result.decrypted = pwd;
                return result;
            }
        }

        return result;
    }

    crackJWT(token, options = {}) {
        const result = {
            success: false,
            type: 'JWT',
            decrypted: null,
            method: 'none'
        };

        try {
            const parts = token.split('.');
            if (parts.length !== 3) return result;

            const header = JSON.parse(Buffer.from(parts[0], 'base64').toString());
            const payload = JSON.parse(Buffer.from(parts[1], 'base64').toString());

            result.decoded = {
                header: header,
                payload: payload
            };

            if (header.alg === 'none') {
                result.success = true;
                result.method = 'none_algorithm';
                return result;
            }

            for (const secret of this.commonSecrets) {
                const reconstructed = this.signJWT(header, payload, secret);
                if (reconstructed === token) {
                    result.success = true;
                    result.decrypted = secret;
                    result.method = 'weak_secret';
                    return result;
                }
            }

        } catch (e) {}

        return result;
    }

    signJWT(header, payload, secret) {
        const headerB64 = Buffer.from(JSON.stringify(header)).toString('base64url');
        const payloadB64 = Buffer.from(JSON.stringify(payload)).toString('base64url');
        const signature = crypto
            .createHmac('sha256', secret)
            .update(`${headerB64}.${payloadB64}`)
            .digest('base64url');
        return `${headerB64}.${payloadB64}.${signature}`;
    }

    crackAES(encrypted, options = {}) {
        const result = {
            success: false,
            type: 'AES',
            decrypted: null,
            method: 'brute'
        };

        if (!options.key && !options.iv) {
            for (const secret of this.commonSecrets) {
                try {
                    const decrypted = this.decryptAES(encrypted, secret, secret);
                    if (decrypted) {
                        result.success = true;
                        result.decrypted = decrypted;
                        result.key = secret;
                        result.method = 'weak_key';
                        return result;
                    }
                } catch (e) {}
            }
            return result;
        }

        try {
            const decrypted = this.decryptAES(
                encrypted, 
                options.key, 
                options.iv || options.key
            );
            if (decrypted) {
                result.success = true;
                result.decrypted = decrypted;
                result.method = 'known_key';
            }
        } catch (e) {}

        return result;
    }

    decryptAES(encrypted, key, iv) {
        try {
            const keyBytes = CryptoJS.enc.Utf8.parse(key.padEnd(16, '0').slice(0, 16));
            const ivBytes = CryptoJS.enc.Utf8.parse(iv.padEnd(16, '0').slice(0, 16));
            
            const decrypted = CryptoJS.AES.decrypt(encrypted, keyBytes, {
                iv: ivBytes,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            });

            return decrypted.toString(CryptoJS.enc.Utf8);
        } catch (e) {
            return null;
        }
    }

    tryAllMethods(data, options = {}) {
        let result = this.crackBase64(data);
        if (result.success) return result;

        result = this.crackMD5(data, options);
        if (result.success) return result;

        result = this.crackSHA1(data, options);
        if (result.success) return result;

        result = this.crackSHA256(data, options);
        if (result.success) return result;

        result = this.crackJWT(data, options);
        if (result.success) return result;

        return {
            success: false,
            type: 'Unknown',
            decrypted: null,
            method: null
        };
    }

    generateCombinations(params) {
        const combinations = [];
        const keys = Object.keys(params);
        const values = Object.values(params);

        for (let i = 0; i < values.length; i++) {
            combinations.push(values[i]);
            combinations.push(values[i] + '');
            
            for (let j = i + 1; j < values.length; j++) {
                combinations.push(values[i] + values[j]);
                combinations.push(values[j] + values[i]);
                combinations.push(values[i] + '&' + values[j]);
            }
        }

        const timestamp = Date.now().toString();
        combinations.push(timestamp);
        
        for (const value of values) {
            combinations.push(value + timestamp);
            combinations.push(timestamp + value);
        }

        return combinations;
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

    generateScript(type, data) {
        const scripts = {
            python: this.generatePythonScript(type, data),
            nodejs: this.generateNodeScript(type, data)
        };
        return scripts;
    }

    generatePythonScript(type, data) {
        let script = `#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import base64
import hmac
import json
from datetime import datetime

`;

        switch (type) {
            case 'MD5':
                script += `def generate_sign(params):
    """生成MD5签名"""
    sorted_params = sorted(params.items())
    param_str = '&'.join([f"{k}={v}" for k, v in sorted_params])
    return hashlib.md5(param_str.encode()).hexdigest()

# 使用示例
params = ${JSON.stringify(data.params || {}, null, 4)}
sign = generate_sign(params)
print(f"签名: {sign}")
`;
                break;

            case 'SHA256':
                script += `def generate_sign(params, secret):
    """生成HMAC-SHA256签名"""
    sorted_params = sorted(params.items())
    param_str = '&'.join([f"{k}={v}" for k, v in sorted_params])
    return hmac.new(
        secret.encode(),
        param_str.encode(),
        hashlib.sha256
    ).hexdigest()

# 使用示例
params = ${JSON.stringify(data.params || {}, null, 4)}
secret = "${data.secret || 'your_secret'}"
sign = generate_sign(params, secret)
print(f"签名: {sign}")
`;
                break;

            case 'Base64':
                script += `def encode_base64(data):
    """Base64编码"""
    return base64.b64encode(data.encode()).decode()

def decode_base64(data):
    """Base64解码"""
    return base64.b64decode(data).decode()

# 使用示例
data = "${data.value || 'test'}"
encoded = encode_base64(data)
print(f"编码: {encoded}")
decoded = decode_base64(encoded)
print(f"解码: {decoded}")
`;
                break;

            default:
                script += `# 通用签名生成函数
def generate_sign(params, method='md5', secret=''):
    sorted_params = sorted(params.items())
    param_str = '&'.join([f"{k}={v}" for k, v in sorted_params])
    
    if method == 'md5':
        return hashlib.md5(param_str.encode()).hexdigest()
    elif method == 'sha256':
        return hashlib.sha256(param_str.encode()).hexdigest()
    elif method == 'hmac_sha256':
        return hmac.new(secret.encode(), param_str.encode(), hashlib.sha256).hexdigest()
    
    return param_str

# 使用示例
params = ${JSON.stringify(data.params || {}, null, 4)}
sign = generate_sign(params, method='md5')
print(f"签名: {sign}")
`;
        }

        return script;
    }

    generateNodeScript(type, data) {
        let script = `const crypto = require('crypto');

`;

        switch (type) {
            case 'MD5':
                script += `function generateSign(params) {
    const sortedKeys = Object.keys(params).sort();
    const paramStr = sortedKeys.map(k => \`\${k}=\${params[k]}\`).join('&');
    return crypto.createHash('md5').update(paramStr).digest('hex');
}

// 使用示例
const params = ${JSON.stringify(data.params || {}, null, 2)};
const sign = generateSign(params);
console.log('签名:', sign);
`;
                break;

            case 'SHA256':
                script += `function generateSign(params, secret) {
    const sortedKeys = Object.keys(params).sort();
    const paramStr = sortedKeys.map(k => \`\${k}=\${params[k]}\`).join('&');
    return crypto.createHmac('sha256', secret)
        .update(paramStr)
        .digest('hex');
}

// 使用示例
const params = ${JSON.stringify(data.params || {}, null, 2)};
const secret = '${data.secret || 'your_secret'}';
const sign = generateSign(params, secret);
console.log('签名:', sign);
`;
                break;

            default:
                script += `function generateSign(params, method = 'md5', secret = '') {
    const sortedKeys = Object.keys(params).sort();
    const paramStr = sortedKeys.map(k => \`\${k}=\${params[k]}\`).join('&');
    
    switch (method) {
        case 'md5':
            return crypto.createHash('md5').update(paramStr).digest('hex');
        case 'sha256':
            return crypto.createHash('sha256').update(paramStr).digest('hex');
        case 'hmac_sha256':
            return crypto.createHmac('sha256', secret).update(paramStr).digest('hex');
        default:
            return paramStr;
    }
}

// 使用示例
const params = ${JSON.stringify(data.params || {}, null, 2)};
const sign = generateSign(params, 'md5');
console.log('签名:', sign);
`;
        }

        return script;
    }
}

module.exports = { EncryptionCracker };
