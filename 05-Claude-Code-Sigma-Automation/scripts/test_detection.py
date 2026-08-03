"""
Detection test harness for suspicious_certutil_download.yml.

NOTE: This is NOT a full Sigma engine. It only validates the specific detection
logic defined in this prototype rule — no generic Sigma parsing or evaluation.
"""

import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = REPO_ROOT / "logs" / "sample_process_events.json"
RULE_FILE = REPO_ROOT / "rules" / "suspicious_certutil_download.yml"

EXPECTED_SUSPICIOUS = 1
EXPECTED_BENIGN = 5


def _fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    sys.exit(1)


def load_logs() -> list[dict]:
    try:
        with LOG_FILE.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        _fail(f"Could not load JSON log file: {exc}")
    print("[PASS] JSON log file loaded")
    return data


def load_rule() -> dict:
    try:
        with RULE_FILE.open(encoding="utf-8") as fh:
            rule = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError) as exc:
        _fail(f"Could not load Sigma rule file: {exc}")
    print("[PASS] Sigma rule loaded")
    return rule


def matches_rule(event: dict) -> bool:
    """
    Apply the detection condition from suspicious_certutil_download.yml:
      selection     : Image|endswith '\\certutil.exe'
                      AND CommandLine|contains|all ['-urlcache', '-f']
      selection_url : CommandLine|contains ('http://' OR 'https://')
      condition     : selection and selection_url
    All comparisons are case-insensitive.
    """
    image = (event.get("Image") or "").lower()
    cmdline = (event.get("CommandLine") or "").lower()

    selection = (
        image.endswith("\\certutil.exe")
        and "-urlcache" in cmdline
        and "-f" in cmdline
    )

    selection_url = "http://" in cmdline or "https://" in cmdline

    return selection and selection_url


def run_tests(events: list[dict]) -> None:
    matched = [e for e in events if matches_rule(e)]
    benign = [e for e in events if not matches_rule(e)]

    if len(matched) != EXPECTED_SUSPICIOUS:
        _fail(
            f"Positive test failed: expected {EXPECTED_SUSPICIOUS} suspicious event(s), "
            f"got {len(matched)}. Matched images: {[e.get('Image') for e in matched]}"
        )

    if not matched[0].get("Image", "").lower().endswith("\\certutil.exe"):
        _fail(
            f"Positive test failed: matched event is not certutil.exe "
            f"(Image={matched[0].get('Image')!r})"
        )

    print(f"[PASS] Positive test: {EXPECTED_SUSPICIOUS} suspicious event detected")

    if len(benign) != EXPECTED_BENIGN:
        _fail(
            f"Negative test failed: expected {EXPECTED_BENIGN} benign event(s), "
            f"got {len(benign)}."
        )

    print(f"[PASS] Negative test: {EXPECTED_BENIGN} benign events ignored")
    print("[PASS] All detection tests passed")


def main() -> None:
    events = load_logs()
    load_rule()
    run_tests(events)


if __name__ == "__main__":
    main()
