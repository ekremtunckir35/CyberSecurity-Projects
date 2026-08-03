"""
Claude Code PostToolUse hook: automatically validates Sigma rules after Write/Edit.

Exit codes:
  0 - skipped (not applicable) or validation passed
  2 - validation failed (blocks the tool use in Claude Code)
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Optional

REPO_ROOT: Path = Path(__file__).resolve().parent.parent
RULES_DIR: Path = REPO_ROOT / "rules"
VALIDATE_SCRIPT: Path = REPO_ROOT / "scripts" / "validate_sigma.py"

YAML_EXTENSIONS: frozenset[str] = frozenset({".yml", ".yaml"})
TARGET_TOOLS: frozenset[str] = frozenset({"Write", "Edit"})


def read_hook_input() -> dict:
    try:
        raw = sys.stdin.read()
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"[ERROR] Invalid hook JSON input: {exc}", file=sys.stderr)
        sys.exit(1)


def resolve_file_path(raw: str) -> Path:
    """Resolve file_path to an absolute Path, supporting both Windows and Unix forms."""
    p = Path(raw)
    if not p.is_absolute():
        p = REPO_ROOT / p
    return p.resolve()


def run_validation(file_path: Path) -> int:
    """Run validate_sigma.py via subprocess. Returns the process exit code."""
    result = subprocess.run(
        [sys.executable, str(VALIDATE_SCRIPT), str(file_path)],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode


def main() -> None:
    data: dict = read_hook_input()

    tool_name: str = data.get("tool_name", "")
    if tool_name not in TARGET_TOOLS:
        print(f"[SKIP] Tool '{tool_name}' is not Write or Edit")
        sys.exit(0)

    tool_input: dict = data.get("tool_input", {})
    file_path_raw: Optional[str] = tool_input.get("file_path")
    if not file_path_raw:
        print("[SKIP] No file_path in tool_input")
        sys.exit(0)

    file_path: Path = resolve_file_path(file_path_raw)

    if file_path.suffix.lower() not in YAML_EXTENSIONS:
        print(f"[SKIP] Not a YAML file: {file_path_raw}")
        sys.exit(0)

    try:
        file_path.relative_to(RULES_DIR)
    except ValueError:
        print(f"[SKIP] Not in rules directory: {file_path_raw}")
        sys.exit(0)

    print(f"[INFO] Validating Sigma rule: {file_path_raw}")
    returncode = run_validation(file_path)

    if returncode == 0:
        print(f"[PASS] Hook completed successfully for: {file_path_raw}")
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ERROR] Unexpected hook error: {exc}", file=sys.stderr)
        sys.exit(2)
