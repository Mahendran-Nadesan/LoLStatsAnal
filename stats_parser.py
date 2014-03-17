# LoLStatsAnal
# stats_parser.py
# Main Class for creating stats

'''
Written 16/03/2014
	- created main class


'''

'''
Current List Format:
[0-10]gamenum,champ,side,time(m),time(s),result,k,d,a,cs,gold
[11-20]tk,td,ta,tcs,tgold,ek,ed,ea,ecs,egold
[21]lp
[22-30]t1,t2,t3,t4,e1,e2,e3,e4,e5
[31]info

Main Attributes:

1. Total Games, Total Wins, Total Losses, Total % Wins, Total % Losses
2. Blue Games, Blue Wins, Blue Losses, Blue % Wins, Blue % Losses
3. Purple Games, Purple Wins, Purple Losses, Purple % Wins, Purple % Losses
4. Total (K&D&A), Wins (K&D&A), Losses(K&D&A)
5. Blue (K&D&A), Blue Wins (K&D&A), Blue Losses (K&D&A)
6. Purple (K&D&A), Purple Wins (K&D&A), Purple Losses (K&D&A)


'''

from csv_parser import cat_obj

class stats_obj:
	def __init__(self, cat_obj):
		self.totalg = {}
		self.blueg = {}
		self.purpleg = {}
		self.totalkda = {}
		self.bluekda = {}
		
		
		

