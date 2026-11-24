---
date: 2026-11-24
tool: codex
tool_name: Codex CLI
title: "用 /debug-config 核对下发策略"
level: 进阶
source_title: "Self-host Codex configuration for your team"
source_url: https://learn.chatgpt.com/docs/enterprise/configuration-server.md
---

# 用 /debug-config 核对下发策略

## 什么时候用得上

团队自建 HTTPS 配置服务器给 Codex CLI 分发默认值与强制要求时，发布前需要在测试机确认配置层和策略来源都正确。

## 怎么做

在测试机把 `[config_server]` 写入系统 `requirements.toml`（Linux/macOS 为 `/etc/codex/requirements.toml`）：
```toml
[config_server]
base_url = "https://codex-config.example.com/team"
```
确保服务端对 `GET {config_server.base_url}/codex/config/bundle` 返回 `200 OK` 和 JSON configuration bundle。然后在项目目录启动并检查：
```bash
codex
```
在交互提示符输入：
```text
/debug-config
```
在 **Config layer stack** 找 `enterprise-managed (Default web search, search-default) (enabled)`；在 **Requirements** 查你强制项的 policy source。

## 为什么

这样能在测试机同时验证 defaults 和 requirements 两条下发链路，而不是只看服务端返回。若跳过检查，Codex 可能先用缓存设置启动并在后台刷新，策略未真正生效就被推广。

## 原文依据

> Codex can start with cached settings and refresh them in the background. After you change a policy on the server, wait for Codex to refresh it, then start a new session and repeat the check before rolling it out to other machines.

来源：[Self-host Codex configuration for your team](https://learn.chatgpt.com/docs/enterprise/configuration-server.md)
