"""Create a content/news/ post from a GitHub release."""
import os
import sys

tag = os.environ["TAG"]
version = os.environ["VERSION"]
date = os.environ["DATE"]
folder = os.environ["FOLDER"]

slug = version.replace(".", "-")
post_path = f"content/news/{date}-v{slug}-release.md"

if os.path.exists(post_path):
    print(f"{post_path} already exists, skipping")
    sys.exit(0)

with open("/tmp/release_notes.md") as f:
    notes = f.read().strip()

sep = "---"
lines = [
    sep,
    f'title: "CamillaDSP {tag} released"',
    f"date: {date}",
    sep,
    "",
    f"[Download {tag}](https://github.com/HEnquist/camilladsp/releases/tag/{tag}) &nbsp;·&nbsp; [Documentation](/docs/camilladsp/{folder}/)",
    "",
    notes,
    "",
]

with open(post_path, "w") as f:
    f.write("\n".join(lines))
print(f"Created {post_path}")
