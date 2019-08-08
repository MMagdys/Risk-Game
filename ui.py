import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from game import Game


class GameBoard(object):

	def __init__(self, terriories_map, players, country="usa"):

		self.terriories_map = terriories_map
		self.players = players
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
		
		self.states = set()
		for state in self.state_names:
			self.states.add(state)

		self.states = list(self.states)
		for terr in self.terriories_map:
			if terr.taken_by == self.players[0]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(self.states[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='blue',edgecolor='blue')
				self.ax.add_patch(poly)
			elif terr.taken_by == self.players[1]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(self.states[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='red',edgecolor='red')
				self.ax.add_patch(poly)

		plt.title('Risk Game')
		cid = plt.gcf().canvas.mpl_connect("button_press_event", self.onclick)
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
				s = np.array(self.country_map.states[self.state_names.index(self.states[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='blue',edgecolor='blue')
				self.ax.add_patch(poly)
			elif terr.taken_by == self.players[1]:
				# Number of troops in each state
				s = np.array(self.country_map.states[self.state_names.index(self.states[terr.id])]).mean(axis=0)
				txt = plt.text(s[0],s[1], str(terr.troops), ha="center")
				self.texts.append(txt)
				# Coloring the state
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='red',edgecolor='red')
				self.ax.add_patch(poly)
			else:
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='white',edgecolor='white')
				self.ax.add_patch(poly)
		
		plt.draw()



	def onclick(self, event):
		
		g.turn()
		self.update()



	def press(self, event):
		
		g.turn()
		self.update()





# FOR TESTING
g = Game("usa", ("greedy", "aggressive"),20)
g.random_dist_terr()

gui = GameBoard(g.territories, g.players)


