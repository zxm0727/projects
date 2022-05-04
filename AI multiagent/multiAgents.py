# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import math
import sys

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]



        "*** YOUR CODE HERE ***"
        
        gState = list(newGhostStates)
        gDist = []
        minDist = sys.maxsize
        
        for i in range(len(newScaredTimes)):
            if newScaredTimes[i]==0:
                scaredG = gState[i]
                x_p , y_p = scaredG.getPosition()
                gDist += [manhattanDistance((x_p, y_p), newPos)]

        if len(gDist):
            minDist = min(gDist)
        food = currentGameState.getFood()
        foodList = food.asList()
        foodDist = []
        for cur in foodList:
            foodDist += [manhattanDistance(cur ,newPos)]

        if len(foodDist):
            minFoodDist = min(foodDist)

        if minDist == 0:
            return -sys.maxsize-1

        if minFoodDist == 0:
            return sys.maxsize

        return 1/(minFoodDist) - 2/(minDist)
        

        

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        res = self.max(gameState,self.depth)
        
        return res[1]

    #Max value function
    def max(self, gameState, depth):
        ##Win, lost return none
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        best = Directions.STOP
        value = -sys.maxsize-1
        for cur in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, cur)
            res = self.min(successor,1, depth)
            if res[0] > value:
                value = res[0]
                best = cur
        return (value,best)

    #Min Value function
    def min(self, gameState, idx, depth):
        if  depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        value = sys.maxsize
        if idx == gameState.getNumAgents()-1:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.max(successor, depth - 1)
                if res[0] < value:
                    value = res[0]
                    best = cur
        else:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.min(successor, idx + 1, depth)
                if res[0] < value:
                    value = res[0]
                    best = cur
        return (value, best)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        res = self.max(gameState, self.depth, -sys.maxsize-1, sys.maxsize)

        return res[1]

    ##Similar way but we include alpha and beta this time
    def max(self, gameState, depth, a, b):
        ##Win, lose return none
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        best = Directions.STOP
        value = -sys.maxsize-1
        for cur in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, cur)
            res = self.min(successor, 1, depth, a, b)
            if res[0] > value:
                value = res[0]
                best = cur
            
            ## Compare beta with the value
            if value > b:
                return (value, best)

            ## Update alpha
            a = max(a, value)
        return (value,best)

    def min(self, gameState, idx, depth, a, b):
        if  depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        value = sys.maxsize
        last = gameState.getNumAgents() - 1
        if idx == last:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.max(successor, depth - 1, a, b)
                if res[0] < value:
                    value = res[0]
                    best = cur
                ## Compare beta with the value
                if value < a:
                    return (value, best)

                ## Update alpha
                b = min(b, value)
        else:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.min(successor, idx + 1, depth, a, b)
                if res[0] < value:
                    value = res[0]
                    best = cur
                ## Compare beta with the value
                if value < a:
                    return (value, best)

                ## Update alpha
                b = min(b, value)
        return (value, best)


        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        res = self.max(gameState,self.depth)
        
        return res[1]

    #Max value function (Same as the q2)
    def max(self, gameState, depth):
        ##Win, lost return none
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        best = Directions.STOP
        value = -sys.maxsize-1
        for cur in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, cur)
            res = self.expect(successor,1, depth)
            if res[0] > value:
                value = res[0]
                best = cur
        return (value,best)

    def expect(self, gameState, idx, depth):
        ##Win, lost return none
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return (self.evaluationFunction(gameState), None)
        best = Directions.STOP
        value = -sys.maxsize-1
        ## initalize sum and count for calculate average
        count = 0
        sum = 0

        # initalize average
        average = 0

        last = gameState.getNumAgents() - 1
        if idx == last:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.max(successor, depth - 1)
                count += 1
                sum += res[0]
            ## Not empty then calculates
            if count != 0:
                average = sum / count
            best = res[1]
        ## Not last
        else:
            for cur in gameState.getLegalActions(idx):
                successor = gameState.generateSuccessor(idx, cur)
                res = self.expect(successor, idx + 1, depth)
                count += 1
                sum += res[0]
            ## Not empty then calculate
            if count != 0:
                average = sum / count
            best = res[1]

        return (average, best)

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
