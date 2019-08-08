from collections import deque


class GreedyAgent:
    def __init__(self, board=[], territories=[]):
        self.board = board
        self.territories = territories
    # calculate troops difference 
    def calculateHeuristics(self):
        my_goal_terr = []
        count = 0
        h = 0
        # h : troops diff
        for terr in self.territories:
            for n in terr.neighbours:
                if n.taken_by != self:
                    h = terr.troops - n.troops
            my_goal_terr.append((terr, n, h))
            h = 0

        return my_goal_terr

    def play(self, army):
        frontier = deque(self.calculateHeuristics())
        count = 1
        while frontier:
            frontier = deque(sorted(list(frontier), key=lambda terr: terr[2]))
            attackable_terr = frontier.popleft()
            if count == 1:
                attackable_terr[0].troops += army
                count = 0

            if attackable_terr[1].troops < attackable_terr[0].troops - 1:
                attack(attackable_terr[1], attackable_terr[0])


def attack(victim, attacker):

    print("Attacking " + str(victim) + " with " + str(attacker))

    if victim.taken_by:
        victim.taken_by.territories.remove(victim)
    
    attacker.taken_by.territories.append(victim)
    victim.taken_by = attacker.taken_by
    victim.troops = attacker.troops - 1
    attacker.troops = 1
