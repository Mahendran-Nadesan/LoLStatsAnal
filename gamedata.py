# Game class file
# Takes raw json data and converts to easier/small dicts
# Considered making it work on the basis of summoner id, but I want all classes to be standalone.

##from riotapi_py import riotapi_py
import collections

class grabgamedata:
    def __init__(self, games):
        self.summoner_id = games['summonerId']
        self.raw_games = games['games']
        self.summoner_ids = {}
        self.table_mpd = ["GameID", "SummonerID", "ChampionID", "assists","barracksKilled"
             ,"championsKilled","doubleKills","firstBlood","goldEarned"
             ,"goldSpent","item0","item1","item2","item3","item4","item5"
             ,"item6","killingSprees","largestCriticalStrike"
             ,"largestKillingSpree","largestMultiKill","level"
             ,"magicDamageDealtPlayer","magicDamageDealtToChampions"
             ,"magicDamageTaken","minionsKilled","neutralMinionsKilled"
             ,"neutralMinionsKilledEnemyJungle","neutralMinionsKilledYourJungle"
             ,"nexusKilled","numDeaths","pentaKills","physicalDamageDealtPlayer"
             ,"physicalDamageDealtToChampions","physicalDamageTaken"
             ,"quadraKills","sightWardsBought","spell1","spell2","team","timePlayed"
             ,"totalDamageDealt","totalDamageDealtToChampions"
             ,"totalDamageTaken","totalHeal","totalTimeCrowdControlDealt"
             ,"totalUnitsHealed","tripleKills","trueDamageDealtPlayer"
             ,"trueDamageDealtToChampions","trueDamageTaken","turretsKilled"
             ,"visionWardsBought","wardKilled","wardPlaced","win"]


    def can_find_same_game(self, gameid):
        self.get_game_ids()
        if gameid in self.all_game_ids:
            return True
        else:
            return False

    def get_same_game(self, gameid):
        gamenum = self.all_game_ids.index(gameid)
        return self.get_all_mpd(self.raw_games[gamenum])
            
    def get_game_ids(self):
        self.all_game_ids = []
        for game in self.raw_games:
            self.all_game_ids.append(game['gameId'])

    def get_summoner_ids(self, match):
        self.summoner_ids[match['gameId']] = []
        for players in match['fellowPlayers']:
            self.summoner_ids[match['gameId']].append(players['summonerId'])
        return self.summoner_ids[match['gameId']]

    def get_raw_stats(self, match):
        return sorted(match['stats'])

    def get_game_by_id(self, gameid):
        self.game = []
        for games in self.raw_games:
            if games['gameId'] == gameid:
                self.game = games
                break
        return self.game
                
    def get_all_mpd(self, matchvar):
        all_stats = collections.OrderedDict()
        all_stats['GameID'] = matchvar['gameId']
        all_stats['SummonerID'] = self.summoner_id
        all_stats['ChampionID'] = matchvar['championId']
        for i in self.table_mpd:
            if i in matchvar['stats'].keys():
                all_stats[i] = matchvar['stats'][i]
            elif i in all_stats.keys():
                pass
            else:
                all_stats[i] = 0
        all_stats['spell1'] = matchvar['spell1']
        all_stats['spell2'] = matchvar['spell2']
        # final_stats = collections.OrderedDict(sorted(all_stats.items(), key=lambda item: item[0]))
        final_stats = collections.OrderedDict(all_stats)
        return final_stats

        
        
