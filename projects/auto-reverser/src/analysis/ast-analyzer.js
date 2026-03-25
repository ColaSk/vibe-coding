const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const t = require('@babel/types');
const generate = require('@babel/generator').default;

class ASTAnalyzer {
    constructor(code) {
        this.code = code;
        this.ast = null;
        this.encryptionFunctions = [];
        this.apiCalls = [];
        this.callGraph = new Map();
    }

    parse() {
        try {
            this.ast = parser.parse(this.code, {
                sourceType: 'module',
                plugins: ['jsx', 'typescript']
            });
            return true;
        } catch (error) {
            console.error('Parse error:', error.message);
            return false;
        }
    }

    analyze() {
        if (!this.ast) {
            if (!this.parse()) return null;
        }

        this.findEncryptionFunctions();
        this.findAPICalls();
        this.extractCallGraph();
        this.findStringDecryptions();

        return {
            encryptionFunctions: this.encryptionFunctions,
            apiCalls: this.apiCalls,
            callGraph: Object.fromEntries(this.callGraph)
        };
    }

    findEncryptionFunctions() {
        const encryptionPatterns = [
            /encrypt/i, /decrypt/i, /sign/i, /signature/i,
            /hash/i, /encode/i, /decode/i, /cipher/i,
            /crypto/i, /md5/i, /sha/i, /aes/i, /rsa/i,
            /base64/i, /hmac/i, /digest/i, /token/i
        ];

        const self = this;

        traverse(this.ast, {
            FunctionDeclaration(path) {
                const name = path.node.id?.name;
                if (name && encryptionPatterns.some(p => p.test(name))) {
                    self.encryptionFunctions.push({
                        type: 'FunctionDeclaration',
                        name: name,
                        params: path.node.params.map(p => p.name || p.type),
                        loc: path.node.loc,
                        code: generate(path.node).code
                    });
                }
            },

            VariableDeclarator(path) {
                if (t.isFunctionExpression(path.node.init) || 
                    t.isArrowFunctionExpression(path.node.init)) {
                    const name = path.node.id?.name;
                    if (name && encryptionPatterns.some(p => p.test(name))) {
                        self.encryptionFunctions.push({
                            type: 'VariableDeclarator',
                            name: name,
                            params: path.node.init.params.map(p => p.name || p.type),
                            loc: path.node.loc,
                            code: generate(path.node).code
                        });
                    }
                }
            },

            CallExpression(path) {
                const callee = path.node.callee;
                
                if (t.isIdentifier(callee)) {
                    if (encryptionPatterns.some(p => p.test(callee.name))) {
                        self.encryptionFunctions.push({
                            type: 'CallExpression',
                            name: callee.name,
                            arguments: path.node.arguments.map(a => generate(a).code),
                            loc: path.node.loc
                        });
                    }
                }

                if (t.isMemberExpression(callee)) {
                    const obj = callee.object;
                    const prop = callee.property;

                    if (t.isIdentifier(obj, { name: 'CryptoJS' }) ||
                        t.isIdentifier(obj, { name: 'crypto' })) {
                        self.encryptionFunctions.push({
                            type: 'CryptoCall',
                            object: obj.name,
                            method: prop.name,
                            arguments: path.node.arguments.map(a => generate(a).code),
                            loc: path.node.loc
                        });
                    }
                }
            }
        });
    }

    findAPICalls() {
        const self = this;

        traverse(this.ast, {
            CallExpression(path) {
                const callee = path.node.callee;

                if (t.isIdentifier(callee, { name: 'fetch' })) {
                    self.apiCalls.push({
                        type: 'fetch',
                        arguments: path.node.arguments.map(a => generate(a).code),
                        loc: path.node.loc
                    });
                }

                if (t.isMemberExpression(callee)) {
                    if (t.isIdentifier(callee.object)) {
                        const objName = callee.object.name;
                        const propName = callee.property?.name;

                        if (objName === 'axios' || objName === 'http' || objName === 'request') {
                            self.apiCalls.push({
                                type: objName,
                                method: propName,
                                arguments: path.node.arguments.map(a => generate(a).code),
                                loc: path.node.loc
                            });
                        }

                        if (propName === 'open' || propName === 'send') {
                            self.apiCalls.push({
                                type: 'XMLHttpRequest',
                                method: propName,
                                arguments: path.node.arguments.map(a => generate(a).code),
                                loc: path.node.loc
                            });
                        }
                    }
                }
            }
        });
    }

    extractCallGraph() {
        const self = this;

        traverse(this.ast, {
            FunctionDeclaration(path) {
                const functionName = path.node.id?.name;
                if (!functionName) return;

                const calls = [];

                path.traverse({
                    CallExpression(innerPath) {
                        const callee = innerPath.node.callee;
                        if (t.isIdentifier(callee)) {
                            calls.push(callee.name);
                        }
                    }
                });

                self.callGraph.set(functionName, calls);
            },

            VariableDeclarator(path) {
                if (t.isFunctionExpression(path.node.init) ||
                    t.isArrowFunctionExpression(path.node.init)) {
                    const functionName = path.node.id?.name;
                    if (!functionName) return;

                    const calls = [];

                    path.traverse({
                        CallExpression(innerPath) {
                            const callee = innerPath.node.callee;
                            if (t.isIdentifier(callee)) {
                                calls.push(callee.name);
                            }
                        }
                    });

                    self.callGraph.set(functionName, calls);
                }
            }
        });
    }

    findStringDecryptions() {
        const self = this;

        traverse(this.ast, {
            CallExpression(path) {
                const callee = path.node.callee;

                if (t.isIdentifier(callee, { name: 'atob' }) ||
                    t.isIdentifier(callee, { name: 'btoa' })) {
                    self.encryptionFunctions.push({
                        type: 'Base64',
                        operation: callee.name,
                        arguments: path.node.arguments.map(a => generate(a).code),
                        loc: path.node.loc
                    });
                }
            }
        });
    }

    findParamAssignments(paramName) {
        const assignments = [];

        traverse(this.ast, {
            AssignmentExpression(path) {
                const left = path.node.left;
                const right = path.node.right;

                if (t.isMemberExpression(left)) {
                    const obj = left.object;
                    const prop = left.property;

                    if (t.isIdentifier(prop, { name: paramName })) {
                        assignments.push({
                            object: obj.name || generate(obj).code,
                            property: propName,
                            value: generate(right).code,
                            loc: path.node.loc
                        });
                    }
                }

                if (t.isIdentifier(left, { name: paramName })) {
                    assignments.push({
                        variable: paramName,
                        value: generate(right).code,
                        loc: path.node.loc
                    });
                }
            }
        });

        return assignments;
    }

    findObjectCreations() {
        const objects = [];

        traverse(this.ast, {
            VariableDeclarator(path) {
                if (t.isObjectExpression(path.node.init)) {
                    const name = path.node.id?.name;
                    const properties = path.node.init.properties.map(p => {
                        if (t.isObjectProperty(p)) {
                            return {
                                key: p.key.name || p.key.value,
                                value: generate(p.value).code
                            };
                        }
                        return null;
                    }).filter(Boolean);

                    objects.push({
                        name: name,
                        properties: properties,
                        loc: path.node.loc
                    });
                }
            }
        });

        return objects;
    }

    generate() {
        if (!this.ast) return null;
        return generate(this.ast).code;
    }
}

module.exports = { ASTAnalyzer };
