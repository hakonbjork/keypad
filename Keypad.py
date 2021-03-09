from GPIOSimulator_v5 import *
import time

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
        for r, rp in enumerate(self.rowpins):
            # setting the rowpin HIGH one at a time.
            GPIO.output(rp, GPIO.HIGH)

            for c, cp in enumerate(self.columnpins):
                # If column C has a HIGH reading, then the key at location (R,C) is revealed as the one being pressed.
                if GPIO.input(cp) == GPIO.HIGH:
                    GPIO.output(rp, GPIO.LOW)
                    return r, c

            GPIO.output(rp, GPIO.LOW)
            time.sleep(0.02)
        return None

    def get_next_signal(self):
        """
        This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected.
        :return: String representation of button pressed
        """

        # TODO: Make sure this is not an infinite loop
        while True:
            result = self.do_polling()
            if result:
                row, col = result[0], result[1]
                # print(f"Row: {row}, Column: {col}")
                if row <= 3 and col <= 2:

                    # How to find the right button number for button pressed
                    button = row*3 + col + 1

                    if button < 10:
                        return str(button)

                    else:
                        if button == 10:
                            return '*'
                        elif button == 11:
                            return '0'
                        elif button == 12:
                            return '#'

    def main(self):
        pass


if __name__ == '__main__':
    print("Heihei test")
    keypad = Keypad()
    while True:
        sign = keypad.get_next_signal()
        print("Signal = ", sign)

        # skal gjøre polling
        # self
        # This is the main interface between the agent and the keypad.
        # It should initiate repeated calls to do polling until a key press is detected.
