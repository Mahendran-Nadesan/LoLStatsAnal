# LoLStatsAnal
# csv_parser.py
# Main Class for separating data from list made from csv files, assumes csv has been opened and 
# processed elsewhere

'''
Written 12/03/2014
	- created main class


'''

'''
Current List Format:
[0-10]gamenum,champ,side,time(m),time(s),result,k,d,a,cs,gold
[11-20]tk,td,ta,tcs,tgold,ek,ed,ea,ecs,egold
[21]lp
[22-30]t1,t2,t3,t4,e1,e2,e3,e4,e5
[31]info

Main Methods:

1. By Champ
2. By Side
3. By Allies
4. By Enemies

Main Attributes:

1. blue_side
2. purple_side
3. no_side
4. champs = {'champ 1':[[game 1], [game 2]], 'champ 2': [[game 1], [game 2]]}
'''

# Imports


class cat_obj:
	def __init__(self, csv_list):
		self.csv_list = list(csv_list)
		self.create_empty_lists()
		
	def create_empty_lists(self):
		self.blue_side = []
		self.purple_side = []
		self.no_side = []
		self.champs = {}
	
	def by_side(self):
		for game in self.csv_list:
			if game[2] == 'blue':
				self.blue_side.append(game)
			elif game[2] == 'purple':
				self.purple_side.append(game)
			else:
				self.no_side.append(game)
				
	def by_champ(self):
		for game in self.csv_list:
			if game[1] in self.champs.keys():
				pass
			else:
				self.champs[game[1]] = []
			
			self.champs[game[1]].append(game)
			
			
		
	





