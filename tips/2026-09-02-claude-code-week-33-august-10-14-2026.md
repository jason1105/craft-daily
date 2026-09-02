---
date: 2026-09-02
tool: claude-code
tool_name: Claude Code
title: "用 /subtask 开子任务，自动继承上下文"
level: 进阶
source_title: "Week 33 · August 10–14, 2026"
source_url: https://code.claude.com/docs/en/whats-new/2026-w33.md
---

# 用 /subtask 开子任务，自动继承上下文

## 什么时候用得上

Claude 已经陪你讨论了很久，你又想让它去补测试或查一个侧线问题；不想把前面的背景再重讲一遍。

## 怎么做

在交互式会话输入框直接发起 fork 子任务：

```text
> /subtask draft unit tests for the parser changes so far
```

fork 会出现在 prompt 下方的面板中，做完后结果回到当前对话。若不想要默认的 fork 模式，设置环境变量 `CLAUDE_CODE_FORK_SUBAGENT=0` 即可关闭。

## 为什么

fork 子任务会继承完整对话和 prompt cache，侧线任务不用重新解释上下文；否则子任务从空白开始，容易丢约束、反复补背景。

## 原文依据

> Start a fork yourself with a task that needs everything you've discussed so far:

来源：[Week 33 · August 10–14, 2026](https://code.claude.com/docs/en/whats-new/2026-w33.md)
