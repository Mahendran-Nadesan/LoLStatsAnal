# -*- coding: latin-1 -*-

"""The model for LoLTeamChecker

Retrieves, and stores data retrieved by the API and manipulates them
as needed. Called by the controller."""
from __future__ import division # must be first import
##from LoLTeamCheckerController import LoLTeamCheckerController
from riotapi_py import *
from rankeddata import GrabRankedData
from staticdata import GrabStaticData
from collections import Counter



class LoLTeamCheckerModel:
    def __init__(self, region="euw"):
        self.data = {}
        self.team_data = {}
        self.summoners = {}
        self.final_stats = {}
        self.api_key = "e20154f8-3601-40ac-ae35-5af13e62cc8c" 
        self.region = region
        self.versions = {"gsbn": "v1.4", "gsbid": "v1.4", "ggbid":
                         "v1.3", "grsbid": "v1.3", "sgcbid": "v1.2",
                         "gmhbid": "v2.2"} 
        self.api_instance = RiotApiPy(self.api_key, self.versions,
                                      self.region)
        self.champdata = self.api_instance.static_get_champion_list()
        self.staticdata = GrabStaticData(self.champdata)

    def _add_args(self, summoner_name, champ_name):
        """Unused class. Will be used if I decide to make an instance
        of model only take one summoner's data"""
        pass

    def _get_summoner_data(self):
        """Get the summoner ranked data from the RiotAPI."""
        
        print self.summoner_name
        print "stuff is happening..."
        # Is there a better way to do the encoding issue?
        self.summoners[self.summoner_name] = self.api_instance.get_summoners_by_name(self.summoner_name.encode('utf-8'), self.region)

    def _make_data_relevant(self):
        self.data[self.summoner_name].make_relevant(self.data[self.summoner_name].get_stats_by_champid(self.staticdata.get_champid(self.champ_name)))
        
    def _get_ranked_data(self):
        """Method for getting all ranked data for a summoner, which
        will be used to get requested champion's data."""
        # I don't use all the stats provided, but this is the only
        # reliable way to get individual champion stats for a
        # summoner.
        self.data[self.summoner_name] = {}
##        self.final_stats[self.summoner_name]= Counter({})
        summoner_id = str(self.summoners[self.summoner_name][(self.summoner_name.replace(" ", "")).lower()]['id'])
        self.data[self.summoner_name] = GrabRankedData(self.api_instance.get_ranked_stats_by_summoner_id(summoner_id, 4))

    def _get_champ_stats(self, summoner_name, champ_name):
        """Method for getting all relevant stats for summoner/champ
        combination."""
        self.error = None
        self.summoner_name = summoner_name
        self.champ_name = champ_name
##        self.final_stats[summoner_name]= {}
        if self.summoner_name == "":
            self.error = "No summoner name given."
            raise self.error
        if self.summoner_name not in self.summoners:
            try:
                self._get_summoner_data()
            except:
                self.error = "No such summoner: {s}".format(s=summoner_name)
                self.summoners.pop(self.summoner_name)
                self.final_stats.pop(summoner_name)
        if self.summoner_name not in self.data:
            try:
                self._get_ranked_data()
            except:
                self.error = "No ranked stats this season."
                raise self.error
        try:
            self.data[self.summoner_name].make_relevant(self.data[self.summoner_name].get_stats_by_champid(self.staticdata.get_champid(self.champ_name)))
            self.data[self.summoner_name].get_averages(self.data[self.summoner_name].relevant_stats)
            self.final_stats[self.summoner_name] = Counter(self.data[self.summoner_name].convert())
        except:
            self.error = "No data for champ"
            self.final_stats.pop(summoner_name)
            self.final_stats[self.summoner_name] = Counter({k: 0 for k in self.data[self.summoner_name].converted_stats_names})
            raise self.error

    def _get_summary_stats(self, summoner_names, champ_names):
        """Method for averaging team stats based on summoners already
        retrieved."""
        
##        self.num = len([len(self.data) for i in self.data if self.data[i] is not None])
        self.num = len({i for i in self.final_stats if self.final_stats[i] is not
                        None}) # find best way to do this
##        self.num_games = sum([self.final_stats[i]['Total Games'] for i in self.final_stats if 'Total Games' in self.final_stats[i].keys()])

        self.num_games = sum([self.final_stats[name]['Total Games'] for name in summoner_names])


        
##        newdict = dict((x, {k: 0 for k in range(3)}) for x in range(2))
##        self.team_data = dict((summoner, {stat: 0 for stat in self.data[summoner]}) for summoner in self.data)
##        for summoner in self.data:
##            self.team_data[summoner] = {}
##            for
        self.ew_data = Counter()
        self.nonew_data = Counter()
        
        for name in summoner_names:
            self.nonew_data += self.final_stats[name]

        for name in summoner_names:
            if hasattr(self.data[name], 'champ_stats'):
                self.ew_data += Counter(self.data[name].champ_stats)

        self.ave_stats = {'EWAve': {key: round((self.ew_data[key]/self.num_games), 2) for key in self.ew_data}, 'Ave': {key: round((self.nonew_data[key]/self.num), 2) for key in self.nonew_data}}
            
        print "Equally weighted averages: "
        for k, v in self.ave_stats['EWAve'].items():
            print k, ": ", v

        print
        print "Just averages: "
        for k, v in self.ave_stats['Ave'].items():
            print k, ": ", v


##        print self.final_stats['EWAve']
##        print self.final_stats['Ave']

            
    def _update(self):
        """Updates when the region is not the default."""
        self.api_instance = RiotApiPy(self.api_key, self.versions, self.region)
        # Don't reload static champ list, assume they're the same
        # across regions.
        
