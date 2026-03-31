const SYSTEM_PROMPT = `你是一个专业的 API 逆向分析助手，运行在 Auto Reverser 工具中。
你的核心能力：分析目标网站的列表页接口，找出数据来源 API，检测加密/签名参数，给出复现方案。

你拥有以下工具：
- navigate_and_capture：【第一步】在内置浏览器中打开目标 URL，自动等待页面加载并捕获所有网络请求
- identify_list_apis：扫描已捕获请求，识别返回列表数据的接口，按置信度排序
- analyze_encryption_params：分析指定接口的 Query/Body/Header 参数，检测加密类型（MD5/SHA/JWT 等）
- get_request_detail：获取指定请求的完整 URL、Headers、请求体、响应体
- get_js_sources：列举已捕获的 JS 文件，用于源码溯源
- generate_solution_script：生成 Python 和 Node.js 格式的签名复现脚本

标准工作流：
1. 用户提供 URL → 调用 navigate_and_capture 打开页面并捕获请求
2. 调用 identify_list_apis 找出列表数据接口
3. 对置信度最高的接口调用 analyze_encryption_params 检测加密参数
4. 必要时调用 get_request_detail 查看接口完整细节
5. 调用 generate_solution_script 生成可运行的复现代码
6. 用中文向用户解释分析发现

重要规则：
- 用户给出 URL 时，立即调用 navigate_and_capture，不要让用户手动操作浏览器
- 每次调用工具前用一句话说明原因
- 若已有捕获数据（用户提问时未提供 URL），可跳过 navigate_and_capture 直接分析
- 对工具返回数据用自然语言解读，不直接粘贴大量 JSON
- 置信度不高时主动说明局限性`;

const MAX_ROUNDS = 10;

class LLMAgent {
    /**
     * @param {object}   provider      - OllamaProvider 实例
     * @param {object}   toolRegistry  - ToolRegistry 实例
     * @param {function} streamCallback - (event) => void，实时推送给渲染进程
     */
    constructor(provider, toolRegistry, streamCallback) {
        this.provider       = provider;
        this.toolRegistry   = toolRegistry;
        this.streamCallback = streamCallback;
        this._stopped       = false;
    }

    /**
     * 执行 ReAct 推理循环
     * @param {string}   userMessage - 用户输入的自然语言问题
     * @param {object[]} history     - 历史对话消息（可选，用于多轮对话）
     */
    async chat(userMessage, history = []) {
        this._stopped = false;

        const messages = [
            { role: 'system', content: SYSTEM_PROMPT },
            ...history,
            { role: 'user', content: userMessage }
        ];

        let rounds = 0;

        for (let round = 0; round < MAX_ROUNDS; round++) {
            if (this._stopped) break;
            rounds = round + 1;

            // 通知 UI 当前在第几轮等待 LLM 响应
            this.streamCallback({ type: 'thinking', round: rounds });

            let response;
            try {
                response = await this.provider.chat(messages, this.toolRegistry.getSchemas());
            } catch (err) {
                this.streamCallback({
                    type:    'error',
                    message: `调用 Ollama 失败：${err.message}\n\n请检查：\n• 服务地址是否正确\n• 模型是否已在服务端下载`
                });
                return;
            }

            // 推送 LLM 的文本回复（思考过程 / 最终答案）
            if (response.content && response.content.trim()) {
                this.streamCallback({ type: 'text', content: response.content });
            }

            // 无工具调用 → 推理结束
            if (!response.tool_calls || response.tool_calls.length === 0) {
                // 第一轮就没有工具调用且无内容，说明模型可能不支持 tool calling
                if (round === 0 && (!response.content || !response.content.trim())) {
                    this.streamCallback({
                        type:    'error',
                        message: '模型未返回任何内容。可能原因：\n• 该模型不支持 Tool Calling（请换用 qwen2.5、llama3.1 等支持工具调用的模型）\n• 网络超时'
                    });
                }
                break;
            }

            // 将 assistant 回复追加到历史
            // 注意：必须使用 _raw（原始 Ollama 格式），否则下一轮 LLM 无法识别工具调用历史
            messages.push({
                role:       'assistant',
                content:    response.content || '',
                tool_calls: response.tool_calls.map(tc => tc._raw)
            });

            // 执行所有工具调用（顺序执行，保持对话历史一致性）
            for (const tc of response.tool_calls) {
                if (this._stopped) break;

                const start   = Date.now();
                const result  = await this.toolRegistry.execute(tc.name, tc.arguments);
                const elapsed = Date.now() - start;

                // 推送工具步骤给 UI
                this.streamCallback({
                    type:       'tool_step',
                    toolName:   tc.name,
                    toolCallId: tc.id,
                    input:      tc.arguments,
                    result:     result,
                    elapsed_ms: elapsed
                });

                // 将工具结果追加到历史
                // Ollama 不使用 tool_call_id，只需 role: tool + content
                messages.push({
                    role:    'tool',
                    content: JSON.stringify(result)
                });
            }
        }

        this.streamCallback({ type: 'done', rounds });
    }

    /** 中止当前推理循环 */
    stop() {
        this._stopped = true;
    }
}

module.exports = { LLMAgent };
