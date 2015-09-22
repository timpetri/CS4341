"""
	towerPuzzle.py
	Author: Nicholas S. Bradford

"""

import re
from random import randint, sample
from abstractPuzzle import AbstractPuzzle


class TowerPuzzle(AbstractPuzzle):
	"""Puzzle 3: TowerPuzzle"""

	def __init__(self):
		""" Constructor. The initialTowerList is initialized in generateInitialPopulation()."""
		self.initialTower = None

	def parseInitialTower(self, inputText):
		"""	Input: Takes inputText in as a list of text file lines.
			Output: A list of pieces that can be used to generate new Towers.

		"""
		print "Loading input file..."
		_answerList = list()

		for line in inputText:
			if not line: break
			_values = re.split(r'[;,\s]\s*', line)
			#print str(_values)
			_piece = Piece(_values[0], _values[1], _values[2], _values[3])
			print _piece
			_answerList.append(_piece)
		#print str(_answerList)
		print "Finished loading input.\n"
		return _answerList

	def generateRandomTower(self):
		"""	Generates a tower with a random size (>= 2) and random pieces)."""
		_pieceList = sample(self.initialTower.pieceList, randint(2, len(self.initialTower.pieceList)))
		return Tower(_pieceList)

	def generateInitialPopulation(self, popSize, inputText):
		""" Input: Takes inputText in as a list of text files lines.
			Returns: 
		"""

		self.initialTower = Tower(self.parseInitialTower(inputText))
		assert self.initialTower.containsDoorAndLookout(), "Error: Tower does not contain a door and lookout."
		_population = []
		
		for i in xrange(popSize):
			_population.append(self.generateRandomTower())
		for tower in _population:
			print tower
		return _population

	def createChild(self, parent1, parent2):
		""" Returns: a child taken by taking the first half of parent1 and the second half of parent2."""
		child = Tower(parent1.pieceList[:len(parent1.pieceList)/2] + parent2.pieceList[len(parent2.pieceList)/2-1:])
		print "Created child: " + str(child) + " from parents: " + str(parent1) + " and " + str(parent2)
		return child

	def mutate(self, individual):
		"""	Input: member of the population.
			Returns: individual with a random change. Validity of resulting mutation not enforced.
				The random change will be a swap of the positions of two pieces in the Tower.
		"""
		assert isinstance(individual, Tower), "Error: Passed a non-Tower into a TowerPuzzle.score() individual." 
		pos1 = randint(0, len(self.initialTower.pieceList) - 1)
		pos2 = randint(0, len(self.initialTower.pieceList) - 1)
		individual.pieceList[pos1], individual.pieceList[pos2] = individual.pieceList[pos2], individual.pieceList[pos1]
		return individual

	def fitness(self, individual):
		"""	Input: member of the population.
			Returns: the fitness of the individual (not necessarily the score)."""
		assert isinstance(individual, Tower), "Error: Passed a non-Tower into a TowerPuzzle.score() individual." 
		return self.score(individual)

	def score(self, individual):
		""" Input: member of the population.
			Returns: the score of the individual. Returns 0 for invalid individuals."""
		assert isinstance(individual, Tower), "Error: Passed a non-Tower into a TowerPuzzle.score() individual." 
		if individual.containsDoorAndLookout():
			return 1
		else:
			return 0
		#total = 0
		#for x in individual:
		#	total += x
		# 200 - abs(200 - total)

# End class TowerPuzzle

class Tower():
	"""Represents a list of Piece objects, which form a Tower when stacked."""

	def __init__(self, pieceList):
		for piece in pieceList:
			assert isinstance(piece, Piece), "Error: Passed a non-piece into a Tower() pieceList." 
		self.pieceList = list(pieceList) #make sure that you use all new references

	def __str__(self):
		return str([str(x) for x in self.pieceList])

	def containsDoorAndLookout(self):
		""" Returns: True if the Tower has a Door and Lookout somewhere in it."""

		hasDoor = False
		hasLookout = False
		for piece in self.pieceList:
			if not hasDoor and piece.pieceType == Piece._door:
				hasDoor = True
			elif not hasLookout and piece.pieceType == Piece._lookout:
				hasLookout = True
			if hasLookout and hasDoor:
				break
		return hasDoor and hasLookout

# End class Tower

class Piece():
	"""Represents a piece used to build the tower."""

	_door = "Door"
	_wall = "Wall"
	_lookout = "Lookout"
	_pieceTypes = [_door, _wall, _lookout]

	def __init__(self, pieceType, width, length, cost):
		"""	Input:  pieceType (String), width (int), length (int), cost (int)"""
		assert (pieceType in self._pieceTypes), "Error: Invalid pieceType."
		assert (width > 0) and (length > 0) and (cost > 0), "Error: width, length, and cost must be greater than 0."
		self.pieceType = pieceType
		self.width = width
		self.length = length
		self.cost = cost

	def __str__(self):
		#return self.pieceType + "\twid:" + str(self.width) + "\tlen:" + str(self.length) + "\tcost:" + str(self.cost)
		return self.pieceType + " " + str(self.width) + " " + str(self.length) + " " + str(self.cost)

# End class Piece

#EOF