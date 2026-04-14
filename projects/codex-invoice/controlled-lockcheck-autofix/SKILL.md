---
name: controlled-lockcheck-autofix
description: Use for unattended QQ controlled frontend lockcheck runs, failure classification, bounded autofix decisions, and packaging-gate evidence in this repository. Trigger when the task is to automate full frontend batch tests, run controlled lockcheck loops, classify QQ truth-audit failures, or decide whether an autofix may continue without touching protected core rules.
---

# Controlled Lockcheck Autofix

Project-local skill for unattended QQ frontend lockcheck automation.

Read `references/workflow.md` first. Read `references/failure-taxonomy.md` when classifying a failed round. Read `references/guardrails.md` before proposing or applying any fix.

## Hard Boundaries

- Keep the current frontend design and visible interaction unchanged.
- Treat `tree20260315` as the reference behavior for core invoice-grab rules.
- Do not expand invoice discovery rules just to chase a failing round.
- Airbnb and similar non-target documents must keep exclusion evidence, but must not be counted as missing truth invoices.
- If a candidate fix touches FROZEN or GUARDED ZONE, stop and emit a blocking report instead of editing.

## Required Workflow

1. Prepare an isolated controlled run with `prepare_qq_lockcheck_run.py`.
2. Launch monitor and frontend, then rely on controlled autostart instead of manual clicking.
3. Wait for the round to finish or block.
4. Run `postprocess_qq_lockcheck.py`.
5. Classify the round from `process_log.txt`, `monitor_status.json`, `strict_truth_audit.json`, and `qq_lockcheck_report.json`.
6. Only continue unattended iteration when the failure is inside the bounded autofix scope.

## Output Expectations

- Persist per-round `classification.json`, `decision.json`, and `round_summary.md`.
- Keep run-root evidence paths, top blockers, and packaging-gate metrics in every round summary.
- State explicitly whether the round passed packaging gate: `P0=0` and `user_should_review_count<=6`.
