import heapq
from heapq import heappush
import random
from matplotlib.patches import Polygon


class PassiveAgent(object):
    def __init__(self):
        self.territories = []

    def play(self, army):
        if not self.territories: return  # Only placing bouns armies into territory with the fewest armies
        terr = min_terr(self.territories)
        terr.troops += army
        # defense_mechanism(self, army)
        # Only placing bouns armies into territory with the fewest armies
        terr = min_terr(self.territories)
        terr.troops += army


class AggressiveAgent(object):
    def __init__(self):
        self.territories = []
        self.terr_heap = []

    def play(self, army):
        if not self.territories: return
        # Placing bouns armies on the territory with the most armies
        terr = max_terr(self.territories)
        terr.troops += army

        # Greedly attacks whatever he can
        attack(self, max)


class Pacifist(object):
    def __init__(self):
        self.territories = []

    def play(self, army):
        if not self.territories: return
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

            if not attack_surface: return

            target, attacker = function(attack_surface)
            # print(attackable_territory)
            if target.taken_by != player:
                if attacker.can_win(target):
                    conquer(attacker, target, attacker)
                    new_attack_surface = target
            attack_surface.remove((target, attacker))


def diff(a, b):
    return [i for i in a if i not in b]


def defense_mechanism(player, bouns_armies):
    weak_points = {}
    boarder_terr = []

    for terr in player.territories:
        for neigh in terr.neighbours:
            if neigh.taken_by != player:
                if terr not in boarder_terr:
                    boarder_terr.append(terr)

    print("===================")
    print(boarder_terr)
    for terr in boarder_terr:
        for neigh in terr.neighbours:
            # print("+++++++++")
            # print(neigh)
            if neigh.can_win(terr):
                diff_troops = neigh.troops - terr.troops
                try:
                    if weak_points[terr.id]:
                        weak_points[terr.id] = max(diff_troops, weak_points[terr.id])
                except KeyError:
                    weak_points[terr.id] = diff_troops

    # Place Bouns armies in one of the weak boarder territory,
    # in order to defeat an upcoming attack
    if weak_points:
        weak_points = sorted(weak_points.items(), key=lambda kv: kv[1])
        for terr in weak_points:
            if terr[1] <= bouns_armies:
                for t in boarder_terr:
                    if t.id == terr[0]:
                        t.troops += bouns_armies
                        return

    # If boarder territory can't defeat upcoming attacks with these bouns armies
    # then enforce non boarder territory
    elif diff(player.territories, boarder_terr):
        temp = diff(player.territories, boarder_terr)
        print("***************************")
        print(player.territories)
        print(boarder_terr)
        i = random.randint(0, len(player.territories) - 1)
        t = player.territories[i]
        t.troops += bouns_armies
        return

    # if all territory are boarder territory, then choose one at random
    else:
        i = random.randint(0, len(player.territories) - 1)
        t = player.territories[random.randint(0, len(player.territories) - 1)]
        t.troops += bouns_armies
        return


class HumanAgent(object):
    def __init__(self):

        self.territories = []
        self.bouns_armies = 0

    def play(self, event, ui_map, plt):

        attack_surface = []
        for terr in self.territories:
            for neigh in terr.neighbours:
                if neigh.taken_by != self:
                    attack_surface.append((neigh, terr))

        event.x, event.y = event.xdata, event.ydata
        for s in range(len(ui_map.state_names)):
            if Polygon(ui_map.country_map.states[s]).contains(event)[0]:
                # print(ui_map.state_names[s], event.button)
                state_id = name2id[ui_map.state_names[s]]
                # Attack
                if event.button == 1:
                    for terr in self.territories:
                        if terr.id == state_id:
                            return

                    conquer_list = []
                    for attack_tup in attack_surface:
                        if attack_tup[0].id == state_id:
                            conquer_list.append(attack_tup)

                    attack_tup = max(conquer_list)
                    conquer(attack_tup[1], attack_tup[0], self)

                # Place Bouns Armies
                elif event.button == 3:
                    for terr in self.territories:
                        if terr.id == state_id:
                            terr.troops += self.bouns_armies
                            self.bouns_armies = 0
        plt.draw()


name2id = {
    "Washington": 1,
    "Oregon": 2,
    "California": 3,
    "Nevada": 4,
    "Idaho": 5,
    "Montana": 6,
    "Wyoming": 7,
    "Utah": 8,
    "Arizona": 9,
    "Colorado": 10,
    "New Mexico": 11,
    "Texas": 12,
    "Oklahoma": 13,
    "Kansas": 14,
    "Nebraska": 15,
    "South Dakota": 16,
    "North Dakota": 17,
    "Minnesota": 18,
    "Iowa": 19,
    "Missouri": 20,
    "Arkansas": 21,
    "Louisiana": 22,
    "Mississippi": 23,
    "Alabama": 24,
    "Florida": 25,
    "Georgia": 26,
    "South Carolina": 27,
    "North Carolina": 28,
    "Virginia": 29,
    "West Virginia": 30,
    "Tennessee": 31,
    "Kentucky": 32,
    "Illinois": 33,
    "Wisconsin": 34,
    "Indiana": 35,
    "Michigan": 36,
    "Ohio": 37,
    "Pennsylvania": 38,
    "New York": 39,
    "Vermont": 40,
    "New Hampshire": 41,
    "Maine": 42,
    "Massachusetts": 43,
    "Rhode Island": 44,
    "Connecticut": 45,
    "New Jersey": 46,
    "Delaware": 47,
    "Maryland": 48,
    "Hawaii": 49,
    "Alaska": 50
}
