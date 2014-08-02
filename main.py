# Temporary main file # # Call the RiotApiPy # Sort it into a main 
# var/dict # Call/Write to database # Call GUI 

# Imports
from __future__ import division # must be first import
from riotapi_py import RiotApiPy 
from gamedata import grabgamedata
from staticdata import GrabStaticData
from dbconnection import aux_db
from rankeddata import GrabRankedData
from LoLTeamCheckerGUI import LoLTeamChecker
import MySQLdb
import collections 

########################################################
# Some functions

#########################################################
##import lolapp_gui 

# RiotApiPy 
# Later, code regions into RiotApiPy
# Add RiotLimit...
api_key = "e20154f8-3601-40ac-ae35-5af13e62cc8c" 
region = "euw" 
versions = {"gsbn": "v1.4", "gsbid": "v1.4", "ggbid": "v1.3", "grsbid": "v1.3", "sgcbid": "v1.2"} 

api_instance = RiotApiPy(api_key, versions, region) 
##api_instance = RiotApiPy() 

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

# Get champion static data
champdata = api_instance.static_get_champion_list()
staticdata = GrabStaticData(champdata)

# Get ranked data *for a single player* and sort
player_ranked_data = GrabRankedData(api_instance.get_ranked_stats_by_summoner_id(playerid, 4))

# Get stats for a single champ
##champ_stats = {}
##relevant_stats = {}
##champ_stats['Corki'] = player_ranked_data.get_stats_by_champid(staticdata.get_champid('Corki'))
##for i in player_ranked_data.relevant_stat_names:
##	if champ_stats['Corki'].has_key(i):
##		relevant_stats[i] = champ_stats['Corki'][i]
player_ranked_data.make_relevant(player_ranked_data.get_stats_by_champid(staticdata.get_champid('Corki')))
final_stats = player_ranked_data.get_averages(player_ranked_data.relevant_stats)

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
##currgame = mygamedata.all_game_ids[0]
##all_stats = []
##all_stats.append(mygamedata.get_same_game(currgame))
##
##print "Starting data retrieval"
##for i in mygamedata.summoner_ids[currgame]:
##    playergames = api_instance.get_games_by_summoner_id(i)
##    gamedata = grabgamedata(playergames)
##    if gamedata.can_find_same_game(currgame) == True:
##        all_stats.append(gamedata.get_same_game(currgame))
##    else:
##        print "This game not found for this player: {p}.".format(p=i)
##        
##
##            
##print all_stats[0].keys()
##for i in all_stats:
##	print "Champ: {c} Kills: {k} Deaths: {d} Assists: {a}".format(c=i['ChampionID'], k=i['championsKilled'], d=i['numDeaths'], a=i['assists'])


# Some pseudocode:
##for game in allthegames:
##    game_player_data = []
##    for summonerid in allsummoners:
##        get all the ids:
##            find the same game
##            append the game
##    write the data to db (basically, in groups of 10)            
'''        
# Bigger test (without the db check for redundant game_ids)
db_name = "LoLStatsApp"
db = MySQLdb.connect("127.0.0.1","root","","") 
cursor = db.cursor()
cursor.execute("USE {s}".format(s=db_name))
table = aux_db("MatchPlayerDetails", cursor)

for game_num, game in enumerate(mygamedata.all_game_ids):
    mygamedata.get_summoner_ids(mygamedata.raw_games[game_num])
    all_stats = []
    all_stats.append(mygamedata.get_same_game(game))
    print "Data retrieval game {num}".format(num=game)
    for i in mygamedata.summoner_ids[game]:
        playergames = api_instance.get_games_by_summoner_id(i)
        gamedata = grabgamedata(playergames)
        if gamedata.can_find_same_game(game) == True:
            all_stats.append(gamedata.get_same_game(game))
            
        else:
            print "This game not found for this player: {p}.".format(p=i)
    print "-----------------"
    print " Game {num}    ".format(num=game)
    print "-----------------"
    for i in all_stats:
        print "Champ: {c} Kills: {k} Deaths: {d} Assists: {a}".format(c=i['ChampionID'], k=i['championsKilled'], d=i['numDeaths'], a=i['assists'])
        table.write_to_db("insert_string", i)

db.commit()
    
   '''                  
                     


##for i, k in enumerate(all_stats):
##	print "Summoner {n}".format(n=i+1)
##	for j, l in enumerate(all_stats[i]):
##		print all_stats[i].keys()[j], ": ", all_stats[i][l]
##        print

mygui = LoLTeamChecker()
mygui.mainloop()
