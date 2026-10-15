---
date: 2026-10-15
tool: claude-code
tool_name: Claude Code
title: "企业版云会话先开 GitHub 连接器"
level: 进阶
source_title: "Get started with Claude Code in the cloud"
source_url: https://code.claude.com/docs/en/web-quickstart.md
---

# 企业版云会话先开 GitHub 连接器

## 什么时候用得上

你在 Team/Enterprise 计划下打开 claude.ai/code 想跑云会话，但登录后没有 GitHub 授权按钮，只看到 GitHub access is required for Claude Code cloud sessions。别急着查仓库权限或 Claude GitHub App，先确认组织连接器是否开启。

## 怎么做

让 Claude 组织的 Owner 打开配置并启用 GitHub connector：
```text
Organization settings > Connectors
```
开启后刷新 `claude.ai/code`，从第一步重新开始。若还想让成员用 `/web-setup` 和自动创建环境，再打开 Quick setup：
```text
Organization settings > Claude Code
/web-setup
```

## 为什么

在 Team/Enterprise 计划中，未开启连接器时 Sign in with GitHub 步骤不会出现，云会话直接被卡住。先让 Owner 开连接器并刷新页面，比在仓库权限、App 安装上排查更快。Quick setup 打开后 `/web-setup` 才可用，onboarding 也会为成员创建环境。

## 原文依据

> On Team and Enterprise plans, the **Sign in with GitHub** step works only after an [Owner](/docs/en/server-managed-settings#access-control) of your Claude organization turns on the GitHub connector at [**Organization settings > Connectors**](https://claude.ai/admin-settings/connectors).

来源：[Get started with Claude Code in the cloud](https://code.claude.com/docs/en/web-quickstart.md)
