# MIDIPlus X6 Ableton Live 10 script

This is an initial effort for writing a remote script for the MIDIPlus X6 MIDI keyboard for the Ableton Live 10 DAW (tested on 10.0.5, should be compatible with any 10.x version hopefully)

## Installing

1. Get the current release from the [Releases page](https://github.com/sbaier1/ableton-midiplus-x6/releases)

2. Install using the [official Ableton documentation](https://help.ableton.com/hc/en-us/articles/209072009-Installing-Third-Party-Control-Surfaces) for your platform

## Development

To get started on developing this script further (contributions welcome), or for developing your own Live remote scripts, you should set up a makeshift development environment first. Here's how i do it:

1. Decompile the remote script framework and other scripts for reference using either the [decompile script](dev/decompile.sh), which should work on any system with a bash and python installed or manually using [uncompyle6](https://pypi.org/project/uncompyle6/) and a terminal of your choice.

2. For editing, i personally use Visual Studio Code with the Python plugin and set my working directory to the `MIDI Remote Scripts` folder. This leads to most of the syntax highlighting working correctly, safe for the "Live" module, which corresponds to the latest remote script version. There should be a way to create a dirty workaround to fix this as well though. (maybe symlink the current version somehow)
