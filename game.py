import random
from  player import PassiveAgent, AggressiveAgent, Pacifist
from territory import Territory
from util import map_to_terr


EGY = ["Cairo", "Alexandria"]
# USA = ["CA", "MA"]
USA = [0,1,2,3,4,5,6,7,8,9]

TYPE = {"passive": PassiveAgent, "aggressive": AggressiveAgent, "pacifist": Pacifist}



class game(object):


	def __init__(self, country, ply_type, armies=20, number=2):

		if country.lower() == "egypt":
			self.available_terr = EGY
		elif country.lower() == "usa":
			self.available_terr = map_to_terr(usaMap) #USA

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
				self.available_terr[t].troops = 1
				self.available_terr[t].taken_by = self.players[i]
				self.players[i].territories.append(self.available_terr[t])
				del self.available_terr[t]
			print(self.players[i].territories)
			# print(self.players[i].territories[0].taken_by)




	def game_over(self):

		return 1



	def run(self):

		# while self.game_over():
		t=0
		while t < 3:
			for player in self.players:
				bouns_armies = len(player.territories) // 3
				if bouns_armies < 3: bouns_armies = 3
				player.play(bouns_armies)
				t += 1
			print("\n\nTURN")
			print("player 1")
			print(self.players[0].territories)
			print("player 2")
			print(self.players[1].territories)






# USA MAP TEST
usaMap = {
		1: [2, 50, 5],
		2: [3, 4, 5, 1],
		3: [2, 4],
		4: [2, 3, 5, 8, 9],
		5: [1, 2, 4, 6, 7, 8],
		6: [5, 7, 16, 17],
		7: [6, 5, 8, 10, 15, 16],
		8: [4, 5, 7, 10, 9, 11],
		9: [8, 10, 11],
		10: [7, 8, 9, 11],
		11: [8, 9, 10, 12, 13],
		12: [11, 13, 22, 21],
		13: [12, 10, 11, 14],
		14: [10, 15, 13, 20],
		15: [10, 7, 16, 19, 20, 14],
		16: [7, 6, 17, 18, 19, 15],
		17: [6, 16, 18],
		18: [17, 16, 19, 34],
		19: [16, 15, 18, 34, 20, 33],
		20: [19, 15, 14, 13, 21, 33, 32, 31],
		21: [12, 13, 20, 31, 23, 22],
		22: [12, 21, 23],
		23: [21, 22, 31, 24],
		24: [23, 31, 26, 25],
		25: [24, 26],
		26: [25, 24, 31, 28, 27],
		27: [26, 28],
		28: [27, 26, 31, 29],
		29: [28, 31, 32, 30, 48],
		30: [29, 48, 32, 37, 38],
		31: [21, 20, 32, 29, 28, 26, 24, 23],
		32: [20, 33, 35, 37, 30, 29, 31],
		33: [20, 19, 34, 35, 32],
		34: [18, 19, 33],
		35: [33, 36, 37, 32],
		36: [35, 37],
		37: [36, 35, 32, 30, 38],
		38: [37, 30, 39, 46, 47, 48],
		39: [38, 46, 45, 43, 40],
		40: [43, 39, 41],
		41: [40, 42, 43],
		42: [41],
		43: [40, 41, 42, 39, 44, 45],
		44: [43, 45],
		45: [44, 43, 39],
		46: [47, 38, 39],
		47: [48, 38, 46],
		48: [29, 30, 38, 47],
		49: [3, 9],
		50: [1, 2],
	}



# FOR TESTING
g = game("usa", ("passive", "aggressive"),3)
g.random_dist_terr()
g.run()