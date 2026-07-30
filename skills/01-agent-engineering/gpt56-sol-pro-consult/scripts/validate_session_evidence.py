#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def nested(payload: dict[str, Any], *keys: str) -> Any:
    value: Any = payload
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def validate(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(payload.get("executed_by") == "main-codex-task", "executed_by must be main-codex-task")
    require(payload.get("schema_version") == "1.2", "schema_version must be 1.2")
    require(bool(payload.get("task_run_id")), "task_run_id is required")
    require(nested(payload, "browser", "type") == "iab", "browser.type must be iab")

    browser_ref = {
        "browser_id": nested(payload, "browser", "browser_id"),
        "tab_id": nested(payload, "browser", "tab_id"),
        "tab_url": nested(payload, "browser", "tab_url"),
    }
    require(all(browser_ref.values()), "browser_id, tab_id, and tab_url are required")

    for section in ("model_gate", "late_clean_gate", "dispatch", "response"):
        section_ref = nested(payload, section, "binding_ref")
        require(isinstance(section_ref, dict), f"{section}.binding_ref is required")
        if isinstance(section_ref, dict):
            require(section_ref.get("browser_id") == browser_ref["browser_id"], f"{section}.browser_id must match browser")
            require(section_ref.get("tab_id") == browser_ref["tab_id"], f"{section}.tab_id must match browser")
            require(bool(section_ref.get("tab_url")), f"{section}.tab_url is required")
        require(bool(nested(payload, section, "captured_at")), f"{section}.captured_at is required")

    require(nested(payload, "model_gate", "gpt_5_6_sol_checked") is True, "GPT-5.6 Sol must be checked")
    require(nested(payload, "model_gate", "pro_tier_checked") is True, "Pro tier must be checked")
    signals = nested(payload, "model_gate", "observed_signals")
    require(isinstance(signals, list) and len(signals) >= 2, "two model selection signals are required")

    require(
        nested(payload, "late_clean_gate", "checked_after_model_menu") is True,
        "late clean gate must run after model menu interaction",
    )
    require(nested(payload, "late_clean_gate", "composer_empty") is True, "late clean gate must prove empty composer")
    require(
        nested(payload, "late_clean_gate", "composer_text_sha256") == EMPTY_SHA256,
        "late clean gate composer hash must equal empty text SHA-256",
    )
    require(nested(payload, "late_clean_gate", "project_context") is False, "late clean gate must prove no Project context")
    require(nested(payload, "late_clean_gate", "pending_upload_count") == 0, "late clean gate must prove no pending uploads")
    late_unexpected = nested(payload, "late_clean_gate", "unexpected_attachments")
    require(isinstance(late_unexpected, list) and not late_unexpected, "late clean gate must prove no unexpected attachments")

    require(bool(SHA256_RE.fullmatch(str(nested(payload, "packet", "sha256") or ""))), "packet.sha256 must be lowercase SHA-256")
    require(bool(nested(payload, "packet", "distinctive_prefix")), "packet distinctive_prefix is required")
    require(str(nested(payload, "packet", "sentinel") or "").startswith("GPT56_SOL_PRO_RESULT_"), "packet sentinel is invalid")
    require(isinstance(nested(payload, "packet", "visible_attachments"), list), "visible_attachments must be a list")

    require(nested(payload, "dispatch", "state") == "SENT", "dispatch.state must be SENT")
    require(nested(payload, "dispatch", "send_click_count") == 1, "send_click_count must equal 1")
    require(bool(nested(payload, "dispatch", "submit_signal")), "dispatch submit_signal is required")

    require(nested(payload, "response", "generation_complete") is True, "response generation must be complete")
    require(bool(SHA256_RE.fullmatch(str(nested(payload, "response", "assistant_turn_sha256") or ""))), "assistant_turn_sha256 must be lowercase SHA-256")
    require(nested(payload, "response", "assistant_sentinel_verified") is True, "assistant sentinel must be verified")

    for key in ("chrome_extension_used", "chrome_cli_used", "opencli_used", "external_playwright_used"):
        require(nested(payload, "route_exclusions", key) is False, f"route_exclusions.{key} must be false")

    require(bool(nested(payload, "cleanup", "captured_at")), "cleanup.captured_at is required")
    require(nested(payload, "cleanup", "finalize_called") is True, "cleanup.finalize_called must be true")
    require(
        nested(payload, "cleanup", "finalize_was_last_browser_action") is True,
        "cleanup.finalize_was_last_browser_action must be true",
    )
    require(
        nested(payload, "cleanup", "retained_tab_status") in {"none", "deliverable"},
        "completed consultations may retain only none or deliverable",
    )
    require(
        nested(payload, "cleanup", "pre_finalize_project_context") is False,
        "cleanup must prove no Project context",
    )
    require(
        nested(payload, "cleanup", "pre_finalize_draft_present") is False,
        "cleanup must prove no leftover draft",
    )
    require(
        nested(payload, "cleanup", "pre_finalize_pending_upload_count") == 0,
        "cleanup must prove no pending uploads",
    )
    unexpected = nested(payload, "cleanup", "pre_finalize_unexpected_attachments")
    require(isinstance(unexpected, list) and not unexpected, "cleanup must prove no unexpected attachments")

    require(payload.get("binding_verified") is True, "binding_verified must be true")
    require(payload.get("status") == "completed", "status must be completed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate same-session Codex iab consultation evidence.")
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.evidence.read_text(encoding="utf-8"))
    errors = validate(payload)
    result = {"ok": not errors, "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
