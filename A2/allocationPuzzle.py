"""
	allocationPuzzle.py
	Author: Lucas R. Lebrao
"""

from random import randint, random, uniform, shuffle
from abstractPuzzle import AbstractPuzzle

class AllocationPuzzle(AbstractPuzzle):
	""" Puzzle 2: Number Allocation """

	def __init__(self, inputText, popSize):
		self.startList = self.parseInitialList(inputText)
		self.popSize = popSize
		self.bestScore = 0
		self.ID = 0

	def checkValid(self, num):
		""" checkValid
		Input: Takes the given number and determine if it is valid for the problem
		Output: Whether the input is valid or not (True or False) """
		if -10 <= num <= 10:
			return True
		return False

	def parseInitialList(self, inputText):
		""" parseInitialList
		Input: Takes inputText in as a list of numbers in a Text file
		Output: A list of numbers that can be allocated into different bins """
		print "Loading input file..."
		numList = []

		# Input text
		for line in inputText:
			num = float(line)
			# Determine if it was given valid numbers
			assert self.checkValid(num), "AllocationPuzzle.parseInitialList(): Error, given invalid input"
			numList.append(num)

		print "Finished loading input.\n"
		return numList

	def arraySplitter(self, p1, p2, index):
		""" arraySplitter
		Input: Takes in two Allocation objects and then split their arrays at given index
		Output: Returns the newly generated array as a list of numbers """
		result = []

		# Split starting array at given index
		result = list(p1.orig)[:index]
		# Copy secondary list
		temp = list(p2.orig)

		# Remove duplicates from secondary list
		for x in xrange(len(result)):
			temp.remove(result[x])

		# Merge both lists
		result.extend(temp)

		return result

	def generateInitialPopulation(self):
		""" generateInitialPopulation
		Output: Returns a list of Allocation objects, with their corresponding list of
		numbers split into different bins """
		population = []

		# Generate multiple individuals until target population size
		for x in xrange(self.popSize):
			copyList = self.startList

			# Shuffle input list for different individuals
			shuffle(copyList)
			individual = Allocation(copyList, self.ID)
			self.ID += 1

			# Add generated individual to population list
			population.append(individual)
			score = self.score(individual)

			# Check if individual has best score
			if score > self.bestScore:
				self.bestScore = score

		return population

	def createChild(self, parent1, parent2):
		""" createChild
		Input: Two parents as Allocation Objects
		Output: A child created using the parent arrays """
		assert isinstance(parent1, Allocation), "allocationPuzzle().createChild() Error: Invalid input for parent1."
		assert isinstance(parent2, Allocation), "allocationPuzzle().createChild() Error: Invalid input for parent2."

		childList = []

		# Generate an index value and then create a new array based off its parents
		index = 15 # randint(0, len(parent1.orig))
		childList = self.arraySplitter(parent1, parent2, index)

		# Create and return the child
		child = Allocation(childList, self.ID)
		self.ID += 1
		return child

	def mutate(self, individual):
		""" mutate
		Input: An individual Allocation object to have its array mutated
		Output: A new Allocation object with a new number array """
		assert isinstance(individual, Allocation), "allocationPuzzle().mutate() Error: Invalid input for individual."

		childList = []
		tempList = list(individual.orig)

		# Run through the individual's array of numbers and mutate 5% of its numbers
		for val in tempList:
			if randint(0, 99) < 5:
				childList.append(uniform(-10, 10))
			else:
				childList.append(val)

		# Generate a new individual
		mutated = Allocation(tempList, self.ID)
		self.ID += 1
		return mutated

	def fitness(self, individual):
		""" fitness
		Input: An individual to have its fitness score determined
		Output: The individual's score against the best score generated from the first population """
		assert isinstance(individual, Allocation), "allocationPuzzle().fitness() Error: Invalid input for individual."

		# Fitness is determined from score minus original population's score
		return self.score(individual) # - self.bestScore

	def score(self, individual):
		""" score
		Input: An individual to be scored
		Output: The individual's score"""
		assert isinstance(individual, Allocation), "allocationPuzzle().score() Error: Invalid input for individual."
		
		total = 0
		bin1Total = 0
		bin2Total = 0
		first = True

		# Calculate Bin1: Multiplication of individual numbers
		for x in individual.bin1:
			if (first):
				first = False
				bin1Total = x
			else:
				bin1Total *= x

		# Calculate Bin2: Addition of individual numbers
		for x in individual.bin2:
			bin2Total += x

		# Ignore Bin3: No numbers are considered for scoring

		# Calculate the average of the two bins
		total = (bin1Total+bin2Total)/2
		return total;

	def levenshteinDistance(self, parent1, parent2):
		return super(AllocationPuzzle, self).levenshteinDistance(parent1.orig, parent2.orig)


class Allocation():
	""" Represents a group of bins, which are scored differently. """

	def __init__(self, inputList, ID):
		""" Constructor
		Input: List of numbers """

		self.ID = ID
		self.orig = list(inputList)
		self.bin1 = []
		self.bin2 = []
		self.bin3 = []

		# Run through the array of numbers and split each one to a different bin
		for x in xrange(len(inputList)):
			if x % 3 == 1:
				self.bin1.append(inputList[x])
			elif x % 3 == 2:
				self.bin2.append(inputList[x])
			else:
				self.bin3.append(inputList[x])


	def __str__ (self):
		""" String Override
		Output: String form of an Allocation object """
		output = 'Individual #' + str(self.ID) + '\n'
		output += '{Bin1 ' + str(['{:.1f}'.format(x) for x in self.bin1]) + '}\n'
		output += '{Bin2 ' + str(['{:.1f}'.format(x) for x in self.bin2]) + '}\n'
		output += '{Bin3 ' + str(['{:.1f}'.format(x) for x in self.bin3]) + '}\n'
		return output

	def __len__(self):
		""" Array length
		Output: Length of the base array of numbers """
		return len(self.orig)

