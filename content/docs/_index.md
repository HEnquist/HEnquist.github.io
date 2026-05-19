---
title: Documentation
---

CamillaDSP is a family of three components that can be used independently or together.

{{< cards >}}
  {{< card link="/docs/camilladsp/" title="CamillaDSP Engine" subtitle="The processing engine." >}}
  {{< card link="/docs/camillagui/" title="CamillaGUI" subtitle="The graphical interface." >}}
  {{< card link="/docs/pycamilladsp/" title="pyCamillaDSP" subtitle="The Python library." >}}
  {{< card link="/docs/camilladsp-controller/" title="Controller" subtitle="Automatic sample rate switching." >}}
{{< /cards >}}

## CamillaDSP Engine

The engine is the core of the system. It reads audio from a capture device, runs it through a configurable pipeline of filters and mixers, and sends the result to a playback device. The pipeline is defined in a YAML config file and can include FIR and IIR filters, resampling, channel mixing, and more. The engine runs on Linux, macOS, and Windows, with support for ALSA, PulseAudio, PipeWire, JACK, WASAPI, ASIO, and CoreAudio.

## CamillaGUI

CamillaGUI is a browser-based interface for building and managing the signal pipeline without editing config files by hand. It connects to a running engine over the WebSocket API and lets you edit filters, routing, and device settings, monitor signal levels, and apply changes live. It runs as a small local server, with the UI served to your browser.

## pyCamillaDSP

pyCamillaDSP is a Python library that wraps the CamillaDSP WebSocket API. It is aimed at developers who want to build their own integrations — automation scripts, hardware controllers, or anything that needs to read state from or send commands to the engine programmatically.

## Controller

The controller is a Python script that monitors an audio device for changes in sample rate or format, and automatically applies a new CamillaDSP configuration when a change is detected. It is useful in setups where multiple sources play at different sample rates and seamless switching is needed.
