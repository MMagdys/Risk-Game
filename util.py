from territory import Territory


def map_to_terr(country_map):

	terr = []
	for i in country_map:
		# print(i, country_map[i])
		terr.append(Territory(i, country_map[i]))
	return terr



# FOR TESTING
# t = map_to_terr(usaMap)
# print(t[0].neighbours)