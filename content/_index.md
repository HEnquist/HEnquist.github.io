---
title: CamillaDSP
layout: hextra-home
---

<div class="hx:flex hx:flex-col hx:items-center hx:text-center hx:py-12 hx:gap-6">
  <img src="/camilladsp.svg" alt="CamillaDSP" style="width:300px;max-width:70%;">

  {{< hextra/hero-subtitle >}}
  An open source family of tools for real-time audio processing.
  Build active crossovers, apply room correction, or create advanced DSP
  pipelines — with a graphical interface and a Python API.
  Runs on anything from a Raspberry Pi to a full desktop: Linux, macOS, and Windows.
  {{< /hextra/hero-subtitle >}}

  <div class="hx:flex hx:gap-3 hx:flex-wrap hx:justify-center">
    {{< hextra/hero-button text="Documentation" link="/docs/" >}}
    {{< hextra/hero-button text="Download" link="https://github.com/HEnquist/camilladsp/releases/latest" >}}
    {{< hextra/hero-button text="GitHub" link="https://github.com/HEnquist/camilladsp" >}}
  </div>
</div>

## What you can do

{{< cards >}}
  {{< card title="Active crossovers" subtitle="Split a full-range signal into frequency bands and route each to a separate amplifier and driver. Achieve precise crossover slopes and time alignment in software." >}}
  {{< card title="Room correction" subtitle="Measure your room and apply FIR correction filters to compensate for acoustic problems. Combine with EQ and delay adjustment for accurate sound reproduction." >}}
  {{< card title="Advanced DSP" subtitle="Mix channels, apply dynamic loudness, add resampling, and chain together dozens of filter stages in a flexible signal routing pipeline — all running in real-time." >}}
{{< /cards >}}

## The tools

{{< cards >}}
  {{< card link="https://github.com/HEnquist/camilladsp" title="CamillaDSP" subtitle="The processing engine. Runs on Linux, macOS, and Windows with support for ALSA, PulseAudio, JACK, WASAPI, and CoreAudio. Low-latency, written in Rust." >}}
  {{< card link="https://github.com/HEnquist/camillagui-backend" title="CamillaGUI" subtitle="A web-based interface for building and editing the processing pipeline, monitoring levels, and applying changes live — running locally in your browser." >}}
  {{< card link="https://github.com/HEnquist/pycamilladsp" title="pyCamillaDSP" subtitle="Python library for scripting, automation, and integration with other tools via the CamillaDSP WebSocket API." >}}
{{< /cards >}}
