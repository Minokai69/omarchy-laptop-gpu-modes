# Omarchy Laptop GPU Modes

A theme-aware Omarchy power-panel plugin for laptops with NVIDIA hybrid graphics.
It adds Integrated, Hybrid, and VFIO mode controls below the existing power-profile controls.

## What it does

- Shows the current `supergfxctl` graphics mode.
- Discovers the modes supported by the installed `supergfxd`.
- Uses Omarchy’s existing panel, button, spacing, color, and dialog components.
- Writes the requested mode to `supergfxd`’s persistent configuration.
- Forces reboot-only transitions so NVIDIA modules are never unloaded while Hyprland is running.
- Requires confirmation before rebooting.

Reboot-only behavior is intentional. Live switching can terminate Hyprland when applications or the compositor hold `/dev/nvidia0`.

## Requirements

- Omarchy with the Quickshell plugin system.
- `supergfxctl`/`supergfxd` installed and enabled.
- NVIDIA laptop hardware supported by the installed NVIDIA driver.
- `jq` available for the privileged configuration helper.

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

The plugin runs unsandboxed code and invokes privileged `pkexec` operations. Review the source before installing. The helper accepts only the three known mode names and rewrites only `/etc/supergfxd.conf` before rebooting.

## License

MIT. See [LICENSE](LICENSE).
