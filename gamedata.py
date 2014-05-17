# Game class file
# Takes raw json data and converts to easier/small dicts

from riotapi_py import riotapi_py

class grabgamedata:
    def __init__(self, games):
        self.summoner_id = games['summonerId']
        self.raw_games = games['games']

    def get_game_ids(self):
        self.all_game_ids = []
        for game in self.raw_games:
            self.all_game_ids.append(game['gameId'])

    def get_summoner_ids(self, match):
        self.summoner_ids = []
        for players in match['fellowPlayers']:
            self.summoner_ids.append(players['summonerId'])
        return self.summoner_ids

##    def 
        
        
        
