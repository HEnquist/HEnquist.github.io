"""Add minimal Jekyll front matter to .md files that don't already have it."""
import glob
import os
import sys

folder = sys.argv[1]
for path in glob.glob(f"{folder}/*.md"):
    with open(path, "r") as f:
        content = f.read()
    if content.startswith("---"):
        continue
    filename = os.path.basename(path)
    if filename.upper() == "README.MD":
        # Set permalink to the directory URL so the README becomes the index page
        front_matter = f"---\npermalink: /{folder}/\nlayout: single\n---\n\n"
    else:
        front_matter = "---\nlayout: single\n---\n\n"
    with open(path, "w") as f:
        f.write(front_matter + content)
    print(f"  {path}")
