from random import randint, random, shuffle, choice
from abstractPuzzle import AbstractPuzzle

"""
Puzzle #1: PackingPuzzle
Author: Tim Petri
"""
class PackingPuzzle(AbstractPuzzle):

	targetValue = 0
	validNumbers = []

	def __init__(self):
		self.test = 1

	def generateInitialPopulation(self, popSize, inputText):
			
		self.targetValue = int(inputText[0].strip()) # get first element
		self.validNumbers = map(lambda s: int(s.strip()), inputText[1:]) # rest of lines are valid numbers

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



	def createChild(self, parent1, parent2):

		child = []

		child.extend(parent1[:len(parent1)/2]) # add first half of parent 1
		child.extend(parent2[len(parent2)/2:]) # add second half of parent 2

		print "----------------"
		print "Parent 1 : " + str(parent1)
		print "Parent 2 : " + str(parent2)
		print "Child : " + str(child)
		print "----------------"

		return child

	def mutate(self, individual):

		# pick a random number from valid number that is not already in individual
		validMutationOptions = [x for x in self.validNumbers if x not in individual]
		
		pos = randint(0, len(individual)-1)
		posInValid = randint(0, len(validMutationOptions)-1)

		# pick a random number from all valid numbers (could already be in individual)
		individual[pos] = self.validNumbers[posInValid]

		return individual

	def fitness(self, individual):
		return self.score(individual)

	def score(self, individual):
		total = 0
		for x in individual:
			total += x

		if total <= self.targetValue:
			return total
		else:
			return 0
