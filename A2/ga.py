import sys
import os
import time
from Queue import PriorityQueue
from SimplePuzzle import SimplePuzzle
from random import randint, random

isElitism = False
isCulling = False

puzzleDict = {
	0: SimplePuzzle(),
	#1: PackingPuzzle,
	#2: AllocationPuzzle,
	#3: TowerPuzzle
}
str_usage = "Usage: python genAlg.py <puzzle 1-3> <puzzle input filename> <runtime (seconds)>"

def genAlg(puzzle, maxTime, popSize, strings):

	#start a clock to track run time
	startTime = time.clock()

	#create the initial population
	initialPop = puzzle.generateInitialPopulation(popSize, strings)
	population = sortPop(initialPop, puzzle.fittness)

	#keep track of the best score
	bestIndividual = population[0]
	bestScore = puzzle.score(bestIndividual)
	bestIndividualGen = 0

	#create new generations until we run out of time
	genNum = 1
	while time.clock()-startTime < maxTime:

		#Generate a new generation
		population = newGen(population, popSize, puzzle)

		genBest = population[0]
		genBestScore = puzzle.score(genBest)

		#if the best of this generation beat the best overall record it
		if genBestScore > bestScore:
			bestIndividual = genBest
			bestScore = genBestScore
			bestIndividualGen = genNum

		genNum += 1

	print "Best scoring was " + str(bestIndividual) + " with score of " + str(bestScore) + " in generation " + str(bestIndividualGen)


def newGen(population, popSize, puzzle):

	survivingRatio = .25
	elitismRatio = .1
	mutationChance = .05

	newGen = []

	#if we are practicing elitism then keep the top elitismRatio perfromers for the nextGen
	if isElitism:
		eliteLen = int(len(population) * elitismRatio)
		newGen.extend(population[:eliteLen])

	#if we are culling remove the survivingRation worst performers
	if isCulling:
		cullLen = int(len(population) * survivingRatio)
		population = population[:cullLen]

	#generate children until we have hit popsize
	parentLen = len(population)
	while len(newGen) < popSize:
		parent1 = population[randint(0, parentLen-1)]
		parent2 = population[randint(0, parentLen-1)]

		child = puzzle.createChild(parent1, parent2)
		if random() < mutationChance:
			child = puzzle.mutate(child)

		newGen.append(child)

	return sortPop(newGen, puzzle.fittness)

def sortPop(population, fittnessFunct):
	sortedPopulation = [ (fittnessFunct(x), x) for x in population]
	sortedPopulation = [ x[1] for x in sorted(sortedPopulation, reverse = True)]
	return sortedPopulation

def readFile(fileName):
	inputFile = open(fileName, "r")
	lines = []
	while True:
		line = inputFile.readline()
		if not line: break
		lines.append(line)

	return lines

def main():
	scores = []

	if len(sys.argv) != 4:
		print "Wrong number of args.\n" + str_usage

	#the variable to set the population size for the genetic alg
	populationSize = 200

	puzzleNum = int(sys.argv[1])
	fileName = sys.argv[2]
	maxRuntime = int(sys.argv[3])

	inputLines = readFile(fileName)

	puzzle = puzzleDict[puzzleNum]

	genAlg(puzzle, maxRuntime, populationSize, inputLines)


if __name__ == "__main__":
	main()