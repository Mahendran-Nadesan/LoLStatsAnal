# Riot API for Python
# Initial API wrapper for my purposes/tests
# Current key: e20154f8-3601-40ac-ae35-5af13e62cc8c (mn.norm.reg@gmail.com)
#
# 31/5:
# -     by_name and by_id now accept multiple or single names/ids, as long as multiples are couched in a list.
#       That needs a fix, dealing with **kwargs (issue is that "static=False" follows)


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

        def get_summoners_by_name(self, summoner_list, static=False):
                if str(type(summoner_list)) == "<type \'list\'>":
                        pass
                else:
                        summoner_list = [summoner_list, ]
                return self.send_request(self.versions['gsbn']+"/summoner/by-name/{names}".format(names=",".join([str(i) for i in summoner_list]))) 

        def get_summoners_by_id(self, summoner_list, static=False):
                if str(type(summoner_list)) == "<type \'list\'>":
                        pass
                else:
                        summoner_list = [summoner_list, ]
                return self.send_request(self.versions['gsbid']+"/summoner/{ids}".format(ids=",".join([str(i) for i in summoner_list])))

        def get_games_by_name(self, summoner, static=False):
                summoner = self.get_summoners_by_name(summoner)
                summonerid = summoner[summoner.keys()[0]]['id']
                return self.get_games_by_summoner_id(summonerid)
       
        def get_games_by_summoner_id(self, summonerid_list, static=False):
                if str(type(summonerid_list))== "<type /'list\'>":
                        pass
                else:
                        summonerid_list = [summonerid_list]
                return self.send_request(self.versions['ggbid']+"/game/by-summoner/{ids}/recent".format(ids=",".join([str(i) for i in summonerid_list])))

        

        
                

                
                
                




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

##Traceback (most recent call last):
##  File "C:\Users\Mahen\workspace\LoLStatsAnal\main.py", line 34, in <module>
##    summoner = api_instance.get_summoners_by_name(summoner_name, "euw")
##  File "C:\Users\Mahen\workspace\LoLStatsAnal\riotapi_py.py", line 37, in get_summoners_by_name
##    return self.send_request(self.versions['gsbn']+"/summoner/by-name/{names}".format(names=",".join([str(i) for i in summoner_list])))
##  File "C:\Users\Mahen\workspace\LoLStatsAnal\riotapi_py.py", line 29, in send_request
##    self.r = requests.get(self.base_url+"{static}{region}/{request}?api_key={key}".format(static='static/' if static else '', region=self.region, request=request, key=self.api_key))
##  File "C:\Python27\lib\site-packages\requests\api.py", line 55, in get
##    return request('get', url, **kwargs)
##  File "C:\Python27\lib\site-packages\requests\api.py", line 44, in request
##    return session.request(method=method, url=url, **kwargs)
##  File "C:\Python27\lib\site-packages\requests\sessions.py", line 361, in request
##    resp = self.send(prep, **send_kwargs)
##  File "C:\Python27\lib\site-packages\requests\sessions.py", line 464, in send
##    r = adapter.send(request, **kwargs)
##  File "C:\Python27\lib\site-packages\requests\adapters.py", line 356, in send
##    raise ConnectionError(e)
##ConnectionError: HTTPSConnectionPool(host='prod.api.pvp.net', port=443): Max retries exceeded with url: /api/lol/euw/v1.4/summoner/by-name/nadsofmahen?api_key=e20154f8-3601-40ac-ae35-5af13e62cc8c (Caused by <class 'socket.gaierror'>: [Errno 11004] getaddrinfo failed)
