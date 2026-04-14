# Failure Taxonomy

Use only evidence-backed categories:

- `frontend_launch_blocked`
  - Signals: no `run_state_events.jsonl`, no valid `start_processing` transition, or controller timeout before a stable run state.
  - Typical actions: raise controlled autostart delay, inspect saved credentials, inspect frontend launcher evidence.

- `controlled_url_blocking`
  - Signals: `process_log.txt` shows non-target URL/captcha/timeout patterns such as Airbnb, Proofpoint, Fidelity, or repeated Playwright timeout.
  - Typical actions: preserve exclusion evidence, stop if the required fix would touch protected core processing flow.

- `provider_recovery_failed`
  - Signals: logs or findings point to Baiwang or direct-invoice provider recovery gaps.
  - Typical actions: stop for guarded review unless a strictly bounded helper-layer fix exists.

- `attachment_pipeline_regression`
  - Signals: target attachments fall into `raw_invoices`, retention, or `Manual_Check` with attachment-oriented evidence.
  - Typical actions: stop for protected-zone review.

- `truth_match_gap`
  - Signals: postprocess completed, but there is still unexplained `P0`.
  - Typical actions: summarize truth gaps and stop unless the defect is clearly outside protected core logic.

- `manual_check_overload`
  - Signals: `P0=0` but `user_should_review_count>6`.
  - Typical actions: investigate bounded helper-layer fixes only if they do not change visible frontend or protected extraction logic.

- `new_regression_outside_scope`
  - Signals: missing artifacts, broken postprocess, or unclassified failure patterns.
  - Typical actions: stop and report.
