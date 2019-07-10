from __future__ import absolute_import, print_function, unicode_literals
from .X6 import X6
import sys

def create_instance(c_instance):
    return X6(c_instance)

from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=6860, product_ids=[6709], model_name='X6'),
        PORTS_KEY: [
                    inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                    inport(props=[NOTES_CC, REMOTE]),
                    outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
