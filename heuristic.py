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
                #print "adding state with score " + str(successorState.score)
                fringe.put((-(successorState.score - heuristic(successorState)), successorState))

            """for elem in list(fringe.queue):
                print(elem[0]),
            print ""
            """

def zeroHeuristic(state):
    """0: Returns 0."""
    return 0

def minHeuristic(state):
    xdiff, ydiff = absGoalDiff(state)
    return min(xdiff, ydiff)

def maxHeuristic(state):
    xdiff, ydiff = absGoalDiff(state)
    return max(xdiff, ydiff)

def addHeuristic(state):
    xdiff, ydiff = absGoalDiff(state)
    return xdiff + ydiff

def admissibleHeuristic(state):
    xdiff, ydiff = goalDiff(state)

    turnCost = 0

    if state.direction is state.north:
        if xdiff is not 0:
            turnCost +=1
        if ydiff > 0:
            turnCost += 2

    if state.direction is state.east:
        if xdiff < 0:
            turnCost += 2
        if ydiff is not 0:
            turnCost +=1

    if state.direction is state.south:
        if xdiff is not 0:
            turnCost +=1
        if ydiff < 0:
            turnCost += 2

    if state.direction is state.west:
        if xdiff > 0:
            turnCost += 2
        if ydiff is not 0:
            turnCost +=1

    return addHeuristic(state) + turnCost
    
def nonAdmissibleHeuristic(state):
    """6: multiply #5 * 3."""
    return admissibleHeuristic(state)*3

def absGoalDiff(state):
    xdiff, ydiff = goalDiff(state)
    return (abs(xdiff), abs(ydiff))

def goalDiff(state):
    """Helper for returning distance to goal."""
    xdiff = state.goalX - state.posX
    ydiff = state.goalY - state.posY
    return (xdiff, ydiff)