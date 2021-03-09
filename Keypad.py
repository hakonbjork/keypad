"""Module for the Keypad class"""

import time
from GPIOSimulator_v5 import GPIOSimulator, keypad_row_pins, keypad_col_pins


GPIO = GPIOSimulator()


class Keypad:
    """  Keypad """

    def __init__(self):
        """
        Init method
        """
        self.rowpins = keypad_row_pins
        self.columnpins = keypad_col_pins
        self.setup()

    def setup(self):
        """
        initialize the row pins as outputs and the column pins as inputs.
        :return: None
        """

        for row_pin, rp in enumerate(self.rowpins):
            GPIO.setup(rp, GPIO.OUT)

        for col_pin, cp in enumerate(self.columnpins):
            GPIO.setup(cp, GPIO.IN, state=GPIO.LOW)

    def do_polling(self):
        """
        Use nested loops (discussed above) to determine the key currently being
        pressed on the keypad.
        :return: None
        """
        for row_index, row_pin in enumerate(self.rowpins):
            # setting the rowpin HIGH one at a time.
            GPIO.output(row_pin, GPIO.HIGH)

            for col_index, col_pin in enumerate(self.columnpins):
                # If column C has a HIGH reading, then the key at location (R,C)
                # is revealed as the one being pressed.
                if GPIO.input(col_pin) == GPIO.HIGH:
                    GPIO.output(row_pin, GPIO.LOW)
                    return row_index, col_index

            GPIO.output(row_pin, GPIO.LOW)
            time.sleep(0.02)
        return None

    def get_next_signal(self):
        """
        This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected.
        :return: String representation of button pressed
        """

        old_result = None
        while True:
            time.sleep(0.05)
            result = self.do_polling()
            if result:
                old_result = result
            if result != old_result:
                row, col = old_result[0], old_result[1]
                # print(f"Row: {row}, Column: {col}")
                if row <= 3 and col <= 2:

                    # How to find the right button number for button pressed
                    button = row*3 + col + 1

                    if button < 10:
                        return str(button)
                    if button == 10:
                        return '*'
                    if button == 11:
                        return '0'
                    if button == 12:
                        return '#'
