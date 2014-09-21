# -*- coding: latin-1 -*-

"""
Riot API for Python
Initial API wrapper for my purposes/tests Current key:
e20154f8-3601-40ac-ae35-5af13e62cc8c (mn.norm.reg@gmail.com) 31/5:  -
by_name and by_id now accept multiple or single names/ids, as long as
multiples are couched in a list. That needs a fix, dealing with
**kwargs (issue is that"static=False" follows)
"""

# Imports
import requests
import time
import collections

class RateLimit:
        """ Taken from https://github.com/pseudonym117/Riot-Watcher/blob/master/riotwatcher.py"""
        def __init__(self, allowed_requests, seconds):
            self.allowed_requests = allowed_requests
            self.seconds = seconds
            self.made_requests = collections.deque()

        def __reload(self):
            t = time.time()
            while len(self.made_requests) > 0 and self.made_requests[0] < t:
                self.made_requests.popleft()

        def add_request(self):
            self.made_requests.append(time.time() + self.seconds)

        def can_request(self):
            self.__reload()
            return len(self.made_requests) < self.allowed_requests

class RiotApiPyException(Exception):
        def __init__(self, error):
                self.error_codes = {400: "Bad Request", 401:
                                    "Unauthorised", 404:
                                    "Not Found", 429: "Too many"
                                    " Requests", 500: "Internal"
                                    " Service Error", 503: "Service"
                                    " Unavailable"}
                self.error = self.error_codes[error]
                
        def __str__(self):
                return self.error
                     

class RiotApiPy:
        """ Main API for the Riot API, handling requests and returning
        limited stats. Currently supports only player stats."""

        def __init__(self, api_key, versions, region, limits = (RateLimit(10,
        10), RateLimit(500,600), ),default_region="euw"):
                self.api_key = api_key
                self.default_region = default_region
                self.region = region
                self.versions = versions
                self.limits = limits
                self.error = []
                self.base_url = "https://{region}.api.pvp.net/api/lol/".format(region=self.region)
                                

        def __str__(self):
                self.info = {'api_key': self.api_key, 'default_region': self.default_region
                             , 'region': self.region, 'rate_limit':
                             self.limits, 'versions':
                             self.versions}
                return self.info.__str__()

        def send_request(self, request, static=False, **kwargs):
                print str(request)
                for lim in self.limits:
                    if lim.can_request():
                        lim.add_request()
                    else:
                        print "nope"
                if self.region is None:
                        self.region = self.default_region
                print self.region

                try:
                        self.r = requests.get("https://{proxy}.api."
                                              "pvp.net/api/lol/"
                                              "{static}{region}/"
                                              "{req}?{secondary}"
                                              "api_key={key}".format
                                              (proxy="global"
                                              if static else
                                              self.region,
                                              static='static-data/'
                                              if static else
                                              '',region=self.region,
                                              req=str(request[0]),
                                              secondary=request[1],
                                              key=self.api_key))
                        print self.r.url

                        return self.r.json()
                except:
                        self.error = RiotApiPyException(self.r.status_code)
                        raise self.error # This is an important line


        def get_summoners_by_name(self, summoner_list, static=False):
                if str(type(summoner_list)) == "<type \'list\'>":
                    pass
                else:
                    summoner_list = [summoner_list, ]
                return self.send_request([self.versions['gsbn']+"/summoner/by-name/{names}".format(names=",".join([str(i) for i in summoner_list])), ""]) 

        def get_summoners_by_id(self, summoner_list, static=False):
                if str(type(summoner_list)) == "<type \'list\'>":
                        pass
                else:
                        summoner_list = [summoner_list, ]
                return self.send_request([self.versions['gsbid']+"/summoner/{ids}".format(ids=",".join([str(i) for i in summoner_list])), ""])

        def get_games_by_name(self, summoner, static=False):
                summoner = self.get_summoners_by_name(summoner)
                summonerid = summoner[summoner.keys()[0]]['id']
                return self.get_games_by_summoner_id(summonerid)
       
        def get_games_by_summoner_id(self, summonerid_list, static=False):
                if str(type(summonerid_list))== "<type /'list\'>":
                        pass
                else:
                        summonerid_list = [summonerid_list]
                return self.send_request([self.versions['ggbid']+"/game/by-summoner/{ids}/recent".format(ids=",".join([str(i) for i in summonerid_list])), ""])

        def get_match_history_by_name(self, summoner, static=False):
                summoner = self.get_summoners_by_name(summoner)
                summonerid = summoner[summoner.keys()[0]]['id']
                return self.get_match_history_by_summoner_id(summonerid)
       
        def get_match_history_by_summoner_id(self, summonerid_list, static=False):
                if str(type(summonerid_list))== "<type /'list\'>":
                        pass
                else:
                        summonerid_list = [summonerid_list]
                return self.send_request([self.versions['gmhbid']+"/matchhistory/{ids}".format(ids=",".join([str(i) for i in summonerid_list])), ""])

        def get_ranked_stats_by_summoner_id(self, summonerid, season, static=False):
                if str(type(summonerid))== "<type /'int\'>":
                        pass
                else:
                        summonerid = int(summonerid)
                return self.send_request([self.versions['grsbid']+"/stats/by-summoner/{ids}/ranked".format(ids=str(summonerid)), "season=SEASON{s}&".format(s=season)])

        def static_get_champion_list(self):
                return self.send_request([self.versions['sgcbid']+"/champion", ""], static=True)

        def static_get_champion_by_id(self, championid):
                return self.send_request([self.versions['sgcbid']+"/champion/{champ}".format(champ=str(championid)), ""], static=True)
                

        

        
                

                
                
                




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
