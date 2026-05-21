#!/usr/bin/env python3
"""
Check for broken internal links in the Hugo build output.

Checks:
  - Internal hrefs that still end in .md (render hook not working)
  - Internal hrefs pointing to paths that don't exist in public/

Run after `hugo`:  python3 .github/scripts/check_links.py
"""

import re
import sys
from pathlib import Path, PurePosixPath

PUBLIC = Path("public")
href_re = re.compile(r'href="([^"#?]+)"')


def target_exists(public: Path, href: str, html_file: Path) -> bool:
    if href.startswith("/"):
        path = public / href.lstrip("/")
    else:
        # Resolve relative to the directory containing the HTML file.
        # Hugo uses clean URLs: foo/index.html lives at URL foo/
        base = html_file.parent
        path = (base / href).resolve()

    return (
        path.exists()
        or (path / "index.html").exists()
        or path.with_suffix(".html").exists()
    )


errors = []

for html_file in sorted(PUBLIC.rglob("*.html")):
    content = html_file.read_text(errors="replace")
    for m in href_re.finditer(content):
        href = m.group(1)

        # Skip external links and data URIs
        if href.startswith(("http", "mailto", "data:", "//")):
            continue

        # Flag un-rewritten .md links
        if href.endswith(".md"):
            errors.append(f"{html_file}: href still ends in .md: {href!r}")
            continue

        if not target_exists(PUBLIC, href, html_file):
            errors.append(f"{html_file}: broken link: {href!r}")

if errors:
    for e in errors:
        print(e)
    print(f"\n{len(errors)} error(s) found.")
    sys.exit(1)
else:
    print("All internal links OK.")
