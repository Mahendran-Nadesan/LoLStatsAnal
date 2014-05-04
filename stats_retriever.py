# LoLStatsAnal
# stats_retriever.py
# Main Class for retrieving data from the lolapi
# For now, using LoLPy ("C:\Python27\Lib\site-packages\LoLpy")

import sys
sys.path.append("C:\Python27\Lib\site-packages\LoLpy")
from LoLpy import *


# set stuff up/API key

lolpy = LoLpy("e20154f8-3601-40ac-ae35-5af13e62cc8c",region="EUW")
summoner = lolpy.get_summoner_by_name("PurpleEyesDude")
summoner = lolpy.get_summoner_by_name("LadyCas")
# print summoner
game_info = lolpy.get_game_by_id(summoner['id'])

# print game_info
