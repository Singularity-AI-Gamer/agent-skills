---
name: aliyun-openapi-mcp-ops
description: Use when operating Alibaba Cloud through a custom OpenAPI MCP server, especially for SWAS deployment workflows: OAuth setup, selector updates, missing-tool diagnosis, deployment permission closure, and pre-deploy verification.
version: 1.0.0
---

Category: service

# Alibaba Cloud OpenAPI MCP Ops

Use this skill when:

- Codex can see an Alibaba Cloud custom MCP server, but the required tools are missing.
- You need to close SWAS deployment permissions before bootstrap or release.
- You need to verify OAuth, tool loading, region, instance discovery, or Cloud Assistant readiness.
- You are using a project-integrated OpenAPI MCP server instead of an Aliyun plugin.

This skill is based on a verified SWAS deployment-prep workflow against a custom OpenAPI MCP server.

## Scope

This skill covers:

- Custom OpenAPI MCP server endpoint and OAuth handling
- Selector updates for SWAS deployment operations
- Codex desktop reload behavior after MCP changes
- SWAS instance readiness checks before deployment
- Low-risk remote command validation through Cloud Assistant

This skill does not cover:

- Full application deployment steps
- Public web ingress setup
- ECS-specific operations outside the SWAS path

## Core Lessons

1. A custom OpenAPI MCP server may authenticate successfully while still missing required tools.
   OAuth success does not imply deployment selectors are present.

2. The custom MCP server id in the endpoint path is case-sensitive.
   If the id casing is wrong, the browser flow may still open, but the server will not load correctly.

3. Codex desktop does not reliably hot-load newly added MCP servers or updated selector sets.
   After changing the MCP config or custom server selectors, restart Codex before concluding the tools are still missing.

4. Read-only SWAS selectors are not enough for deployment.
   For deployment preparation, you need remote execution capability.

5. For SWAS deployment, the minimal useful mutating selectors are:
   - `RunCommand`
   - `CreateCommand`
   - `InvokeCommand`
   - `DeleteCommand`
   - `CreateSnapshot` (recommended before first deploy)

6. Firewall write permissions are not required by default for this project.
   If the app uses Feishu long connection and does not need inbound public HTTP immediately, do not add firewall write selectors unless a real deployment step needs them.

7. `Alibaba Cloud Linux 3` is an acceptable clean Linux base for this project.
   It is suitable for `Node + systemd + SQLite + logs + backup scripts`.

## Recommended Selector Set

Keep existing read-only selectors such as:

- `ListInstances`
- `ListInstanceStatus`
- `ListFirewallRules`
- `ListSnapshots`
- `DescribeCloudAssistantStatus`
- `DescribeCommands`
- `DescribeInvocations`
- `DescribeInvocationResult`

Add deployment selectors:

- `RunCommand`
- `CreateCommand`
- `InvokeCommand`
- `DeleteCommand`
- `CreateSnapshot`

Add firewall write selectors only if actually needed later:

- `CreateFirewallRule`
- `CreateFirewallRules`
- `ModifyFirewallRule`
- `EnableFirewallRule`
- `DisableFirewallRule`

## Workflow

1. Confirm the active custom MCP server name and endpoint.
   Example pattern: `https://openapi-mcp.<region>.aliyuncs.com/accounts/<account>/custom/<server-name>/id/<server-id>/sse`

2. Verify the server is actually loaded in the current Codex session.
   If the config was just added or changed, restart Codex first.

3. List available tools or attempt a minimal read-only SWAS query.
   If only read-only tools exist, do not try to deploy yet.

4. Close selector gaps on the custom MCP server.
   Use Alibaba Cloud OpenAPI Explorer management APIs to update the custom server.

5. Restart Codex after selector updates.
   Do not rely on the current session to pick up new tools.

6. Validate target instance readiness with read-only checks:
   - Instance exists in the expected region
   - Instance status is `Running`
   - Cloud Assistant is installed and healthy
   - Public IP is correct

7. Validate remote execution with one low-risk command:
   - `uname -a`
   - `node -v || true`

8. Fetch invocation results and confirm:
   - status is `Success`
   - exit code is `0`

9. Only after the above passes should you continue to server bootstrap or app deployment.

## Credential Policy

- Prefer OAuth-backed MCP for normal operation.
- Use AccessKey only for one-off MCP management when OAuth-backed tools cannot update selectors.
- Never leave AccessKey values in repo files, scripts, docs, or shell profiles after the operation.
- If a user pasted credentials into chat for emergency use, recommend rotation after the task.

## Deployment Readiness Checklist

Before claiming the SWAS side is ready, verify all of the following:

- Custom MCP server loads in Codex after restart
- SWAS deployment selectors are present
- Target region is correct
- Target instance id is confirmed
- Instance status is `Running`
- Cloud Assistant status is healthy
- Remote command execution succeeds
- Optional recovery snapshot is created if the upcoming step is risky

## Official Docs

- [OpenAPI MCP Server 使用指南](https://help.aliyun.com/zh/openapi/user-guide/openapi-mcp-server-guide)
- [CreateApiMcpServer](https://help.aliyun.com/zh/openapi/developer-reference/api-openapiexplorer-2024-11-30-createapimcpserver)
- [UpdateApiMcpServer](https://help.aliyun.com/zh/openapi/developer-reference/api-openapiexplorer-2024-11-30-updateapimcpserver)
- [轻量应用服务器 OpenAPI 集成概览](https://help.aliyun.com/zh/simple-application-server/developer-reference/using-openapi)
- [轻量应用服务器 API 概览](https://help.aliyun.com/zh/simple-application-server/developer-reference/api-swas-open-2020-06-01-overview)
- [重置轻量应用服务器系统](https://help.aliyun.com/zh/simple-application-server/user-guide/reset-a-simple-application-server)

## Validation

This skill is valid if it helps you answer these questions quickly and correctly:

- Is the custom Aliyun MCP server loaded in the current Codex session?
- Are the SWAS deployment selectors present?
- Is the instance actually ready for remote execution?
- Is the next blocker MCP permissions, instance state, or app deployment logic?
