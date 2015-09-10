from Queue import PriorityQueue

def aStar(initialState, heuristic):
    visited = []
    fringe = PriorityQueue()
    fringe.put((-(initialState.score - heuristic(initialState)), initialState))

    while True:
        if fringe.empty():
            print "No Solution"
            return None


        nextState = fringe.get()[1]
        print "checking for position " + str(nextState.posX) + ", " + str(nextState.posY) + " at cost " + str(nextState.score)

        if nextState.isGoalState():
            return nextState.actionList
        else:
            for successorState in nextState.getSuccessors():
                print "adding state with score " + str(successorState.score)
                fringe.put((-(successorState.score - heuristic(successorState)), successorState))

            for elem in list(fringe.queue):
                print(elem[0]),
            print ""

def zeroHeuristic(state):
    """0: Returns 0."""
    return 0

def minHeuristic(state):
    xdiff, ydiff = goalDiff(state)
    return min(xdiff, ydiff)

def maxHeuristic(state):
    xdiff, ydiff = goalDiff(state)
    return max(xdiff, ydiff)

def addHeuristic(state):
    xdiff, ydiff = goalDiff(state)
    return xdiff + ydiff

def admissibleHeuristic(state):
    x, y, z = state.getNextValues();
    return addHeuristic(state) - 1 + min(x, y, z)
    
def nonAdmissibleHeuristic(state):
    """6: multiply #5 * 3."""
    return admissibelHeuristic(state)*3

def goalDiff(state):
    """Helper for returning distance to goal."""
    xdiff = abs(state.goalX - state.posX)
    ydiff = abs(state.goalY - state.posY)
    return (xdiff, ydiff)
