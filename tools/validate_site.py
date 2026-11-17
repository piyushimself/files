#!/usr/bin/env python3
"""Post-build checks for generated Reading Room HTML applications."""
from __future__ import annotations
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
APPS = SITE / "apps"

def main() -> int:
    if not APPS.is_dir():
        raise SystemExit("Missing generated site/apps directory")
    pages = sorted(APPS.glob("*.html"))
    if not pages:
        raise SystemExit("No generated interactive apps found")
    checked = 0
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="reading-room-js-") as tmp:
        script_path = Path(tmp) / "inline.js"
        for page in pages:
            source = page.read_text(encoding="utf-8", errors="replace")
            for index, match in enumerate(
                re.finditer(r"<script\\b[^>]*>(.*?)</script\\s*>", source, re.I | re.S),
                start=1,
            ):
                script = match.group(1)
                if not script.strip():
                    continue
                script_path.write_text(script, encoding="utf-8")
                result = subprocess.run(
                    ["node", "--check", str(script_path)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                checked += 1
                if result.returncode:
                    detail = (result.stderr or result.stdout).strip()
                    failures.append(f"{page.name} inline script {index}: {detail}")
    print(f"Validated {len(pages)} generated apps and {checked} inline JavaScript blocks.")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print("All generated inline JavaScript blocks pass Node syntax validation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
