---
layout: splash
excerpt: "Open source tools for real-time audio processing."

feature_row:
  - title: "Active crossovers"
    excerpt: >-
      Split a full-range signal into frequency bands and route each to a
      separate amplifier and driver. Achieve precise crossover slopes and
      time alignment in software.
  - title: "Room correction"
    excerpt: >-
      Measure your room and apply FIR correction filters to compensate for
      acoustic problems. Combine with EQ and delay adjustment for accurate
      sound reproduction.
  - title: "Advanced DSP"
    excerpt: >-
      Mix channels, apply dynamic loudness, add resampling, and chain
      together dozens of filter stages in a flexible signal routing pipeline
      — all running in real-time.

feature_row2:
  - title: "CamillaDSP"
    excerpt: >-
      The processing engine. Runs on Linux, macOS, and Windows with support
      for ALSA, PulseAudio, JACK, WASAPI, and CoreAudio. Low-latency,
      written in Rust.
    url: "https://github.com/HEnquist/camilladsp"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
  - title: "CamillaGUI"
    excerpt: >-
      A web-based interface for building and editing the processing pipeline,
      monitoring levels, and applying changes live — running locally in your
      browser.
    url: "https://github.com/HEnquist/camillagui-backend"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
  - title: "pyCamillaDSP"
    excerpt: >-
      Python library for scripting, automation, and integration with other
      tools via the CamillaDSP WebSocket API.
    url: "https://github.com/HEnquist/pycamilladsp"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
---

<div class="splash-hero">
  <img src="/camilladsp.svg" alt="CamillaDSP" class="splash-hero__logo">
  <div class="splash-hero__intro">
    CamillaDSP is an open source family of tools for real-time audio
    processing. Build active crossovers, apply room correction, or create
    advanced DSP pipelines — with a graphical interface and a Python API.
    Runs on anything from a Raspberry Pi to a full desktop: Linux, macOS,
    and Windows.
  </div>
  <div class="splash-hero__buttons">
    <a href="/docs/" class="btn btn--primary btn--large">Documentation</a>
    <a href="https://github.com/HEnquist/camilladsp/releases/latest" class="btn btn--inverse btn--large">Download</a>
    <a href="https://github.com/HEnquist/camilladsp" class="btn btn--inverse btn--large">GitHub</a>
  </div>
</div>

## What you can do
{: .text-center}

{% include feature_row %}

## The tools
{: .text-center}

{% include feature_row id="feature_row2" %}
