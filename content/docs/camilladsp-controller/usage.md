---
title: Usage
weight: 1
---

The controller is started from the command line. At minimum you need to specify the CamillaDSP WebSocket port and at least one config provider.

## Config providers

### Specific

The "Specific" provider selects a config file by name based on the new audio format. It's enabled with `-s` (or `--specific`) followed by a path that may contain placeholders:

- `{samplerate}`
- `{sampleformat}`
- `{channels}`

When the format changes, the placeholders are filled in with the actual values and the resulting path is loaded. If no file exists at that path the provider cannot serve a config for that format.

**Example:** with the path `/path/to/configs/conf_{samplerate}_{channels}.yml`, a switch to a 44100 Hz, 2-channel stream causes the controller to load `/path/to/configs/conf_44100_2.yml`.

### Adapt

The "Adapt" provider takes a single base config and modifies it to match the new format, rather than requiring a separate file per sample rate. It's enabled with `-a` (or `--adapt`) followed by the path to the base config.

The behavior depends on whether the base config uses a resampler:

- **With a resampler** — the `capture_samplerate` is updated to the new rate. If the new rate matches the output `samplerate`, a synchronous resampler is removed (since it's no longer needed).
- **Without a resampler** — the main `samplerate` is changed to the new rate.

The "Adapt" provider can also update the capture `format` parameter if one is set in the config.

### Using both together

Both providers can be active at the same time. The controller tries them in the order they were specified on the command line. A common pattern is to use "Specific" for sample rates that have handcrafted configs, and "Adapt" as a fallback for rates where a general-purpose config with a resampler is good enough:

```sh
python controller.py -p 1234 \
  -s "/path/to/config_{samplerate}.yml" \
  -a "/path/to/config_with_resampler.yml" \
  -d "BlackHole 2ch"
```

## Device listeners

The controller needs a device listener to know when the format has changed. Specify the device with `-d` (or `--device`).

### Linux (ALSA)

On Linux the controller monitors an ALSA device. This works well with an ALSA loopback, where other applications play audio at various sample rates.

```sh
python controller.py -p 1234 \
  -s "/path/to/configs/config_{samplerate}.yml" \
  -d hw:Loopback,0
```

A pair of configs for this setup might look like:

`config_44100.yml`
```yaml
devices:
  samplerate: 44100
  chunksize: 1024
  enable_rate_adjust: true
  capture:
    type: Alsa
    channels: 2
    device: "hw:Loopback,0"
    format: S32_LE
  playback:
    type: Alsa
    channels: 2
    device: "hw:MyDac"
```

`config_48000.yml`
```yaml
devices:
  samplerate: 48000
  chunksize: 1024
  enable_rate_adjust: true
  capture:
    type: Alsa
    channels: 2
    device: "hw:Loopback,0"
    format: S32_LE
  playback:
    type: Alsa
    channels: 2
    device: "hw:MyDac"
```

### macOS (CoreAudio)

On macOS the controller monitors the sample rate of a CoreAudio device. `cffi` must be installed, and on first run a small C module is compiled — this requires the Xcode command line tools.

```sh
python controller.py -p 1234 \
  -s "/path/to/config_{samplerate}.yml" \
  -a "/path/to/config_with_resampler.yml" \
  -d "BlackHole 2ch"
```

A base config for the "Adapt" provider on macOS:

`config_with_resampler.yml`
```yaml
devices:
  samplerate: 96000
  capture_samplerate: 44100
  chunksize: 1024
  resampler:
    type: Synchronous
  capture:
    type: CoreAudio
    channels: 2
    device: "BlackHole 2ch"
  playback:
    type: CoreAudio
    channels: 2
    device: "MyDAC"
```

When a 44.1 kHz stream plays, `capture_samplerate` is updated to 44100. When a 96 kHz stream plays, `capture_samplerate` is set to 96000 and the resampler is removed.

### Windows

There is currently no device listener for Windows. The available loopback APIs do not expose the sample rate of the playback side, and WASAPI does not report the new rate when a change occurs — only that a change happened. This is a limitation of the Windows audio APIs.

The controller can still run on Windows, but its main use there is restarting CamillaDSP automatically if processing stops with a capture or playback error.
