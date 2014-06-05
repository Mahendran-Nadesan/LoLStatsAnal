# Temporary main file # # Call the riotapi_py # Sort it into a main 
# var/dict # Call/Write to database # Call GUI 

# Imports 
from riotapi_py import riotapi_py 
from gamedata import grabgamedata 
##import dbconnection from dbconnection import aux_db 
import MySQLdb
import collections 

########################################################
# Some functions

#########################################################
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
# For now, this is here, fixed. Later, will have to go into its own 
# class and get called by the GUI 


summoner_name = "nadsofmahen" 
summoner = api_instance.get_summoners_by_name(summoner_name, "euw") 
playerid = str(summoner['nadsofmahen']['id']) 
##print summoner ##summoner = 
api_instance.get_summoners_by_id(playerid, "euw") 
##print summoner 

# Get last 10 games
games = api_instance.get_games_by_summoner_id(playerid, "euw")
newgames = api_instance.get_games_by_name(summoner_name) 

# Make instance of gamedata class
mygamedata = grabgamedata(newgames) 

# Get IDs of 10 games - unsorted, most recent first 
mygamedata.get_game_ids() 
##print mygamedata.all_game_ids 

# This will be looped eventually...
example_match = mygamedata.raw_games[0] 

# Get summoner IDs of other players in example match 
mygamedata.get_summoner_ids(example_match)


### # Eventually: # 1. For all games, # 2. get all summoners, # 3. find 
### relevant match, # 4. get data # Sample:
##data_dump = {} 
### 1. and 2. 
##for game in mygamedata.raw_games: 
##	data_dump[game['gameId']] = mygamedata.get_summoner_ids(game) 
##
### 3. (going to need to start worrying about number of requests now) 
##allgames_summoner_data = {}
##for gameid in data_dump:
##	allgames_summoner_data[gameid] = {}
##	for playerid in data_dump[gameid]:
##		allgames_summoner_data[gameid][playerid] = {}
                
        
# Test functions
currgame = mygamedata.all_game_ids[0]
all_stats = []
all_stats.append(mygamedata.get_same_game(currgame))

for i in mygamedata.summoner_ids[currgame]:
    playergames = api_instance.get_games_by_summoner_id(i)
    gamedata = grabgamedata(playergames)
    if gamedata.can_find_same_game(currgame) == True:
        all_stats.append(gamedata.get_same_game(currgame))
    else:
        print "This game not found for this player."

            
print all_stats[0].keys()
for i in all_stats:
	print "Champ: {c} Kills: {k} Deaths: {d} Assists: {a}".format(c=i['ChampionID'], k=i['championsKilled'], d=i['numDeaths'], a=i['assists'])


##for i, k in enumerate(all_stats):
##	print "Summoner {n}".format(n=i+1)
##	for j, l in enumerate(all_stats[i]):
##		print all_stats[i].keys()[j], ": ", all_stats[i][l]
##        print
