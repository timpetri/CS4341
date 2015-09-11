from Queue import PriorityQueue

def aStar(initialState, heuristic):
    #stores a list of visited coords, the direction and whether the tile was affected by demolish
    visited = []
    fringe = PriorityQueue()

    #add the start node to the fringe
    fringe.put((-(initialState.score - heuristic(initialState)), initialState))

    while True:

        if fringe.empty():
            print "No Solution"
            return None

        nextState = fringe.get()[1]

        #check if the tile has been affected by demolish
        if len(nextState.actionList) > 0 and nextState.actionList[-1] is nextState.act_demolish:
                if (nextState.posX, nextState.posY, "s") in nextState.demolishedTiles:
                    tileDemolished = "S"
        else:
            if (nextState.posX, nextState.posY) in nextState.demolishedTiles:
                tileDemolished = "D"
            else:
                tileDemolished = "N"

        if nextState.isGoalState():
            #we have reached the goal. Return the relevant stats
            return (nextState.actionList, nextState.score, len(visited))

        elif (nextState.posX, nextState.posY, nextState.direction, tileDemolished) not in visited:
            visited.append((nextState.posX, nextState.posY, nextState.direction, tileDemolished))
            for successorState in nextState.getSuccessors():
                fringe.put((-(successorState.score - heuristic(successorState)), successorState))

     
def zeroHeuristic(state):
    """0: Returns 0."""
    return 0

def minHeuristic(state):
    xdiff, ydiff = absGoalDiff(state)
    minNum = min(xdiff, ydiff)
    return minNum

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
        if ydiff > 0:
            turnCost += 2
        elif xdiff is not 0:
            turnCost +=1
        

    if state.direction is state.east:
        if xdiff < 0:
            turnCost += 2
        elif ydiff is not 0:
            turnCost +=1

    if state.direction is state.south:
        if ydiff < 0:
            turnCost += 2
        elif xdiff is not 0:
            turnCost +=1
        

    if state.direction is state.west:
        if xdiff > 0:
            turnCost += 2
        elif ydiff is not 0:
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

def printWorld(world):
    print "World loaded: "
    for line in world:
        for element in line:
            print element,
        print ""
    print ""