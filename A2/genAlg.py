from random import randint, random

class GenAlg():

	def __init__(self, puzzle, inputLines, popSize, elitismRatio, cullRatio, mutateRatio):
		self.puzzle = puzzle
		self.popSize = popSize
		self.elitismRatio = elitismRatio
		self.cullRatio = cullRatio
		self.mutateRatio = mutateRatio

		#store the best, worst, and median of each generation
		self.history = []
		self.genNum = 0

		#create the initial population
		initialPop = puzzle.generateInitialPopulation(popSize, inputLines)
		self.population = self.sortPop(initialPop, puzzle.fitness)

		#keep track of the best score
		self.bestIndividual = self.population[0]
		self.bestScore = puzzle.score(self.bestIndividual)
		self.bestIndividualGen = 0

	def newGeneration(self):
		self.genNum += 1
		#Generate a new generation
		self.generateNewPopulation()

		genBest = self.population[0]
		genBestScore = self.puzzle.score(genBest)

		if (self.genNum % 100) == 0:
			genWorst = self.population[-1]
			genWorstScore = self.puzzle.score(genWorst)
			genMedian = self.population[len(self.population)/2]
			genMedianScore = self.puzzle.score(genMedian)

			self.history.append((genBestScore, genWorstScore, genMedianScore))

		#if the best of this generation beat the best overall record it
		if genBestScore > self.bestScore:
			self.bestIndividual = genBest
			self.bestScore = genBestScore
			self.bestIndividualGen = self.genNum

	def generateNewPopulation(self):

		newGen = []

		#if we are practicing elitism then keep the top elitismRatio perfromers for the nextGen
		if self.elitismRatio:
			eliteLen = int(len(self.population) * self.elitismRatio)
			newGen.extend(self.population[:eliteLen])

		#if we are culling remove the survivingRation worst performers
		if self.cullRatio:
			cullLen = int(len(self.population) * self.cullRatio)
			self.population = self.population[:cullLen]

		#generate children until we have hit popsize
		parentLen = len(self.population)
		while len(newGen) < self.popSize:
			parent1 = self.population[randint(0, parentLen-1)]
			parent2 = self.population[randint(0, parentLen-1)]

			child = self.puzzle.createChild(parent1, parent2)
			if random() < self.mutateRatio:
				child = self.puzzle.mutate(child)

			newGen.append(child)

		self.population = self.sortPop(newGen, self.puzzle.fitness)


	def sortPop(self, population, fitnessFunct):
		sortedPopulation = [ (fitnessFunct(x), x) for x in population]
		sortedPopulation = [ x[1] for x in sorted(sortedPopulation, reverse = True)]
		return sortedPopulation

	def recordResults(self):
		print "Best scoring was " + str(self.bestIndividual) + " with score of " + str(self.bestScore) + " in generation " + str(self.bestIndividualGen)
		print "Ran for " + str(self.genNum) + " generations"

		#Write the generation history out to file
		f = open("genHistory.csv", 'w')
		for gen in self.history:
			line = str(gen).replace('(', '').replace(')', '') + '\n'
			f.write(line)