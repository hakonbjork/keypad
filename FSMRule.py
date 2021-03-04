
class FSMRule:
    """
    Each rule has the following meaning:
    IF the FSM is in a state that matches rule.state1 and the current signal matches
    rule.signal THEN change the FSM’s state to rule.state2 and call the method specified
    by rule.action (and give that method two arguments (the agent itself and the current
    signal).
    """

    def __init__(self, s1, s2, signal, action):
        #  state of the FSM.
        self.s1 = s1

        # new state of the FSM if this rule fires.
        self.s2 = s2

        # triggering signal.
        self.signal = signal

        # the agent will be instructed to perform this action if this rule fires.
        self.action = action

    def main(self):
        pass
