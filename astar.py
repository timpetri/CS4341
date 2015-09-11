#!/usr/bin/python

""" 
	astar.py

	See README.md for details.
	
"""

import sys
import os
import time
from heuristic import *
from state import State

DEBUG = True
charStartState = "S"
charGoalState = "G"
str_usage = "Usage: python astar.py <input_file>.txt <heuristic 1-6>"
heuristicDict = {
	1: zeroHeuristic,
	2: minHeuristic,
	3: maxHeuristic,
	4: addHeuristic,
	5: admissibleHeuristic,
	6: nonAdmissibleHeuristic
}



def loadInputFile(fileName):
	"""Returns a 2D array"""
	#if DEBUG: print "Loading..."
	inputFile = open(fileName, "r")
	world = []
	count = 0

	while True:
		line = inputFile.readline()
		if not line: break
		values = line.split("\t")
		world.append(list())
		for value in values:
			if len(value) is not 1:
				value = value[:1]
			if value is charStartState or value is charGoalState:

				world[count].append(value)
			elif value != '' and value != '\n':
				world[count].append(int(str.rstrip(value)))
		count += 1
	#printWorld(world)
	return world

def replaceStatesWithNumberOne(world, y, x):
	world[y][x] = 1

def findCharInWorld(world, charState):
	"""Returns a tuple (y,x) of the coordinates of the designated char."""
	for y in range (len(world)):
		for x in range (len(world[0])):
			if world[y][x] == charState:
				#print "Found " + charState + ": y=" + str(y) + ", x=" + str(x) 
				return y, x
	
def solve(initialState, heuristic):
	actionList, score = aStar(initialState, heuristic)
	print "List of actions: " + str(actionList)	
	print "Score: " + str(score)
	return score

def createInitialState(fileName):
	world = loadInputFile(fileName)
	startY, startX = findCharInWorld(world, charStartState)
	goalY, goalX = findCharInWorld(world, charGoalState)
	replaceStatesWithNumberOne(world, startY, startX)
	replaceStatesWithNumberOne(world, goalY, goalX)
	#printWorld(world)
	initialState = State(world, startX, startY, goalX, goalY, State.north, 100, list())
	return initialState

def main():
	scores = []
	startTime = time.clock()
	num_heuristic = int(sys.argv[2])
	fileName = sys.argv[1]
	if len(sys.argv) != 3:
		print "Wrong number of args.\n" + str_usage
	elif not 0 <= num_heuristic < 7:
		print "Invalid heuristic: " + sys.argv[2] + "\n" + str_usage
	elif not os.path.isfile(fileName):
		raise IOError("Input file does not exist.")
	else:
		initialState = createInitialState(fileName)
		printWorld(initialState.world)
		if num_heuristic is 0:
			n = 1
			while n <= 6:
				print "heuristic " + str(n)
				#initialState = createInitialState(fileName)
				scores.append(solve(initialState, heuristicDict[n]))
				n += 1
			print str(scores)
		else:
			solve(initialState, heuristicDict[num_heuristic])
	endTime = time.clock()

	print endTime - startTime

if __name__ == "__main__":
	main()
