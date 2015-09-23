"""
	towerPuzzle.py
	Author: Nicholas S. Bradford

"""

import re
import sys
from random import randint, sample
from abstractPuzzle import AbstractPuzzle


class TowerPuzzle(AbstractPuzzle):
	"""Puzzle 3: TowerPuzzle"""

	def __init__(self):
		""" Constructor. The initialTowerList is initialized in generateInitialPopulation()."""
		self.initialTower = None
		self.towerDict = None

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

	def generateTowerDict(self):
		"""	Generate a dictionary to later ensure that there are no duplicates during crossovers."""
		_answerDict = {}
		for piece in self.initialTower.pieceList:
			if piece in _answerDict:
				_answerDict[piece] += 1
			else:
				_answerDict[piece] = 1
		return _answerDict

	def generateRandomTower(self):
		"""	Generates a tower with a random size (>= 2) and random pieces)."""
		_pieceList = sample(self.initialTower.pieceList, randint(2, len(self.initialTower.pieceList)))
		return Tower(_pieceList)

	def generateInitialPopulation(self, popSize, inputText):
		""" Input: Takes inputText in as a list of text files lines.
			Returns: a list of Tower objects, comprising the population.
		"""
		self.initialTower = Tower(self.parseInitialTower(inputText))
		self.towerDict = self.generateTowerDict()
		assert self.initialTower.containsDoorAndLookout(), "Error: NO SOLUTION, Tower does not contain a door and lookout."
		_population = []

		print "Initial population:"
		for i in xrange(popSize):
			_population.append(self.generateRandomTower())
		for tower in _population:
			print tower
		print ""
		
		#self.testCreateChild()
		#print "END TEST"
		#sys.exit(0)
		return _population

	def createNewCheckDict(self):
		""" Makes a copy of self.towerDict, to be used for checking during createChild()."""
		return dict(self.towerDict)

	def testCreateChild(self):
		""" Run only with tower0.txt."""
		door = Piece("Door", 5, 3, 2)
		wall = Piece("Wall", 5, 5, 1)
		lookout = Piece("Lookout", 3, 1, 2)

		par1 = Tower([door, lookout, wall, wall])
		par2 = Tower([wall, wall, lookout, door])
		print str(self.createChild(par1, par2))

		par1 = Tower([wall, wall, lookout, door])
		par2 = Tower([wall, wall])
		print str(self.createChild(par1, par2))


	def createChild(self, parent1, parent2):
		""" Returns: a child taken by taking the first half of parent1 and the second half of parent2."""
		assert isinstance(parent1, Tower) and isinstance(parent2, Tower), "Error: Passed a non-Tower into a TowerPuzzle.score() individual." 
		_child = Tower([])
		_checkDict = self.createNewCheckDict()

		# first, add half of parent1, no need to check
		#print "PARENT 1: "
		for piece in parent1.pieceList[:len(parent1.pieceList)/2]:
			_child.pieceList.append(piece)
			_checkDict[piece] -= 1
			#print str(piece)

		#print "PARENT 2: "
		# next, add elements from parent2, must check to make sure no incorrect duplicates
		for piece in parent2.pieceList[len(parent2.pieceList)/2-1:]:
			# check child already contains the piece
			if _checkDict[piece] > 0:
				_child.pieceList.append(piece)
				_checkDict[piece] -= 1
				#print piece

		#print "Created child: " + str(_child) + " from parents: " + str(parent1) + " and " + str(parent2)
		return _child

	def mutate(self, individual):
		"""	Input: member of the population.
			Returns: individual with a random change. Validity of resulting mutation not enforced.
				The random change will be a swap of the positions of two pieces in the Tower.
		"""
		assert isinstance(individual, Tower), "Error: Passed a non-Tower into a TowerPuzzle.score() individual."
		pos1 = randint(0, len(individual.pieceList) - 1)
		pos2 = randint(0, len(individual.pieceList) - 1)
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
		return individual.score()


# End class TowerPuzzle

class Tower():
	"""Represents a list of Piece objects, which form a Tower when stacked."""

	def __init__(self, pieceList):
		for piece in pieceList:
			assert isinstance(piece, Piece), "Error: Passed a non-piece into a Tower() pieceList."
		self.pieceList = list(pieceList) #make sure that you use all new references

	def __str__(self):
		""" Overrides printing."""
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

	def isValidTower(self):
		""" Returns true if the tower is valid."""
		isValid = False
		if len(self.pieceList) >= 2:
			if self.pieceList[0].pieceType == Piece._door and self.pieceList[-1].pieceType == Piece._lookout:
				towerHeight = len(self.pieceList)
				position = 0

				while position < towerHeight:
					piece = self.pieceList[position]

					#if the piece is not the top or bottom
					if position < towerHeight - 1 and position is not 0:
						#check that the piece is a wall
						if piece.pieceType != Piece._wall:
							break

					#check that the piece has the strength to hold the rest of the tower
					if piece.strength < towerHeight - (position + 1):
						break

					if position is not 0:
						pieceBelow = self.pieceList[position-1]
						#check that the width is <= the width of the piece below it
						if piece.width > pieceBelow.width:
							break

					position += 1

				if position == towerHeight:
					isValid = True

		return isValid

	def score(self):
		score = 0
		if self.isValidTower():
			for piece in self.pieceList:
				score -= piece.cost
			score += 10
			score += (len(self.pieceList) ** 2)

		return score

# End class Tower

class Piece():
	"""Represents a piece used to build the tower."""

	_door = "Door"
	_wall = "Wall"
	_lookout = "Lookout"
	_pieceTypes = [_door, _wall, _lookout]

	def __init__(self, pieceType, width, strength, cost):
		"""	Input:  pieceType (String), width (int), strength (int), cost (int)"""
		assert (pieceType in self._pieceTypes), "Error: Invalid pieceType."
		assert (width > 0) and (strength > 0) and (cost > 0), "Error: width, strength, and cost must be greater than 0."
		self.pieceType = pieceType
		self.width = int(width)
		self.strength = int(strength)
		self.cost = int(cost)

	def __str__(self):
		#return self.pieceType + "\twid:" + str(self.width) + "\tlen:" + str(self.strength) + "\tcost:" + str(self.cost)
		return self.pieceType + " " + str(self.width) + " " + str(self.strength) + " " + str(self.cost)

	def __hash__(self):
		return hash((self.pieceType, self.width, self.strength, self.cost))

	def __eq__(self, other):
		return (self.pieceType, self.width, self.strength, self.cost) == (other.pieceType, other.width, other.strength, other.cost)

# End class Piece

#EOF