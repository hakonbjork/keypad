""" Module for the KPC class """

from Keypad import Keypad
from LED_Board import LED_Board


class KPC:
    """  KPC """

    def __init__(self):
        self.keypad = Keypad()
        self.led_board = LED_Board()
        self.path_name = "/password.txt"
        self.override_signal = NotImplemented

    def reset_passcode_entry(self):
        """ Clear passcode buffer, initiate power_up lightning sequence
        on led board """
