# 双邮箱回归门禁

## 何时触发

当代码改动触碰 `CLAUDE.md` 中定义的 FROZEN 或 GUARDED ZONE 时，必须执行此门禁。

## 门禁流程

```
代码改动
  ↓
检查改动范围 → SAFE ZONE → 跳过门禁，直接提交
  ↓（FROZEN/GUARDED）
并行启动两个验证：
  ├── Agent A: 163 真值集跑批 → strict_truth_audit → P0 报告
  └── Agent B: QQ 真值集跑批 → strict_truth_audit → P0 报告
  ↓
两个都 P0=0 → ✅ 允许提交
任一 P0>0   → ❌ 回滚改动，分析原因
```

## 验证命令模板

### 163 验证
```bash
cd .claude/worktrees/test-163-batch
python run_163_batch_test.py
python strict_truth_audit.py --run-root <output_dir> --truth-manifest test_dataset/163_20260301_20260319/truth_manifest.json
```

### QQ 验证
```bash
python strict_truth_audit.py --run-root <output_dir> --truth-manifest test_dataset/qq_20260201_20260311_final/truth_manifest.json
```

## 判定规则

| 163 结果 | QQ 结果 | 决定 |
|---|---|---|
| P0=0 | P0=0 | ✅ 提交 |
| P0=0 | P0>0 | ❌ 改动影响了QQ，回滚 |
| P0>0 | P0=0 | ❌ 163还没修好，继续迭代 |
| P0>0 | P0>0 | ❌ 严重问题，优先修复 |
