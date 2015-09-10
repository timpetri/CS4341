from Queue import PriorityQueue

def aStar(initialState, heuristic):
    visited = []
    fringe = PriorityQueue()
    fringe.put(initialState, -(initialState.score - heuristic(initialState)))

    while True:
        if fringe.empty():
            print "No Solution"
            return None

        nextState = fringe.get()

        if nextState.isGoalState():
            return nextState.seqActions()
        else:
            for successorState in nextState.getSuccessors():
                fringe.put(-(nextState.score - heuristic(successorState)), successorState)


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
