---
date: 2026-09-29
tool: claude-code
tool_name: Claude Code
title: "外部编辑器编辑提示时自动带入上一轮回复"
level: 进阶
source_title: "Interactive mode"
source_url: https://code.claude.com/docs/en/interactive-mode.md
---

# 外部编辑器编辑提示时自动带入上一轮回复

## 什么时候用得上

你要在默认编辑器里大幅改写提示，且希望新提示能直接引用 Claude 上一轮回复中的具体内容时。手动复制上一轮回复既慢又容易漏掉错误信息或代码片段。

## 怎么做

```text
/config
```
开启 **Show last response in external editor** 后，回到输入框按 `Ctrl+G` 或 `Ctrl+X Ctrl+E`。编辑器里会在你的提示上方带入 Claude 上一轮回复，并以 `#` 注释标记；保存后注释块会被剥离。

## 为什么

开启后，上一轮回复会作为 `#` 注释自动置于编辑器中的提示上方，保存时注释块被剥离，不会污染最终 prompt；不开启则只能手动搬运上下文，容易漏关键信息。

## 原文依据

> Turn on **Show last response in external editor** in `/config` to prepend Claude's previous reply as `#`-commented context above your prompt; Claude Code strips the comment block when you save

来源：[Interactive mode](https://code.claude.com/docs/en/interactive-mode.md)
