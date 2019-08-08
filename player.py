import heapq
from heapq import heappush


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
		self.terr_heap = []


	def play(self, army):

		# Placing bouns armies on the territory with the most armies
		terr = max_terr(self.territories)
		terr.troops += army

		# Greedly attacks whatever he can
		# get all neigbours he can attack
		attack_surface = []
		for i in self.territories:
			for n in i.neighbours:
				if n.taken_by != self:
					attack_surface.append((n, i))

		new_attack_surface = None
		while attack_surface:
			#  Newly accquired territory
			if new_attack_surface:
				# print("AFTER ATTACK")
				# print(new_attack_surface)
				for n in new_attack_surface.neighbours:
					if n.taken_by != self:
						attack_surface.append((n, i))
				new_attack_surface = None

			attackable_territory = max(attack_surface)
			# print(attackable_territory)
			if attackable_territory[0].taken_by != self:
				if attackable_territory[1].can_win(attackable_territory[0]):
					attack(attackable_territory[1], attackable_territory[0], self)
					new_attack_surface = attackable_territory[1]
			attack_surface.remove(attackable_territory)



class Pacifist(object):

	def __init__(self):

		self.territories = []


	def play(self, army):

		# Placing bouns armies on the territory with the fewest armies
		terr = min_terr(self.territories)
		terr.troops += army

		# Conquer territory with the fewest armies
		# get neigbours all territories
		attack_surface = []
		for i in self.territories:
			for n in i.neighbours:
				if n.taken_by != self:
					attack_surface.append((n, i))

		new_attack_surface = None
		while attack_surface:
			#  Newly accquired territory
			if new_attack_surface:
				# print("AFTER ATTACK")
				# print(new_attack_surface)
				for n in new_attack_surface.neighbours:
					if n.taken_by != self:
						attack_surface.append((n, i))
				new_attack_surface = None

			attackable_territory = min(attack_surface)
			# print(attackable_territory)
			if attackable_territory[0].taken_by != self:
				if attackable_territory[1].can_win(attackable_territory[0]):
					attack(attackable_territory[1], attackable_territory[0], self)
					new_attack_surface = attackable_territory[1]
			attack_surface.remove(attackable_territory)



def attack(attacker, victim, player):

	print("Attacking " + str(victim) + " with " + str(attacker))
	if victim.troops < attacker.troops - 1:

		if victim.taken_by: victim.taken_by.territories.remove(victim)
		attacker.taken_by.territories.append(victim)

		victim.taken_by = attacker.taken_by
		victim.troops = attacker.troops - 1
		attacker.troops = 1
		
	else:
		attacker.troops = 1



def max_terr(territories):

	temp = []
	for t in territories:
		heappush(temp, (t.troops, t.id))

	terr = max(temp)
	for t in territories:  
		if t.id == terr[1]:
			return t



def min_terr(territories):

	temp = []
	for t in territories:
		heappush(temp, (t.troops, t.id))

	terr = min(temp)
	for t in territories:  
		if t.id == terr[1]:
			return t