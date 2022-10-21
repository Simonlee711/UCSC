from cmath import inf
import random

from pacai.agents.base import BaseAgent
from pacai.agents.search.multiagent import MultiAgentSearchAgent
from pacai.core.search.problem import SearchProblem
from pacai.core.actions import Actions


class ReflexAgent(BaseAgent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.
    You are welcome to change it in any way you see fit,
    so long as you don't touch the method headers.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        `ReflexAgent.getAction` chooses among the best options according to the evaluation function.

        Just like in the previous project, this method takes a
        `pacai.core.gamestate.AbstractGameState` and returns some value from
        `pacai.core.directions.Directions`.
        """

        # Collect legal moves.
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions.
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [
            index for index in range(len(scores)) if scores[index] == bestScore
        ]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best.

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current `pacai.bin.pacman.PacmanGameState`
        and an action, and returns a number, where higher numbers are better.
        Make sure to understand the range of different values before you combine them
        in your evaluation function.

        author: Simon Lee
        """

        successorGameState = currentGameState.generatePacmanSuccessor(action)

        # Useful information you can extract.
        # newPosition = successorGameState.getPacmanPosition()
        from pacai.core import distance

        def manhattan(position, problem):
            """
            This heuristic is the manhattan distance to the goal.
            """

            position1 = position
            position2 = problem

            return distance.manhattan(position1, position2)

        # *** Your Code Here ***
        # get successor positions
        # realized current position causes score to be really low
        newPosition = successorGameState.getPacmanPosition()
        newGhostStates = successorGameState.getGhostStates()
        score = successorGameState.getScore()

        # if you win the game return high score
        if successorGameState.isWin():
            score += 1e6

        # checks for if pacman stops. We want to avoid stopping so we subtract score
        # suggestion saw on Piazza from brian
        if action == "Stop":
            score -= 200

        # Calculate successor ghost distances
        for ghosts in newGhostStates:
            pos = ghosts.getPosition()
            ghost_dist = manhattan(newPosition, pos)

            # played around with this number and it drastically changes. 2 is best
            # meaning if they are 2 away to avoid at all costs
            if ghost_dist <= 2:
                score -= 500

        # Calculate food distances
        Food = successorGameState.getFood()
        foodList = Food.asList()
        for pos in foodList:
            food_dist = manhattan(newPosition, pos)
            score += float(
                1 / food_dist
            )  # inverse manhattan distance - Brian suggestion piazza

        return score


class MinimaxAgent(MultiAgentSearchAgent):
    """
    A minimax agent.

    Here are some method calls that might be useful when implementing minimax.

    `pacai.core.gamestate.AbstractGameState.getNumAgents()`:
    Get the total number of agents in the game

    `pacai.core.gamestate.AbstractGameState.getLegalActions`:
    Returns a list of legal actions for an agent.
    Pacman is always at index 0, and ghosts are >= 1.

    `pacai.core.gamestate.AbstractGameState.generateSuccessor`:
    Get the successor game state after an agent takes an action.

    `pacai.core.directions.Directions.STOP`:
    The stop direction, which is always legal, but you may not want to include in your search.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the minimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using
        `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
        and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.

        author: Simon Lee
        """

        def min_value(state, depth, player_num):
            """
            Took some inspiration from pseudocode from book and class

            author: Simon Lee
            """
            # initialize to really big number
            minVal = inf

            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)
            # get actions
            actions = state.getLegalActions(player_num)

            # iterate all ghosts then call max value to move pacman
            for succ in actions:
                # once index == 0 we know we need to move pacman
                if player_num == 0:
                    minVal = min(
                        minVal,
                        max_value(gameState.generateSuccessor(player_num, succ), depth),
                    )
                else:
                    # we want to subtract the index of the ghosts until it gets to 0 aka pacman
                    minVal = min(
                        minVal,
                        min_value(
                            gameState.generateSuccessor(player_num, succ),
                            depth,
                            player_num - 1,
                        ),
                    )
            return minVal

        def max_value(state, depth):
            """
            Took some inspiration from pseudocode from book and class

            **no loner need player_num parameter since pacman is the only one moving**

            author: Simon Lee
            """
            # intialize to very small number
            maxVal = -inf
            depth += 1
            num_ghosts = gameState.getNumAgents() - 1

            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)

            # get actions
            actions = state.getLegalActions(0)
            for succ in actions:
                maxVal = max(
                    maxVal,
                    min_value(gameState.generateSuccessor(0, succ), depth, num_ghosts),
                )

            return maxVal

        def minimax(gameState):
            """
            MAIN

            author: Simon lee
            """
            # run terminal test like pseudocode says
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(gameState)
            # get number of ghost agents
            num_ghosts = gameState.getNumAgents() - 1
            # intialize small score that will be replaces
            final_score = -inf
            actions = gameState.getLegalActions(0)
            for succ in actions:
                # call min value with the ghosts on the map
                score = min_value(
                    gameState.generateSuccessor(0, succ),
                    self.getTreeDepth(),
                    num_ghosts,
                )

                # return the highest value and that proceeding action
                if score > final_score:
                    final_score = score
                    final_action = succ
            return final_action

        return minimax(gameState)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    A minimax agent with alpha-beta pruning.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the minimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        """
        `pacai.agents.base.BaseAgent.getAction`:
        Returns the minimax action from the current gameState using
        `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
        and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.

        # code is very similar to minimax just add alpha and beta checking

        author: Simon Lee
        """

        def min_value(state, depth, player_num, alpha, beta):
            """
            copy pasted mini max then added alpha beta portion from lecture slides
            pseudocode

            author: Simon Lee
            """
            # initialize to really big number
            minVal = inf

            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)
            # get actions
            actions = state.getLegalActions(player_num)

            # iterate all ghosts then call max value to move pacman
            for succ in actions:
                # once index == 0 we know we need to move pacman
                if player_num == 0:
                    minVal = min(
                        minVal,
                        max_value(
                            gameState.generateSuccessor(player_num, succ),
                            depth,
                            alpha,
                            beta,
                        ),
                    )
                    # following pseudocode
                    if minVal <= alpha:
                        return minVal
                    beta = min(beta, minVal)
                else:
                    # we want to subtract the index of the ghosts until it gets to 0 aka pacman
                    minVal = min(
                        minVal,
                        min_value(
                            gameState.generateSuccessor(player_num),
                            depth,
                            player_num - 1,
                            alpha,
                            beta,
                        ),
                    )
                    # following pseudocode
                    if minVal <= alpha:
                        return minVal
                    beta = min(beta, minVal)
            return minVal

        def max_value(state, depth, alpha, beta):
            """
            copy pasted mini max then added alpha beta portion from lecture slides
            pseudocode

            **no loner need player_num parameter since pacman is the only one moving**

            author: Simon Lee
            """
            # intialize to very small number
            maxVal = -inf
            depth += 1
            num_ghosts = gameState.getNumAgents() - 1

            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)

            # get actions
            actions = state.getLegalActions(0)
            for succ in actions:
                maxVal = max(
                    maxVal,
                    min_value(
                        gameState.generateSuccessor(0, succ),
                        depth,
                        num_ghosts,
                        alpha,
                        beta,
                    ),
                )
                # following pseudocode
                if maxVal >= beta:
                    return maxVal
                alpha = max(alpha, maxVal)

            return maxVal

        def alphabetapruning(gameState):
            """
            MAIN

            author: Simon lee
            """
            # get number of ghost agents
            num_ghosts = gameState.getNumAgents() - 1

            # intialize small score that will be replaces
            # initialize alpha and beta values as well
            final_score = -inf
            alpha = -inf
            beta = inf
            actions = gameState.getLegalActions(0)
            for succ in actions:
                # call min value with the ghosts on the map
                score = min_value(
                    gameState.generateSuccessor(0, succ),
                    self.getTreeDepth(),
                    num_ghosts,
                    alpha,
                    beta,
                )

                # return the highest value and that proceeding action
                if score > final_score:
                    final_score = score
                    final_action = succ

                # final checker to return final actions
                if score > beta:
                    return final_action
                alpha = max(alpha, score)

            return final_action

        return alphabetapruning(gameState)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    An expectimax agent.

    All ghosts should be modeled as choosing uniformly at random from their legal moves.

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`:
    Returns the expectimax action from the current gameState using
    `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
    and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)

    def getAction(self, gameState):
        """
        `pacai.agents.base.BaseAgent.getAction`:
        Returns the expectimax action from the current gameState using
        `pacai.agents.search.multiagent.MultiAgentSearchAgent.getTreeDepth`
        and `pacai.agents.search.multiagent.MultiAgentSearchAgent.getEvaluationFunction`.

        author: Simon Lee
        """

        def exp_value(state, depth, player_num):
            """
            inspired by lecture notes. takes probabilities based on actions instead
            of a min.

            author: Simon Lee
            """
            # intialize expected value to 0
            exp_val = 0
            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)
            # get actions and probability
            actions = state.getLegalActions(player_num)
            actionCount = len(actions)
            probability = float(1.0 / actionCount)

            # iterate all ghosts then call max value to move pacman
            for succ in actions:
                # once index == 0 we know we need to move pacman
                if player_num == 0:
                    expected = max_value(
                        gameState.generateSuccessor(player_num, succ), depth
                    )
                else:
                    # we want to subtract the index of the ghosts until it gets to 0 aka pacman
                    expected = exp_value(
                        gameState.generateSuccessor(player_num, succ),
                        depth,
                        player_num - 1,
                    )

                # multiply expected value by probability
                exp_val += float(expected * probability)

            return exp_val

        def max_value(state, depth):
            """
            same max method as minimax

            **no loner need player_num parameter since pacman is the only one moving**

            author: Simon Lee
            """
            # intialize to very small number
            maxVal = -inf
            depth += 1
            num_ghosts = gameState.getNumAgents() - 1

            # run a terminal test to check if its terminal state
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(state)
            if depth == self.getTreeDepth():
                return self.getEvaluationFunction()(state)

            # get actions
            actions = state.getLegalActions(0)
            for succ in actions:
                maxVal = max(
                    maxVal,
                    exp_value(gameState.generateSuccessor(0, succ), depth, num_ghosts),
                )

            return maxVal

        def expectimax(gameState):
            """
            MAIN

            author: Simon lee
            """
            # run terminal test like pseudocode says
            if gameState.isWin() or gameState.isLose():
                return self.getEvaluationFunction()(gameState)
            # get number of ghost agents
            num_ghosts = gameState.getNumAgents() - 1
            # intialize small score that will be replaces
            final_score = -inf
            actions = gameState.getLegalActions(0)

            for succ in actions:
                # call expected value with the ghosts on the map
                score = exp_value(
                    gameState.generateSuccessor(0, succ),
                    self.getTreeDepth(),
                    num_ghosts,
                )

                # return the highest value and that proceeding action
                if score > final_score:
                    final_score = score
                    final_action = succ
            return final_action

        return expectimax(gameState)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable evaluation function.

    DESCRIPTION: similar to part 1 of the assignment since I cleared it with a score of 1000 or
    better, we take the maze distance. I took this approach from assignemnt 1 to get a more
    accurate distance. It runs kind of slow but when it does win averages a score of 900

    author: Simon Lee
    """
    # Need this for the maze method that I found in distance.py
    from pacai.student.search import breadthFirstSearch

    # a modified method from distance.py - finds distance of any two points using bfs
    def maze(position1, position2, gameState):
        """
        A modified version of maze method from pacai.core.distance.py
        """
        # sends new custom parameter which gets the map layout from our problem
        wall = gameState.getWalls()
        # calls the modified version of the PositionSearchProblem class
        # found this class in position.py and it is a needed class to make
        # the maze method work
        prob = PSP(wall, position1, position2)

        # calculates the distance using bfs
        return len(breadthFirstSearch(prob))

    # get successor positions
    # realized current position causes score to be really low
    newPosition = currentGameState.getPacmanPosition()
    newGhostStates = currentGameState.getGhostStates()
    score = currentGameState.getScore()

    # if you win the game return high score
    if currentGameState.isWin():
        score += 1e6

    # Calculate successor ghost distances
    for ghosts in newGhostStates:
        pos = ghosts.getPosition()
        ghost_dist = maze(newPosition, pos, currentGameState)
        # played around with this number and it drastically changes. 2 is best
        # meaning if they are 2 away to avoid at all costs
        if ghost_dist <= 2:
            score -= 5000

    # Calculate food distances
    Food = currentGameState.getFood()
    foodList = Food.asList()
    nearest_food = inf
    for pos in foodList:
        food_dist = maze(newPosition, pos, currentGameState)
        if food_dist < nearest_food:
            nearest_food = food_dist

    score += float(1 / nearest_food)  # inverse maze distance
    # we subtract the food count so pacman pick the state with less food left
    score -= len(foodList)

    # As doctsring suggests, we also take into account capsules
    # same lofic as food pretty much
    capsule = currentGameState.getCapsules()
    smallestCap = inf
    for cap in capsule:
        cap_dist = maze(newPosition, cap, currentGameState)
        if cap_dist < smallestCap:
            smallestCap = cap_dist

    # same logic as food
    score += float(1 / smallestCap)  # inverse maze distance

    return score


# Imported and slightly modified Position Search problem class #


class PSP(SearchProblem):
    """
    A modified version of the Position Search problem
    from pacai.core.search.position.py
    """

    def __init__(self, walls, goal, start):
        super().__init__()

        self.walls = walls
        self.goal = goal
        self.costFn = 1
        self.startState = start

    def startingState(self):
        return self.startState

    def isGoal(self, state):
        if state != self.goal:
            return False

        # Register the locations we have visited.
        # This allows the GUI to highlight them.
        self._visitedLocations.add(state)
        # Note: visit history requires coordinates not states. In this situation
        # they are equivalent.
        coordinates = state
        self._visitHistory.append(coordinates)

        return True

    def successorStates(self, state):
        """
        Returns successor states, the actions they require, and a constant cost of 1.
        """
        from pacai.core.directions import Directions

        successors = []

        for action in Directions.CARDINAL:
            x, y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)

            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = 1

                successors.append((nextState, action, cost))

        # Bookkeeping for display purposes (the highlight in the GUI).
        self._numExpanded += 1
        if state not in self._visitedLocations:
            self._visitedLocations.add(state)
            # Note: visit history requires coordinates not states. In this situation
            # they are equivalent.
            coordinates = state
            self._visitHistory.append(coordinates)

        return successors

    def actionsCost(self, actions):
        """
        Returns the cost of a particular sequence of actions.
        If those actions include an illegal move, return 999999.
        """

        if actions is None:
            return 999999

        x, y = self.startingState()
        cost = 0

        for action in actions:
            # Check figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999

            cost += self.costFn((x, y))

        return cost


# END OF IMPORTED CLASS #


class ContestAgent(MultiAgentSearchAgent):
    """
    Your agent for the mini-contest.

    You can use any method you want and search to any depth you want.
    Just remember that the mini-contest is timed, so you have to trade off speed and computation.

    Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
    just make a beeline straight towards Pacman (or away if they're scared!)

    Method to Implement:

    `pacai.agents.base.BaseAgent.getAction`
    """

    def __init__(self, index, **kwargs):
        super().__init__(index, **kwargs)
