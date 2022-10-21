# from cmath import inf
from pacai.agents.learning.value import ValueEstimationAgent

# from pacai.core import mdp


class ValueIterationAgent(ValueEstimationAgent):
    """
    A value iteration agent.

    Make sure to read `pacai.agents.learning` before working on this class.

    A `ValueIterationAgent` takes a `pacai.core.mdp.MarkovDecisionProcess` on initialization,
    and runs value iteration for a given number of iterations using the supplied discount factor.

    Some useful mdp methods you will use:
    `pacai.core.mdp.MarkovDecisionProcess.getStates`,
    `pacai.core.mdp.MarkovDecisionProcess.getPossibleActions`,
    `pacai.core.mdp.MarkovDecisionProcess.getTransitionStatesAndProbs`,
    `pacai.core.mdp.MarkovDecisionProcess.getReward`.

    Additional methods to implement:

    `pacai.agents.learning.value.ValueEstimationAgent.getQValue`:
    The q-value of the state action pair (after the indicated number of value iteration passes).
    Note that value iteration does not necessarily create this quantity,
    and you may have to derive it on the fly.

    `pacai.agents.learning.value.ValueEstimationAgent.getPolicy`:
    The policy is the best action in the given state
    according to the values computed by value iteration.
    You may break ties any way you see fit.
    Note that if there are no legal actions, which is the case at the terminal state,
    you should return None.

    author: Simon Lee
    """

    def __init__(self, index, mdp, discountRate=0.9, iters=100, **kwargs):
        super().__init__(index, **kwargs)

        self.mdp = mdp
        self.discountRate = discountRate
        self.iters = iters
        self.values = {}  # A dictionary which holds the q-values for each state.

        # Compute the values here.

        # we need all the components to the set up the bellman equation
        # first iterate through maximum iterations hoping for convergence
        states = mdp.getStates()
        for i in range(0, self.iters):
            values_copy = self.values.copy()
            # iterate through states and actions next to get transition states and probability
            for s in states:
                # noticed that solutions are different with a small number versus 0
                # book intializes to 0 but it doesn't work
                maxVal = -99999
                actions = self.mdp.getPossibleActions(s)
                for a in actions:
                    bellman_update = self.getQValue(s, a)
                    maxVal = max(maxVal, bellman_update)
                # terminal state is zero and kept getting error from grading robot.
                if len(actions) == 0:
                    maxVal = 0.00
                values_copy[s] = maxVal

            # updating our q-values constructor
            self.values = values_copy

        # raise NotImplementedError()

    def getValue(self, state):
        """
        Return the value of the state (computed in __init__).
        """

        return self.values[state]

    def getAction(self, state):
        """
        Returns the policy at the state (no exploration).
        """
        return self.getPolicy(state)

    def getPolicy(self, state):
        """
        returns the best action according to computed values.

        author: Simon Lee
        """
        # intialize smaller number than zero?
        value = -99999
        b_action = None
        # similar to what we wrote in the __init__ except now we care about action
        actions = self.mdp.getPossibleActions(state)

        # iterate through actions and get q values
        for a in actions:
            q_value = self.getQValue(state, a)
            if q_value > value:
                value = q_value
                b_action = a

        # return best action
        return b_action

    def getQValue(self, state, action):
        """
        returns the q-value of the (state, action) pair.

        author: Simon Lee
        """
        # method that gets called in the constructor for value iteration
        bellman_update = 0
        tranStateAndProb = self.mdp.getTransitionStatesAndProbs(state, action)
        # perform the bellman update
        for nextState, probility in tranStateAndProb:
            vStar = 0
            reward = self.mdp.getReward(state, action, nextState)
            if state in self.values:
                vStar = self.values[nextState]
            # Bellman equation summation
            bellman_update += probility * (reward + self.discountRate * vStar)

        return bellman_update
