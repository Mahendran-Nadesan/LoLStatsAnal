# LoLStatsAnal
# parser_test.py
# Main Routine to get some stats, testing stuff

'''
Written 16/03/2014
	- created main class


'''

from csv_sep import csv_file
from csv_parser import cat_obj
# import 

csv_dir = "C:\Users\Mahen\Documents\LOLStats\\"
csv_txt = "EUW_S4_Stats.csv"


my_file = csv_file(csv_dir, csv_txt)
my_file.open()

print len(my_file.stats)

my_obj = cat_obj(my_file.stats)
# print my_obj.csv_list()
my_obj.by_side()
my_obj.by_champ()

purple_obj = cat_obj(my_obj.purple_side)
purple_obj.by_champ()

champ_obj = cat_obj(my_obj.champs.values())
# for i in purple_obj.champs.values():
	# print len(i)
print dir(purple_obj.champs)
print len(purple_obj.champs['Amumu'])
print champ_obj.csv_list


# for i in purple_obj.champs:
	# print i, len(purple_obj.champs[i])
	
# print purple_obj.champs.keys()
# print purple_obj.champs.values()

for i in champ_obj.csv_list:
	print i