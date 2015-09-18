from random import randint, random
from abstractPuzzle import AbstractPuzzle

"""
Simple example puzzle with necessary functions.
"""
class SimplePuzzle(AbstractPuzzle):

	def __init__(self):
		# global 2d array
		self.test = 1


	def generateInitialPopulation(self, popSize, inputText):
		population = []

		for x in xrange(popSize):
			x1 = randint(0, 150)
			x2 = randint(0, 150)
			x3 = randint(0, 150)
			x4 = randint(0, 150)
			x5 = randint(0, 150)

			population.append([x1, x2, x3, x4, x5])

		return population

	def createChild(self, parent1, parent2):
		child = parent1[2:] + parent2[:2]

		#print "Created child " + str(child) + " from parents " + str(parent1) + " and " + str(parent2)
		return child

	def mutate(self, individual):
		pos = randint(0, len(individual)-1)

		individual[pos] = randint(0, 100)

		return individual

	def fitness(self, individual):
		return self.score(individual)

	def score(self, individual):
		total = 0
		for x in individual:
			total += x

		return 200 - abs(200 - total)

