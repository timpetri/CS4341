"""
	state.py 

"""
import math
import copy

class State:
	
	north = "north"
	south = "south"
	east = "east"
	west = "west"
	act_forward = "forward"
	act_left = "turn left"
	act_right = "turn right"
	act_bash = "bash"
	act_demolish = "demolish"


	def __init__(self, world, posX, posY, goalX, goalY, direction, score , actionList):
		# global 2d array
		self.world = world

		# world
		self.goalX = goalX
		self.goalY = goalY

		# agent
		self.posX = posX
		self.posY = posY
		self.direction = direction

		# important
		self.score = score
		self.actionList = actionList

	def copy(self):
		"""	Params: none
			Return: a copy of the 
		"""
		newState = copy.deepcopy(self)
		return newState

	def isGoalState(self):
		return self.posX == self.goalX and self.posY == self.goalY

	def isLegalState(self):
		# print "(" + str(self.posX) + ", "+ str(self.posY) +")"
		return 0 <= self.posY < len(self.world) and 0 <= self.posX < len(self.world[0])


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

		return [elt for elt in successors if elt is not None]

	def performForward(self):
		"""	Params: none
			Return: state after performing forward action
		"""
		newState = self.copy()

		# add forward to action list
		newState.actionList.append(self.act_forward)

		# set new position of agent
		if self.direction is self.north:
			newState.posY -= 1
		elif self.direction is self.east:
			newState.posX += 1
		elif self.direction is self.south:
			newState.posY += 1
		elif self.direction is self.west:
			newState.posX -= 1

		if not newState.isLegalState():
			return None

		print "current position is x " + str(newState.posX) + " and y " + str(newState.posY)

		# decrement score by time complexity of new square
		newState.score -= self.world[newState.posY][newState.posX]

		return newState
	
	def performTurnLeft(self):
		"""	Params: none
			Return: state after performing turn left action
		"""
		newState = self.copy()

		# add forward to action list
		newState.actionList.append(self.act_left)

		# set new position of agent
		if self.direction is self.north:
			newState.direction = self.west
		elif self.direction is self.east:
			newState.direction = self.north
		elif self.direction is self.south:
			newState.direction = self.east
		elif self.direction is self.west:
			newState.direction = self.south

		if not newState.isLegalState():
			return None

		# decrement score by 1/3 of time complexity in current square
		newState.score -= math.ceil(self.world[newState.posY][newState.posX]/3)

		return newState

	def performTurnRight(self):
		"""	Params: none
			Return: state after performing turn right action
		"""

		newState = self.copy()

		# add forward to action list
		newState.actionList.append(self.act_right)

		# set new position of agent
		if self.direction is self.north:
			newState.direction = self.east
		elif self.direction is self.east:
			newState.direction = self.south
		elif self.direction is self.south:
			newState.direction = self.west
		elif self.direction is self.west:
			newState.direction = self.north

		# decrement score by 1/3 of time complexity in current square
		newState.score -= math.ceil(self.world[newState.posY][newState.posX]/3)

		return newState

	def performBash(self):
		"""	Params: none
			Return: state after performing turn left action
		"""
		newState = self.copy()

		# add forward to action list
		newState.actionList.append(self.act_bash)

		# set new position of agent
		if self.direction is self.north:
			newState.posY -= 1
		elif self.direction is self.east:
			newState.posX += 1
		elif self.direction is self.south:
			newState.posY += 1
		elif self.direction is self.west:
			newState.posX -= 1

		if not newState.isLegalState():
			return None

		# decrement score by 3
		newState.score -= 3

		return newState.performForward()


	def performDemolish(self):
		"""	Params: none
			Return: state after performing demolish
		"""

		newState = self.copy()

		# add forward to action list
		newState.actionList.append(self.act_demolish)

		# set adjacent squares to 3
		maxY = len(self.world)
		maxX = len(self.world[0])

		startPosX = 0 if newState.posX is 0 else newState.posX-1
		startPosY = 0 if newState.posY is 0 else newState.posY-1
		endPosX = maxX if newState.posX is maxX else  newState.posX+1
		endPosY = maxY if newState.posY is maxY else newState.posY+1

		for i in range(startPosY, endPosY):
			for j in range(startPosX, endPosX):
				if i is not newState.posY and j is not newState.posX: # exclude current pos
					self.world[i][j] = 3

		# decrement score by 4
		newState.score -= 4

		return newState

