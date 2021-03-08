from FSMRule import FSMRule
from inspect import isfunction
from Keypad import Keypad


class FSM:
    """  An FSM object should house a pointer back to the agent, since it will make many requests to the
    agent (KPC) object. """

    def __init__(self, agent):
        self.rules = []
        self.state = 'S-Init'
        self.signal = None
        self.agent = agent

    def add_rule(self, s1, s2, signal, action):
        """
        add a new rule to the end of the FSM’s rule list.
        :return: None
        """
        self.rules.append(FSMRule(s1, s2, signal, action))

    def get_next_signal(self):
        """
        query the agent for the next signal.
        :return: None
        """

        return agent.get_next_signal()

    def run(self):
        """
        begin in the FSM’s default initial state and then repeatedly call get next signal and
        run the rules one by one until reaching the final state.
        :return: None
        """

        while self.state != 'S-Exit':
            self.signal = self.get_next_signal()
            for rule in self.rules:
                if self.state == rule.state1 and rule.match():
                    self.fire(rule)

    def add_rules(self):
        """ create and add the rules to be used """

    def main(self):
        pass
