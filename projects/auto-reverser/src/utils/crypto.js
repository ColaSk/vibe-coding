const crypto = require('crypto');

function generateMD5(str) {
    return crypto.createHash('md5').update(str).digest('hex');
}

function generateSHA1(str) {
    return crypto.createHash('sha1').update(str).digest('hex');
}

function generateSHA256(str) {
    return crypto.createHash('sha256').update(str).digest('hex');
}

function generateHMAC(algorithm, key, data) {
    return crypto.createHmac(algorithm, key).update(data).digest('hex');
}

function base64Encode(str) {
    return Buffer.from(str).toString('base64');
}

function base64Decode(str) {
    return Buffer.from(str, 'base64').toString('utf-8');
}

function urlEncode(str) {
    return encodeURIComponent(str);
}

function urlDecode(str) {
    return decodeURIComponent(str);
}

function generateTimestamp() {
    return Math.floor(Date.now() / 1000);
}

function generateTimestampMs() {
    return Date.now();
}

function generateUUID() {
    return crypto.randomUUID();
}

function generateRandomString(length = 16) {
    return crypto.randomBytes(length).toString('hex').slice(0, length);
}

function sortParams(params) {
    const sortedKeys = Object.keys(params).sort();
    const sorted = {};
    sortedKeys.forEach(key => {
        sorted[key] = params[key];
    });
    return sorted;
}

function paramsToString(params, separator = '&', keyValueSeparator = '=') {
    return Object.entries(params)
        .map(([key, value]) => `${key}${keyValueSeparator}${value}`)
        .join(separator);
}

function parseQueryString(queryString) {
    const params = {};
    const searchParams = new URLSearchParams(queryString);
    for (const [key, value] of searchParams) {
        params[key] = value;
    }
    return params;
}

function isJSON(str) {
    try {
        JSON.parse(str);
        return true;
    } catch (e) {
        return false;
    }
}

function safeJSONParse(str, defaultValue = null) {
    try {
        return JSON.parse(str);
    } catch (e) {
        return defaultValue;
    }
}

function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}

function flattenObject(obj, prefix = '') {
    const result = {};
    
    for (const [key, value] of Object.entries(obj)) {
        const newKey = prefix ? `${prefix}.${key}` : key;
        
        if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
            Object.assign(result, flattenObject(value, newKey));
        } else {
            result[newKey] = value;
        }
    }
    
    return result;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

function formatDuration(ms) {
    if (ms < 1000) return `${ms}ms`;
    if (ms < 60000) return `${(ms / 1000).toFixed(2)}s`;
    return `${(ms / 60000).toFixed(2)}m`;
}

module.exports = {
    generateMD5,
    generateSHA1,
    generateSHA256,
    generateHMAC,
    base64Encode,
    base64Decode,
    urlEncode,
    urlDecode,
    generateTimestamp,
    generateTimestampMs,
    generateUUID,
    generateRandomString,
    sortParams,
    paramsToString,
    parseQueryString,
    isJSON,
    safeJSONParse,
    deepClone,
    flattenObject,
    sleep,
    formatBytes,
    formatDuration
};
