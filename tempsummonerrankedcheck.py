
summoner_names = ["Fildo McDildo", "", "", ""]
champs = ""

for i, j in enumerate(summoner_names):
    summoner = api_instance.get_summoners_by_name(j, "euw") 
    playerid = str(summoner[summoner_name.lower()]['id'])
    player_ranked_data = GrabRankedData(api_instance.get_ranked_stats_by_summoner_id(playerid, 4))
    player_ranked_data.make_relevant(player_ranked_data.get_stats_by_champid(staticdata.get_champid(champs[i])))
    final_stats = player_ranked_data.get_averages(player_ranked_data.relevant_stats)
    print final_stats
