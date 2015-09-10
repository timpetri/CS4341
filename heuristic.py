#import Queue.Priority


def aStar(initialState, heuristic):
    visited = []
    fringe = util.PriorityQueue()
    fringe.push(initialState, -(initialState.getScore() - heuristic(initialState)))

    while True:
        if fringe.isEmpty():
            print "No Solution"
            return None

        nextState = fringe.pop()

        if nextState.isGoalState():
            return nextState.seqActions()
        else:
            for successorState in nextState.getSuccessors():
                fringe.push(successorState, -(nextState.getScore() - heuristic(successorState)))


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
