---
date: 2026-10-07
tool: claude-code
tool_name: Claude Code
title: "LSP 无诊断时用 /plugin 查缺失二进制"
level: 进阶
source_title: "Code intelligence plugins"
source_url: https://code.claude.com/docs/en/plugins/code-intelligence.md
---

# LSP 无诊断时用 /plugin 查缺失二进制

## 什么时候用得上

你装了 `typescript-lsp`，但 Claude 改完 TypeScript 文件后没有出现诊断行，怀疑语言服务器根本没起来。

## 怎么做

在 Claude Code 会话中运行：

```text
/plugin
```

打开 **Errors** 标签，若看到：

```text
Executable not found in $PATH: "<binary>"
```

按提示安装缺失二进制。以 TypeScript 为例：

```bash
npm install -g typescript-language-server typescript
```

确认它在启动 `claude` 的 shell 的 PATH 中：

```bash
which typescript-language-server
```

PowerShell 可用：

```powershell
Get-Command typescript-language-server
```

安装后，下次 Claude 编辑匹配文件时会自动重试；若二进制不在 PATH，从正确的 shell 新开 session。

## 为什么

插件只告诉 Claude Code 用哪个命令启动语言服务器，并不包含服务器二进制。没有诊断行不一定是插件没装好，可能是二进制不在 PATH；直接查 Errors 标签能拿到缺失的二进制名，避免重装插件或重启会话。

## 原文依据

> run `/plugin` and open the **Errors** tab. A row reading `Executable not found in $PATH: "<binary>"` names the binary to install.

来源：[Code intelligence plugins](https://code.claude.com/docs/en/plugins/code-intelligence.md)
