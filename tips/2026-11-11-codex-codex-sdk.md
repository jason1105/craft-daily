---
date: 2026-11-11
tool: codex
tool_name: Codex CLI
title: "run 的 sandbox 会延续到后续轮次"
level: 进阶
source_title: "Codex SDK"
source_url: https://learn.chatgpt.com/docs/codex-sdk.md
---

# run 的 sandbox 会延续到后续轮次

## 什么时候用得上

在 Python SDK 驱动的自动化里，你让 Codex 先改工作区，再只读审查 diff。别以为 read_only 只影响审查这一轮——它会把限制带到该线程后续轮次。

## 怎么做

直接复用官方沙箱预设示例，先写后只读审查：
```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)
```
注意：传给 `run(...)` 的 sandbox 会应用到该 turn 及该线程后续 turns；如果后面还要继续写文件，不要把 `read_only` 放在中间。

## 为什么

这样可以按轮次收紧权限，用只读沙箱审查 diff；但忽略延续性会让后续轮次仍被 read_only 限制，出现看似莫名的写入失败。把只读审查放在最后，或明确意识到后续轮次继承该 sandbox，能避免这类自动化坑。

## 原文依据

> A sandbox
passed to `run(...)` or `turn(...)` applies to that turn and later turns
on the thread.

来源：[Codex SDK](https://learn.chatgpt.com/docs/codex-sdk.md)
