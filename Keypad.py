import GPIOSimulator_v5 as GPIO

class Keypad:
    """  Keypad """

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

    def get_next_signal(self):
        """
        This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected.
        :return: None
        """

    def main(self):
        pass