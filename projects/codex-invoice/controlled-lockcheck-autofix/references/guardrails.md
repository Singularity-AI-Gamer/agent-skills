# Guardrails

## Packaging Gate

- QQ controlled run must end with `P0=0`.
- `manual_check_user_burden.user_should_review_count` must be `<=6`.
- P2 does not block, but must remain recorded.

## Protected Areas

- FROZEN or GUARDED logic must not be edited by unattended autofix.
- In this project, protected review includes changes that would alter:
  - core extraction logic
  - core processing loop behavior
  - guarded provider logic
  - shared mail parsing helpers

## Allowed Autofix Scope

- Controlled-run context helpers
- Controlled autostart wiring
- Monitor scripts
- Postprocess orchestration
- Analysis/reporting helpers
- New `autofix_*` files
- Skill files under `.agent/skills/*`

## Stop Conditions

- Packaging gate passed
- Same failure repeats without metric improvement
- Two rounds show no primary-metric improvement
- The next candidate fix would touch protected files
- The session reaches its configured maximum rounds

## Evidence Rules

- Keep `cleanup_state.json/.md`.
- Keep `monitor_status.json`, `runtime_samples.jsonl`, `run_state_events.jsonl`, `stage_events.jsonl`, and `artifact_events.jsonl`.
- Keep `process_log.txt`.
- Keep truth-audit and lockcheck report outputs.
- Keep exclusion evidence for Airbnb and other non-target documents; do not silently drop them.
