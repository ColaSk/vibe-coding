const fs = require('fs');
const path = require('path');

function ensureDir(dirPath) {
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
    }
    return dirPath;
}

function writeFile(filePath, content) {
    ensureDir(path.dirname(filePath));
    fs.writeFileSync(filePath, content, 'utf-8');
}

function readFile(filePath) {
    if (!fs.existsSync(filePath)) {
        return null;
    }
    return fs.readFileSync(filePath, 'utf-8');
}

function deleteFile(filePath) {
    if (fs.existsSync(filePath)) {
        fs.unlinkSync(filePath);
    }
}

function fileExists(filePath) {
    return fs.existsSync(filePath);
}

function getFiles(dirPath, pattern = null) {
    if (!fs.existsSync(dirPath)) {
        return [];
    }
    
    let files = fs.readdirSync(dirPath);
    
    if (pattern) {
        const regex = new RegExp(pattern);
        files = files.filter(file => regex.test(file));
    }
    
    return files.map(file => path.join(dirPath, file));
}

function getJson(filePath, defaultValue = null) {
    const content = readFile(filePath);
    if (!content) return defaultValue;
    
    try {
        return JSON.parse(content);
    } catch (e) {
        return defaultValue;
    }
}

function setJson(filePath, data) {
    writeFile(filePath, JSON.stringify(data, null, 2));
}

function appendFile(filePath, content) {
    ensureDir(path.dirname(filePath));
    fs.appendFileSync(filePath, content + '\n', 'utf-8');
}

function getFileSize(filePath) {
    if (!fs.existsSync(filePath)) {
        return 0;
    }
    const stats = fs.statSync(filePath);
    return stats.size;
}

function getFileInfo(filePath) {
    if (!fs.existsSync(filePath)) {
        return null;
    }
    
    const stats = fs.statSync(filePath);
    return {
        path: filePath,
        name: path.basename(filePath),
        ext: path.extname(filePath),
        size: stats.size,
        created: stats.birthtime,
        modified: stats.mtime,
        isDirectory: stats.isDirectory(),
        isFile: stats.isFile()
    };
}

module.exports = {
    ensureDir,
    writeFile,
    readFile,
    deleteFile,
    fileExists,
    getFiles,
    getJson,
    setJson,
    appendFile,
    getFileSize,
    getFileInfo
};
