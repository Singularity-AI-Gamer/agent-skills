---
name: email-batch-test
description: 跑批测试标准与双邮箱回归门禁。当任务涉及"跑批"、"batch test"、"真值审计"、"回归验证"、"regression"时触发。确保每次跑批都遵守 P0/P1/P2 标准，且触碰保护区域的改动必须通过双邮箱验证。
---

# 跑批测试 Skill

## 触发条件

当任务涉及以下关键词时自动触发：
- 跑批、batch test、批量测试
- 真值审计、truth audit
- 回归验证、regression
- P0、P1、P2

## 必读文件

1. 项目根目录 `CLAUDE.md` — 了解 FROZEN/GUARDED/SAFE 区域定义
2. `references/test-standards.md` — P0/P1/P2 量化标准
3. `references/regression-gate.md` — 双邮箱回归门禁流程

## 核心规则

1. **跑批前**：确认使用哪个邮箱的真值集
2. **跑批后**：必须运行 `strict_truth_audit.py` 对比真值
3. **修改代码后**：检查改动是否触碰 FROZEN/GUARDED ZONE
4. **触碰保护区域**：必须同时跑 QQ + 163 真值集验证
5. **提交前**：P0 必须 = 0

## 真值集位置

- QQ：`test_dataset/qq_20260201_20260311_final/truth_manifest.json`
- 163：`.claude/worktrees/test-163-batch/test_dataset/163_20260301_20260319/truth_manifest.json`
