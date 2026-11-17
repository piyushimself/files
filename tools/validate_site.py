#!/usr/bin/env python3
"""Post-build integrity checks for generated Reading Room pages and apps."""
from __future__ import annotations
import json
import re
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
APPS = SITE / "apps"
COLLECTIONS = SITE / "collections"

def local_target(base: Path, value: str) -> Path | None:
    value = value.strip()
    if not value or value.startswith(("#", "data:", "http:", "https:", "//", "javascript:", "blob:", "mailto:", "tel:")):
        return None
    path = unquote(urlparse(value).path)
    return (base / path).resolve() if path else None

def main() -> int:
    if not APPS.is_dir() or not COLLECTIONS.is_dir():
        raise SystemExit("Missing generated site/apps or site/collections directory")
    pages = sorted(APPS.glob("*.html"))
    wrappers = sorted(COLLECTIONS.glob("*/index.html"))
    if not pages:
        raise SystemExit("No generated interactive apps found")

    checked = 0
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="reading-room-js-") as tmp:
        script_path = Path(tmp) / "inline.js"
        for page in pages:
            source = page.read_text(encoding="utf-8", errors="replace")
            for index, match in enumerate(re.finditer(r"<script\\b[^>]*>(.*?)</script\\s*>", source, re.I | re.S), start=1):
                script = match.group(1)
                if not script.strip():
                    continue
                script_path.write_text(script, encoding="utf-8")
                result = subprocess.run(["node", "--check", str(script_path)], capture_output=True, text=True, check=False)
                checked += 1
                if result.returncode:
                    detail = (result.stderr or result.stdout).strip()
                    failures.append(f"{page.name} inline script {index}: {detail}")

    catalog_path = SITE / "data" / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    items = catalog.get("items", [])
    if len(items) != len(wrappers):
        failures.append(f"catalog has {len(items)} entries but {len(wrappers)} collection wrappers exist")

    home_js = (SITE / "assets" / "reading-room.js").read_text(encoding="utf-8")
    category_match = re.search(r"const categoryOrder=(\\[[^;]+\\]);", home_js)
    if not category_match:
        failures.append("Could not find the homepage category order")
    else:
        available = set(json.loads(category_match.group(1)))
        missing_categories = sorted({x.get("category", "") for x in items} - available)
        if missing_categories:
            failures.append("Homepage filter missing catalogue categories: " + ", ".join(missing_categories))

    for item in items:
        target = local_target(SITE, item.get("href", ""))
        if target is None or not target.exists():
            failures.append(f"catalog target missing for {item.get('title', '(untitled)')}: {item.get('href')}")

    for wrapper in wrappers:
        soup = BeautifulSoup(wrapper.read_text(encoding="utf-8", errors="replace"), "html.parser")
        if not soup.title or not soup.title.get_text(strip=True):
            failures.append(f"{wrapper.relative_to(SITE)} has no document title")
        for frame in soup.select("iframe[src]"):
            target = local_target(wrapper.parent, frame.get("src", ""))
            if target is not None and not target.exists():
                failures.append(f"{wrapper.relative_to(SITE)} has missing iframe target {frame.get('src')}")

    local_refs = 0
    for app in pages:
        soup = BeautifulSoup(app.read_text(encoding="utf-8", errors="replace"), "html.parser")
        for tag, attr in (("img", "src"), ("script", "src"), ("link", "href"), ("source", "src"), ("video", "src"), ("audio", "src")):
            for element in soup.find_all(tag):
                target = local_target(app.parent, element.get(attr, ""))
                if target is None:
                    continue
                local_refs += 1
                if not target.exists():
                    failures.append(f"{app.name} missing local {tag} reference: {element.get(attr)}")

    print(f"Validated {len(pages)} apps, {checked} inline JavaScript blocks, {len(items)} catalogue entries, {len(wrappers)} wrappers and {local_refs} local app assets.")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print("All generated-site integrity checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
