---
date: 2026-09-15
tool: hermes-studio
tool_name: Hermes Studio
title: "用新 mobile run 重新绑定设备"
level: 进阶
source_title: "docs/chat-chain-changes/2026-09-05-mobile-device-target.md"
source_url: https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-mobile-device-target.md
---

# 用新 mobile run 重新绑定设备

## 什么时候用得上

部署了把 calendar/reminder consent 绑定到认证发起设备的变更后，你要做验收。若直接 resume 旧会话或从 web 触发，设备目标不会转移，测试会误判。

## 怎么做

1. 在 `docs/chat-chain-changes/2026-09-05-mobile-device-target.md` 中确认 frontmatter 已声明 fail-closed：
```yaml
---
date: 2026-09-05
pr: pending
feature: Bind calendar/reminder consent to authenticated originating device
impact: No broadcast to every App; foreign responses ignored and replay filtered. Unknown origin or offline target fails closed.
---
```
2. 验收时不要 resume 旧 session；在已认证 mobile 上发起新的 direct run，读取返回的 pseudonymous `device_id` 作为证据。Web/unknown-origin runs cannot silently choose a device.

## 为什么

身份来自 verified app_access token，不是客户端声明的 device ID；reading/resuming a session does not transfer ownership。旧 session 或 unknown origin 会 fails closed，只有 new originating mobile run after deployment 才能拿到验收证据。

## 原文依据

> Requires new originating mobile run after deployment.

来源：[docs/chat-chain-changes/2026-09-05-mobile-device-target.md](https://github.com/EKKOLearnAI/hermes-studio/blob/main/docs/chat-chain-changes/2026-09-05-mobile-device-target.md)
