import random
from  player import PassiveAgent, AggressiveAgent
# from territory import Territory

EGY = ["Cairo", "Alexandria"]
# USA = ["CA", "MA"]
USA = [0,1,2,3,4,5,6,7,8,9]

TYPE = {"passive": PassiveAgent, "aggressive": AggressiveAgent}

class game(object):
	def __init__(self, country, ply_type, armies=20, number=2):

		if country.lower() == "egypt":
			self.available_terr = EGY
		elif country.lower() == "usa":
			self.available_terr = USA

		# array of territories;
		# 0 : available, 1 : player 1, 2 : Player 2
		self.territories = [0]*len(self.available_terr)
		# number of initial aramies each player has
		self.armies = armies
		# array of Players
		self.players = []
		for p in range(number):
			self.players.append(TYPE[ply_type[p]]())



	def random_dist_terr(self):
		for i in range(len(self.players)):
			for j in range(self.armies):
				t = random.randint(0, len(self.available_terr)-1)
				self.players[i].territories.append(self.available_terr[t])
				del self.available_terr[t]






# FOR TESTING
g = game("usa", ("passive", "passive"),3)
g.random_dist_terr()