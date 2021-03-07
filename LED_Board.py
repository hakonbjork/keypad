class LED_Board:
    """  LED_Board """

    def __init__(self):
        pass

    def light_led(self, led_number):
        """
        Turn on one of the 6 LEDs by making the appropriate combination of input
        and output declarations, and then making the appropriate HIGH / LOW settings on the
        output pins.
        :return: None
        """

    def flash_all_leds(self):
        """
        Flash all 6 LEDs on and off for k seconds, where k is an argument of the
        method.
        :return: None
        """

    def twinkle_all_leds(self, k):
        """
        Turn all LEDs on and off in sequence for k seconds, where k is an
        argument of the method.
        :return: None
        """

    # In addition, you will need methods for the lighting patterns associated with powering up (and
    # down) the system.

    # A display of lights (of your choosing) that indicates “powering up”. This should be performed
    # when the user does the very first keystroke of a session.
    def power_up_the_system(self):
        pass

    # Flashing of all lights “in synchrony” when the user enters the wrong password during login.
    def flash_all_lights(self):
        pass

    # Twinkling the lights (in any sequence you choose) when the user successfully logs in
    def successful_login(self):
        pass

    # A fourth type of light display (of your choosing) that indicates “powering down”. This
    # should be performed immediately after the user logs out.
    def power_down_the_system(self):
        pass

    # Turn one user-specified LED on for a user-specified number of seconds, where information
    # about the particular LED and duration are entered via the simulated keypad.
    def user_choose_led(self):
        pass
