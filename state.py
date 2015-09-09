class state:
	def __init__(self, world, heuristic, startX, startY, goalX, goalY, score = 0, actionList = list()):
		this.world = world
		this.heuristic = heuristic
		this.posX = startX
		this.posY = startY
		this.score = score

class world:
	def __init__(self, field, startX, startY, goalX, goalY)
		this.field = field
		this.startX = startX
		this.startY = startY
		this.goalX = goalX
		this.goalY = goalY