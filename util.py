from territory import Territory


def map_to_terr(country_map):

	terr = []
	for i in country_map:
		# print(i, country_map[i])
		terr.append(Territory(i))

	# print(len(country_map))
	for i in country_map:
		for n in country_map[i]:
			# print(i, n)
			terr[i-1].neighbours.append(terr[n-1])
			# print(terr[i].neighbours)
	
	return terr



# FOR TESTING
# usaMap = {
# 		1: [2, 50, 5],
# 		2: [3, 4, 5, 1],
# 		3: [2, 4],
# 		4: [2, 3, 5, 8, 9],
# 		5: [1, 2, 4, 6, 7, 8],
# 		6: [5, 7, 16, 17],
# 		7: [6, 5, 8, 10, 15, 16],
# 		8: [4, 5, 7, 10, 9, 11],
# 		9: [8, 10, 11],
# 		10: [7, 8, 9, 11],
# 		11: [8, 9, 10, 12, 13],
# 		12: [11, 13, 22, 21],
# 		13: [12, 10, 11, 14],
# 		14: [10, 15, 13, 20],
# 		15: [10, 7, 16, 19, 20, 14],
# 		16: [7, 6, 17, 18, 19, 15],
# 		17: [6, 16, 18],
# 		18: [17, 16, 19, 34],
# 		19: [16, 15, 18, 34, 20, 33],
# 		20: [19, 15, 14, 13, 21, 33, 32, 31],
# 		21: [12, 13, 20, 31, 23, 22],
# 		22: [12, 21, 23],
# 		23: [21, 22, 31, 24],
# 		24: [23, 31, 26, 25],
# 		25: [24, 26],
# 		26: [25, 24, 31, 28, 27],
# 		27: [26, 28],
# 		28: [27, 26, 31, 29],
# 		29: [28, 31, 32, 30, 48],
# 		30: [29, 48, 32, 37, 38],
# 		31: [21, 20, 32, 29, 28, 26, 24, 23],
# 		32: [20, 33, 35, 37, 30, 29, 31],
# 		33: [20, 19, 34, 35, 32],
# 		34: [18, 19, 33],
# 		35: [33, 36, 37, 32],
# 		36: [35, 37],
# 		37: [36, 35, 32, 30, 38],
# 		38: [37, 30, 39, 46, 47, 48],
# 		39: [38, 46, 45, 43, 40],
# 		40: [43, 39, 41],
# 		41: [40, 42, 43],
# 		42: [41],
# 		43: [40, 41, 42, 39, 44, 45],
# 		44: [43, 45],
# 		45: [44, 43, 39],
# 		46: [47, 38, 39],
# 		47: [48, 38, 46],
# 		48: [29, 30, 38, 47],
# 		49: [3, 9],
# 		50: [1, 2],
# 	}


# t = map_to_terr(usaMap)
# print(t[1].neighbours)

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
	49 : "",
	50 : "",

}