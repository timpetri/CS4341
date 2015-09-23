from random import randint, random, uniform, shuffle
from abstractPuzzle import AbstractPuzzle

"""
Puzzle 2: Number Allocation
"""
class AllocationPuzzle(AbstractPuzzle):

	def __init__(self):
		# global 2d array
		self.test = 1

	def checkValid(self, num):
		if -10 <= num <= 10:
			return True
		return False

	def parseInitialList(self, inputText):
	
		print "Loading input file..."
		numList = []
		
		# Input text
		for line in inputText:
			num = float(line)
			if (self.checkValid(num)):
				numList.append(num)
			else:
				print "Invalid input was given"
				return null

		print "Finished loading input.\n"
		return numList
		
	def arraySplitter(self, p1, p2, index):
		result = []
		
		result = list(p1.orig)[:index]
		#print 'index ' + str(index)
		#print 'b1 ' + str(len(p1.orig))
		temp = list(p2.orig)
		#print 'b2 ' + str(len(temp))
		for x in xrange(len(result)):
			temp.remove(result[x])
		
		result.extend(temp)
		
		#print 'len ' + str(len(result))
		#Sprint str(result)
		
		return result
		

	def generateInitialPopulation(self, popSize, inputText):
		population = []
		
		startList = self.parseInitialList(inputText)
		self.popSize = popSize

		for x in xrange(popSize):
			
			copyList = startList
			shuffle(copyList)
			individual = Allocation(copyList)
			population.append(individual)
		
		return population

	def createChild(self, parent1, parent2):
		childList = []
		
		index = randint(0, len(parent1.orig))
		
		childList = self.arraySplitter(parent1, parent2, index)
			
		return Allocation(childList)
		
	def mutate(self, individual):
		
		return individual
		
	def fitness(self, individual): 
		return self.score(individual)
		
	def score(self, individual):
		total = 0
		bin1Total = 0
		bin2Total = 0
		first = True
		
		assert isinstance(individual, Allocation), "allocationPuzzle().score() Error: Invalid input for individual."
			
		for x in individual.bin1:
			if (first):
				first = False
				bin1Total = x
			else:
				bin1Total *= x
			
		for x in individual.bin2:
			bin2Total += x
			
		total = (bin1Total+bin2Total)/2
		
		return total;


class Allocation():

	def __init__(self, inputList):

		self.orig = inputList
		self.bin1 = []
		self.bin2 = []
		self.bin3 = []
		
		for x in xrange(30):
			if x < 10:
				self.bin1.append(inputList[x])
			elif x < 20:
				self.bin2.append(inputList[x])
			else:
				self.bin3.append(inputList[x])
		
	
	def __str__ (self):
		output =  'bin1 ' + str(['{:.1f}'.format(x) for x in self.bin1]) + '\n'
		output += 'bin2 ' + str(['{:.1f}'.format(x) for x in self.bin2]) + '\n'
		output += 'bin3 ' + str(['{:.1f}'.format(x) for x in self.bin3]) + '\n'
		return output
		
