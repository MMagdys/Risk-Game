
class PassiveAgent(object):

	def __init__(self):
		self.territories = []



	def add_army(army, terr):

		armies, name = heapq.heappop(frontier)
		armies += army
