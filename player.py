import heapq


class PassiveAgent(object):

	def __init__(self):
		self.territories = []


	def play(self, army):

		terr = heapq.heappop(self.territories)
		# print(terr.troops)
		terr.troops += army
		heapq.heappush(self.territories, terr)
		# print(terr.troops)



class AggressiveAgent(object):

	def __init__(self):
		
		self.territories = []


	def play(army, terr):

		armies, name = heapq.heappop()
		armies += army


class Pacifist:
    def __init__(self):
        self.territories = []

    def play(self, army, opponent):
        terr = heapq.heappop(self.territories)
        terr.troops += army
        heapq.heappush(self.territories, terr)

        # get neigbours all territories
        attack_surface = []
        for i in self.territories:
            for n in i.neighbours:
                if n.taken_by != self:
                    attack_surface.append((n, i))

        attackable_territory = min(attack_surface)
        if attackable_territory[0].troops < attackable_territory[1].troops - 1:
