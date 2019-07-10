from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import *

from _Framework.ModeSelectorComponent import ModeSelectorComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent
from _Framework.SessionComponent import SessionComponent

import sys

IS_MOMENTARY = True

X6_SIG = (
    # SysEx start
    240, 
    # Vendor ID (and product id?) for MIDIPlus (X6)
    127, 74, 6
    )

def log(message):
    sys.stderr.write("X6 script: " + message.encode("utf-8"))

class X6(ControlSurface):
    """
    MIDIPlus X6 transport support
    """
    
    def __init__(self, c_instance):
        self.__c_instance = c_instance
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            self._suggested_input_port = 'X6'
            self._suggested_output_port = 'X6'

    def handle_sysex(self, midi_bytes):
        if midi_bytes[0:-2] == X6_SIG:
            command = midi_bytes[(-2)]
            if command is 1:
                self.stop()
            elif command is 2:
                self.play()
            elif command is 6:
                self.record()
            else:
                log("Unexpected command: "+str(command))
        self.request_rebuild_midi_map()
        return

    def song(self):
        """
        Returns a reference to the Live song instance that we control
        """
        return self.__c_instance.song()

    def play(self):
        self.song().continue_playing()

    def stop(self):
        self.song().is_playing = False

    def record(self):
        self.song().record_mode = not self.song().record_mode
