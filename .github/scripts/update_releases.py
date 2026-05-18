"""Insert a new row into the releases table in releases.md and update _data/versions.yml."""
import os
import re
import sys

tag = os.environ["TAG"]
folder = os.environ["FOLDER"]
date = os.environ["DATE"]

# Update releases.md
with open("releases.md") as f:
    content = f.read()

if tag in content:
    print(f"Tag {tag} already present, skipping releases.md")
else:
    new_row = (
        f"| {tag}  | {date} | "
        f"[Documentation]({folder}/README.md) | "
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

    with open("releases.md", "w") as f:
        f.write("\n".join(lines))
    print(f"Inserted row for {tag}")

# Update _data/versions.yml — prepend the new version folder if not already listed
versions_path = "_data/versions.yml"
with open(versions_path) as f:
    versions_content = f.read()

version = tag.lstrip("v")
label = folder  # e.g. "3.0.x" or "3.1.0"

if f'folder: "{folder}"' in versions_content:
    print(f"Version folder {folder} already in versions.yml, skipping")
else:
    new_entry = f'- label: "{label}"\n  folder: "{folder}"\n'
    with open(versions_path, "w") as f:
        f.write(new_entry + versions_content)
    print(f"Prepended {folder} to versions.yml")
