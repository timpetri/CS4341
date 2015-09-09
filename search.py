#import Queue.PriorityQueue


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    fringe = util.PriorityQueue()
    fringe.push(    (problem.getStartState(), list()), 
                    problem.getCostOfActions([]) + heuristic(problem.getStartState(), problem))

    while True:
        if fringe.isEmpty():
            print "\tFringe empty: FAILURE"
            return None

        nextState, listActions = fringe.pop()

        if problem.isGoalState(nextState):
            #print "SUCCESS"
            return listActions
        elif nextState not in visited:
            #print "\tExplore nextState"
            visited.append(nextState)
            for childState, childAction, cost in problem.getSuccessors(nextState):
                fringe.push(    (childState, myListAppend(list(listActions), childAction)), 
                                problem.getCostOfActions(myListAppend(list(listActions), childAction)) 
                                                        + heuristic(childState, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
