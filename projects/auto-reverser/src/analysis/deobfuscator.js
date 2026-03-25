const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const t = require('@babel/types');
const generate = require('@babel/generator').default;

class Deobfuscator {
    constructor(code) {
        this.code = code;
        this.ast = null;
        this.stringArrays = new Map();
        this.rotationFunctions = new Map();
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

    deobfuscate() {
        if (!this.ast) {
            if (!this.parse()) return this.code;
        }

        this.decodeHexStrings();
        this.decodeUnicodeStrings();
        this.findStringArrays();
        this.replaceStringArrayCalls();
        this.simplifyExpressions();
        this.renameVariables();
        this.removeDeadCode();

        return generate(this.ast).code;
    }

    decodeHexStrings() {
        const self = this;

        traverse(this.ast, {
            StringLiteral(path) {
                const value = path.node.value;
                if (/\\x[0-9a-fA-F]{2}/.test(value)) {
                    try {
                        const decoded = value.replace(
                            /\\x([0-9a-fA-F]{2})/g,
                            (match, hex) => String.fromCharCode(parseInt(hex, 16))
                        );
                        path.node.value = decoded;
                    } catch (e) {}
                }
            }
        });
    }

    decodeUnicodeStrings() {
        const self = this;

        traverse(this.ast, {
            StringLiteral(path) {
                const value = path.node.value;
                if (/\\u[0-9a-fA-F]{4}/.test(value)) {
                    try {
                        const decoded = value.replace(
                            /\\u([0-9a-fA-F]{4})/g,
                            (match, hex) => String.fromCharCode(parseInt(hex, 16))
                        );
                        path.node.value = decoded;
                    } catch (e) {}
                }
            }
        });
    }

    findStringArrays() {
        const self = this;

        traverse(this.ast, {
            VariableDeclarator(path) {
                if (t.isArrayExpression(path.node.init)) {
                    const name = path.node.id?.name;
                    if (name && /^_0x[a-f0-9]+$/i.test(name)) {
                        const elements = path.node.init.elements.map(el => {
                            if (t.isStringLiteral(el)) {
                                return el.value;
                            }
                            return null;
                        });
                        self.stringArrays.set(name, elements);
                    }
                }

                if (t.isFunctionExpression(path.node.init) ||
                    t.isArrowFunctionExpression(path.node.init)) {
                    const name = path.node.id?.name;
                    if (name && /^_0x[a-f0-9]+$/i.test(name)) {
                        const body = path.node.init.body;
                        if (t.isBlockStatement(body)) {
                            self.rotationFunctions.set(name, path.node);
                        }
                    }
                }
            }
        });
    }

    replaceStringArrayCalls() {
        const self = this;

        traverse(this.ast, {
            CallExpression(path) {
                const callee = path.node.callee;

                if (t.isIdentifier(callee)) {
                    const funcName = callee.name;
                    if (self.stringArrays.has(funcName)) {
                        const args = path.node.arguments;
                        if (args.length === 1 && t.isNumericLiteral(args[0])) {
                            const index = args[0].value;
                            const arr = self.stringArrays.get(funcName);
                            if (arr[index] !== undefined) {
                                path.replaceWith(t.stringLiteral(arr[index]));
                            }
                        }
                    }
                }

                if (t.isMemberExpression(callee)) {
                    if (t.isIdentifier(callee.object) && t.isIdentifier(callee.property)) {
                        const objName = callee.object.name;
                        const propName = callee.property.name;

                        if (self.stringArrays.has(objName) && propName === 'indexOf') {
                            const args = path.node.arguments;
                            if (args.length === 1 && t.isStringLiteral(args[0])) {
                                const searchValue = args[0].value;
                                const arr = self.stringArrays.get(objName);
                                const index = arr.indexOf(searchValue);
                                if (index !== -1) {
                                    path.replaceWith(t.numericLiteral(index));
                                }
                            }
                        }
                    }
                }
            }
        });
    }

    simplifyExpressions() {
        const self = this;

        traverse(this.ast, {
            BinaryExpression(path) {
                const left = path.node.left;
                const right = path.node.right;
                const operator = path.node.operator;

                if (t.isStringLiteral(left) && t.isStringLiteral(right)) {
                    if (operator === '+') {
                        path.replaceWith(t.stringLiteral(left.value + right.value));
                    }
                }

                if (t.isNumericLiteral(left) && t.isNumericLiteral(right)) {
                    let result;
                    switch (operator) {
                        case '+': result = left.value + right.value; break;
                        case '-': result = left.value - right.value; break;
                        case '*': result = left.value * right.value; break;
                        case '/': result = left.value / right.value; break;
                        case '%': result = left.value % right.value; break;
                    }
                    if (result !== undefined) {
                        path.replaceWith(t.numericLiteral(result));
                    }
                }
            },

            UnaryExpression(path) {
                const argument = path.node.argument;
                const operator = path.node.operator;

                if (operator === '!' && t.isBooleanLiteral(argument)) {
                    path.replaceWith(t.booleanLiteral(!argument.value));
                }

                if (operator === '-' && t.isNumericLiteral(argument)) {
                    path.replaceWith(t.numericLiteral(-argument.value));
                }
            }
        });
    }

    renameVariables() {
        const self = this;
        const nameMap = new Map();
        let counter = 0;

        traverse(this.ast, {
            VariableDeclarator(path) {
                const name = path.node.id?.name;
                if (name && /^_0x[a-f0-9]+$/i.test(name)) {
                    if (!nameMap.has(name)) {
                        nameMap.set(name, `var${counter++}`);
                    }
                }
            }
        });

        traverse(this.ast, {
            Identifier(path) {
                const name = path.node.name;
                if (nameMap.has(name)) {
                    path.node.name = nameMap.get(name);
                }
            }
        });
    }

    removeDeadCode() {
        const self = this;

        traverse(this.ast, {
            IfStatement(path) {
                const test = path.node.test;

                if (t.isBooleanLiteral(test)) {
                    if (test.value) {
                        path.replaceWith(path.node.consequent);
                    } else if (path.node.alternate) {
                        path.replaceWith(path.node.alternate);
                    } else {
                        path.remove();
                    }
                }
            },

            ConditionalExpression(path) {
                const test = path.node.test;

                if (t.isBooleanLiteral(test)) {
                    if (test.value) {
                        path.replaceWith(path.node.consequent);
                    } else {
                        path.replaceWith(path.node.alternate);
                    }
                }
            },

            LogicalExpression(path) {
                const left = path.node.left;
                const operator = path.node.operator;

                if (t.isBooleanLiteral(left)) {
                    if (operator === '&&') {
                        if (left.value) {
                            path.replaceWith(path.node.right);
                        } else {
                            path.replaceWith(t.booleanLiteral(false));
                        }
                    } else if (operator === '||') {
                        if (left.value) {
                            path.replaceWith(t.booleanLiteral(true));
                        } else {
                            path.replaceWith(path.node.right);
                        }
                    }
                }
            }
        });
    }

    deflattenControlFlow() {
        const self = this;

        traverse(this.ast, {
            WhileStatement(path) {
                const test = path.node.test;
                const body = path.node.body;

                if (t.isBooleanLiteral(test, { value: true }) ||
                    t.isStringLiteral(test)) {
                    
                    const switchStmt = body.body.find(t.isSwitchStatement);
                    if (!switchStmt) return;

                    const discriminant = switchStmt.discriminant;
                    if (!t.isIdentifier(discriminant)) return;

                    const cases = switchStmt.cases;
                    const orderedStmts = [];
                    let currentCase = cases.find(c => 
                        t.isStringLiteral(c.test) && c.test.value === '0'
                    );

                    if (!currentCase) return;

                    const visited = new Set();
                    while (currentCase && !visited.has(currentCase)) {
                        visited.add(currentCase);

                        const stmts = currentCase.consequent.filter(s => 
                            !t.isContinueStatement(s) && 
                            !t.isBreakStatement(s)
                        );
                        orderedStmts.push(...stmts);

                        const lastStmt = currentCase.consequent[currentCase.consequent.length - 1];
                        if (t.isContinueStatement(lastStmt)) {
                            const nextValue = this.findNextValue(lastStmt, discriminant.name);
                            if (nextValue !== null) {
                                currentCase = cases.find(c =>
                                    t.isStringLiteral(c.test) && c.test.value === nextValue
                                );
                            } else {
                                break;
                            }
                        } else {
                            break;
                        }
                    }

                    if (orderedStmts.length > 0) {
                        path.replaceWithMultiple(orderedStmts);
                    }
                }
            }
        });
    }

    findNextValue(stmt, varName) {
        let nextValue = null;

        traverse(this.ast, {
            AssignmentExpression(path) {
                if (t.isIdentifier(path.node.left, { name: varName })) {
                    if (t.isStringLiteral(path.node.right)) {
                        nextValue = path.node.right.value;
                    }
                }
            }
        }, { noScope: true });

        return nextValue;
    }
}

module.exports = { Deobfuscator };
