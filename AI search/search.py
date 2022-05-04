# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

# stack, queue, and pQue used


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    from util import Stack
    # path to return
    path = []
    # by stack order out
    stack = Stack()
    # set of the visited node (no duplicates)
    visit = set()
    start = problem.getStartState()
    stack.push((path, start))
    while not stack.isEmpty():
        # pop out
        path, cur = stack.pop()
        # check if it is finished, finished -> return
        if problem.isGoalState(cur):
            return path
        
        # if visited, next one
        if cur in visit:
            continue
        
        #add the current in the visited nodes, doesnt matter if it is in the set
        visit.add(cur)
        # next
        next = problem.getSuccessors(cur)
        for state, n_path, cost in next:
            cur = ((path + [n_path]), state)
            stack.push(cur)
    return path




    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # queue order instead of stack
    from util import Queue
    que = Queue()
    path = []
    # set of the visited node (no duplicates)
    visit = set()
    start = problem.getStartState()
    que.push(( path, start))
    while not que.isEmpty():
        # pop out
        path , cur= que.pop()
        # check if it is finished, finished -> return
        if problem.isGoalState(cur):
            return path
        
        # if visited, next one
        if cur in visit:
            continue
        
        #add the current in the visited nodes, doesnt matter if it is in the set
        visit.add(cur)
        # next
        next = problem.getSuccessors(cur)
        # cost doesnt need again
        for state, n_path, cost in next:
            new = ((path + [n_path]), state)
            que.push(new)
        
    return path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # pQue order instead of normal queue
    from util import PriorityQueue
    que = PriorityQueue()
    path = []
    # set of the visited node (no duplicates)
    visit = set()
    start = problem.getStartState()
    cost = 0
    node = ( start, path, cost)
    que.push(node, cost)
    while not que.isEmpty():
        # pop out, cost needed this time
        cur, path,cost= que.pop()
        # check if it is finished, finished -> return
        if problem.isGoalState(cur):
            return path
        
        # if visited, next one
        if cur in visit:
            continue
        
        #add the current in the visited nodes, doesnt matter if it is in the set
        visit.add(cur)
        # next
        for state, n_path, ncost in problem.getSuccessors(cur):
            node = (state, path + [n_path], cost + ncost)
            que.update(node, cost + ncost)
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # pQue order instead of normal queue
    from util import PriorityQueue
    que = PriorityQueue()
    path = []
    # set of the visited node (no duplicates)
    visit = set()
    start = problem.getStartState()
    cost = 0
    node = (start, path, cost)
    que.push(node, cost)
    while not que.isEmpty():
        # pop out, cost needed this time
        cur, path, cost= que.pop()
        # check if it is finished, finished -> return
        if problem.isGoalState(cur):
            return path
        
        # if visited, next one
        if cur in visit:
            continue
        
        #add the current in the visited nodes, doesnt matter if it is in the set
        visit.add(cur)
        # next
        for state, n_path, ncost in problem.getSuccessors(cur):
            ncost = cost + ncost
            n_path = path + [n_path]
            node = (state, n_path, ncost)
            a_cost = problem.getCostOfActions(n_path) + heuristic(state, problem)
            que.update(node, a_cost)

    return path



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
