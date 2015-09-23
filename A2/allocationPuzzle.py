from random import randint, random, uniform
from abstractPuzzle import AbstractPuzzle

"""
Puzzle 2: Number Allocation
"""
class AllocationPuzzle(AbstractPuzzle):

	def __init__(self):
		# global 2d array
		self.test = 1

	def checkValid(num):
		if -10 <= num <= 10:
			return True
		return False

	def parseInitialList(self, inputText):
	
		print "Loading input file..."
		numList = []
		
		# Input text
		for line in inputText:
			num = float(line)
			if (checkValid(num)):
				numList.append(line)
			else:
				print "Invalid input was given"
				return null

		print "Finished loading input.\n"
		return numList

	def generateInitialPopulation(self, popSize, inputText):
		population = []
		
		self.initialAllocation = Allocation(self.parseInitialList(inputText))
		self.popSize = popSize
		
		population.append(self.initialAllocation)

		return population

	def createChild(self, parent1, parent2):
		
	def mutate(self, individual):
		
	def fitness(self, individual):       
		return self.score(individual)
		
	def score(self, individual):
		total = 0

		assert isinstance(individual, Allocation), "allocationPuzzle().score() Error: Invalid input for individual."

		for x in individual.bin1:
			total = total * x
			
		for x in individual.bin2:
			total = total + x
			
		return total;


class Allocation():

	def __init__(self, numList):

		self.orig = numlist
		self.bin1 = []
		self.bin2 = []
		self.bin3 = []
		
		for x in xrange(30):
			if x < 10:
				bin1.append(numList[x])
			else if x < 20:
				bin2.append(numList[x])
			else:
				bin3.append(numList[x])
		
		
		
	
	
