---
title: Installation
weight: 1
---

There are two ways to run CamillaGUI: a self-contained bundle (recommended for most users), or a
setup inside a Python environment.

## Bundled release

The bundle includes the backend server, the frontend files, and a complete Python environment —
no separate Python installation needed.

Download the archive for your system from the
[camillagui-backend releases page](https://github.com/HEnquist/camillagui-backend/releases)
and uncompress it. A suggested directory layout:

```
~/camilladsp/
  camillagui_backend/   ← extracted bundle
  configs/
  coeffs/
```

The default configuration expects `configs` and `coeffs` directories. Edit the config file inside
the bundle if you want to use different locations — see [Configuration](../configuration).

Start the server by running the executable inside the `camillagui_backend` directory. On Linux
and macOS this is `./camillagui_backend`, on Windows it's `camillagui_backend.exe` (which can
also be double-clicked).

The GUI will be available at
[http://localhost:5005/gui/index.html](http://localhost:5005/gui/index.html).
From another machine, replace `localhost` with the server's IP or hostname.

## Python environment

Use this approach if you want to run custom Python scripts alongside the GUI, or if you need more
flexibility.

Download `camillagui.zip` from the
[releases page](https://github.com/HEnquist/camillagui-backend/releases).
This zip contains both the backend and the frontend. Unzip it and install the Python dependencies
— the repo provides environment files for pip, conda, and Poetry. The
[camilladsp-setupscripts](https://github.com/HEnquist/camilladsp-setupscripts) repository has
scripts that automate this step.

Start the server with:

```sh
python main.py
```

## Command-line options

All startup methods accept the same arguments. Run the server with `--help` to see the current
options. The most commonly used ones are a flag to provide a custom path to the backend config
file, and flags to control the logging verbosity.
