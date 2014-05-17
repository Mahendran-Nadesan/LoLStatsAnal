# Riot API for Python
# Initial API wrapper for my purposes/tests
# Current key: e20154f8-3601-40ac-ae35-5af13e62cc8c (mn.norm.reg@gmail.com)
#



# Imports
import requests


class riotapi_py:
        def __init__(self, api_key, rate_limit, versions, default_region="euw"):
                self.api_key = api_key
                self.default_region = default_region
                self.region = self.default_region
                self.rate_limit = rate_limit
                self.versions = versions
                self.base_url = "https://prod.api.pvp.net/api/lol/"

        def __str__(self):
                pass

        def send_request(self, request, static=False, **kwargs):
                if self.region is None:
                        self.region = self.default_region
                self.r = requests.get(self.base_url+"{static}{region}/{request}?api_key={key}".format(static='static/' if static else '', region=self.region, request=request, key=self.api_key))
                return self.r.json()

        def get_summoner_by_name(self, summoner_list, static=False):
                return self.send_request(self.versions['gsbn']+"/summoner/by-name/{names}".format(names=",".join([summoner_list]))) 

        def get_summoner_by_id(self, summoner_list, static=False):
##                summonerid_list = []
##                summoner_list = [summoner_list]
##                for summoner in summoner_list:
##                        summonerid_list.append(str(summoner))
                return self.send_request(self.versions['gsbid']+"/summoner/{ids}".format(ids=",".join([str(i) for i in summoner_list])))

        def get_games_by_name(self, summoner_list, static=False):
                summonerid_list = []
                summoner_list = [summoner_list]
                for name in summoner_list:
                        summoner = self.get_summoner_by_name(name)
                        summonerid_list.append(str(summoner[summoner.keys()[0]]['id']))
                return self.get_games_by_summoner_id(summonerid_list)
       
        def get_games_by_summoner_id(self, summonerid_list, static=False):
                return self.send_request(self.versions['ggbid']+"/game/by-summoner/{ids}/recent".format(ids=",".join(summonerid_list)))

        

        
                

                
                
                




##main_url = "https://prod.api.pvp.net/api/lol"
##static_url = "https://prod.api.pvp.net/api/lol/static-data"
##region = "euw"
##key = 
##
### Eventually grab versions off https://developer.riotgames.com/api/methods (learn html parsing beautiful soup?)
##vers_staticdata = "v1.2"
##vers_game = "v1.3"
##vers_summoner = "v1.4"
##versions = [vers_staticdata, vers_game, vers_summoner]
# Grab summoner by name, store ID (for other requests)


