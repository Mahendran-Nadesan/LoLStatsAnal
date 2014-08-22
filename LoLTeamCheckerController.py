"""The Controller for LoLTeamChecker

Controls calls to GUI and the data model."""



class LoLTeamCheckerController:
    """Handles calls to the model, Riot API, and the GUI."""
    def __init__(self, gui, model): #, model, 
        """Initialises stuff???"""
##        pass
        self.gui = gui
        self.model = model
        self._set_bindings()

##        self.gui = LoLTeamCheckerGUI()
        

    def binding(self):
        pass

    def _process_line(self, line):
        """Runs all the methods for getting the data in one row of the
        gui."""
        [summoner_name, champ_name] = self.gui._get_user_values(line)
        if self.model.region != self.gui._get_region_value():
            self.model.region = self.gui._get_region_value()
            self.model._update()
        # This section needs to be rethought out and rewritten - i.e.
        # it has to catch the error code (from riotapy), send it here,
        # so it can be sent to the gui, to generate an appropriate
        # message box.
##        try:
        self.model._get_champ_stats(summoner_name, champ_name)
##        except:
##            self._error()
        
        self.gui._set_right_info_row_values(line, self.model.final_stats[summoner_name])

    def _set_bindings(self):
        """Set bindings for buttons in GUI."""
        for i, button in enumerate(self.gui.row_buttons[0]):
            button.config(command=lambda row=i: self._process_line(row))
        

        
##    def get_user_values(self, row):#, value):
##        """Gets the summoner and champ value from the gui"""
##        # Do a check
       
        
        # Make these 2 into 1 step later.

        
        # Some of this must go into the model later.

##        
##        relevant_stats = player_ranked_data.get_averages(player_ranked_data.relevant_stats)
##        self.final_stats = player_ranked_data.convert()
##        for i in self.final_stats.keys():
##            self.gui.header_values[i][row].set(str(self.final_stats[i]))
        
        
##        print var1, var2
##        for i in self.gui.header_values.keys():
##            self.gui.header_values[i][row].set("1")
        
##        pass


##if __name__=="__main__":
##    app = LoLTeamCheckerController()
##    app.gui.mainloop()
