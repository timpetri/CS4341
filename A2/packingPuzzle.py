from random import randint, random, shuffle, choice
from abstractPuzzle import AbstractPuzzle
import sys

"""
Puzzle #1: PackingPuzzle
Author: Tim Petri
"""
class PackingPuzzle(AbstractPuzzle):

	targetValue = 0
	validNumbers = []
	validNumDict = {}

	def __init__(self):
		self.test = 1

	def generateInitialPopulation(self, popSize, inputText):
		"""	Input: Takes inputText in as a list of text file lines.
			Output: A list of randomly generated individuals, each being an array of numbers.
		"""

		self.targetValue = int(inputText[0].strip()) # get first element
		self.validNumbers = map(lambda s: int(s.strip()), inputText[1:]) # rest of lines are valid numbers
		self.validNumDict = self.generateNumDict() # keep track of count of the valid numbers

		print "Target value: " + str(self.targetValue)
		print "Valid numbers: " + str(self.validNumbers)
		# print "valid numbers length: " + str(len(self.validNumbers))

		population = []

		for x in xrange(popSize):

			individual = []
			lengthOfIndividual = randint(1, len(self.validNumbers)-1)

			# copy of valid numbers
			validForIndividual = self.validNumbers[:]

			for x in xrange(lengthOfIndividual):
				# remove a number from currently valid list and add to this individual
				shuffle(validForIndividual)
				individual.append(validForIndividual.pop())

			population.append(individual)

		print "Initial population: "
		for x in xrange(popSize):
			print str(x) + ": " + str(population[x])

		return population

	def generateNumDict(self):
		"""	Generate a dictionary to later ensure that no individuals can 
			contain more occurrences of a number than allowed in input.
		"""
		_answerDict = {}
		for num in self.validNumbers:
			if num in _answerDict:
				_answerDict[num] += 1
			else:
				_answerDict[num] = 1
		return _answerDict

	def createNewNumDict(self):
		""" Makes a copy of self.validNumDict."""
		return dict(self.validNumDict)

	def createChild(self, parent1, parent2):
		""" Returns: a child taken by taking a random number of elements in the front
			of parent1 and appending a random number of elements from the back of
			parent2.
		"""

		child = []

		if len(parent1) > 2:
			index1 = randint(1, len(parent1)-2)
		else:
			index1 = len(parent1)/2
		if len(parent2) > 2:
			index2 = randint(1, len(parent2)-2)
		else:
			index2 = len(parent2)/2

		checkDict = self.createNewNumDict()

		child.extend(parent1[:index1])

		for x in child:
			checkDict[x] -= 1

		# only add
		for x in parent2[index2:]:
			if checkDict[x] > 0:
				child.append(x)
				checkDict[x] -= 1

		#print "----------------"
		#print "Parent 1 : " + str(parent1)
		#print "Parent 2 : " + str(parent2)
		#print "Child : " + str(child)
		#print "----------------"

		return child

	def mutate(self, individual):
		"""	Input: member of the population.
			Returns: individual with a random change. Validity of resulting mutation not enforced.
				The random change will be a
		"""

		checkDict = self.createNewNumDict()

		for x in individual:
			checkDict[x] -= 1


		print str(len(individual))
		print str(self.validNumDict)

		# index to mutate in individual
		if len(individual) != 1:
			pos = randint(0, len(individual)-1)
		else:
			pos = 0

		validChoices = []

		for num in checkDict:
			if checkDict[num] > 0:
				validChoices.append(num)

		posInValidChoices = randint(0, len(validChoices)-1)

		individual[pos] = validChoices[posInValidChoices]

		return individual

	def fitness(self, individual):
		total = 0
		for x in individual:
			total += x

		return self.targetValue - abs(self.targetValue - total)
		"""if total <= self.targetValue:
			return total
		else:
			return -total"""

	def score(self, individual):
		total = 0
		for x in individual:
			total += x

		if total <= self.targetValue:
			return total
		else:
			return 0
