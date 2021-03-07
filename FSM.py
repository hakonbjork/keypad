from FSMRule import FSMRule
from inspect import isfunction
from Keypad import Keypad


def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


class FSM:
    """  An FSM object should house a pointer back to the agent, since it will make many requests to the
    agent (KPC) object. """

    def __init__(self):
        self.rules = []
        self.state = 'S-Init'
        self.signal = None
        # current password
        self.CP = ''
        # cumulative password
        self.CUMP = ''

    def add_rule(self, s1, s2, signal, action):
        """
        add a new rule to the end of the FSM’s rule list.
        :return: None
        """
        self.rules.append(FSMRule(s1, s2, signal, action))

    def gen_next_signal(self):
        """
        query the agent for the next signal.
        :return: None
        """

        pass

    def run(self):
        """
        begin in the FSM’s default initial state and then repeatedly call get next signal and
        run the rules one by one until reaching the final state.
        :return: None
        """
        for rule in self.rules:
            if self.state == rule.s1 and self.match(rule):
                self.fire(rule)

    # There are two key methods for a FSM rule
    def match(self, rule):
        """
        check whether the rule condition is fulfilled.
        :return: True if condition is fulfilled, False if not
        """
        if self.singal == rule.signal and signal_is_digit(self.singal):
            return True
        else:
            return False

    def fire(self, rule):
        """
        use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate
        agent action method.
        :return: None
        """
        self.state = rule.s2

        # give that method two arguments (the agent itself and the current signal
        rule.action()

    def main(self):
        pass
