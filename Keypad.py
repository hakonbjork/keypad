from GPIOSimulator_v5 import GPIOSimulator
import time

GPIO = GPIOSimulator()


class Keypad:
    """  Keypad """

    def __init__(self):
        """
        Init method
        """
        self.rowpins = []
        self.columnpins = []

    def setup(self):
        """
        initialize the row pins as outputs and the column pins as inputs.
        :return: None
        """

        pass

    def do_polling(self):
        """
        Use nested loops (discussed above) to determine the key currently being
        pressed on the keypad.
        :return: None
        """
        for rp in enumerate(self.rowpins):
            # setting the rowpin HIGH one at a time.
            GPIO.output(rp, GPIO.HIGH)

            for cp in enumerate(self.columnpins):
                # If column C has a HIGH reading, then the key at location (R,C) is revealed as the one being pressed.
                pass

    def get_next_signal(self):
        """
        This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected.
        :return: None
        """

    def main(self):
        pass
