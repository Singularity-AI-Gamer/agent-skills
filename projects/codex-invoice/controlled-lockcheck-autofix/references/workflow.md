# Workflow

Use this sequence for unattended QQ controlled lockcheck automation:

1. Run `python autofix_controller.py run-once ...` for a single unattended round, or `python autofix_controller.py loop ...` for bounded iteration.
2. Let the controller call `prepare_qq_lockcheck_run.py --automation-autostart`.
3. Let the controller start `launch_monitor_run.ps1` first, then `launch_frontend_run.ps1`.
4. Let the frontend start itself once through controlled autostart; do not inject a backend-only bypass.
5. Wait for monitor completion or controller timeout.
6. Run `postprocess_run.ps1`.
7. Read `run_summary.json`, `manual_check_user_burden.json`, `strict_truth_audit.json`, `qq_lockcheck_report.json`, and `truth_detail_matrix.csv`.
8. Emit a decision:
   - `pass` when `P0=0` and `user_should_review_count<=6`
   - `blocked_human_review` when the next fix would touch protected core logic
   - `continue` only when the failure is inside bounded autofix scope and the next round policy is explicit

Keep every round in its own diagnostics subdirectory. Never overwrite historical evidence.
