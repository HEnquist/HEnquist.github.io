---
title: Customization
weight: 3
---

Two files control how the GUI looks and behaves. Both ship with the bundle and have inline comments explaining the available options:

- `camillagui_backend/config/gui-config.yml` — behavior, shortcuts, and which options are visible
- `camillagui_backend/build/css-variables.css` — visual styling

## Page title

Setting a custom page title helps distinguish multiple CamillaDSP instances on the same network. The title appears in the browser tab, making it easy to identify which GUI controls which system.

## Volume control

The range and maximum of the volume slider can be adjusted. The defaults suit most setups, but a headphone system might want a narrower range or different ceiling.

## Hiding options

Options and sections that aren't relevant to a particular setup can be hidden entirely — for example, hiding the rate monitoring controls on a system where that feature isn't used. The config file lists what can be hidden.

## Automatic config apply

By default, config changes made in the GUI are only sent to CamillaDSP when you explicitly apply them. This can be changed so edits are applied immediately, which is useful for live tweaking.

## Custom shortcuts

Shortcuts let you expose specific filter parameters as sliders or checkboxes in a dedicated section of the GUI — without having to navigate the full config tree. They appear both in the Shortcuts tab and in the compact view.

Each shortcut targets one or more paths in the CamillaDSP config (e.g. a filter gain value), and is shown as either a slider (`type: "number"`) or a checkbox (`type: "boolean"`). When a shortcut controls multiple config elements, the first one drives the slider position; the others are kept in sync, and the GUI warns if they drift.

The config file ships with examples for common use cases like bass and treble controls. The backend logs a clear error on startup if any shortcut entry has invalid values.

## Styling

The CSS variables file controls colors, fonts, and other visual properties. It includes instructions for common changes and how to switch between the default dark theme and the black-and-white theme.
