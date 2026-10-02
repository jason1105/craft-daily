---
date: 2026-10-02
tool: claude-code
tool_name: Claude Code
title: "Alpine 装 Claude 后补 PATH"
level: 进阶
source_title: "Claude Code GitLab CI/CD"
source_url: https://code.claude.com/docs/en/gitlab-ci-cd.md
---

# Alpine 装 Claude 后补 PATH

## 什么时候用得上

在 GitLab CI 的 node:24-alpine3.21 作业里安装 Claude Code 后，脚本一调用 claude 就报找不到命令。这个坑在自定义 before_script 或精简 job 时最容易踩。

## 怎么做

在 `before_script` 中安装 Claude 后，立刻把安装目录加入 PATH，再执行原来的 `claude` 调用：

```yaml
before_script:
  - apk update
  - apk add --no-cache git curl bash
  - curl -fsSL https://claude.ai/install.sh | bash
  # The installer places claude in ~/.local/bin, which isn't on PATH in this image
  - export PATH="$HOME/.local/bin:$PATH"
script:
  - >
    claude
    -p "${AI_FLOW_INPUT:-'Review this MR and implement the requested changes'}"
    --permission-mode acceptEdits
    --allowedTools "Bash Read Edit Write mcp__gitlab"
    --debug
```

## 为什么

安装器把 claude 放到 ~/.local/bin，而该镜像默认 PATH 不包含它。省略 export PATH 时，后续 claude -p 无法启动；补上后同一 job 可直接使用。

## 原文依据

> # The installer places claude in ~/.local/bin, which isn't on PATH in this image

来源：[Claude Code GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd.md)
