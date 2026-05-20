---
title: CamillaGUI
weight: 2
---

CamillaGUI is a web-based interface for CamillaDSP. It runs a small backend server locally and
serves the UI to your browser — no internet connection required.

A live demo is available at [camilladsp.com/camillagui/](https://www.camilladsp.com/camillagui/).

{{< cards >}}
  {{< card link="installation" title="Installation" subtitle="Download and run the bundled release, or set up in a Python environment." >}}
  {{< card link="configuration" title="Configuration" subtitle="Connect to CamillaDSP, set file paths, enable HTTPS, and tune backend options." >}}
  {{< card link="customization" title="Customization" subtitle="Add shortcuts, hide options, adjust the volume range, and restyle the UI." >}}
{{< /cards >}}

## How it works

The GUI has two parts:

- **Backend** — a Python server that communicates with CamillaDSP over its WebSocket API, and
  serves the frontend to the browser
- **Frontend** — a React app that runs entirely in the browser

The two parts are distributed together. See [Installation](installation) for how to get them running.
