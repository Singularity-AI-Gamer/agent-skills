---
name: 163-email-ground-truth
description: 163 邮箱真值集构建、审计与跑批测试。当任务涉及 163 邮箱、网易邮箱、163 真值集、163 跑批时触发。包含 163 IMAP 特殊处理（ID 命令）、已知分类陷阱、已验证案例。
---

# 163 Email Ground Truth

## 触发条件

当任务涉及以下关键词时自动触发：
- 163 邮箱、网易邮箱、netease
- 163 真值集、163 跑批
- imap.163.com

## 必读文件

1. `references/workflow-163.md` — 163 专属工作流程
2. `references/pitfalls-163.md` — 163 踩坑记录
3. `references/case-study-163.md` — 本次 41 张已验证案例

## 与 QQ Skill 的关系

163 和 QQ 共用同一套核心处理逻辑，本 Skill 只记录 163 的**差异点**。
通用规则请参考 `qq-email-ground-truth` Skill。

## 关键差异

1. **IMAP ID 命令**：163 登录后必须发送 RFC 2971 ID 命令
2. **行程单分类**：163 转发邮件中行程报销单容易被误判为打车发票
3. **通讯费识别**：联通发票 seller 为"中国联合网络通信"，不能按"联通"匹配

## 真值集位置

`.claude/worktrees/test-163-batch/test_dataset/163_20260301_20260319/truth_manifest.json`

## 凭证

- 邮箱：<your-163-email>@163.com
- 授权码：<YOUR_163_AUTH_CODE>
- 区间：2026-03-01 ~ 2026-03-19
- INBOX 窗口邮件数：83
