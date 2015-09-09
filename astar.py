import sys
import os

DEBUG = True

def loadInputFile(fileName):
	"""Loads the input file into a 2D array"""
	if DEBUG: print "Loading..."

	

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
		loadInputFile(fileName)