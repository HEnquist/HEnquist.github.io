---
title: Room correction
---

Every room colors the sound reaching your ears. Reflections, resonances, and standing waves add peaks and dips to the frequency response that have nothing to do with the recording. Room correction measures these anomalies and applies inverse filters to cancel them out.

## The basic workflow

1. **Measure** the room's frequency response using a measurement microphone and software such as [REW (Room EQ Wizard)](https://www.roomeqwizard.com/). Place the microphone at the listening position and play a sweep through the system.

2. **Generate correction filters.** REW and similar tools can export FIR filter coefficients designed to flatten the measured response. These are typically `.wav` files containing the impulse response of the correction filter.

3. **Load the filters into CamillaDSP.** Add a `Conv` (convolution) filter to the pipeline, pointing it at the exported coefficient file. CamillaDSP will convolve every audio sample with the filter in real time.

4. **Combine with EQ and delay.** Room correction filters handle broad frequency response problems, but you may also want to add a few parametric EQ bands for smaller adjustments, or a delay to align left and right channels for an asymmetric listening position.

## What it does and doesn't fix

FIR correction works well for steady-state frequency response — the peaks and dips that show up in a measurement. It does not fix time-domain problems like strong late reflections, and it corrects for one specific microphone position. Moving further from the sweet spot reduces the effectiveness of the correction.

For the convolution filter configuration, see the [CamillaDSP engine documentation](/docs/camilladsp/).
