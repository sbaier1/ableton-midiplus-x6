#!/usr/bin/env bash

set -eo pipefail

if ! which pip >/dev/null 2>/dev/null; then
  echo "pip not found, attemping to install, admin privileges required"
  sudo -H python -m ensurepip
fi

if ! which uncompyle6 >/dev/null 2>/dev/null; then
  echo "uncompyle6 not found in path, attempting to install..."
  pip install uncompyle6
fi

cd "/Applications/Ableton Live 10 Suite.app/Contents/App-Resources/MIDI Remote Scripts"
# Decompile files in-place
uncompyle6 -o . -r .
