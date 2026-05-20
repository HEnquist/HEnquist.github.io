---
title: Advanced DSP
---

Filters, mixers, and processors can be chained in any order, applied per channel, and combined
freely. A few examples of what that makes possible:

## Channel mixing and upmixing

The mixer routes any input channel to any output channel, with individual gain and polarity control
per connection. This makes it straightforward to sum a stereo signal to mono for a center speaker,
create a subwoofer channel by mixing bass from left and right, or upmix stereo to a multi-channel
speaker system.

## Resampling

If the capture and playback devices run at different sample rates, or if a source plays at a rate
your DAC doesn't support natively, CamillaDSP can resample in real time. It supports both
synchronous resamplers (fixed ratio) and asynchronous resamplers (for rate-mismatched devices with
independent clocks).

## Dynamic loudness

At low listening levels, human hearing is less sensitive to bass and treble. The loudness filter
applies a frequency-dependent boost that compensates for this, tracking the volume control so the
tonal balance stays consistent as you turn the volume up and down.

## Compression and limiting

The compressor reduces dynamic range by attenuating loud passages relative to quiet ones. Attack
and release times control how fast it responds. This is useful for late-night listening where you
want to keep transients under control, or for protecting equipment in an active crossover system.

The limiter is a simpler tool: it hard- or soft-clips the signal above a set threshold, acting as
a last line of protection against clipping in the output stage.

## RACE — Recursive Ambiophonic Crosstalk Elimination

When listening to stereo speakers, some of the left speaker's sound reaches the right ear and vice
versa. This crosstalk is a natural part of how speakers create a stereo image. RACE is an algorithm
that eliminates this crosstalk, making the stereo separation sharper and pushing the soundstage
wider — sometimes described as making speakers sound more like headphones. CamillaDSP implements
the recursive part of the RACE algorithm as a dedicated processor, typically combined with filters
to limit the processing to the relevant frequency range.

## Headphone crossfeed

Crossfeed is the opposite problem: headphones have complete separation between left and right ears,
which is unnatural and can cause listening fatigue with panned material. A crossfeed filter mixes a
small amount of the opposite channel — slightly delayed and filtered — into each ear, simulating
the way sound from speakers reaches both ears. CamillaDSP's mixer and filter pipeline can implement
various crossfeed algorithms: from simple first-order IIR approaches to more accurate FIR-based
designs based on measured head-related transfer functions (HRTFs).

## Combining everything

These building blocks can be stacked. One example:

1. Capture a stereo source
2. Resample to the output sample rate
3. Apply room correction via convolution
4. Apply a compressor for dynamic control
5. Mix to multi-channel with a subwoofer
6. Apply an active crossover to each speaker pair
7. Add delay for time alignment
8. Apply loudness compensation

Because the pipeline is defined in a YAML config file, you can have multiple configs for different
scenarios and switch between them — manually or automatically via the
[controller](/docs/camilladsp-controller/) or [pyCamillaDSP](/docs/pycamilladsp/).

For the full list of available filters and processors, see the
[CamillaDSP engine documentation](/docs/camilladsp/).
