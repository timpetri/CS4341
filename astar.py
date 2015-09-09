#!/usr/bin/python

import sys
import os
from state import State

DEBUG = True
charStartState = "S"
charGoalState = "G"

def printWorld(world):
	print "World loaded: "
	for line in world:
		for element in line:
			print element,
	print ""

def loadInputFile(fileName):
	"""Returns a 2D array"""
	if DEBUG: print "Loading..."
	inputFile = open(fileName, "r")
	world = []
	count = 0

	while True:
		line = inputFile.readline()
		if not line: break
		values = line.split("\t")
		world.append(list())
		for value in values:
			world[count].append(value)
		count += 1
	printWorld(world)
	return world

def findCharInWorld(world, charState):
	"""Returns a tuple (y,x) of the coordinates of the designated char."""
	for y in range (len(world)):
		for x in range (len(world[0])):
			if world[y][x] == charState:
				print "Found " + charState + "\t y=" + str(y) + ", x=" + str(x) 
				break #return (1,2) #x, y
	return y, x

def solve(initialState, heuristic):
	#answer = aStarSearch(initialState, heuristic)
	#print str(answer)	
	pass

if __name__ == "__main__":
	str_usage = "Usage: python astar.py <input_file>.txt <heuristic 1-6>"
	num_heuristic = int(sys.argv[2])
	fileName = sys.argv[1]
	if len(sys.argv) != 3:
		print "Wrong number of args.\n" + str_usage
	elif not 0 < num_heuristic < 7:
		print "Invalid heuristic: " + sys.argv[2] + "\n" + str_usage
	elif not os.path.isfile(fileName):
		raise IOError("Input file does not exist.")
	else:
		world = loadInputFile(fileName)
		startX, startY = findCharInWorld(world, charStartState)
		goalX, goalY = findCharInWorld(world, charGoalState)
		initialState = State() # ( State.north, 0, list() )
		solve(initialState, None)
