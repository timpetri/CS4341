import sys
import os
import time
import argparse
from SimplePuzzle import SimplePuzzle
from towerPuzzle import TowerPuzzle
from packingPuzzle import PackingPuzzle
from allocationPuzzle import AllocationPuzzle
from genAlg import GenAlg

puzzleDict = {
	0: SimplePuzzle(),
	1: PackingPuzzle(),
	2: AllocationPuzzle(),
	3: TowerPuzzle()
}

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

	parser = argparse.ArgumentParser()

	parser.add_argument("-p", "--popSize", type=int, default=200)
	parser.add_argument("-c", "--cull", nargs='?', const=0.25, type=float)
	parser.add_argument("-e", "--elitism", nargs='?', const=0.1, type=float)
	parser.add_argument("-m", "--mutateChance", default=0.01, type=float)
	parser.add_argument("puzzleNum", type=int)
	parser.add_argument("fileName")
	parser.add_argument("runtime", type=int)
	args = parser.parse_args()

	inputLines = readFile(args.fileName)
	puzzle = puzzleDict[args.puzzleNum]
	genAlg = GenAlg(puzzle, inputLines, args.popSize, args.elitism, args.cull, args.mutateChance)

	#start a clock to track run time
	startTime = time.clock()
	while time.clock()-startTime < args.runtime:
		genAlg.newGeneration()

	genAlg.recordResults()

if __name__ == "__main__":
	main()