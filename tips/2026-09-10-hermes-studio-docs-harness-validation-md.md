---
date: 2026-09-10
tool: hermes-studio
tool_name: Hermes Studio
title: "用verify-desktop-mcp测打包"
level: 专家
source_title: "docs/harness/validation.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/validation.md
---

# 用verify-desktop-mcp测打包

## 什么时候用得上

你在改 managed MCP 注入或桌面打包，需要确认真实包在 Node 模式被移除时仍能启动内置 MCP。此时不必起 Gateway，直接对打包产物跑验证脚本。

## 怎么做

```bash
node scripts/verify-desktop-mcp.mjs '<packaged executable>' '<resources directory>'
```
将 `<packaged executable>` 和 `<resources directory>` 替换为实际打包可执行文件与 resources 目录。脚本会以临时状态运行，不需要运行中的 Gateway。

## 为什么

长驻 External Gateway 可能把旧 MCP 定义留在内存里，只测开发态会漏掉打包入口在 Node 模式缺失时的 fallback。该脚本会故意移除 Node 模式，检查四个工具集、JSON-RPC initialize 响应和 stdin EOF 干净退出，且不需要运行中的 Gateway。

## 原文依据

> loading GUI or updater code, even when Node mode is absent. Test the real package:

来源：[docs/harness/validation.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/harness/validation.md)
