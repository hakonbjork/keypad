from FSMRule import FSMRule
from inspect import isfunction
from Keypad import Keypad
from KPC import *

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


class FSM:
    """  An FSM object should house a pointer back to the agent, since it will make many requests to the
    agent (KPC) object. """

    def __init__(self):
        self.rules = []
        self.state = 'S-Init'
        self.signal = None
        self.agent = KPC(self)

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
            self.signal = self.get_next_signal()
            # print(f"Received signal: {self.signal}")
            for rule in self.rules:
                if self.state == rule.state1 and rule.match():
                    print(f"Rule to fire: {rule}")
                    self.fire(rule)

                else:
                    print("No rules fired :(")

    def all_signals(self):
        """ Simple method to accept a signal """
        return True

    def all_digits(self):
        """ Simple method to accept all digits """
        return signal_is_digit(self.signal)

    def add_rules(self):
        """ create and add the rules to be used """
        self.add_rule('S-Init', 'S-Read',
                      self.all_signals, self.agent.reset_passcode_entry)

        self.add_rule('S-Read', 'S-Read', self.all_digits,
                      self.agent.append_next_password_digit)

        self.add_rule('S-Read', 'S-Verify', '*', self.agent.verify_login)

        self.add_rule('S-Read', 'S-Init', self.all_signals,
                      self.agent.exit_action)

        self.add_rule('S-Verify', 'S-Active', 'Y',
                      self.agent.fully_activate_agent)

        self.add_rule('S-Verify', 'S-Init',
                      self.all_signals, self.agent.exit_action)

        # look at page 9 in project description for more rules,
        # and take a look at drawing of FSM.
        # Each arc/line there should correspond to a rule.


def main():
    fsm = FSM()
    fsm.add_rules()
    print("Rules added succesfully")
    fsm.run()


if __name__ == "__main__":
    main()
