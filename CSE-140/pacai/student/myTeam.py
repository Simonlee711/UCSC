"""
This game is not a marathon. Its a race.
"""
import logging
import random
import time
from pacai.util import reflection
from pacai.agents.capture.capture import CaptureAgent
import random
from pacai.util import util
from pacai.core.actions import Directions


def createTeam(
    firstIndex,
    secondIndex,
    isRed,
    #first="pacai.student.myTeam.ParringtonLockdownAgent",
    first="pacai.student.myTeam.ParringtonAttackAgent",
    second="pacai.student.myTeam.ParringtonLockdownAgent",
    #second ="pacai.student.myTeam.ParringtonAttackAgent",
):
    """
    This function should return a list of two agents that will form the capture team,
    initialized using firstIndex and secondIndex as their agent indexed.
    isRed is True if the red team is being created,
    and will be False if the blue team is being created.
    """

    firstAgent = reflection.qualifiedImport(first)
    secondAgent = reflection.qualifiedImport(second)

    return [
        firstAgent(firstIndex),
        secondAgent(secondIndex),
    ]


class ParringtonAttackAgent(CaptureAgent):
    """
    The offensive agent:
    We are simply improving the Offensive and Defensive agents from the codebase
    authors: Simon Lee, Tuan Ngyuen, Harlene Virk
    """

    def __init__(self, index):
        self.index = index
        self.features = {}
        self.weights = {}
        self.epsilon = 0.03
        self.observationHistory = []

    def chooseAction(self, gameState):
        """
        Picks among the actions with the highest return from `ReflexCaptureAgent.evaluate`.
        """

        actions = gameState.getLegalActions(self.index)

        start = time.time()
        values = [self.evaluate(gameState, a) for a in actions]
        logging.debug(
            "evaluate() time for agent %d: %.4f" % (self.index, time.time() - start)
        )

        maxValue = max(values)
        bestActions = [a for a, v in zip(actions, values) if v == maxValue]

        return random.choice(bestActions)

    def getSuccessor(self, gameState, action):
        """
        Finds the next successor which is a grid position (location tuple).
        """

        successor = gameState.generateSuccessor(self.index, action)
        pos = successor.getAgentState(self.index).getPosition()

        if pos != util.nearestPoint(pos):
            # Only half a grid position was covered.
            return successor.generateSuccessor(self.index, action)
        else:
            return successor

    def evaluate(self, gameState, action):
        """
        Computes a linear combination of features and feature weights.
        """

        features = self.getFeatures(gameState, action)
        weights = self.getWeights(gameState, action)
        stateEval = sum(features[feature] * weights[feature] for feature in features)

        return stateEval

    def getFeatures(self, gameState, action):
        self.start = gameState.getAgentPosition(self.index)
        features = {}
        successor = self.getSuccessor(gameState, action)
        features["successorScore"] = self.getScore(successor)

        # gets food tuples and length of foods left as well as walls
        foodList = self.getFood(successor).asList()
        foodleft = len(foodList)
        enemyFood = self.getFoodYouAreDefending(successor).asList()

        # Enemy locations
        enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
        invaders = [a for a in enemies if a.isPacman() and a.getPosition() is not None]
        EnemyDefenders = [
            a for a in enemies if not a.isPacman() and a.getPosition() is not None
        ]
        EnemyGhostscared = [
            a
            for a in enemies
            if not a.isPacman()
            and a.getPosition() is not None
            and a.getScaredTimer() > 0
        ]

        # This calculates the nearest food but if food left is lower than 3 it plays defense
        if foodleft > 0:
            myPos = successor.getAgentState(self.index).getPosition()
            minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
            features["distanceToFood"] = minDistance 
            features["foodLeft"] = len(enemyFood) 
            # if our features of food left is less than equal to 3, we have to play defense
            
            if features["foodLeft"] <= 5:
                # our agent becomes defensive and strictly looks for enemies and kills them
                avoidmin = 999999
                for enemy in invaders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                if avoidmin == 999999:
                    avoidmin = 0
                # we return a big number to ensure that the importance of chasing is amplified
                features["chaseEnemy"] = avoidmin 
                features["invaderDistance"] = avoidmin 
            

        # Also calculates capsules
        # Exact same logic as food left
        # when capsules are eaten we have to eat enemies
        capsules = self.getCapsules(gameState)
        capsulesLeft = len(capsules)
        if capsulesLeft > 0:
            minDistance = min(
                [self.getMazeDistance(myPos, capsule) for capsule in capsules]
            )
            if minDistance == 0:
                minDistance = -100
            features["distanceToCapsules"] = minDistance * 2
            features["capsulesLeft"] = len(capsules)
            if features["capsulesLeft"] == 0:
                avoidmin = 999999
                for enemy in EnemyDefenders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                minval = avoidmin
                if avoidmin == 999999:
                    minval = 0
                # if the enemy is close to the user after we have ran out of pellets
                if minval <= 3:
                    # avoid ghosts
                    features["ghostInBound"] = -1

        # eats enemy's that are in the vaccinity
        if not successor.getAgentState(self.index).isPacman():
            avoidmin = 999999
            for enemy in invaders:
                dist = self.getMazeDistance(myPos, enemy.getPosition())
                avoidmin = min(avoidmin, dist)
            finDist = avoidmin
            if avoidmin == 999999:
                finDist = 0
            if finDist <= 8 and avoidmin != 999999:
                features["chaseEnemy"] = (finDist) * 15
                features["invaderDistance"] = finDist 

        # Similarly to assignment 2, we want our agents to avoid stopping
        if action == Directions.STOP:
            features["stop"] = 1

        # How to avoid defenders on the other team
        if successor.getAgentState(self.index).isPacman():
            avoidMin = 999999
            for enemy in EnemyDefenders:
                dist = self.getMazeDistance(myPos, enemy.getPosition())
                avoidMin = min(avoidMin, dist)
            minVal = avoidMin
            if avoidMin == 999999:
                minVal = 0
            if minVal <= 1 and avoidMin != 999999:
                # a high score to avoid the ghosts
                features["ghostInBound"] = -15
                features["distanceToFood"] = 100

        # if ghost is scared, we tell pacman to eat it
        # when scared if ghosts are near we prioritize eating them
        # else we just get food

        # !!! PACMAN eats scared ghost !!!
        for enemy in invaders:
            if enemy.getScaredTimer() > 0:
                minfoodDistance = min(
                    [self.getMazeDistance(myPos, food) for food in foodList]
                )
                features["distanceToFood"] = minfoodDistance * 100
                features["ghostInBound"] = 15
            else:
                break


        return features

    def getWeights(self, gameState, action):
        # negative numbers is stuff we want them to do
        # positive numbers mean we dont want them to do
        # i.e. 'stop': 999999 then our agent will stop
        return {
            "successorScore": 100,
            "distanceToFood": -1,
            "chaseEnemy": 1,
            "distanceToCapsules": -1,
            "capsulesLeft": 10,
            "ghostInBound": 10,
            "foodLeft": -100,
            "stop": -999,
            "abort": -1,
            "invaderDistance": -100,
        }


