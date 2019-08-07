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


	def play(self, army):

		terr = max(self.territories)
		terr.troops += army
		# heapq.heappush(self.territories, terr)

		# get neigbours all territories
		attack_surface = []
		for i in self.territories:
			for n in i.neighbours:
				if n.taken_by != self:
					attack_surface.append((n, i))
		while attack_surface:
			attackable_territory = max(attack_surface)
			print(attackable_territory)
			if attackable_territory[0].troops < attackable_territory[1].troops - 1:
				attack(attackable_territory[1], attackable_territory[0])
			attack_surface.remove(attackable_territory)



class Pacifist(object):

	def __init__(self):

		self.territories = []


	def play(self, army):

		terr = heapq.heappop(self.territories)
		terr.troops += army
		# heapq.heappush(self.territories, terr)

		# get neigbours all territories
		attack_surface = []
		for i in self.territories:
			for n in i.neighbours:
				if n.taken_by != self:
					attack_surface.append((n, i))

		while attack_surface:
			attackable_territory = min(attack_surface)
			print(attackable_territory)
			if attackable_territory[0].troops < attackable_territory[1].troops - 1:
				attack(attackable_territory[1], attackable_territory[0])
			attack_surface.remove(attackable_territory)



def attack(attacker, victim):

	print("Attacking " + str(victim) + " with " + str(attacker))
	if victim.troops < attacker.troops:

		attacker.taken_by.territories.append(victim)
		if victim.taken_by: victim.taken_by.territories.remove(victim)

		victim.taken_by = attacker.taken_by
		victim.troops = attacker.troops - 1
		attacker.troops = 1
		
	else:
		attacker.troops = 1