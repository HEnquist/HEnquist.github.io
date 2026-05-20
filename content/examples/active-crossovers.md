---
title: Active crossovers
---

A traditional passive crossover sits between the amplifier and the speakers, splitting the signal
with capacitors and inductors. An active crossover does the same split in the digital domain,
before amplification — one amplifier channel per driver. This gives much better control over the
crossover shape, and avoids the power losses and phase distortion of passive components.

## A simple two-way example

Consider a pair of speakers with a woofer and a tweeter, each driven by its own amplifier channel.
A basic setup in CamillaDSP would look like:

- Capture a stereo signal (left and right)
- Apply a low-pass filter to the signal going to each woofer
- Apply a high-pass filter to the signal going to each tweeter
- Route the four resulting channels to four output channels

The crossover frequency and filter type (Butterworth, Linkwitz-Riley, etc.) are chosen to match
the speakers. CamillaDSP supports both IIR filters for simple crossovers and FIR filters for
linear-phase designs.

## Time alignment

Woofers and tweeters are physically offset from each other, which means the sound from each driver
arrives at the listening position at slightly different times. CamillaDSP can add a small delay to
the closer driver to bring the two into alignment. This is a simple `Delay` filter in the pipeline.

## Going further

The same approach extends to three-way or four-way systems. Each additional driver gets its own
band-pass (or high-pass/low-pass pair) and its own output channel. Because everything is in
software, crossover points and slopes can be adjusted and heard in real time — no soldering
required.

For the available filter types and configuration details, see the
[CamillaDSP engine documentation](/docs/camilladsp/).
