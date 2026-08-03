# Uses pySigma directly for validation because the `sigma check` command in
# Sigma CLI is not yet implemented and cannot be relied upon.

import sys
from pathlib import Path

import yaml
from sigma.collection import SigmaCollection

REPO_ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = REPO_ROOT / "rules"


def usage() -> None:
    print(
        "Usage: python scripts/validate_sigma.py <path-to-sigma-rule.yml>",
        file=sys.stderr,
    )


def main() -> None:
    if len(sys.argv) != 2:
        usage()
        sys.exit(2)

    raw_path: str = sys.argv[1]
    rule_path = Path(raw_path).resolve()

    if rule_path.suffix.lower() not in {".yml", ".yaml"}:
        print(
            f"[FAIL] Not a YAML file (expected .yml or .yaml): {raw_path}",
            file=sys.stderr,
        )
        sys.exit(2)

    if not rule_path.exists():
        print(f"[FAIL] File not found: {raw_path}", file=sys.stderr)
        sys.exit(2)

    # Only validate files that live inside the rules directory.
    try:
        rule_path.relative_to(RULES_DIR)
    except ValueError:
        print(f"[SKIP] Not in rules directory: {raw_path}")
        sys.exit(0)

    try:
        with rule_path.open(encoding="utf-8") as fh:
            parsed = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        print(f"[FAIL] YAML syntax error: {exc}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"[FAIL] Unexpected validation error: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(parsed, dict):
        print(
            "[FAIL] YAML syntax error: document root is not a mapping",
            file=sys.stderr,
        )
        sys.exit(1)

    print("[PASS] YAML syntax valid")

    try:
        collection: SigmaCollection = SigmaCollection.load_ruleset([rule_path])
    except Exception as exc:
        print(f"[FAIL] Sigma validation error: {exc}", file=sys.stderr)
        sys.exit(1)

    rule_count: int = len(collection)

    if rule_count < 1:
        print(
            "[FAIL] Sigma validation error: no rules loaded from file",
            file=sys.stderr,
        )
        sys.exit(1)

    print("[PASS] Sigma rule parsed by pySigma")
    print(f"[PASS] Rule count: {rule_count}")
    print(f"[PASS] Sigma validation completed: {raw_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[FAIL] Unexpected validation error: {exc}", file=sys.stderr)
        sys.exit(1)
