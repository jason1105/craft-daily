---
date: 2026-09-28
tool: hermes-studio
tool_name: Hermes Studio
title: "注入的 MCP Server：禁用而非删除"
level: 进阶
source_title: "docs/planning/ekko-agent-configuration-pages.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/ekko-agent-configuration-pages.md
---

# 注入的 MCP Server：禁用而非删除

## 什么时候用得上

你想让 Studio 启动时注入到某个 Ekko Profile 的 MCP server 长期保持关闭状态，于是在页面上把它删掉，结果这个改动在后续启动中并不可靠。

## 怎么做

1. 打开 Ekko 唯一的规范配置文件（Studio 没有自己的 MCP sidecar）：

```text
.ekko/config/config.json
```

2. 在 `mcp.profiles.<profile>.servers` 下定位 Studio 启动时注入的那 4 个 managed 定义，**不要删除条目**，只改这一个键：

```text
mcp.profiles.<profile>.servers.<name>.enabled: false
```

3. 改完用这个路由验证 transport 与连通性：

```text
POST /api/ekko/mcp/servers/:name/test
```

## 为什么

Managed 定义是在 Studio 启动时注入到每个 Ekko Profile 的，所以「删除」并不是一个持久状态，而文档明确只承诺 `enabled: false` 会跨重新注入被保留。由于 API、页面和这个 config module 读写的是同一份数据，直接改文件与在页面上改效果等价，但只有显式禁用才是稳定的。不这样做，你精心调整的 Profile 会在下一次启动时被注入逻辑覆盖。

## 原文依据

> As on the Hermes MCP page, those injected entries can be edited, removed, enabled, or disabled; an existing `enabled: false` value is preserved across reinjection.

来源：[docs/planning/ekko-agent-configuration-pages.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/ekko-agent-configuration-pages.md)
