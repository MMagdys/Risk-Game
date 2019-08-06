
class Territory:


	def __init__(self, value, neighbours, troops=0, taken_by=None):

		self.id = value
		self.neighbours = neighbours
		self.troops = troops
		self.taken_by = taken_by



	def __lt__(self, other):

		return self.troops < other.troops



	def __eq__(self, other):

		return self.troops == other.troops



	def is_taken(self):

		if self.taken_by is None:
			return False
		return True



	def add_troops(self, player, troops):

		self.taken_by = player
		self.troops = self.troops + troops

