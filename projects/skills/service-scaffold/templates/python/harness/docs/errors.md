# 错误信封

业务错误、`HTTPException`、请求校验错误、未捕获异常都进入已注册的 handler。handler 把它们收成同一个失败信封：`success` 为假，`code` 为状态码，`msg` 为说明，`data` 为空。

校验错误的 `msg` 由各字段的位置和消息拼成。未捕获异常记日志，响应里的 `msg` 是固定的 `internal server error`，状态码是 500。
