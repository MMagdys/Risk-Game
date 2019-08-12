import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from matplotlib.widgets import Button
from game import Game
from player import PassiveAgent, AggressiveAgent, Pacifist, HumanAgent
from ai import GreedyAgent, AstarAgent, MiniMaxNode

TYPE = {"passive": PassiveAgent, "aggressive": AggressiveAgent, "pacifist": Pacifist,
		"greedy": GreedyAgent, "astar": AstarAgent, "human": HumanAgent, "minimax": MiniMaxNode}


class GameBoard(object):

	def __init__(self, ply_type, terriories_map=None, number=2, country="usa"):

		self.players = []
		self.human = None
		self.game = Game("usa", armies=3)
		self.terriories_map = self.game.territories

		for p in range(number):
			if ply_type[p] == "human":
				self.human = TYPE[ply_type[p]]()
				self.players.append(self.human)

			elif ply_type[p] == "minimax":
				self.players.append(TYPE[ply_type[p]](self.game.territories, self.players[0]))

			else:
				self.players.append(TYPE[ply_type[p]]())

		
		self.game.players = self.players
		self.game.random_dist_terr()

		self.texts = []


		self.country_map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
		projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

		self.shp_info = self.country_map.readshapefile('st99_d00','states',drawbounds=True)
		self.ax = plt.gca()

		self.state_names=[]
		for shapedict in self.country_map.states_info:
			statename = shapedict['NAME']
			self.state_names.append(statename)
		# print(self.state_names)
		
		for terr in self.terriories_map:
			if terr.taken_by == self.players[0]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(id2name[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(id2name[terr.id])]
				poly = Polygon(seg, facecolor='blue',edgecolor='blue')
				self.ax.add_patch(poly)
			elif terr.taken_by == self.players[1]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(id2name[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(id2name[terr.id])]
				poly = Polygon(seg, facecolor='red',edgecolor='red')
				self.ax.add_patch(poly)

		plt.title('Risk Game')

		if self.human:
			cid = plt.gcf().canvas.mpl_connect("button_press_event", lambda event: self.onclick(event))
		
		plt.gcf().canvas.mpl_connect('key_press_event', self.press)
		# plt.plot('-b', label=self.players[0])
		# plt.plot('-r', label=self.players[1])
		# plt.legend(loc='lower right')
		plt.show()

		

	def update(self):
		# Clear all previous number of troops in each territory
		# print(self.texts)
		for txt in self.texts:
			txt.remove()
		self.texts = []
		plt.draw()

		# Update the map with the new game state
		for terr in self.terriories_map:
			if terr.taken_by == self.players[0]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(id2name[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(id2name[terr.id])]
				poly = Polygon(seg, facecolor='blue',edgecolor='blue')
				self.ax.add_patch(poly)
			elif terr.taken_by == self.players[1]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(id2name[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(id2name[terr.id])]
				poly = Polygon(seg, facecolor='red',edgecolor='red')
				self.ax.add_patch(poly)
			else:
				seg = self.country_map.states[self.state_names.index(id2name[terr.id])]
				poly = Polygon(seg, facecolor='white',edgecolor='white')
				self.ax.add_patch(poly)
		
		plt.draw()



	def onclick(self, event):

		self.human.play(event, self, plt)
		print(self.human.territories)

		self.update()
		


	def press(self, event):
		
		if self.game.turn():
			self.update()





id2name = {
	1 : "Washington",
	2 : "Oregon",
	3 : "California",
	4 : "Nevada",
	5 : "Idaho",
	6 : "Montana",
	7 : "Wyoming",
	8 : "Utah",
	9 : "Arizona",
	10 : "Colorado",
	11 : "New Mexico",
	12 : "Texas",
	13 : "Oklahoma",
	14 : "Kansas",
	15 : "Nebraska",
	16 : "South Dakota",
	17 : "North Dakota",
	18 : "Minnesota",
	19 : "Iowa",
	20 : "Missouri",
	21 : "Arkansas",
	22 : "Louisiana",
	23 : "Mississippi",
	24 : "Alabama",
	25 : "Florida",
	26 : "Georgia",
	27 : "South Carolina",
	28 : "North Carolina",
	29 : "Virginia",
	30 : "West Virginia",
	31 : "Tennessee",
	32 : "Kentucky",
	33 : "Illinois",
	34 : "Wisconsin",
	35 : "Indiana",
	36 : "Michigan",
	37 : "Ohio",
	38 : "Pennsylvania",
	39 : "New York",
	40 : "Vermont",
	41 : "New Hampshire",
	42 : "Maine",
	43 : "Massachusetts",
	44 : "Rhode Island",
	45 : "Connecticut",
	46 : "New Jersey",
	47 : "Delaware",
	48 : "Maryland",
	49 : "Hawaii",
	50 : "Alaska",
}

# FOR TESTING
# g = Game("usa", ("passive", "human"),3)
# g.random_dist_terr()

# gui = GameBoard(g.territories, g.players)
gui = GameBoard(("pacifist", "minimax"))



