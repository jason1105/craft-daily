---
date: 2026-11-09
tool: hermes-studio
tool_name: Hermes Studio
title: "旧 runtime 下 /learn 要显式报错"
level: 进阶
source_title: "docs/planning/learn-command-integration.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/learn-command-integration.md
---

# 旧 runtime 下 /learn 要显式报错

## 什么时候用得上

Web UI 已接入 `/learn`，但运行时 Hermes Agent 还没更新到包含 `agent/learn_prompt.py` 的版本。用户输入 `/learn` 时若 bridge 静默透传，看起来只是普通聊天，失败原因很难发现。

## 怎么做

在 `packages/server/src/modules/hermes/services/bridge/python/bridge_pool.py` 的 `dispatch_command()` 中识别 `learn`，从 `agent.learn_prompt` 导入 `build_learn_prompt`；导入失败时不要放行，返回明确错误：

```text
/learn requires a newer Hermes Agent runtime with agent.learn_prompt.
```

成功路径保持 bridge 返回 handled 结果，让 Web UI 用生成的 message 启动 run：

```python
{
    "session_id": session_id,
    "command": name,
    "handled": True,
    "type": "learn",
    "message": build_learn_prompt(arg),
}
```

## 为什么

明确报错能把版本不匹配立即暴露给用户和排障者；静默把 `/learn` 当普通文本透传，会让命令看似执行但实际没有生成技能。这样也保持上游 Agent 作为技能撰写规则的唯一来源，避免前端复制 prompt。

## 原文依据

> /learn requires a newer Hermes Agent runtime with agent.learn_prompt.

来源：[docs/planning/learn-command-integration.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/planning/learn-command-integration.md)
