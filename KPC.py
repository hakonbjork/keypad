""" Module for the KPC class """

from Keypad import Keypad
from LED_Board import LED_Board
from FSM import FSM
from FSMRule import FSMRule


class KPC:
    """  KPC """

    def __init__(self):
        self.keypad = Keypad()
        self.led_board = LED_Board()
        self.FSM = FSM()
        self.path_name = "/password.txt"
        self.override_signal = None
        # cumulative password
        self.CUMP = ""
        self.Lid = 0
        self.Ldur = 0

    def reset_passcode_entry(self):
        """ Clear passcode buffer, initiate power_up lightning sequence
        on led board """

        self.CP = ''
        self.override_signal = ''
        self.led_board.power_up_the_system()

    def get_next_signal(self):
        """ Return the overrid_signal if not blank, else query keypad for
        next pressed key """

        if self.override_signal:
            return self.override_signal

        return self.keypad.get_next_signal()

    def verify_login(self):
        """ Check if password is correct, store result in override_signal, 
        inititate appropriate lightning pattern for success or failure """

        f = open(self.path_name, "r")
        password = f.readline()
        f.close()

        if self.CUMP == password:
            self.override_signal = "Y"
            self.led_board.successful_login()
        else:
            self.override_signal = "N"
            self.led_board.flash_all_lights()

        # TODO: Find out whether we should clear override_signal sometime

    def validate_password_change(self, password):
        """ Check that new password is legal and write it to password file """
        if len(password) > 4:
            for i in password:
                if 0 <= int(i) <= 9:
                    f = open(self.path_name, "w")
                    f.write(password)
                    f.close()
                    # led lights
        else:
            # led lights
            pass

    def light_one_led(self):
        self.led_board.user_choose_led(self.Lid, self.Ldur)

    def flash_leds(self):
        self.led_board.flash_all_leds()

    def exit_action(self):
        self.led_board.power_down_the_system()
        self.__init__()
