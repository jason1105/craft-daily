---
date: 2026-10-08
tool: codex
tool_name: Codex CLI
title: "用 /llms.txt 和 .md 拉取原始文档"
level: 进阶
source_title: "Codex manual (Markdown)"
source_url: https://learn.chatgpt.com/docs/codex-manual.md
---

# 用 /llms.txt 和 .md 拉取原始文档

## 什么时候用得上

需要把 Codex 文档喂给本地检索、索引或做版本对比时，逐页复制很慢。先取完整索引，再对目标文档页 URL 追加 `.md` 获取 Markdown 版本。

## 怎么做

先取完整文档索引，再对目标页 URL 追加 `.md`。下面两个地址可直接复制使用：
```text
/llms.txt
https://learn.chatgpt.com/docs/web.md
```
例如页面 URL 追加 `.md` 即可得到 Markdown 版本；`/llms.txt` 是完整文档索引。

## 为什么

直接拿 Markdown 比逐页复制或维护 HTML 解析规则更稳定，便于 grep、diff 和向量化。否则每次同步文档都要重新处理页面结构，容易漏掉更新。

## 原文依据

> For the complete documentation index, see [llms.txt](/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

来源：[Codex manual (Markdown)](https://learn.chatgpt.com/docs/codex-manual.md)
