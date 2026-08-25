#!/bin/bash
set -euo pipefail

mode=${1:-}
case "$mode" in
  Integrated|Hybrid|Vfio) ;;
  *)
    echo "Unsupported GPU mode: $mode" >&2
    exit 2
    ;;
esac

tmp=$(mktemp /run/supergfxd.conf.XXXXXX)
trap 'rm -f "$tmp"' EXIT

jq --arg mode "$mode" \
  '.mode = $mode | .always_reboot = true' \
  /etc/supergfxd.conf > "$tmp"

install -o root -g root -m 0644 "$tmp" /etc/supergfxd.conf
