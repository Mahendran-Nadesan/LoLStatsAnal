# Temporary main file
#
# Call the riotapi_py
# Sort it into a main var/dict
# Call/Write to database
# Call GUI



# Imports
from riotapi_py import riotapi_py
from gamedata import grabgamedata
##import dbconnection
from dbconnection import aux_db
import MySQLdb
import collections

##import lolapp_gui



# riotapi_py
# Later, code regions into riotapi_py
api_key = "e20154f8-3601-40ac-ae35-5af13e62cc8c"
region = "euw"
rate_limit = 5
versions = {"gsbn": "v1.4", "gsbid": "v1.4", "ggbid": "v1.3"}

api_instance = riotapi_py(api_key, rate_limit, versions, region)
##api_instance = riotapi_py()


# Get details
# Get main summoner
# For now, this is here, fixed. Later, will have to go into its own class and get called by the GUI
summoner_name = "nadsofmahen"
summoner = api_instance.get_summoner_by_name(summoner_name, "euw")
playerid = str(summoner['nadsofmahen']['id'])
##print summoner
##summoner = api_instance.get_summoner_by_id(["25833884"], "euw")
##print summoner

# Get last 10 games
games = api_instance.get_games_by_summoner_id([playerid], "euw")
newgames = api_instance.get_games_by_name(summoner_name)

# Make instance of gamedata class
mygamedata = grabgamedata(games)

# Get IDs of 10 games - unsorted, most recent first
mygamedata.get_game_ids()
##print mygamedata.all_game_ids

example_match = mygamedata.raw_games[0]

# Get summoner IDs of other players in example match
mygamedata.get_summoner_ids(example_match)

# Eventually:
# 1. For all games,
# 2. get all summoners,
# 3. find relevant match,
# 4. get data
# Sample:
data_dump = {}
# 1. and 2.
for game in mygamedata.raw_games:
	data_dump[game['gameId']] = mygamedata.get_summoner_ids(game)    

# 3. (going to need to start worrying about number of requests now)
##allgames_summoner_data = {}
##for gameid in data_dump.keys():
##	allgames_summoner_data[gameid] = {}
##	for summonerid in data_dump[gameid]:
##		print summonerid

temp_table_names = {}

# Add names from stats for all champs
pr = 'champ'
for x in range(9):
    prn = '{name}{num}_'.format(name=pr, num=str(x+1))
    for i in example_match['stats']:
        temp_table_names['{s}'.format(s=prn+i)] = []
    temp_table_names['{s}spell1'.format(s=prn)] = []
    temp_table_names['{s}spell2'.format(s=prn)] = []

# Add main/early names
table_names = {'gameId': [], 'createDate': [], 'gameMode': [], 'mapId': [], 'gameType': [], 'subType': [], 'gameResult': []}

# Order stat names (dict & list)
od_temp_table_names = collections.OrderedDict(sorted(temp_table_names.items()))
list_temp_table_names = sorted(temp_table_names)

# Remove excess 'win' names (dict & list)
for i in od_temp_table_names.keys():
    if i[-4:] == '_win':
        od_temp_table_names.popitem(i)

for i in list_temp_table_names:
    if i[-4:] == '_win':
        list_temp_table_names.remove(i)

# Add them (dict & list)
new_table_names = collections.OrderedDict(table_names)
for i in od_temp_table_names.keys():
    new_table_names[i] = []

list_table_names = list(table_names)
for i in list_temp_table_names:
    list_table_names.append(i)

### Write to db
db_name = "LoLStatsApp"
db = MySQLdb.connect("127.0.0.1","root","","") 
cur = db.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS {s}".format(s=db_name))
cur.execute("USE {s}".format(s=db_name)) # switch to current db

table_name = "column_naming_test_3"
auxdbinst = aux_db(table_name)
mystr = auxdbinst.create_string("CREATE TABLE", list_table_names)


##command_base = str()
##for i, j in enumerate(list_table_names):
##	command_base = command_base+" {a} {b} {c},".format(a="add column",b=j,c="varchar(20)")

##table = "test_1"
##sql = "alter table {table} {com}".format(table=table, com=command_base)
##cur.execute(sql)


    


