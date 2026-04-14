---
name: qq-email-ground-truth
description: Build, rebuild, audit, and compare QQ mailbox invoice ground truth datasets for this repository using the existing truth-building scripts and evidence artifacts. Use when the task is to generate a QQ mailbox ground truth set, validate QQ batch output against truth, review QQ mailbox invoice evidence, or investigate QQ-specific invoice extraction pitfalls in this project.
---

# QQ Email Ground Truth

Use this project-level skill for QQ mailbox ground truth work in this repository.

Read `references/workflow.md` and `references/pitfalls.md` first. Read `references/case-study-qq-20260201-20260311.md` and `references/project-artifacts.md` when you need a validated example, current artifact paths, or prior evidence.

## Hard Boundaries

- Treat this as a project-local skill, not a global mailbox skill.
- Treat the current case-study counts, type distribution, and mail IDs as one validated example only. Do not reuse them as fixed thresholds for future QQ runs.
- Treat the currently known reimbursable types as a reference range, not a closed list. If a new type, provider, attachment pattern, or procurement scenario appears, send it to review instead of auto-excluding it.
- Reuse `build_truth_dataset.py` and `audit_email_truth.py`. Do not create a parallel truth-building flow unless the user explicitly asks for one.

## Required Workflow

1. Confirm the mailbox account, mailbox folder, and time window.
2. Follow `references/workflow.md` for the build and validation sequence.
3. Use `references/pitfalls.md` as the default debug checklist when counts or fields look wrong.
4. Use `references/case-study-qq-20260201-20260311.md` only as a worked example and evidence sample.
5. Use `references/project-artifacts.md` to find the current canonical manifests, reports, and diagnostics.

## Output Expectations

- Prefer `truth_manifest.json` for machine comparison.
- Prefer `ground_truth_report.md` for human review.
- Require `pending_review_count = 0` before calling a dataset final.
- Keep excluded-email and excluded-document audit trails instead of silently dropping evidence.
