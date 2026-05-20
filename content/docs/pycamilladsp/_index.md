---
title: pyCamillaDSP
weight: 3
---

pyCamillaDSP is a Python library for communicating with a running CamillaDSP process over its
WebSocket API. It's aimed at developers who want to build their own integrations — automation
scripts, hardware controllers, system daemons, or anything that needs to read state from or send
commands to CamillaDSP programmatically.

The [full API reference](https://www.camilladsp.com/pycamilladsp/) covers all classes and methods
with descriptions and type signatures.

The source and issue tracker are on [GitHub](https://github.com/HEnquist/pycamilladsp).

## Installation

See the [installation guide](https://www.camilladsp.com/pycamilladsp/) in the published docs.

## How it works

The library provides a client that connects to CamillaDSP's WebSocket server. Through this
connection you can query the current state, read and modify the active configuration, control
volume, and monitor signal levels — anything exposed by the WebSocket API.

CamillaDSP must be started with its WebSocket server enabled (the `-p` flag) for the library to
connect.

## Examples

The repository ships with a few small example scripts that show common patterns:

- **read_rms** — poll the playback signal level continuously and print it to the terminal
- **get_config** — fetch the running configuration and read values from it
- **set_volume** — set the main volume to a specific dB value
- **play_wav** — load a config from file, swap in a wav file as the capture device, and send the
  modified config to CamillaDSP

These are a good starting point for understanding how to structure an integration. They're in the
repository root and run directly with Python.

## Going further

For more complex use cases, pyCamillaDSP is also the library that powers CamillaGUI's backend.
Reading that code is a good way to see how the library handles connection management, config
manipulation, and error conditions in a real application.
