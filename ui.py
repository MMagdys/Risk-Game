import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon


class GameBoard(object):

	def __init__(self, terriories_map, players, country="usa"):

		self.terriories_map = terriories_map
		self.players = players

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
		# for terr in self.terriories_map:
		# 	if terr.taken_by == self.players[0]:
		# 		seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
		# 		poly = Polygon(seg, facecolor='blue',edgecolor='blue')
		# 		self.ax.add_patch(poly)
		# 	elif terr.taken_by == self.players[1]:
		# 		seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
		# 		poly = Polygon(seg, facecolor='red',edgecolor='red')
		# 		self.ax.add_patch(poly)


		

	def update(self):
		# plt.clear()
		for terr in self.terriories_map:
			if terr.taken_by == self.players[0]:
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='blue',edgecolor='blue')
				self.ax.add_patch(poly)
			elif terr.taken_by == self.players[1]:
				seg = self.country_map.states[self.state_names.index(self.states[terr.id])]
				poly = Polygon(seg, facecolor='red',edgecolor='red')
				self.ax.add_patch(poly)
		

		plt.title('Risk Game')
		plt.show(block=False)







# g = GameBoard("")




# country_map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
# 		projection='lcc',lat_1=33,lat_2=45,lon_0=-95)


# shp_info = country_map.readshapefile('st99_d00','states',drawbounds=True)

# state_names=[]
# for shapedict in country_map.states_info:
# 	statename = shapedict['NAME']
# 	state_names.append(statename)

# states = set()
# for state in state_names:
#     states.add(state)

# print(states, len(states))


# ax = plt.gca()
# # get Texas and draw the filled polygon
# seg = country_map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red',edgecolor='red')
# ax.add_patch(poly)

# seg = country_map.states[state_names.index('Virginia')]
# poly = Polygon(seg, facecolor='blue',edgecolor='blue')
# ax.add_patch(poly)


# plt.title('Risk Game')
# # plt.show()
