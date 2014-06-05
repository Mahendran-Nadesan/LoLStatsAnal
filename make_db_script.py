# Script to manually make the necessary database
# with necessary tables
# Eventually add error checking like in Thomas' https://github.com/blipped/PosterCreator/blob/master/DatabaseHandler.py

'''
DB: "LoLStatsApp"
"127.0.0.1" "root" "" ""

Tables:
1. Player Details (playerId)
2. Match Details (gameId)
3. Players Stats (gameId + SummonerIds)
4. Team Stats (gameId + SummonerIds + side)
'''

import MySQLdb

# Creates the entire database from scratch if not found

db_name = "LoLStatsApp"
db = MySQLdb.connect("127.0.0.1","root","","") 
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS {s}".format(s=db_name))
cursor.execute("USE {s}".format(s=db_name)) 

table_columns_names = {"PlayerDetails": ["SummonerName", "PlayerID", "Server"],
               "MatchGeneralDetails": ["GameID", "GameType", "SubType", "GameDate", "MapID", "Duration", "Side", "Win"],
               "MatchPlayerDetails": ["GameID", "SummonerID", "ChampionID","assists","barracksKilled","championsKilled","doubleKills","firstBlood"
                                      ,"goldEarned","goldSpent","item0","item1","item2","item3","item4","item5","item6"
                                      ,"killingSprees","largestCriticalStrike","largestKillingSpree","largestMultiKill"
                                      ,"level","magicDamageDealtPlayer","magicDamageDealtToChampions","magicDamageTaken"
                                      ,"minionsKilled","neutralMinionsKilled","neutralMinionsKilledEnemyJungle"
                                      ,"neutralMinionsKilledYourJungle","nexusKilled","numDeaths","pentaKills"
                                      ,"physicalDamageDealtPlayer","physicalDamageDealtToChampions","physicalDamageTaken"
                                      ,"quadraKills","sightWardsBought","spell1","spell2","team","timePlayed","totalDamageDealt"
                                      ,"totalDamageDealtToChampions","totalDamageTaken","totalHeal"
                                      ,"totalTimeCrowdControlDealt","totalUnitsHealed","tripleKills","trueDamageDealtPlayer"
                                      ,"trueDamageDealtToChampions","trueDamageTaken","turretsKilled","visionWardsBought"
                                      ,"wardKilled","wardPlaced","win"],
               "MatchTeamDetails": ["GameID", "PlayerID", "Side"]}

table_columns_types = {"PlayerDetails": ["VARCHAR(20)", "INT(10)", "VARCHAR(20)"],
               "MatchGeneralDetails": ["INT(15)", "VARCHAR(50)", "VARCHAR(50)", "VARCHAR(30)", "VARCHAR(50)", "INT(10)", "INT(10)", "BOOLEAN"],
               "MatchPlayerDetails": ["INT(15)", "INT(10)","INT(10)","INT(10)","INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)","INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","BOOLEAN","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","INT(10)","INT(10)"
                                      ,"INT(10)","INT(10)","BOOLEAN"],
               "MatchTeamDetails": ["INT(15)", "INT(10)", "INT(10)"]}

dic_strings = {}

for dic in sorted(table_columns_names):
    dic_strings[dic] = "CREATE TABLE IF NOT EXISTS {s} (".format(s=dic)
    for i, str_value in enumerate(table_columns_names[dic]):
        print i, str_value, table_columns_types[dic][i]
        dic_strings[dic] += "{c} {t}, ".format(c=str_value, t=table_columns_types[dic][i])
    dic_strings[dic] = dic_strings[dic][0:-2]    
    dic_strings[dic] += ")"
        
for dic in sorted(table_columns_names):
    cursor.execute(dic_strings[dic])

# Command to delete table:
# cursor.execute("DROP TABLE {n}".format(n=??))
