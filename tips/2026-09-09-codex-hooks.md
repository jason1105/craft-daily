---
date: 2026-09-09
tool: codex
tool_name: Codex CLI
title: "改完 hook 不生效？先到 /hooks 里 trust 新哈希"
level: 进阶
source_title: "Hooks"
source_url: https://learn.chatgpt.com/docs/hooks.md
---

# 改完 hook 不生效？先到 /hooks 里 trust 新哈希

## 什么时候用得上

你在 ~/.codex/hooks.json 或 <repo>/.codex/hooks.json 里新增或修改了 hook，但运行 Codex 时它没有触发。启动时往往只有一行提示，不留意就错过了。

## 怎么做

新增或修改 hook 后，不要直接怀疑脚本逻辑。启动 Codex；若 hook 没跑，在 CLI 里执行：
```
/hooks
```
然后在弹出的列表里 review 这次新出现或被改动的 hook，并 trust 它。只有当前 hash 被 trust 的 hook 才会运行。

## 为什么

Codex 把 trust 绑定在 hook 的当前 hash 上，所以新增或改动过的 hook 会被标记为需要 review 并直接跳过。不先进入 /hooks trust，就会出现“配置看着对但就是不执行”的情况；安全类 hook 被跳过时尤其危险。

## 原文依据

> Codex records trust against the hook's current hash, so new or changed hooks are marked for review and skipped until trusted.

来源：[Hooks](https://learn.chatgpt.com/docs/hooks.md)
