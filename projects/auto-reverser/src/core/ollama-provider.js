const { Ollama } = require('ollama');

class OllamaProvider {
    constructor(config = {}) {
        this.client = new Ollama({ host: config.host || 'http://localhost:11434' });
        this.model  = config.model || 'qwen2.5:7b';
    }

    /**
     * 发送一轮对话，返回统一格式的响应
     * @param {object[]} messages - 对话历史
     * @param {object[]} tools    - tool schema 数组
     * @returns {{ content: string|null, tool_calls: object[] }}
     */
    async chat(messages, tools) {
        const ollamaTools = (tools || []).map(t => ({
            type: 'function',
            function: t
        }));

        const res = await this.client.chat({
            model:    this.model,
            messages: messages,
            tools:    ollamaTools.length ? ollamaTools : undefined,
            stream:   false
        });

        const msg = res.message;
        return {
            content: msg.content || null,
            tool_calls: (msg.tool_calls || []).map(tc => ({
                // 规范化字段：用于执行工具和 UI 展示
                id:        `${tc.function.name}_${Date.now()}`,
                name:      tc.function.name,
                arguments: tc.function.arguments || {},
                // 原始 Ollama 格式：添加回对话历史时必须使用此格式
                _raw: {
                    type: 'function',
                    function: {
                        name:      tc.function.name,
                        arguments: tc.function.arguments || {}
                    }
                }
            }))
        };
    }

    /**
     * 验证 Ollama 服务是否可连接
     * @returns {{ success: boolean, models?: string[], error?: string }}
     */
    async verify() {
        try {
            const list = await this.client.list();
            return {
                success: true,
                models:  (list.models || []).map(m => m.name)
            };
        } catch (err) {
            return {
                success: false,
                error:   err.message
            };
        }
    }
}

module.exports = { OllamaProvider };
