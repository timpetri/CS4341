"""
	state.py 

"""

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
		this.posX = startX
		this.posY = startY
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

		# add turn left

		# add turn right

		# add demolish

		pass

	def performForward(self):
		newState = State(self)

		# add forward to action list
		newState.actionList.append("forward")

		# set new position of agent
		if self.direction is this.north:
			newState.posY += 1
		else if self.direction is this.east:
			newState.posX += 1
		else if self.diretion is this.south:
			newState.posY -= 1
		else if self.direction is this.west
			newState.posX -= 1

		# decrement score by time complexity of new square
		newState.score -= world[newState.posX][newState.posY]
	
	def performBash(self):


	def performTurnLeft(self):

	def performTurnRight(self):

	def performDemolish(self):
	







