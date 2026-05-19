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
    {{< hextra/hero-button text="Download" link="/releases/" >}}
    {{< hextra/hero-button text="GitHub" link="https://github.com/HEnquist/camilladsp" >}}
  </div>
</div>

## What you can do

{{< cards >}}
  {{< card title="Active crossovers" subtitle="Split a signal into frequency bands and route each to a separate amplifier and driver, with precise slopes and time alignment." >}}
  {{< card title="Room correction" subtitle="Apply FIR correction filters to compensate for acoustic problems, combined with EQ and delay adjustment." >}}
  {{< card title="Advanced DSP" subtitle="Mix channels, add resampling, apply dynamic loudness, and chain dozens of filter stages in a flexible real-time pipeline." >}}
{{< /cards >}}

## The tools

{{< cards >}}
  {{< card link="/docs/camilladsp/" title="CamillaDSP" subtitle="The processing engine. Runs on Linux, macOS, and Windows with support for ALSA, PulseAudio, JACK, WASAPI, and CoreAudio. Low-latency, written in Rust." >}}
  {{< card link="/docs/camillagui/" title="CamillaGUI" subtitle="A web-based interface for building and editing the processing pipeline, monitoring levels, and applying changes live — running locally in your browser." >}}
  {{< card link="/docs/pycamilladsp/" title="pyCamillaDSP" subtitle="Python library for scripting, automation, and integration with other tools via the CamillaDSP WebSocket API." >}}
{{< /cards >}}

## Community

The [CamillaDSP thread at diyAudio](https://www.diyaudio.com/community/threads/camilladsp-cross-platform-iir-and-fir-engine-for-crossovers-room-correction-etc.349818/) is the best place to ask questions, share your setup, and follow development discussion. Bugs and feature requests can be filed as issues in the relevant GitHub repository.
