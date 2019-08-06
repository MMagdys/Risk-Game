import heapq


class PassiveAgent(object):
    def __init__(self):
        self.territories = []

    def add_army(army, terr):
        armies, name = heapq.heappop(frontier)
        armies += army


class AggressiveAgent(object):
    def __init__(self):
        self.territories = []

    def add_army(army, terr):
        armies, name = heapq.heappop(frontier)
        armies += army


class Pacifist:
    def __init__(self):
        self.territories = []

    def add_army(self, terr):
        terr.add_troops(player=self, troops=3)

    def play(self, opponent):
        # get all territories for self player
        # add troops to territory with least troops
        self.add_army(min(self.territories))

        # get neigbours all territories
        neighbours = []
        for i in self.territories:
            for n in i.neighbours:
                if n not in neighbours:
                    neighbours.append(n)

        # check for opponent territories in neigbors and put them in an array
        attackable =[]
        for i in neighbours:
            if i in opponent.territories:


    # check for opponent territory with least troops and attack it
