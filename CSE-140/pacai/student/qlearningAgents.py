from pacai.agents.learning.reinforcement import ReinforcementAgent
from pacai.util import reflection
from pacai.util.probability import flipCoin
import random


class QLearningAgent(ReinforcementAgent):
    """
    A Q-Learning agent.

    Some functions that may be useful:

    `pacai.agents.learning.reinforcement.ReinforcementAgent.getAlpha`:
    Get the learning rate.

    `pacai.agents.learning.reinforcement.ReinforcementAgent.getDiscountRate`:
    Get the discount rate.

    `pacai.agents.learning.reinforcement.ReinforcementAgent.getEpsilon`:
    Get the exploration probability.

    `pacai.agents.learning.reinforcement.ReinforcementAgent.getLegalActions`:
    Get the legal actions for a reinforcement agent.

    `pacai.util.probability.flipCoin`:
    Flip a coin (get a binary value) with some probability.

    `random.choice`:
    Pick randomly from a list.

    Additional methods to implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Compute the action to take in the current state.
    With probability `pacai.agents.learning.reinforcement.ReinforcementAgent.getEpsilon`,
    we should take a random action and take the best policy action otherwise.
    Note that if there are no legal actions, which is the case at the terminal state,
    you should choose None as the action.

    `pacai.agents.learning.reinforcement.ReinforcementAgent.update`:
    The parent class calls this to observe a state transition and reward.
    You should do your Q-Value update here.
    Note that you should never call this function, it will be called on your behalf.

    DESCRIPTION: <Write something here so we know what you did.>
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

        # You can initialize Q-values here.
        self.QValues = {}  # empty dictionary to store Q values

    def getQValue(self, state, action):
        """
        Get the Q-Value for a `pacai.core.gamestate.AbstractGameState`
        and `pacai.core.directions.Directions`.
        Should return 0.0 if the (state, action) pair has never been seen.
        """
        # like it says in the docstring we return 0.0 if the state action pair has not been seen
        if (state, action) not in self.QValues:
            return 0.0
        return self.QValues[(state, action)]

    def getValue(self, state):
        """
        Return the value of the best action in a state.
        I.E., the value of the action that solves: `max_action Q(state, action)`.
        Where the max is over legal actions.
        Note that if there are no legal actions, which is the case at the terminal state,
        you should return a value of 0.0.

        This method pairs with `QLearningAgent.getPolicy`,
        which returns the actual best action.
        Whereas this method returns the value of the best action.
        """
        OptimalQval = -99999
        actions = self.getLegalActions(state)
        # iterate through actions to find the optimal aka max Qval
        for a in actions:
            OptimalQval = max(OptimalQval, self.getQValue(state, a))
        # this if statement checker is needed for terminal state.
        # was essential for the value iteration
        if len(actions) == 0:
            return 0.0
        return OptimalQval

    def getPolicy(self, state):
        """
        Return the best action in a state.
        I.E., the action that solves: `max_action Q(state, action)`.
        Where the max is over legal actions.
        Note that if there are no legal actions, which is the case at the terminal state,
        you should return a value of None.

        This method pairs with `QLearningAgent.getValue`,
        which returns the value of the best action.
        Whereas this method returns the best action itself.
        """
        # if q values match we have to break it with a tie
        b_action = []
        OptimalQval = self.getValue(state)  # use our method to find Optimal Q-values
        actions = self.getLegalActions(state)
        s = state
        for a in actions:
            if self.getQValue(s, a) == OptimalQval and len(b_action) == 0:
                b_action = [a]
            elif self.getQValue(s, a) == OptimalQval:
                b_action.append(a)
        # if there is no best action return None
        if len(b_action) == 0:
            return None
        return random.choice(b_action)

    def update(self, s, a, sPrime, reward):
        """
        An update function inspired by Lec 11 page 21 slides

        performs Q learning estimate average.
        Q(s,a) <- (1-alpha) Q(s,a) + (alpha)[sample]
        """
        # implemented equations straigh from slides
        sample = reward + ReinforcementAgent.getDiscountRate(self) * self.getValue(
            sPrime
        )
        self.QValues[(s, a)] = (
            1.0 - ReinforcementAgent.getAlpha(self)
        ) * self.getQValue(s, a) + ReinforcementAgent.getAlpha(self) * sample

    def getAction(self, state):
        """
         it chooses random actions epsilon of the time, and follows its current
         best q-values otherwise. uses flip coin
        """
        actions = self.getLegalActions(state)
        # random action
        epsilon = ReinforcementAgent.getEpsilon(self)
        if flipCoin(epsilon):
            return random.choice(actions)
        # or just get best policy
        return self.getPolicy(state)


class PacmanQAgent(QLearningAgent):
    """
    Exactly the same as `QLearningAgent`, but with different default parameters.
    """

    def __init__(
        self, index, epsilon=0.05, gamma=0.8, alpha=0.2, numTraining=0, **kwargs
    ):
        kwargs["epsilon"] = epsilon
        kwargs["gamma"] = gamma
        kwargs["alpha"] = alpha
        kwargs["numTraining"] = numTraining

        super().__init__(index, **kwargs)

    def getAction(self, state):
        """
        Simply calls the super getAction method and then informs the parent of an action for Pacman.
        Do not change or remove this method.
        """

        action = super().getAction(state)
        self.doAction(state, action)

        return action


class ApproximateQAgent(PacmanQAgent):
    """
    An approximate Q-learning agent.

    You should only have to overwrite `QLearningAgent.getQValue`
    and `pacai.agents.learning.reinforcement.ReinforcementAgent.update`.
    All other `QLearningAgent` functions should work as is.

    Additional methods to implement:

    `QLearningAgent.getQValue`:
    Should return `Q(state, action) = w * featureVector`,
    where `*` is the dotProduct operator.

    `pacai.agents.learning.reinforcement.ReinforcementAgent.update`:
    Should update your weights based on transition.

    DESCRIPTION: <Write something here so we know what you did.>
    """

    def __init__(
        self,
        index,
        extractor="pacai.core.featureExtractors.IdentityExtractor",
        **kwargs
    ):
        super().__init__(index, **kwargs)
        self.featExtractor = reflection.qualifiedImport(extractor)

        # You might want to initialize weights here.
        self.weights = {}

    def getQValue(self, state, action):
        features = self.featExtractor.getFeatures(self, state, action)
        sum = 0
        for feature in features:
            sum += self.getWeight(feature) * features[feature]
        return sum

    def getWeight(self, feature):
        if feature not in self.weights:
            return 0.0
        return self.weights[feature]

    def update(self, state, action, nextState, reward):
        discount = self.getDiscountRate()
        alpha = self.getAlpha()
        sprime = self.getValue(nextState)
        correction = (reward + discount * sprime) - self.getQValue(state, action)
        features = self.featExtractor.getFeatures(self, state, action)
        for feature in features:
            self.weights[feature] = alpha * correction + self.getWeight(feature)

    def final(self, state):
        """
        Called at the end of each game.
        """

        # Call the super-class final method.
        super().final(state)

        # Did we finish training?
        if self.episodesSoFar == self.numTraining:
            # You might want to print your weights here for debugging.
            # *** Your Code Here ***
            pass
            #raise NotImplementedError()
