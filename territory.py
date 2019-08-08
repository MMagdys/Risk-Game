
class Territory:


	def __init__(self, value, neighbours=None, troops=0, taken_by=None):

		self.id = value
		if neighbours:
			self.neighbours = neighbours
		else: self.neighbours = list()
		self.troops = troops
		self.taken_by = taken_by



	def __lt__(self, other):

		return self.id < other.id



	def __eq__(self, other):

		return self.id == other.id



	def __str__(self):

		return "Territory: " + str(self.id) + " Army: " + str(self.troops) 



	def __repr__(self):

		return self.__str__()



	def taken_by(self):

		return self.taken_by



	def can_win(self, other):

		return other.troops < self.troops - 1

