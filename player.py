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
		attack(self, max)



class Pacifist(object):

	def __init__(self):

		self.territories = []


	def play(self, army):

		# Placing bouns armies on the territory with the fewest armies
		terr = min_terr(self.territories)
		terr.troops += army

		# Conquer the territory with the fewest armies
		attack(self, min)



def conquer(attacker, victim, player):

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



def attack(player, function):

		# get all neigbours he can attack
	attack_surface = []
	for terr in player.territories:
		for neigh in terr.neighbours:
			if neigh.taken_by != player:
				attack_surface.append((neigh, terr))

		new_attack_surface = None
		while attack_surface:
			#  Newly accquired territory
			if new_attack_surface:
				# print("AFTER ATTACK")
				# print(new_attack_surface)
				for neigh in new_attack_surface.neighbours:
					if neigh.taken_by != player:
						attack_surface.append((neigh, new_attack_surface))
				new_attack_surface = None

			target, attacker = function(attack_surface)
			# print(attackable_territory)
			if target.taken_by != player:
				if attacker.can_win(target):
					conquer(attacker, target, attacker)
					new_attack_surface = target
			attack_surface.remove((target, attacker))