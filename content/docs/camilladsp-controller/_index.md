---
title: CamillaDSP Controller
weight: 4
---

The controller is a Python script that watches an audio device for changes in sample rate or format, and automatically reconfigures CamillaDSP when a change is detected. This is useful in setups where multiple audio sources play at different sample rates — for example, through an ALSA loopback or a virtual CoreAudio device — and you want CamillaDSP to switch configs seamlessly rather than stopping with an error.

The source and issue tracker are on [GitHub](https://github.com/HEnquist/camilladsp-controller).

{{< cards >}}
  {{< card link="usage" title="Usage" subtitle="Config providers, device listeners, and platform-specific setup." >}}
{{< /cards >}}

## How it works

The controller connects to a running CamillaDSP process via the WebSocket API and also listens to an audio device for format changes. When the device signals a new sample rate or format, the controller asks one or more **config providers** for an appropriate configuration and sends it to CamillaDSP.

Multiple providers can be enabled at once. The controller tries them in order and uses the first one that can supply a config for the new format.

## Requirements

The controller requires Python with `pycamilladsp` and `pyyaml`. There are also platform-specific dependencies:

- **Linux** — the `pyalsa` package is needed to monitor ALSA devices
- **macOS** — the `cffi` package is needed; on first run a small C module is compiled, which requires the Xcode command line tools

See the [GitHub repository](https://github.com/HEnquist/camilladsp-controller) for installation details.
