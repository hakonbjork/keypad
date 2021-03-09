""" Module for FSM Rule class """

from inspect import isfunction


class FSMRule:
    """
    Each rule has the following meaning:
    IF the FSM is in a state that matches rule.state1 and the current signal matches
    rule.signal THEN change the FSM’s state to rule.state2 and call the method specified
    by rule.action (and give that method two arguments (the agent itself and the current
    signal).
    """

    def __init__(self, fsm, state1, state2, signal, action):

        # connects the FSM to the rule
        self.fsm = fsm

        #  triggering state of the FSM.
        self.state1 = state1

        # new state of the FSM if this rule fires.
        self.state2 = state2

        # triggering signal.
        self.signal = signal

        # the agent will be instructed to perform this action if this rule fires.
        self.action = action

    def match(self):
        """
        check whether the rule condition is fulfilled.
        :return: True if condition is fulfilled, False if not
        """

        if isfunction(self.signal):
            # print(f"Signal is function, returning boolean")
            return self.signal(self.fsm.signal)

        return self.fsm.signal == self.signal

    def fire(self):
        """
        use the consequent of a rule to a) set the next state of the FSM,
        and b) call the appropriate agent action method.
        :return: None
        """
        self.fsm.state = self.state2

        # give that method two arguments (the agent itself and the current signal
        self.action(self.fsm.signal)
