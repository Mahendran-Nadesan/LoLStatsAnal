# Initial API wrapper for my purposes/tests
# Current key: e20154f8-3601-40ac-ae35-5af13e62cc8c (mn.norm.reg@gmail.com)
#



# Imports
import requests


class riotapi_wrapper:
    def __init__(self, region="euw", versions, ):
        
        



main_url = "https://prod.api.pvp.net/api/lol"
static_url = "https://prod.api.pvp.net/api/lol/static-data"
region = "euw"
key = "e20154f8-3601-40ac-ae35-5af13e62cc8c"

# Eventually grab versions off https://developer.riotgames.com/api/methods (learn html parsing beautiful soup?)
vers_staticdata = "v1.2"
vers_game = "v1.3"
vers_summoner = "v1.4"
versions = [vers_staticdata, vers_game, vers_summoner]
# Grab summoner by name, store ID (for other requests)
