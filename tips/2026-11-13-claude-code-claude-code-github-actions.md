---
date: 2026-11-13
tool: claude-code
tool_name: Claude Code
title: "组织级 secret 用 API key"
level: 进阶
source_title: "Claude Code GitHub Actions"
source_url: https://code.claude.com/docs/en/github-actions.md
---

# 组织级 secret 用 API key

## 什么时候用得上

你正把 Claude Code GitHub Action 推广到多个仓库，准备用组织级 Actions secret 统一认证。若沿用个人 OAuth token，生成者订阅一旦变化，所有仓库的 @claude 会一起失效。

## 怎么做

在组织级 Actions secrets 中保存 `ANTHROPIC_API_KEY`，然后把各仓库 workflow 的认证输入设为：

```yaml
anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

若之前配置的是 OAuth token，删除并替换这一行：

```yaml
claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

这样每个仓库不再需要单独存 secret。

## 为什么

OAuth token 绑定运行 `claude setup-token` 的个人订阅，不适合作为跨仓库共享凭据；一旦该订阅变更或 token 失效，所有仓库同时断。API key 不依赖个人，组织级轮换也更简单。

## 原文依据

> For a secret shared across repositories, authenticate with an API key from the [Claude Console](https://platform.claude.com) rather than an OAuth token, since an OAuth token is tied to the subscription of the person who ran `claude setup-token`.

来源：[Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions.md)
