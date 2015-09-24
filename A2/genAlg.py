from random import randint, random, uniform, shuffle

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
		self.population = []

		#create the initial population
		initialPop = puzzle.generateInitialPopulation(popSize, inputLines)
		for ind in initialPop:
			self.population.append((puzzle.fitness(ind), ind))
		self.population = self.sortPop(self.population, puzzle.fitness)

		#keep track of the best score
		self.bestIndividual = self.population[0][1]
		self.bestScore = self.puzzle.score(self.bestIndividual)
		self.bestIndividualGen = 0

	def newGeneration(self):
		self.genNum += 1
		#Generate a new generation
		self.generateNewPopulation()

		genBest = self.population[0][1]
		genBestScore = self.puzzle.score(genBest)

		if True:#(self.genNum % 100) == 0:
			genWorst = self.population[-1][1]
			genWorstScore = self.puzzle.score(genWorst)
			genMedian = self.population[len(self.population)/2][1]
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
			#print self.population
			cullLen = int(len(self.population) * self.cullRatio)
			self.population = self.population[:len(self.population)-cullLen]
			#print self.population

		#generate children until we have hit popsize
		parentLen = len(self.population)
		thresholdOffSet = 0
		while len(newGen) < self.popSize:

			parents = self.population[:]
			shuffle(parents)
			children = []
			for i in xrange(parentLen/2):
				parent1 = parents.pop()[1]
				parent2 = parents.pop()[1]

				threshold = max(len(parent1), len(parent2))/4 + thresholdOffSet

				if self.puzzle.levenshteinDistance(parent1, parent2) > threshold:
					child = self.puzzle.createChild(parent1, parent2)
					if random() < self.mutateRatio:
						child = self.puzzle.mutate(child)

					childFitness = self.puzzle.fitness(child)
					children.append((childFitness, child))
				#else:
					#print "DENIED"
			if len(children) == 0:
				#print "Reducing thresholdOffSet"
				thresholdOffSet -= 1
			newGen.extend(children)

		self.population = self.sortPop(newGen[:self.popSize], self.puzzle.fitness)

	def sortPop(self, population, fitnessFunct):
		#sortedPopulation = [ (fitnessFunct(x), x) for x in population]
		sortedPopulation = [ x for x in sorted(population, reverse = True)]
		return sortedPopulation

	def recordResults(self):
		print "Best scoring was " + str(self.bestIndividual) + " with score of " + str(self.bestScore) + " in generation " + str(self.bestIndividualGen)
		print "Ran for " + str(self.genNum) + " generations"

		#Write the generation history out to file
		f = open("genHistory.csv", 'w')
		for gen in self.history:
			line = str(gen).replace('(', '').replace(')', '') + '\n'
			f.write(line)

