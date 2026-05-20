---
title: Configuration
weight: 2
---

The backend reads its configuration from a YAML file inside the bundle or zip. The exact path is
shown in the bundled config file itself and in the
[backend README](https://github.com/HEnquist/camillagui-backend/blob/master/README.md).
The config file ships with sensible defaults and inline comments — it's the best reference for
the full list of options.

## Connecting to CamillaDSP

The GUI connects to CamillaDSP over its WebSocket API. The host and port in the config must match
the values CamillaDSP is started with. When both run on the same machine the host is typically
`0.0.0.0` or `localhost`; to control CamillaDSP on a different machine, set the host to that
machine's IP address.

## Network exposure

By default the backend binds to all network interfaces, making the GUI reachable from any machine
on your network. To restrict access, change `bind_address` to a specific interface, or configure
your firewall accordingly.

## File directories

The config points to two directories — one for CamillaDSP config files and one for FIR coefficient
files. The GUI can upload and save files into these directories. Make sure the backend has write
permission to both.

## Active config and statefile

The GUI keeps track of which config file is currently active using the CamillaDSP statefile. For
this to work, CamillaDSP must be started with a statefile (using the `-s` flag), and
`statefile_path` in the GUI config must point to that same file.

When CamillaDSP is running the active config path is fetched by querying the process. When it's
not running, the statefile is read directly. The active config is loaded into the GUI when it
opens, but is **not** automatically applied to CamillaDSP on startup.

If no active config is found, the GUI falls back to `default_config`, and then to an internal
default if that file doesn't exist.

For setups that manage the active config path through external tooling rather than the statefile,
the backend supports custom shell commands for getting and setting the active config path. See the
backend README for details on `on_get_active_config` and `on_set_active_config`.

## HTTPS

The backend can serve over HTTPS by providing a certificate and private key in the config. A
self-signed certificate is enough for local use. See the backend README for the exact options and
an example `openssl` command to generate one.

## Log file

To enable viewing the CamillaDSP log inside the GUI, configure CamillaDSP to write its log to a
file and point `log_file` in the GUI config to that same path.

## Limiting device types

By default the config validator accepts all device types CamillaDSP supports. On a system that
only has, say, ALSA and file I/O, you can restrict the validator to those types. This prevents
the GUI from offering options that won't work on that system. See the backend README for the
option names and accepted values.
