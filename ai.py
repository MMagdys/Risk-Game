class GreedyAgent:
    def __init__(self, board=[], territories=[]):
        self.board = board
        self.territories = territories

    # ana bahbed hena
    # return neighbour with most enemies (higher potenial )
    def calculateHeuristics(self):
        # return (my_terr, vicitim_terr)
        max_enemies = current_enemies = 0
        my_goal_terr = None
        # get terr with most enemies
        for terr in self.territories:
            for neighbour in terr.neighbours:
                if neighbour.taken_by != self:
                    current_enemies = current_enemies + 1
            if current_enemies > max_enemies:
                max_enemies = current_enemies
                my_goal_terr = terr
            current_enemies = 0
        # decide which neighbour with higher potential
        max_neighbours = []
        for i in my_goal_terr.neighbours:
            max_neighbours.append((i,len(i.neighbours)))
        goal_victim = max(max_neighbours)
        
        return (goal_victim[0], my_goal_terr)

    def play(self, army):

        attack_surface = []
        attackable_territory = self.calculateHeuristics()
        attackable_territory[1].troops += army
        while attack_surface:
            if attackable_territory[0].troops < attackable_territory[1].troops - 1:
                attack(attackable_territory[1], attackable_territory[0])
            attack_surface.remove(attackable_territory)
            attack_surface.append(self.calculateHeuristics())

    def attack(self, attacker, victim):
        print("Attacking " + str(victim) + " with " + str(attacker))
        if victim.troops < attacker.troops:
           # add it to me
            self.territories.append(victim)
            # remove it from other player
            if victim.taken_by:
                victim.taken_by.territories.remove(victim)

            victim.taken_by = attacker.taken_by
            victim.troops = attacker.troops - 1
            attacker.troops = 1
            self.board[self.board.index(victim)] = victim
            self.board[self.board.index(attacker)] = attacker

        else:
            attacker.troops = 1
            self.board[self.board.index(attacker)] = attacker
