"""The Controller for LoLTeamChecker

Controls calls to GUI and the data model."""

##from LoLTeamCheckerGUI import LoLTeamCheckerGUI

from rankeddata import GrabRankedData
from staticdata import GrabStaticData

class LoLTeamCheckerController:
    """Handles calls to the model, Riot API, and the GUI."""
    def __init__(self, gui, api_instance): #, model, 
        """Initialises stuff???"""
##        pass
        self.gui = gui
##        self.model = model
        self.api_instance = api_instance
        self.champdata = self.api_instance.static_get_champion_list()
        self.staticdata = GrabStaticData(self.champdata)

##        self.gui = LoLTeamCheckerGUI()
##        for button in self.gui.row_buttons[0]:
##            button.config(command=self.set_value())

    def binding(self):
        pass
        
    def set_value(self, summoner_name, champ_name, row):#, value):
        """Sets the value in the gui"""

        # Make these 2 into 1 step later.
        summoner = self.api_instance.get_summoners_by_name(
            summoner_name, "euw")
        summoner_id = str(summoner[(summoner_name.replace(" ", "")).lower()]['id'])
        # Some of this must go into the model later.
        player_ranked_data = GrabRankedData(self.api_instance.get_ranked_stats_by_summoner_id(summoner_id, 4))
        player_ranked_data.make_relevant(player_ranked_data.get_stats_by_champid(self.staticdata.get_champid(champ_name)))
        relevant_stats = player_ranked_data.get_averages(player_ranked_data.relevant_stats)
        self.final_stats = player_ranked_data.convert()
        for i in self.final_stats.keys():
            self.gui.header_values[i][row].set(str(self.final_stats[i]))
        
        
##        print var1, var2
##        for i in self.gui.header_values.keys():
##            self.gui.header_values[i][row].set("1")
        
##        pass


##if __name__=="__main__":
##    app = LoLTeamCheckerController()
##    app.gui.mainloop()
