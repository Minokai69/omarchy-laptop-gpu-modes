# Omarchy Laptop GPU Modes

A theme-aware Omarchy power-panel plugin for laptops with NVIDIA hybrid graphics.
It adds Integrated, Hybrid, and VFIO mode controls below the existing power-profile controls.

## What it does

- Shows the current `supergfxctl` graphics mode.
- Discovers whether an NVIDIA GPU and usable `supergfxctl` installation are available.
- Hides the GPU controls on unsupported hardware or systems without `supergfxctl`.
- Uses Omarchy’s existing panel, button, spacing, color, and dialog components.
- Reports any pending action and target mode from `supergfxctl` so users know when a logout or reboot is needed.
- Requests mode changes through the installed `supergfxctl` client and daemon.
- Leaves transition and authorization policy to `supergfxd` and the system’s polkit setup.
- Requires confirmation before applying a mode change.

The daemon decides whether a mode transition is immediate or requires a logout/reboot. The plugin asks for confirmation before applying the change and does not automatically reboot the machine.

## Requirements

- Omarchy with the Quickshell plugin system.
- `supergfxctl` installed and able to communicate with `supergfxd`.
- An NVIDIA GPU supported by the installed `supergfxd` configuration.

## Install

```bash
omarchy plugin add https://github.com/Minokai69/omarchy-laptop-gpu-modes.git --enable
omarchy restart shell
```

Open the battery/power menu. GPU modes appear below Power Profile.

## Use

Select Integrated, Hybrid, or VFIO. Authenticate when prompted, confirm the reboot, and save work before applying the change.

- **Integrated**: AMD/iGPU display mode with the NVIDIA GPU powered down.
- **Hybrid**: AMD drives the display; NVIDIA is available for application offloading.
- **VFIO**: reserves the GPU for virtual-machine PCI passthrough.

## Remove

```bash
omarchy plugin remove io.github.minokai69.laptop-gpu-modes
omarchy restart shell
```

Removing the plugin does not change the current system GPU mode. Choose a desired mode before removal if needed.

## Safety

The plugin runs unsandboxed Quickshell code, but it does not ship a privileged helper or write system configuration files directly. It only invokes the installed `supergfxctl -m` client with one of the modes reported by `supergfxctl -s`. Authorization and transition behavior remain controlled by `supergfxd` and the system’s polkit configuration.

## License

MIT. See [LICENSE](LICENSE).
