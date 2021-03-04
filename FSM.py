class FSM:
    """  An FSM object should house a pointer back to the agent, since it will make many requests to the
    agent (KPC) object. """

    def add_rule(self):
        """
        add a new rule to the end of the FSM’s rule list.
        :return: None
        """
        pass

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
        pass

    # There are two key methods for a FSM rule
    def match(self):
        """
        check whether the rule condition is fulfilled.
        :return: None
        """
        pass

    def fire(self):
        """
        use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate
        agent action method.
        :return: None
        """

    def main(self):
        pass
