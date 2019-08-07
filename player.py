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
        heapq.heappush(self.territories, terr)
        # get neigbours all territories
        attack_surface = []
        for i in self.territories:
            for n in i.neighbours:
                if n.taken_by != self:
                    attack_surface.append((n, i))

        attackable_territory = max(attack_surface)
        if attackable_territory[0].troops < attackable_territory[1].troops - 1:
            attack(attackable_territory[1], attackable_territory[0])


class Pacifist(object):

    def __init__(self):

        self.territories = []


    def play(self, army):

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
        	attack(attackable_territory[1], attackable_territory[0])



def attack(attacker, victim):

	if victim.troops < attacker.troops:
		victim.taken_by = attacker.taken_by
		victim.troops = attacker.troops - 1
		attacker.troops = 1

	else:
		attacker.troops = 1