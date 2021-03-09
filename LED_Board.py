from GPIOSimulator_v5 import *
import time

GPIO = GPIOSimulator()


class LED_Board:
    """  LED_Board """

    def __init__(self):
        self._led_comb = {
            # 0: output high
            # -1: output low
            # 1: input high
            0: [0, -1, 1],  # riktig
            1: [-1, 0, 1],  # riktig
            2: [0, 1, - 1],
            3: [0, -1, 1],
            4: [1, 0, -1],
            5: [-1, 0, 1],
            "all_led": [1, 1, 1],
            "no_led": [-1, -1, -1]
        }

    def set_pin(self, pin_number, value):
        """ helper function to set the the charlieplexing pins to 
        the right state """

        if value == 0:
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.HIGH)

        elif value == -1:
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.LOW)

        elif value == 1:
            GPIO.setup(pin_number, GPIO.IN)

        else:
            raise KeyError("Error: Invalid value")

    def light_led(self, led_number):
        """
        Turn on one of the 6 LEDs by making the appropriate combination of input
        and output declarations, and then making the appropriate HIGH / LOW settings on the
        output pins.
        :return: None
        """
        verdier = self._led_comb.get(led_number)
        pin0_value = verdier[0]
        pin1_value = verdier[1]
        pin2_value = verdier[2]

        self.set_pin(PIN_CHARLIEPLEXING_0, pin0_value)
        self.set_pin(PIN_CHARLIEPLEXING_1, pin1_value)
        self.set_pin(PIN_CHARLIEPLEXING_2, pin2_value)

        GPIO.show_leds_states()

    def flash_all_leds(self, k):
        """
        Flash all 6 LEDs on and off for k seconds, where k is an argument of the
        method.
        :return: None
        """

        self.turn_on_all_leds()
        time.sleep(k)
        self.turn_off_all_leds()

    def turn_on_all_leds(self):
        """ Turns all the led lights on """

        for i in range(6):
            self.light_led(i)

    def turn_off_all_leds(self):
        """ Turns off all the leds """

        for i in range(3):
            self.set_pin(i, -1)

    def twinkle_all_leds(self, k):
        """
        Turn all LEDs on and off in sequence for k seconds, where k is an
        argument of the method.
        :return: None
        """

        self.turn_off_all_leds()

        old_time = time.time()
        new_time = time.time()
        while new_time - old_time < k:
            self.turn_on_all_leds()
            time.sleep(0.2)
            self.turn_off_all_leds()
            time.sleep(0.2)
            new_time = time.time()

            # In addition, you will need methods for the lighting patterns associated with powering up (and
            # down) the system.

            # A display of lights (of your choosing) that indicates “powering up”. This should be performed
            # when the user does the very first keystroke of a session.

    def power_up_the_system(self):
        """ Lights up a pattern to signal that the system is booting up """

        print("Powering up the system ...")

        self.turn_off_all_leds()

        for i in range(6):
            self.light_led(i)
            time.sleep(0.2)

        self.turn_off_all_leds()

    # Flashing of all lights “in synchrony” when the user enters the wrong password during login.
    def flash_all_lights(self):
        """ Turns all lights on and off to signal wrong password """

        self.flash_all_leds(0.5)

    # Twinkling the lights (in any sequence you choose) when the user successfully logs in
    def successful_login(self):
        """ Twinkle the lights in a pattern to signal successfully login """

        self.twinkle_all_leds(4)

    # A fourth type of light display (of your choosing) that indicates “powering down”. This
    # should be performed immediately after the user logs out.

    def power_down_the_system(self):
        """ Lights a pattern to signal system powering down """

        print("Powering down the system...")

        self.turn_off_all_leds()

        for i in range(6, 0):
            self.light_led(i)
            time.sleep(0.2)

        self.turn_off_all_leds()

    # Turn one user-specified LED on for a user-specified number of seconds, where information
    # about the particular LED and duration are entered via the simulated keypad.
    def user_choose_led(self, led_num, duration):
        """ Gets user-specified LED and duration from simulated keypad, 
        light up that LED for the user-specified duration """

        self.light_led(led_num)
        time.sleep(duration)
        self.turn_off_all_leds()
