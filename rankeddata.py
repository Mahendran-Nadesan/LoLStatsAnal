# Ranked stats data sorter/parser

from __future__ import division # must be first import
##from staticdata import GrabStaticData

class GrabRankedData:
    """Converts and returns json/dict data requested from the Riot API
    of the type: ranked stats of summoner."""
    def __init__(self, ranked_stats):
        """Stores and manipulates ranked stats data for a single
        summoner. Takes its data returned by
        api.get_ranked_stats_by_summoner_id(...)."""
        self.all = ranked_stats['champions']
        self.relevant_stat_names = ['totalSessionsPlayed',
                                    'totalAssists',
                                    'totalDeathsPerSession',
                                    'totalSessionsWon',
                                    'totalSessionsLost',
                                    'totalGoldEarned',
                                    'totalChampionKills',
                                    'totalMinionKills',
                                    'totalAssists',
                                    'totalTurretsKilled']
        self._sort_by_champid()

    def _sort_by_champid(self):
        """Sorts self.all into a dict with champid as the main key
        (dict['champname']) as opposed to lists."""
        self.all_stats_by_champid = {}
        for i in self.all:
            # note: 'id' is an int, so call it appropriately: as in,
            # stats_by_champname[22], not stats_by_champname['22'].
            self.all_stats_by_champid[i['id']] = i['stats']
##            return

    def get_averages(self, champ_stats):
        """Calculates and returns the average (per game) values for
        one champion only, in whatever dict of stats:
        all_stats_by_id[champid]/relevant_stats. Make sure they are in
        the right format."""
        # The following is weird. I remove num_games from the champ's
        # stats, loop over the remaining stats and divide by
        # num_games, then add it back to the dict because it might be
        # used.
        num_games = champ_stats.pop('totalSessionsPlayed')
        ave_stats = {}
        for stat in champ_stats:
            ave_stats[stat] = round(champ_stats[stat]/num_games, 2)
        champ_stats['totalSessionsPlayed'] = num_games
        return ave_stats

    def get_stats_by_champid(self, champid):
        """Gets ranked stats by champid."""
        champid = int(champid)
        return self.all_stats_by_champid[champid]

    def make_relevant(self, champ_all_stats):
        """Takes only the relevant stats for *one champ* necessary for
        LoLTeamCheck, i.e. all_stats_by_id[champid]."""
        self.relevant_stats = {}
        for name in self.relevant_stat_names:
            if champ_all_stats.has_key(name):
                self.relevant_stats[name] = champ_all_stats[name]
##        return 




    
