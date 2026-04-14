---
name: feishu-automation
description: 飞书（Lark）自动化能力。优先使用飞书官方 OpenAPI MCP/CLI 处理消息、群组、Base、文档、任务与日历等 OpenAPI 能力；不把开发者后台配置动作误判为 MCP 能力。
allowed-tools: mcp__lark-mcp_*, Bash, Read, Write, Edit
---

# 飞书自动化

这个 Skill 以飞书官方文档与官方仓库为准，不再把 Skill 自己当作事实源。

## 官方来源

- OpenAPI MCP 官方仓库: <https://github.com/larksuite/lark-openapi-mcp>
- MCP 概览: <https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/mcp_integration/mcp_introduction>
- 自建应用开发流程: <https://open.feishu.cn/document/home/introduction-to-custom-app-development/self-built-application-development-process>
- 官方配置指南: <https://github.com/larksuite/lark-openapi-mcp/blob/main/docs/usage/configuration/configuration.md>
- 官方 CLI 参考: <https://github.com/larksuite/lark-openapi-mcp/blob/main/docs/reference/cli/cli.md>

## 使用前提

1. 当前会话必须已经加载 `mcp__lark-mcp_*`。
2. 如果工具不存在，先运行：

```bash
node .agents/skills/feishu-automation/feishu-mcp-setup.js <app_id> <app_secret>
```

3. 脚本会优先写入 `~/.codex/config.toml`，仅在 Codex 配置不存在时回退到 `~/.claude.json`。
4. 配置完成后必须重启 Codex，新 MCP server 才会生效。

## 官方 MCP 配置原则

- 使用官方包：`@larksuiteoapi/lark-mcp`
- 默认使用应用身份，不启用 OAuth
- 默认使用飞书中国区，不额外传 `--domain`
- 工具命名固定为 `camel`

对应官方 MCP 命令形态为：

```bash
npx -y @larksuiteoapi/lark-mcp mcp \
  -a <app_id> \
  -s <app_secret> \
  -t preset.light,preset.default,preset.im.default,preset.base.default,preset.base.batch,preset.doc.default,preset.task.default,preset.calendar.default,docx.v1.documentBlock.patch,docx.v1.documentBlockChildren.create,docx.v1.documentBlockChildren.batchDelete \
  -c camel \
  -l zh \
  --token-mode tenant_access_token
```

如果后续必须访问用户私有资源，再执行官方登录命令：

```bash
npx -y @larksuiteoapi/lark-mcp login -a <app_id> -s <app_secret>
```

然后在 MCP 配置里追加：

```text
--oauth --token-mode user_access_token
```

## 适合交给 MCP 的能力

- 消息发送与查询
- 群组创建、搜索、成员管理
- Base 创建、表结构与记录读写
- 文档查询、导入、权限设置
- 任务、日历等开放接口能力

## 不适合交给 MCP 的能力

以下动作属于飞书开放平台控制台，不应假设能由这个 Skill 自动完成：

- 事件订阅配置
- 权限开关勾选
- 机器人“仅接收被 @ 消息”等后场范围设置
- 发布新版本

另外，基于官方仓库当前说明，以下能力仍有限制：

- 文件上传/下载暂不支持
- 飞书云文档直接编辑暂不支持

因此，本项目的 PDF/DOCX 下载与解析继续保留在后端实现，不迁移到 MCP。

## 使用规则

- 用户要求“飞书自动化”时，优先确认 `mcp__lark-mcp_*` 是否可用。
- 如果工具不可用，先补 MCP，再继续自动化，不要把 Skill 本身假装成 MCP。
- 若任务涉及开放平台后台发布或权限切换，明确说明这是控制台动作，再把 MCP 用于后续 OpenAPI 验证或数据同步。
- 对当前仓库，优先把 MCP 用在 Bot、群、Base、文档导入、消息发送等动作上。
