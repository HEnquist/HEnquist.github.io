# CamillaDSP website

Source for [camilladsp.com](https://camilladsp.com), built with Jekyll and the Minimal Mistakes theme, deployed via GitHub Actions.

## Development

Requires Ruby 3.x and Bundler. If you don't have a recent Ruby, install one via [rbenv](https://github.com/rbenv/rbenv) or your system package manager.

```sh
bundle install
bundle exec jekyll serve
```

The site will be at `http://localhost:4000`. Changes to `.md` files rebuild automatically. Changes to `_config.yml` require restarting the server.

## Adding a new release

Handled automatically via the `update-release` workflow. When a new release is published in the [camilladsp repo](https://github.com/HEnquist/camilladsp), it dispatches an event here that:

1. Copies docs from the release tag into the version folder (e.g. `3.0.x/`)
2. Inserts a new row into `releases.md`
3. Creates a news post in `_posts/` from the GitHub release notes

You can also trigger it manually from the [Actions tab](../../actions/workflows/update-release.yml) with a version tag.

## Custom domain

The site is served at `camilladsp.com`. DNS should point to GitHub Pages:

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  henquist.github.io
```

After registering the domain, enable HTTPS in the GitHub Pages settings.
