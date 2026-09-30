---
date: 2026-09-30
tool: codex
tool_name: Codex CLI
title: "Codex 审查与评论分 job 隔离权限"
level: 进阶
source_title: "Codex GitHub Action"
source_url: https://learn.chatgpt.com/docs/github-action.md
---

# Codex 审查与评论分 job 隔离权限

## 什么时候用得上

你希望 Codex 自动审 PR，但不放心让执行 Codex 的 job 持有可写 token。把执行和评论拆成两个 job，只让评论步骤拿 issues 和 pull-requests 写权限。

## 怎么做

使用示例中的两段式 job：codex job 只给 `contents: read`，通过 `outputs.final_message` 暴露结果；post_feedback job 依赖它，并在 `final_message` 非空时用 `github-script` 发评论。配置如下：

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}
```

## 为什么

Codex 能读写仓库，若执行 job 同时拥有 issues 和 pull-requests 写权限，一旦被提示注入或误操作，评论和 issue 面也会暴露。拆 job 后 Codex 只在 `contents: read` 下运行，写权限收敛到只发评论的步骤，且用 `needs.codex.outputs.final_message != ''` 避免空评论。

## 原文依据

> The action emits the last Codex message through the `final-message` output. Map it to a job output (as shown above) or handle it directly in later steps.

来源：[Codex GitHub Action](https://learn.chatgpt.com/docs/github-action.md)
