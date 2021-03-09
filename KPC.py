""" Module for the KPC class """

from Keypad import Keypad
from LED_Board import LED_Board
from FSM import FSM
from FSMRule import FSMRule


class KPC:
    """  KPC """

    def __init__(self, FSM):
        self.keypad = Keypad()
        self.led_board = LED_Board()
        self.FSM = FSM
        self.path_name = "password.txt"
        self.override_signal = ""
        # cumulative password
        self.CUMP = ''
        self.Lid = 0
        self.Ldur = 0

    def reset_passcode_entry(self, signal):
        """ Clear passcode buffer, initiate power_up lightning sequence
        on led board """

        self.CUMP = ''
        self.override_signal = ''
        self.led_board.power_up_the_system()

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

        f = open(self.path_name, "r")
        password = f.readline()
        f.close()

        if self.CUMP == str(password):
            self.override_signal = "Y"
            self.led_board.successful_login()
        else:
            self.override_signal = "N"
            self.led_board.flash_all_lights()

        # TODO: Find out whether we should clear override_signal sometime

    # tror ikke disse parametere er helt good
    def validate_password_change(self, password):
        """ Check that new password is legal and write it to password file """

        legal = True
        if len(password) > 4:
            for i in password:
                if not (0 <= int(i) <= 9):
                    legal = False

        if legal:
            f = open(self.path_name, "w")
            f.write(password)
            f.close()
            self.led_board.successful_login()
        else:
            self.led_board.flash_all_lights()

    def append_next_password_digit(self, signal):
        """ Adds the current signal to cumulative password (CUMP) """
        self.CUMP += signal
        print("Next digit added to CUMP")

    def light_one_led(self):
        self.led_board.user_choose_led(self.Lid, self.Ldur)

    def flash_leds(self):
        self.led_board.flash_all_leds()

    def twinkle_leds(self):
        self.led_board.twinkle_all_leds(2)

    def exit_action(self, signal):
        self.led_board.power_down_the_system()
        self.__init__(self.FSM)

    def fully_activate_agent(self, signal):
        """ Vet ikke om man trenger noe her, etter denne er kjørt skal 
        man være i stand til å gjøre ting i innlogget tilstand, men mulig
        det fikses av FSM  """

        pass
