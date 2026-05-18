# CamillaDSP website

Source for [camilladsp.com](https://camilladsp.com), built with [Hugo](https://gohugo.io) and the [Hextra](https://imfing.github.io/hextra) theme, deployed via GitHub Actions.

## Development

Requires Hugo (extended) and Go.

```sh
hugo server
```

The site will be at `http://localhost:1313`. Changes rebuild automatically.

## Adding a new release

Handled automatically via the `update-release` workflow. When a new release is published in the [camilladsp repo](https://github.com/HEnquist/camilladsp), it dispatches an event here that:

1. Copies docs from the release tag into the version folder (e.g. `content/docs/4.1.x/`)
2. Inserts a new row into `content/releases.md`
3. Creates a news post in `content/news/` from the GitHub release notes

You can also trigger it manually from the [Actions tab](../../actions/workflows/update-release.yml) with a version tag, or run the local helper:

```sh
.github/scripts/add_release.sh v4.2.0
```
