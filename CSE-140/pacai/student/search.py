"""
In this file, you will implement generic search algorithms which are called by Pacman agents.
"""


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    ```
    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    ```

    #(5,6)
    #(12,12)
    #[(6,6), WEST, 1), (5,5), EAST, 1)

    # Author: Simon Lee
    """
    # follows the general tree search format from the lecture 2 slides and textbook 4th edition
    from pacai.util.stack import Stack

    # construct a stack object and initialize empty final path as well as visited states
    # the fringe for dfs is a stack
    stack = Stack()
    visited = []
    final_path = []

    # if the start is also the end, return no path
    if problem.isGoal(problem.startingState()):
        return final_path

    # push the current starting state in path. Stakcs are LIFO
    stack.push((problem.startingState(), final_path))

    # run DFS
    while not stack.isEmpty():
        # gets the coordinate (x,y) as well as the direction which pacman goes
        # (North,South,East,West) and appends the coordinate
        pos, final_path = stack.pop()
        visited.append(pos)

        # if they hit the food then return path it took to the food
        if problem.isGoal(pos):
            return final_path

        # gets the next possible state: options in the form of [(x,y), direction, state movement]
        next = problem.successorStates(pos)

        # if there is a next possible state push the next location and keep running dfs
        if next:
            for feature in next:
                # for readability purposes
                coord = feature[0]
                direction = feature[1]

                # DFS
                if coord not in visited:
                    newPath = final_path + [direction]
                    stack.push((coord, newPath))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """
    # follows the general tree search format from the lecture 2 slides and textbook 4th edition
    # construct a queue object and initialize empty final path as well as visited states

    # Author: Simon Lee
    from pacai.util.queue import Queue

    # the fringe for bfs is a queue
    queue = Queue()
    visited = []
    final_path = []

    # if the start is also the end, return no path
    if problem.isGoal(problem.startingState()):
        return final_path

    # push the current starting state in path. Queues are FIFO
    queue.push((problem.startingState(), final_path))

    # run BFS
    while not queue.isEmpty():
        # gets the coordinate (x,y) as well as the direction which pacman goes
        #  (North,South,East,West) and appends the coordinate
        pos, final_path = queue.pop()
        # print(pos)
        visited.append(pos)

        # if they hit the food then return path it took to the food
        if problem.isGoal(pos):
            return final_path

        # gets the next possible state: options in the form of [(x,y), direction, state movement]
        next = problem.successorStates(pos)
        # print("\n")
        # print(next)

        # if there is a next possible state push the next location and keep running dfs
        if next:
            for feature in next:
                # for readability purposes
                coord = feature[0]
                direction = feature[1]

                # BFS
                if coord not in visited:
                    newPath = final_path + [direction]
                    queue.push((coord, newPath))


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.

    # Author: Simon Lee
    """

    from pacai.util.priorityQueue import PriorityQueue

    # the fringe for ucs is a priority queue
    pq = PriorityQueue()
    visited = []
    final_path = []

    # if the start is also the end, return no path
    if problem.isGoal(problem.startingState()):
        return final_path

    # push the current starting state in path
    pq.push((problem.startingState(), final_path, 0), 0)

    # run UCS
    while not pq.isEmpty():
        # gets the coordinate (x,y) as well as the direction which pacman goes
        # and appends the coordinate. Also gets cost and orders bc it is a pq
        pos, final_path, cost = pq.pop()
        visited.append(pos)

        # if they hit the food then return path it took to the food
        if problem.isGoal(pos):
            return final_path

        # gets the next possible state: options in the form of [(x,y), direction, state movement]
        next = problem.successorStates(pos)

        # if there is a next possible state push the next location and keep running dfs
        if next:
            for feature in next:

                # for readability purposes
                coord = feature[0]
                direction = feature[1]
                cost2 = feature[2]

                # UCS
                if coord not in visited:
                    newPath = final_path + [direction]
                    fcost = (
                        cost + cost2
                    )  # gets path cost which is how UCS expands its search
                    pq.push((coord, newPath, fcost), fcost)


def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.

    # Author: Simon Lee
    """
    from pacai.util.priorityQueue import PriorityQueue

    # the fringe for A* is a priority queue
    pq = PriorityQueue()
    visited = []
    final_path = []

    # if the start is also the end, return no path
    if problem.isGoal(problem.startingState()):
        return final_path

    # push the current starting state in path
    pq.push((problem.startingState(), final_path, 0), 0)

    # run UCS
    while not pq.isEmpty():
        # gets the coordinate (x,y) as well as the direction which pacman goes.
        # and appends the coordinate. Also gets cost and orders bc it is a pq
        pos, final_path, cost = pq.pop()
        visited.append(pos)

        # if they hit the food then return path it took to the food
        if problem.isGoal(pos):
            return final_path

        # gets the next possible state: options in the form of [(x,y), direction, state movement]
        next = problem.successorStates(pos)

        # if there is a next possible state push the next location and keep running dfs
        if next:
            for feature in next:

                # for readability purposes
                coord = feature[0]
                direction = feature[1]
                cost2 = feature[2]

                # A* search
                if coord not in visited:
                    newPath = final_path + [direction]
                    fcost = cost + cost2
                    # A* introduces the heuristic which improves search capabilities
                    heuristic_cost = fcost + heuristic(coord, problem)
                    pq.push((coord, newPath, fcost), heuristic_cost)
