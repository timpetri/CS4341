"""
	towerPuzzle.py

"""

from random import randint, random
from abstractPuzzle import AbstractPuzzle

"""
Puzzle 3: TowerPuzzle

"""
class TowerPuzzle(AbstractPuzzle):

	def __init__(self):
		# global 2d array
		# self.test = 1
		pass

	def generateInitialPopulation(self, popSize, inputText):
		""" Input: Takes inputText in as a list of text files lines.
			Returns: """

		"""
		for x in xrange(popSize):
			x1 = randint(0, 150)
			x2 = randint(0, 150)
			x3 = randint(0, 150)
			x4 = randint(0, 150)
			x5 = randint(0, 150)

			population.append([x1, x2, x3, x4, x5])
		"""
		population = []
		for line in inputText:
			population.append(line)
		return population

	def createChild(self, parent1, parent2):
		child = parent1[2:] + parent2[:2]

		#print "Created child " + str(child) + " from parents " + str(parent1) + " and " + str(parent2)
		return child

	def mutate(self, individual):
		"""	Input: member of the population.
			Returns: individual with a random change. Validity of resulting mutation not enforced."""
		pos = randint(0, len(individual)-1)

		individual[pos] = randint(0, 100)

		return individual

	def fitness(self, individual):
		"""	Input: member of the population.
			Returns: the fitness of the individual (not necessarily the score)."""
		return self.score(individual)

	def score(self, individual):
		""" Input: member of the population.
			Returns: the score of the individual. Returns 0 for invalid individuals."""
		total = 0
		for x in individual:
			total += x

		return 200 - abs(200 - total)

class Tower():
	"""Represents a list of Piece objects, which form a Tower when stacked."""

	def __init__(self, pieceList):
		for piece in pieceList:
			assert (type(piece) is Piece), "Error: Passed a non-piece into a Tower() pieceList." 
		self.pieceList = pieceList

	def printTower(self):
		for piece in pieceList:
			piece.printPiece()


class Piece():
	"""Represents a piece used to build the tower."""

	_door = "door"
	_wall = "wall"
	_lookout = "lookout"
	_pieceTypes = [_door, _wall, _lookout]

	def __init__(self, pieceType, width, length, cost):
		"""	Input:  pieceType (String), width (int), length (int), cost (int)"""
		assert (pieceType in self._pieceTypes), "Error: Invalid pieceType."
		assert (width > 0) and (length > 0) and (cost > 0), "Error: width, length, and cost must be greater than 0."
		self.pieceType = pieceType
		self.width = width
		self.length = length
		self.cost = cost

	def printPiece(self):
		print self.pieceType + "\tw:" + str(self.width) + "\tl:" + str(self.length) + "\tc:" + str(self.cost)