class ParringtonLockdownAgent(CaptureAgent):
    """
    The defensive agent
    authors: Simon Lee, Tuan Ngyuen, Harlene Virk
    """
    '''
    def __init__(self, index):
        self.index = index
        self.features = {}
        self.weights = {}
        self.observationHistory = []
    def chooseAction(self, gameState):
        """
        Picks among the actions with the highest return from `ReflexCaptureAgent.evaluate`.
        """
        actions = gameState.getLegalActions(self.index)
        start = time.time()
        values = [self.evaluate(gameState, a) for a in actions]
        logging.debug(
            "evaluate() time for agent %d: %.4f" % (self.index, time.time() - start)
        )
        maxValue = max(values)
        bestActions = [a for a, v in zip(actions, values) if v == maxValue]
        return random.choice(bestActions)
    def getSuccessor(self, gameState, action):
        """
        Finds the next successor which is a grid position (location tuple).
        """
        successor = gameState.generateSuccessor(self.index, action)
        pos = successor.getAgentState(self.index).getPosition()
        if pos != util.nearestPoint(pos):
            # Only half a grid position was covered.
            return successor.generateSuccessor(self.index, action)
        else:
            return successor
    def evaluate(self, gameState, action):
        """
        Computes a linear combination of features and feature weights.
        """
        features = self.getFeatures(gameState, action)
        weights = self.getWeights(gameState, action)
        stateEval = sum(features[feature] * weights[feature] for feature in features)
        return stateEval
    def getFeatures(self, gameState, action):
        features = {}
        successor = self.getSuccessor(gameState, action)
        features["successorScore"] = self.getScore(successor)
        # gets food tuples and length of foods left as well as walls
        foodList = self.getFood(successor).asList()
        foodleft = len(foodList)
        enemyFood = self.getFoodYouAreDefending(successor).asList()
        # Enemy locations
        enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
        invaders = [a for a in enemies if a.isPacman() and a.getPosition() is not None]
        EnemyDefenders = [
            a for a in enemies if not a.isPacman() and a.getPosition() is not None
        ]
        # This calculates the nearest food but if food left is lower than 3 it plays defense
        if foodleft > 0:
            myPos = successor.getAgentState(self.index).getPosition()
            minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
            features["distanceToFood"] = minDistance
            features["foodLeft"] = len(enemyFood)
            # if our features of food left is less than equal to 3, we have to play defense
            if features["foodLeft"] <= 7:
                # our agent becomes defensive and strictly looks for enemies and kills them
                avoidmin = 999999
                for enemy in invaders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                if avoidmin == 999999:
                    avoidmin = 0
                # we return a big number to ensure that the importance of chasing is amplified
                features["chaseEnemy"] = avoidmin * 100 + 1
                features["invaderDistance"] = avoidmin * 2.5
        # if we have collected the majority of the food one of our agents can be strictly defense
        if foodleft < 6:
            dists = [self.getMazeDistance(myPos, a.getPosition()) for a in invaders]
            features["invaderDistance"] = min(dists, default=0) * 2.5
            features["chaseEnemy"] = min(dists, default=0) * 100 + 1
        # Also calculates capsules
        # Exact same logic as food left
        # when capsules are eaten we have to eat enemies
        capsules = self.getCapsules(gameState)
        capsulesLeft = len(capsules)
        if capsulesLeft > 0:
            minDistance = min(
                [self.getMazeDistance(myPos, capsule) for capsule in capsules]
            )
            if minDistance == 0:
                minDistance = -100
            features["distanceToCapsules"] = minDistance
            features["capsulesLeft"] = len(capsules)
            if features["capsulesLeft"] == 0:
                avoidmin = 999999
                for enemy in EnemyDefenders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                minval = avoidmin
                if avoidmin == 999999:
                    minval = 0
                # if the enemy is close to the user after we have ran out of pellets
                if minval <= 2:
                    # avoid ghosts
                    features["ghostInBound"] = avoidmin
                    #features["distanceToFood"] *= 10 
                    # features['distanceToBadGuy'] = -99999
        # calculates enemy distance - stolen from defense.py
        if len(invaders) > 0:
            dists = [self.getMazeDistance(myPos, a.getPosition()) for a in invaders]
            features["invaderDistance"] = min(dists)
        # Similarly to assignment 2, we want our agents to avoid stopping
        if action == Directions.STOP:
            features["stop"] = 1
        # How to avoid defenders on the other team
        if successor.getAgentState(self.index).isPacman():
            avoidMin = 999999
            for enemy in EnemyDefenders:
                dist = self.getMazeDistance(myPos, enemy.getPosition())
                avoidMin = min(avoidMin, dist)
            minVal = avoidMin
            if avoidMin == 999999:
                minVal = 0
            if minVal <= 2:
                # a high score to avoid the ghosts
                features["ghostInBound"] = -100
                features["distanceToFood"] *= 10
        # reverse direction - stolen from the defense.py
        rev = Directions.REVERSE[gameState.getAgentState(self.index).getDirection()]
        if action == rev:
            features["reverse"] = 1
        if successor.getAgentState(self.index).isPacman():
            for enemy in invaders:
                if enemy.getScaredTimer() > 0:
                    minfoodDistance = min(
                        [self.getMazeDistance(myPos, food) for food in foodList]
                    )
                    features["distanceToFood"] = minfoodDistance * 1000
                else:
                    break
        return features
    def getWeights(self, gameState, action):
        return {
            "successorScore": 100,
            "distanceToFood": -1,
            "chaseEnemy": 20,
            "distanceToCapsules": -1,
            "capsulesLeft": 15,
            "ghostInBound": 2,
            "foodLeft": -10,
            "stop": -999,
            "invaderDistance": -100,
            "reverse": -1,
        }
    '''
    def __init__(self, index):
        self.index = index
        self.features = {}
        self.weights = {}
        self.epsilon = 0.03
        self.observationHistory = []

    def chooseAction(self, gameState):
        """
        Picks among the actions with the highest return from `ReflexCaptureAgent.evaluate`.
        """

        actions = gameState.getLegalActions(self.index)

        start = time.time()
        values = [self.evaluate(gameState, a) for a in actions]
        logging.debug(
            "evaluate() time for agent %d: %.4f" % (self.index, time.time() - start)
        )

        maxValue = max(values)
        bestActions = [a for a, v in zip(actions, values) if v == maxValue]

        return random.choice(bestActions)

    def getSuccessor(self, gameState, action):
        """
        Finds the next successor which is a grid position (location tuple).
        """

        successor = gameState.generateSuccessor(self.index, action)
        pos = successor.getAgentState(self.index).getPosition()

        if pos != util.nearestPoint(pos):
            # Only half a grid position was covered.
            return successor.generateSuccessor(self.index, action)
        else:
            return successor

    def evaluate(self, gameState, action):
        """
        Computes a linear combination of features and feature weights.
        """

        features = self.getFeatures(gameState, action)
        weights = self.getWeights(gameState, action)
        stateEval = sum(features[feature] * weights[feature] for feature in features)

        return stateEval

    def getFeatures(self, gameState, action):
        self.start = gameState.getAgentPosition(self.index)
        features = {}
        successor = self.getSuccessor(gameState, action)
        features["successorScore"] = self.getScore(successor)

        # gets food tuples and length of foods left as well as walls
        foodList = self.getFood(successor).asList()
        foodleft = len(foodList)
        enemyFood = self.getFoodYouAreDefending(successor).asList()

        # Enemy locations
        enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
        invaders = [a for a in enemies if a.isPacman() and a.getPosition() is not None]
        EnemyDefenders = [
            a for a in enemies if not a.isPacman() and a.getPosition() is not None
        ]
        EnemyGhostscared = [
            a
            for a in enemies
            if not a.isPacman()
            and a.getPosition() is not None
            and a.getScaredTimer() > 0
        ]

        # This calculates the nearest food but if food left is lower than 3 it plays defense
        if foodleft > 0:
            myPos = successor.getAgentState(self.index).getPosition()
            minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
            features["distanceToFood"] = minDistance * 10
            features["foodLeft"] = len(enemyFood) * 10
            # if our features of food left is less than equal to 3, we have to play defense
            if features["foodLeft"] <= 10:
                # our agent becomes defensive and strictly looks for enemies and kills them
                avoidmin = 999999
                for enemy in invaders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                if avoidmin == 999999:
                    avoidmin = 0
                # we return a big number to ensure that the importance of chasing is amplified
                features["chaseEnemy"] = avoidmin * 150
                features["invaderDistance"] = avoidmin * 4
                if not successor.getAgentState(self.index).isPacman():
                    features['defenderOnly'] = -100

        # Also calculates capsules
        # Exact same logic as food left
        # when capsules are eaten we have to eat enemies
        capsules = self.getCapsules(gameState)
        capsulesLeft = len(capsules)
        if capsulesLeft > 0:
            minDistance = min(
                [self.getMazeDistance(myPos, capsule) for capsule in capsules]
            )
            if minDistance == 0:
                minDistance = -100
            features["distanceToCapsules"] = minDistance
            features["capsulesLeft"] = len(capsules)
            if features["capsulesLeft"] == 0:
                avoidmin = 999999
                for enemy in EnemyDefenders:
                    dist = self.getMazeDistance(myPos, enemy.getPosition())
                    avoidmin = min(avoidmin, dist)
                minval = avoidmin
                if avoidmin == 999999:
                    minval = 0
                # if the enemy is close to the user after we have ran out of pellets
                if minval <= 3:
                    # avoid ghosts
                    features["ghostInBound"] = -50

        # eats enemy's that are in the vaccinity
        avoidmin = 999999
        for enemy in invaders:
            dist = self.getMazeDistance(myPos, enemy.getPosition())
            avoidmin = min(avoidmin, dist)
        finDist = avoidmin
        if avoidmin == 999999:
            finDist = 0
        if finDist <= 10 and avoidmin != 999999:
            features["chaseEnemy"] = (finDist) * 150
            features["invaderDistance"] = finDist * 2

        # Similarly to assignment 2, we want our agents to avoid stopping
        if action == Directions.STOP:
            features["stop"] = 1

        # How to avoid defenders on the other team
        if successor.getAgentState(self.index).isPacman():
            avoidMin = 999999
            for enemy in EnemyDefenders:
                dist = self.getMazeDistance(myPos, enemy.getPosition())
                avoidMin = min(avoidMin, dist)
            minVal = avoidMin
            if avoidMin == 999999:
                minVal = 0
            if minVal <= 2 and avoidMin != 999999:
                # a high score to avoid the ghosts
                features["ghostInBound"] = -99
                features["distanceToFood"] *= 10

        # if ghost is scared, we tell pacman to eat it
        # when scared if ghosts are near we prioritize eating them
        # else we just get food

        # !!! PACMAN eats scared ghost !!!
        for enemy in invaders:
            if enemy.getScaredTimer() > 0:
                minfoodDistance = min(
                    [self.getMazeDistance(myPos, food) for food in foodList]
                )
                features["distanceToFood"] = minfoodDistance * 100
                features["ghostInBound"] = 50
            else:
                break


        return features

    def getWeights(self, gameState, action):
        # negative numbers is stuff we want them to do
        # positive numbers mean we dont want them to do
        # i.e. 'stop': 999999 then our agent will stop
        return {
            "successorScore": 100,
            "distanceToFood": -1,
            "chaseEnemy": 1,
            "distanceToCapsules": -1,
            "capsulesLeft": 10,
            "ghostInBound": 10,
            "foodLeft": -100,
            "stop": -999,
            "abort": -1,
            "invaderDistance": -100,
            'defenderOnly': 1
        }