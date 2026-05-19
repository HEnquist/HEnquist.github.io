#!/bin/bash
# Usage: .github/scripts/add_release.sh v3.0.2
set -e

TAG=$1
if [ -z "$TAG" ]; then
  echo "Usage: $0 <tag>  (e.g. v3.0.2)"
  exit 1
fi

cd "$(git rev-parse --show-toplevel)"

echo "Fetching release info for $TAG..."
RELEASE=$(curl -fsSL "https://api.github.com/repos/HEnquist/camilladsp/releases/tags/$TAG")
DATE=$(echo "$RELEASE" | python3 -c "import sys,json; print(json.load(sys.stdin)['published_at'][:10])")
echo "$RELEASE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('body') or '')" > /tmp/release_notes.md

VERSION="${TAG#v}"
MAJOR=$(echo "$VERSION" | cut -d. -f1)
MINOR=$(echo "$VERSION" | cut -d. -f2)
FOLDER="${MAJOR}.${MINOR}.x"
WEIGHT=$(( -(MAJOR * 100 + MINOR) ))

echo "Tag: $TAG  Date: $DATE  Folder: $FOLDER  Weight: $WEIGHT"

echo "Cloning camilladsp at $TAG..."
git clone --depth 1 --branch "$TAG" https://github.com/HEnquist/camilladsp.git _source

echo "Copying docs to content/docs/camilladsp/$FOLDER/..."
mkdir -p "content/docs/camilladsp/$FOLDER"
find _source -maxdepth 1 \( -name "*.md" -o -name "*.png" -o -name "*.jpg" -o -name "*.svg" -o -name "LICENSE*.txt" \) -exec cp {} "content/docs/camilladsp/$FOLDER/" \;
if [ -f "content/docs/camilladsp/$FOLDER/README.md" ]; then
  printf -- "---\nweight: $WEIGHT\n---\n\n" | cat - "content/docs/camilladsp/$FOLDER/README.md" > /tmp/index_tmp.md
  mv /tmp/index_tmp.md "content/docs/camilladsp/$FOLDER/_index.md"
  rm "content/docs/camilladsp/$FOLDER/README.md"
fi
rm -rf _source

export TAG DATE VERSION FOLDER
python3 .github/scripts/update_releases.py
python3 .github/scripts/create_post.py

echo "Done. Review changes with: git diff --stat"
