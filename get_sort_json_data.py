# Script for player/game data extraction for larger code
# Assume gamedata has been used, like so:
# 
# recent_games = api_
# for playerid in gameid:
#       game = grabgamedata     

# Imports 
from riotapi_py import riotapi_py 
from gamedata import grabgamedata 
##import dbconnection from dbconnection import aux_db 
import MySQLdb
import collections 

# Functions

def can_find_same_game(gameid, gamedata):
    gamedata.get_game_ids()
    if gameid in gamedata.all_game_ids:
        return True
    else:
        return False

def get_same_game(gameid, ):
    




def initiate_stuff(playerid):
    recent_games = api_instance.get_games_by_summoner_id(playerid)
    recent_game_data = grabgamedata(recent_games)
    return recent_game_data





table_mpd = ["GameID", "SummonerID", "ChampionID","assists","barracksKilled"
             ,"championsKilled","doubleKills","firstBlood","goldEarned"
             ,"goldSpent","item0","item1","item2","item3","item4","item5"
             ,"item6","killingSprees","largestCriticalStrike"
             ,"largestKillingSpree","largestMultiKill","level"
             ,"magicDamageDealtPlayer","magicDamageDealtToChampions"
             ,"magicDamageTaken","minionsKilled","neutralMinionsKilled"
             ,"neutralMinionsKilledEnemyJungle","neutralMinionsKilledYourJungle"
             ,"nexusKilled","numDeaths","pentaKills","physicalDamageDealtPlayer"
             ,"physicalDamageDealtToChampions","physicalDamageTaken"
             ,"quadraKills","sightWardsBought","team","timePlayed"
             ,"totalDamageDealt","totalDamageDealtToChampions"
             ,"totalDamageTaken","totalHeal","totalTimeCrowdControlDealt"
             ,"totalUnitsHealed","tripleKills","trueDamageDealtPlayer"
             ,"trueDamageDealtToChampions","trueDamageTaken","turretsKilled"
             ,"visionWardsBought","wardKilled","wardPlaced","win"]


# Check, sort, and get data values for the player
gamestats = 
# check
if len(:
       
