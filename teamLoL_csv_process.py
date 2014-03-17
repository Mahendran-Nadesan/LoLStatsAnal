# Python script for LoL stats - team stuff
# Uses a csv file, computes and presents data
#
# To do:
# Add a predictor (maybe like the twitter project)

import csv
import math
from operator import itemgetter

# import csv
csv_dir = "C:\Users\Mahen\Documents\LOLStats"
csv_file = "EUW_S4_Stats.csv"

all_stats = []
with open("C:\Users\Mahen\My Documents\\LOLStats\EUW_S4_Stats.csv",'r') as f:
	reader = csv.reader(f)
	for row in reader:
		all_stats.append(row)
		
# delete initial line
all_stats.pop(0)

all_games_champs = []
all_allies
for game in all_stats:
	all_games_champs.append([game[23:31])
	
print all_games_champs	
	
	

