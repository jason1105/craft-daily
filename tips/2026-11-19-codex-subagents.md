---
date: 2026-11-19
tool: codex
tool_name: Codex CLI
title: "固化子代理委派并用 /subagents 巡检"
level: 进阶
source_title: "Subagents"
source_url: https://learn.chatgpt.com/docs/agent-configuration/subagents.md
---

# 固化子代理委派并用 /subagents 巡检

## 什么时候用得上

你每次让 Codex 审分支都要手打并行子代理指令，且探索/测试输出把主线程塞满。把原文示例委派指令固化到适用的 `AGENTS.md` 或 skill instructions，后续让 CLI 自动遵循。

## 怎么做

在适用的 `AGENTS.md` 或 skill instructions 中加入这段委派请求（原文示例）：
```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.
```
在交互式 CLI session 中触发后，用以下命令查看/切换运行中的 agent 线程：
```text
/subagents
```
主线程会收集子代理结果到最终响应。

## 为什么

手动每次写并行指令容易漏掉等待全部、按类别汇总，原始中间输出会污染主线程；固化后 Codex 可按适用的 `AGENTS.md` 或 skill instructions 请求委派，并用 `/subagents` 巡检线程而不是把噪声拉回主线程。

## 原文依据

> applicable `AGENTS.md` or skill instructions that request delegation.

来源：[Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md)
