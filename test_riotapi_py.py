# Tests for riotapi_py


# Generic output function
def test(name, outcome):
    if outcome:
        tout = "successful"
    else:
        tout = "unsuccessful"
    print "Test {t} was {o}".format(t=name, o=tout)
    print

# imports
from riotapi_py import riotapi_py

# Setup
api_key = "e20154f8-3601-40ac-ae35-5af13e62cc8c" 
region = "euw" 
rate_limit = 5 
versions = {"gsbn": "v1.4", "gsbid": "v1.4", "ggbid": "v1.3"} 

#==========================#
# Start up instance of api
try:
    api_instance = riotapi_py(api_key, rate_limit, versions, region)
    outcome = True
except:
    outcome = False

test("start_api_instance", outcome)
    
#==========================#
# Get Summoner info by name/[name]/(name)
summoner_name = "nadsofmahen" 
try:
    summoner = api_instance.get_summoners_by_name(summoner_name, "euw")
    print summoner
    outcome = True
except:
    outcome = False
    print api_instance.r.url
    
test("single summoner by name", outcome)
    
try:
    summoner = api_instance.get_summoners_by_name([summoner_name], "euw")
    print summoner
    outcome = True
    print api_instance.r.url
except:
    outcome = False
    

test("single summoner by [name]", outcome)

try:
    summoner = api_instance.get_summoners_by_name((summoner_name), "euw")
    print summoner
    outcome = True
    print api_instance.r.url
except:
    outcome = False
    print api_instance.r.url

test("single summoner by (name)", outcome)
#==========================#
# Get Summoner info by ID (try [], (), alone)
summoner_id = summoner[summoner.keys()[0]]['id']

try:
    summoner = api_instance.get_summoners_by_id(summoner_id)
    print summoner
    outcome = True
except:
    outcome = False
    print api_instance.r.url

test("single summoner by id", outcome)

try:
    summoner = api_instance.get_summoners_by_id([summoner_id])
    print summoner
    outcome = True
except:
    outcome = False
    print api_instance.r.url

test("single summoner by [id]", outcome)

try:
    summoner = api_instance.get_summoners_by_id((summoner_id))
    print summoner
    outcome = True
except:
    outcome = False
    print api_instance.r.url

test("single summoner by (id)", outcome)
    
#==========================#
# Get Multiple Summoners by ID


    

