# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```sh
hugo server          # dev server at http://localhost:1313, live reload
hugo                 # production build into public/
```

Hugo (extended) and Go are required. There are no tests or linters.

To add a release manually:

```sh
.github/scripts/add_release.sh v4.2.0
```

## Architecture

Hugo static site using the [Hextra](https://imfing.github.io/hextra) theme, vendored in `_vendor/`. Deployed to GitHub Pages via `.github/workflows/deploy.yml`.

### Content structure

```
content/
  _index.md              # front page (hextra-home layout)
  releases.md            # release table, auto-updated by scripts
  news/                  # one .md per release announcement
  docs/
    _index.md                    # component landing page (cards + prose per component)
    camilladsp/                  # engine docs, versioned subfolders
      _index.md
      4.1.x/                     # latest; weight = -(MAJOR*100 + MINOR)
      4.0.x/
      …
    camillagui/                  # live demo at https://www.camilladsp.com/camillagui/
      _index.md
      installation.md
      configuration.md
      customization.md
    pycamilladsp/                # API docs at https://www.camilladsp.com/pycamilladsp/
      _index.md
    camilladsp-controller/       # automatic sample rate switching script
      _index.md
      usage.md
```

Engine version folders are named `{major}.{minor}.x` and get their content copied from the upstream `HEnquist/camilladsp` repo at release time. The `_index.md` in each version folder is the upstream `README.md` with a Hugo front-matter block prepended.

### Sidebar ordering

The `weight` front-matter field controls sidebar order. Engine version weights are `-(MAJOR*100 + MINOR)` so higher versions sort first. The top-level doc sections use weights 1–4: camilladsp, camillagui, pycamilladsp, camilladsp-controller.

### Release automation

`.github/workflows/update-release.yml` is triggered by a `repository_dispatch` event from the `HEnquist/camilladsp` repo when a release is published. It:

1. Copies docs from the release tag into `content/docs/camilladsp/{major}.{minor}.x/`
2. Updates the releases table in `content/releases.md` (via `update_releases.py`)
3. Creates a news post in `content/news/` (via `create_post.py`)

The local helper `add_release.sh` does the same steps manually.

### Custom layouts

Only one override exists: `layouts/_partials/custom/footer.html`. Everything else is inherited from the Hextra theme in `_vendor/`.

### Front page

`content/_index.md` uses the `hextra-home` layout with raw HTML for the hero section and Hextra shortcodes (`hextra/hero-button`, `hextra/hero-subtitle`, `cards`, `card`) for the feature grid. The tool cards in "The tools" section link to the component doc sections, not to GitHub.
