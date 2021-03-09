from FSMRule import FSMRule
from inspect import isfunction
from Keypad import Keypad
from KPC import *
import time

states = [
    'S-Init',  # initial state. cump should be empty
    'S-Read',  # state when reading password
    'S-Verify',  # when verifying password (short amount of time)
    'S-Active',  # usual state when 'logged in'
    'S-Read-2',  # read new password when user want to change password
    'S-Read-3',  # enter new password again
    'S-Led',  # when user want to light up led, read input as led number
    'S-Time'  # for a duration, read input as time in seconds
]


def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


def all_signals(signal):
    """ Simple method to accept a signal """
    return True


def all_digits(signal):
    """ Simple method to accept all digits """
    return signal_is_digit(signal)


class FSM:
    """  An FSM object should house a pointer back to the agent, since it will make many requests to the
    agent (KPC) object. """

    def __init__(self):
        self.rules = []
        self.state = 'S-Init'
        self.signal = None
        self.agent = KPC(self)
        self.add_rules()

    def add_rule(self, s1, s2, signal, action):
        """
        add a new rule to the end of the FSM’s rule list.
        :return: None
        """
        self.rules.append(FSMRule(self, s1, s2, signal, action))

    def get_next_signal(self):
        """
        query the agent for the next signal.
        :return: None
        """

        return self.agent.get_next_signal()

    def run(self):
        """
        begin in the FSM’s default initial state and then repeatedly call get next signal and
        run the rules one by one until reaching the final state.
        :return: None
        """

        while self.state != 'S-Exit':
            print()

            print("Waiting for signal...")
            self.signal = self.get_next_signal()
            print(f"Received signal: {self.signal}")

            ruleFired = False
            for rule in self.rules:
                if self.state == rule.state1 and rule.match():
                    print(
                        f"Rule to fire: {str(rule.state1)} --> {str(rule.state2)}")
                    rule.fire()
                    ruleFired = True
                    break

            if not ruleFired:
                print("Error: No rules fired")

    def add_rules(self):
        """ create and add the rules to be used """
        self.add_rule('S-Init', 'S-Read',
                      all_signals, self.agent.reset_passcode_entry)  # 1

        self.add_rule('S-Read', 'S-Read', all_digits,
                      self.agent.append_next_password_digit)  # 2

        self.add_rule('S-Read', 'S-Verify', '*', self.agent.verify_login)  # 3

        self.add_rule('S-Read', 'S-Init', all_signals,
                      self.agent.exit_action)  # 4

        self.add_rule('S-Verify', 'S-Active', 'Y',
                      self.agent.fully_activate_agent)  # 5

        self.add_rule('S-Verify', 'S-Init',
                      all_signals, self.agent.exit_action)  # 6-1

        self.add_rule('S-Active', 'S-Read-2', '*',
                      self.agent.reset_password)  # 6-2

        self.add_rule('S-Read-2', 'S-Read-2', all_digits,
                      self.agent.append_next_password_digit)  # 7

        self.add_rule('S-Read-2', 'S-Active', '*',
                      self.agent.validate_password_change)  # 8

        self.add_rule('S-Active', 'S-Led', all_digits,
                      self.agent.set_user_led_ID)  # 9

        self.add_rule('S-Led', 'S-Time', '*', self.agent.do_nothing)  # 10

        self.add_rule('S-Time', 'S-Time', all_digits,
                      self.agent.append_digit_to_user_led_duration)  # 11

        self.add_rule('S-Time', 'S-Active', '*',
                      self.agent.light_one_led)  # 12

        self.add_rule('S-Active', 'S-Logout', '#',
                      self.agent.confirm_logout)  # 13

        self.add_rule('S-Logout', 'S-Init', '#', self.agent.exit_action)  # 14

        self.add_rule('S-Logout', 'S-Active', all_signals,
                      self.agent.do_nothing)  # 15

        # look at page 9 in project description for more rules,
        # and take a look at drawing of FSM.
        # Each arc/line there should correspond to a rule.


def main():
    fsm = FSM()
    fsm.run()


if __name__ == "__main__":
    main()
