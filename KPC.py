""" Module for the KPC class """

from Keypad import Keypad
from LED_Board import LED_Board


class KPC:
    """  KPC """

    def __init__(self, fsm):
        self.keypad = Keypad()
        self.led_board = LED_Board()
        self.fsm = fsm
        self.path_name = "password.txt"
        self.override_signal = ""
        # cumulative password
        self.CUMP = ''
        self.Lid = ''
        self.Ldur = ''

    def reset_passcode_entry(self, signal):
        """ Clear passcode buffer, initiate power_up lightning sequence
        on led board """

        self.CUMP = ''
        self.override_signal = ''
        self.led_board.power_up_the_system()

    def reset_password(self, signal):
        """ Resets password to empty string """
        self.CUMP = ''
        print("Current password reset. Please type new password")

    def get_next_signal(self):
        """ Return the override_signal if not blank, else query keypad for
        next pressed key """

        if self.override_signal:
            ov_sig = self.override_signal
            self.override_signal = ''
            return ov_sig

        return self.keypad.get_next_signal()

    def verify_login(self, signal):
        """ Check if password is correct, store result in override_signal,
        inititate appropriate lightning pattern for success or failure """

        print("Verifying login...")

        my_file = open(self.path_name, "r")
        password = my_file.readline()
        my_file.close()

        if self.CUMP == str(password):
            self.override_signal = "Y"
            self.led_board.successful_login()
            print("Successfully logged in")
        else:
            self.override_signal = "N"
            self.led_board.flash_all_lights()
            print("Login failed, password incorrect")

    def validate_password_change(self, signal):
        """ Check that new password is legal and write it to password file """

        password = self.CUMP

        legal = False
        if len(password) > 4:
            for i in password:
                if 0 <= int(i) <= 9:
                    legal = True

                else:
                    legal = False
                    break

        if legal:
            passw_file = open(self.path_name, "w")
            passw_file.write(password)
            passw_file.close()
            self.led_board.successful_login()
            print("Password changed successfully")
        else:
            self.led_board.flash_all_lights()
            print("New password not legal. Password not changed")

    def append_next_password_digit(self, signal):
        """ Adds the current signal to cumulative password (CUMP) """
        self.CUMP += signal
        print("Next digit added to CUMP")

    def set_user_led_ID(self, signal):
        """ Sets the self.Lid (led number) after user input """

        if 0 <= int(signal) <= 5:
            self.Lid = int(signal)

        else:
            print("Wrong digit, must be 0 - 5")

    def append_digit_to_user_led_duration(self, signal):
        """ Sets the self.Ldur after user input """
        self.Ldur += signal
        print("Digit added to duration")

    def light_one_led(self, signal):
        """ Lights up one LED based on user input """
        led_id = int(self.Lid)
        led_duration = int(self.Ldur)
        self.Lid = ''
        self.Ldur = ''
        self.led_board.user_choose_led(led_id, led_duration)

    def flash_leds(self):
        """ Flash all leds """
        self.led_board.flash_all_leds(2)

    def twinkle_leds(self):
        """ Twinkle all leds """
        self.led_board.twinkle_all_leds(2)

    def exit_action(self, signal):
        """ Shuts down and resets values """

        print("Logging out...")

        self.led_board.power_down_the_system()
        self.__init__(self.fsm)

    def confirm_logout(self, signal):
        """ Asks user to confirm logout """

        print("Press # to confirm logout, or anything else to abort")

    def fully_activate_agent(self, signal):
        """ Sends message that the agent is ready to use"""

        print("Ready to use!")

    def do_nothing(self, agent):
        """ Does nothing """
