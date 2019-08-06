class Territory:
    def __init__(self, name, troops=0, takenBy=None):
        self.name = name
        self.troops = troops
        self.takenBy = takenBy

    def isTaken(self):
        if self.takenBy is None:
            return False
        return True

    def addTroops(self, player, troops):
        self.takenBy = player
        self.troops = self.troops + troops
