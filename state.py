"""
	state.py 

"""

class state:
	
	north = "north"
	south = "south"
	east = "east"
	west = "west"

	def __init__(self, world, heuristic, startX, startY, goalX, goalY, direction = this.north, score = 0, actionList = list()):
		# global
		this.world = world
		this.heuristic = heuristic

		# world
		this.startX = startX
		this.startY = startY	
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
		pass