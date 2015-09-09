"""
	state.py 

"""
import math

class State:
	
	north = "north"
	south = "south"
	east = "east"
	west = "west"

	def __init__(self, world, posX, posY, goalX, goalY, direction, score , actionList):
		# global
		this.world = world

		# world
		this.goalX = goalX
		this.goalY = goalY

		# agent
		this.posX = posX
		this.posY = posY
		this.direction = direction

		# important
		this.score = score
		this.actionList = actionList

	def getSuccessors(self):
		"""	Params: none
			Return: a list of states
		"""

		successors = []

		# add forward
		successors.append(self.performForward())
		# add bash
		successors.append(self.performTurnRight())
		# add turn left
		successors.append(self.performTurnLeft())
		# add turn right
		successors.append(self.performBash())
		# add demolish
		successors.append(self.performDemolish())
		
		return successors

	def performForward(self):
		"""	Params: none
			Return: state after performing forward action
		"""
		newState = State(self)

		# add forward to action list
		newState.actionList.append("forward")

		# set new position of agent
		if self.direction is this.north:
			newState.posY -= 1
		elif self.direction is this.east:
			newState.posX += 1
		elif self.diretion is this.south:
			newState.posY += 1
		elif self.direction is this.west
			newState.posX -= 1

		# decrement score by time complexity of new square
		newState.score -= world[newState.posY][newState.posX]

		return newState
	
	def performTurnLeft(self):
		"""	Params: none
			Return: state after performing turn left action
		"""
		newState = State(self)

		# add forward to action list
		newState.actionList.append("turn left")

		# set new position of agent
		if self.direction is this.north:
			newState.direction = this.west
		elif self.direction is this.east:
			newState.direction = this.north
		elif self.diretion is this.south:
			newState.direction = this.east
		elif self.direction is this.west
			newState.direction = this.south

		# decrement score by 1/3 of time complexity in current square
		newState.score -= math.ceil(world[newState.posY][newState.posX]/3)

		return newState

	def performTurnRight(self):
		"""	Params: none
			Return: state after performing turn right action
		"""

		newState = State(self)

		# add forward to action list
		newState.actionList.append("turn right")

		# set new position of agent
		if self.direction is this.north:
			newState.direction = this.east
		elif self.direction is this.east:
			newState.direction = this.south
		elif self.diretion is this.south:
			newState.direction = this.west
		elif self.direction is this.west
			newState.direction = this.north

		# decrement score by 1/3 of time complexity in current square
		newState.score -= math.ceil(world[newState.posY][newState.posX]/3)

		return newState

	def performBash(self):
		"""	Params: none
			Return: state after performing turn left action
		"""
		newState = State(self)

		# add forward to action list
		newState.actionList.append("bash")

		# set new position of agent
		if self.direction is this.north:
			newState.posY -= 1
		elif self.direction is this.east:
			newState.posX += 1
		elif self.diretion is this.south:
			newState.posY += 1
		elif self.direction is this.west
			newState.posX -= 1

		# decrement score by 3
		newState.score -= 3

		return newState.performForward()


	def performDemolish(self):
		"""	Params: none
			Return: state after performing demolish
		"""

		newState = State(self)

		# add forward to action list
		newState.actionList.append("demolish")

		# set adjacent squares to 3
		maxY = len(world)
		maxX = len(world[0])

		int startPosX = newState.posX is 0 ? 0 : newState.posX-1;
		int startPosY = newState.posY is 0 ? 0 : newState.posY-1;
		int endPosX = newState.posX is maxX ? maxX : newState.posX+1;
		int endPosY = newState.posY is maxY ? maxY : newState.posY+1;

		for i in range(startPosY, endPosY):
			for j in range(startPosX, endPosX):
				if i is not newstate.PosY and j is not newState.PosX: # exclude current pos
					world[i][j] = 3

		# decrement score by 4
		newState.score -= 4

		return newState









