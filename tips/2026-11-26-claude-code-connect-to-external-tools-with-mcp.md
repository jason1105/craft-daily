---
date: 2026-11-26
tool: claude-code
tool_name: Claude Code
title: "用启动等待毫秒数驯服 MCP 首轮延迟"
level: 专家
source_title: "Connect to external tools with MCP"
source_url: https://code.claude.com/docs/en/agent-sdk/mcp.md
---

# 用启动等待毫秒数驯服 MCP 首轮延迟

## 什么时候用得上

你的 Agent 启动时挂了多个 MCP server，首轮经常被 pending 的 settings-file 或 plugin server 拖慢，甚至有 stdio server 等到默认 30 秒超时。想按项目或网关环境统一控制首轮最多等多久。

## 怎么做

在传给 `query()` 的 `env` option 里设置该变量。下面按原文示例的值写，`5000` 即最多等待 5000 毫秒：

```text
CLAUDE_CODE_MCP_STARTUP_WAIT_MS: "5000"
```

## 为什么

默认首轮等待会随 `options.mcpServers`、tool search 和 server 来源变化，非关键 server 容易把首轮拖到默认 `MCP_TIMEOUT`。显式设置后，pending 的 settings-file/plugin server 只等这个上限，并同样替换 `options.mcpServers` 中 stdio、HTTP、SSE server 的 `MCP_TIMEOUT` 等待。

## 原文依据

> To choose the first-turn wait yourself, set `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` in the [`env` option](https://code.claude.com/docs/en/agent-sdk/configuration#set-environment-variables), for example `CLAUDE_CODE_MCP_STARTUP_WAIT_MS: "5000"`.

来源：[Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp.md)
