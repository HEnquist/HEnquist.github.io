"""Update content/releases.md for a new release."""
import os
import re
import sys

tag = os.environ["TAG"]
folder = os.environ["FOLDER"]
date = os.environ["DATE"]

# Update content/releases.md
releases_path = "content/releases.md"
with open(releases_path) as f:
    content = f.read()

if tag in content:
    print(f"Tag {tag} already present in releases.md, skipping")
else:
    new_row = (
        f"| {tag}  | {date} | "
        f"[Documentation](/docs/{folder}/) | "
        f"[Download](https://github.com/HEnquist/camilladsp/releases/tag/{tag}) |"
    )

    lines = content.split("\n")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if cells and all(re.match(r"^-+$", c) for c in cells if c):
                lines.insert(i + 1, new_row)
                break

    with open(releases_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Inserted row for {tag} in releases.md")
