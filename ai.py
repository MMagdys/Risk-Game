from collections import deque
from copy import copy
import math
from territory import Territory


class GreedyAgent:
    def __init__(self, territories=[]):
        self.territories = territories

    # calculate troops difference
    # number of =
    def calculateHeuristics(self):
        my_goal_terr = []
        count = 0
        h = 0
        # h : troops diff
        for terr in self.territories:
            for n in terr.neighbours:
                if n.taken_by != self:
                    if terr.troops - n.troops > 0:
                        h = terr.troops - n.troops
                        my_goal_terr.append((terr, n, h))
                        h = 0

        return my_goal_terr

    def play(self, army):
        frontier = deque(self.calculateHeuristics())
        count = 1
        while frontier:
            # will attack enemy with most troops that can be attacked
            frontier = deque(sorted(list(frontier), key=lambda terr: terr[2]))
            attackable_terr = frontier.popleft()
            if count == 1:
                attackable_terr[0].troops += army
                count = 0

            if attackable_terr[1].troops < attackable_terr[0].troops - 1:
                attack(attackable_terr[1], attackable_terr[0])


class AstarAgent:
    def __init__(self, board=[], territories=[]):
        self.board = board
        self.territories = territories

    # calculate troops difference

    def calculateHeuristics(self):
        my_goal_terr = []
        count = 0
        h = 0
        g = 0
        # h : troops diff
        # g : number of steps made added to h
        for terr in self.territories:
            for n in terr.neighbours:
                g += 1
                if n.taken_by != self:
                    h = (terr.troops - n.troops) + g
                    g = 0
            my_goal_terr.append((terr, n, h))
            h = 0
            g = 0

        return my_goal_terr

    def play(self, army):
        frontier = deque(self.calculateHeuristics())
        count = 1
        while frontier:
            frontier = deque(
                sorted(list(frontier), key=lambda terr: terr[2]))
            attackable_terr = frontier.popleft()
            if count == 1:
                attackable_terr[0].troops += army
                count = 0

            if attackable_terr[1].troops < attackable_terr[0].troops - 1:
                attack(attackable_terr[1], attackable_terr[0])

class RealtimeAstarAgent(object):
    def __init__(self, board=[], territories=[]):
        self.board = board
        self.territories = territories
    # calculate troops difference

    def calculateHeuristics(self, h):
        my_goal_terr = []
        count = 0
        #h = 0
        g = 0
        # h : troops diff
        # g : number of steps made added to h
        for terr in self.territories:
            for n in terr.neighbours:
                g += 1
                if n.taken_by != self:
                    h = (terr.troops - n.troops) + g
                    g = 0
            my_goal_terr.append((terr, n, h))
            h = 0
            g = 0

        return my_goal_terr


    def play(self, army):

        f = []
        h = 0
        my_path = []
        for terr in self.territories:
            for n in terr.neighbours:
                if n.taken_by != self:
                    f.append(self.calculateHeuristics(h))
                    f.remove(min(f))
                    h = min(f)
                    my_path.append(f)
        count = 1
        while i in my_path:
            attackable_terr = my_path[i]
            if count == 1:
                attackable_terr[0].troops += army
                count = 0

            if attackable_terr[1].troops < attackable_terr[0].troops - 1:
                attack(attackable_terr[1], attackable_terr[0])


class Player:
    def __init__(self):
        self.territories = []


class MiniMaxNode:
    # each state is a board instance
    # board is the array of territories
    # board is the intial state
    def __init__(self, board=[], other_agent=None):
        self.board = board
        self.max = other_agent
        self.min = Player()
        self.territories = self.min.territories

    def eval(self):
        # enemies_terr ----->>>> max
        # my_terr ----->>>> min
        # return + val if min has more territories
        return len(self.min.territories) - len(self.max.territories)

    def is_terminal_state(self):
        # if one has no territories then it's a terminal state therfore return true
        if len(self.min.territories) == 0 or len(self.max.territories) == 0:
            return True

            # if there is any possible attacks will return false
        for terr in self.min.territories:
            for n in terr.neighbours:
                if n.taken_by != self.min:
                    if terr.can_win(n):
                        return False

        for terr in self.max.territories:
            for n in terr.neighbours:
                if n.taken_by != self.max:
                    if terr.can_win(n):
                        return False

        # else no possible attacks therefore will return true
        return True

    def maximize(self, alpha, beta):

        if self.is_terminal_state():
            return None, self.eval()

        max_child, max_utility = None, - math.inf

        for child in self.get_children():
            _, utility = child.minimize(alpha, beta)

            if utility > max_utility:
                max_child, max_utility = child, utility
            if max_utility >= beta:
                break
            if max_utility > alpha:
                alpha = max_utility

        return max_child, max_utility

    def minimize(self, alpha, beta):

        if self.is_terminal_state():
            return None, self.eval()

        min_child, min_utility = None, math.inf

        for child in self.get_children():
            _, utility = child.maximize(alpha, beta)

            if utility < min_utility:
                min_child, min_utility = child, utility
            if min_utility <= alpha:
                break
            if min_utility < beta:
                beta = min_utility
        return min_child, min_utility

    def get_min_attackables(self):
        attackable = []
        for terr in self.min.territories:
            for n in terr.neighbours:
                if n.taken_by != self.min:
                    attackable.append((terr, n))
        return attackable

    def get_children(self):
        attackable = self.get_min_attackables()
        children = []

        while attackable:
            my_terr, enemy = attackable.pop()
            children.append(self.new_board(my_terr, enemy))
            attackable = self.get_min_attackables()

            # change the attacker and victim in the new board

    def new_board(self, attacker, victim):
        board = copy(self.board)
        vic = board[board.index(victim)]
        att = board[board.index(attacker)]

        vic.taken_by = att.taken_by
        vic.troops = att.troops - 1
        att.troops = 1
        return board

    def play(self, bouns_army):
        self.maximize(math.inf, math.inf)


def attack(victim, attacker):
    print("Attacking " + str(victim) + " with " + str(attacker))

    if victim.taken_by:
        victim.taken_by.territories.remove(victim)

    attacker.taken_by.territories.append(victim)
    victim.taken_by = attacker.taken_by
    victim.troops = attacker.troops - 1
    attacker.troops = 1


'''
board = [Territory(1, [2, 3], taken_by=1), Territory(2, [1, 4], taken_by=1),
         Territory(3, [2, 4], taken_by=2), Territory(5, [12, 40], taken_by=2), ]
minmax = MiniMaxNode(board,other_agent=1)
'''
