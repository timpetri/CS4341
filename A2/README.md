# CS4341
## Assignment 2: Genetic Algorithms

### Work Split:
	Thomas Grimshaw:	GA Framework, Misc.
	Tim Petri:			Puzzle 1
	Lucas Lebrao:		Puzzle 2
	Nicolas Bradford:	Puzzle 3

### Usage:

	$ ga.py puzzleNum fileName runtime [-h] [-p POPSIZE] [-c [CULL]] [-e [ELITISM]] [-m MUTATECHANCE]
# Puzzle 1:
	$ python ga.py 1 ...
# Puzzle 2:
	$ python ga.py 2 input/allocation2.txt 10 -c -e 
# Puzzle 3:
	$ python ga.py 3 input/tower4.txt 10 -c .5 -e -p 500
