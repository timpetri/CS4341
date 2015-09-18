from abc import ABCMeta, abstractmethod
class AbstractPuzzle(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def generateInitialPopulation(self, popSize, inputText):
		pass

	@abstractmethod
	def createChild(self, parent1, parent2):
		pass

	@abstractmethod
	def mutate(self, individual):
		pass

	@abstractmethod
	def fitness(self, individual):
		pass

	@abstractmethod
	def score(self, individual):
		pass