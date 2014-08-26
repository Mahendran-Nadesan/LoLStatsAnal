"""The Controller for LoLTeamChecker

Controls calls to GUI and the data model."""



class LoLTeamCheckerController:
    """Handles calls to the model, Riot API, and the GUI."""
    def __init__(self, gui, model): #, model, 
        """Initialises model and GUI to control."""
        self.gui = gui
        self.model = model
        self._set_bindings()

    def __str__(self):
        pass

    def _process_line(self, line):
        """Runs all the methods for getting the data in one row of the
        gui."""
        # Get the values from the GUI
        [summoner_name, champ_name] = self.gui._get_user_values(line)
##        print summoner_name
        # Check region info
        print "User values retrieved"
        
        if self.model.region != self.gui._get_region_value():
            self.model.region = self.gui._get_region_value()
            self.model._update()
        print "Region value retrieved"
        # Error checking
        try:
            print "inside controller try loop"
            self.model._get_champ_stats(summoner_name, champ_name)
        except:
            print "inside controller except loop"
            self.gui._show_error_message(self.model.error)
        pass
        # Update GUI if checks pass
        self.gui._set_right_info_row_values(line, self.model.final_stats[summoner_name])
        
        
    def _set_bindings(self):
        """Set bindings for buttons in GUI."""
        for i, button in enumerate(self.gui.row_buttons[0]):
            button.config(command=lambda row=i: self._process_line(row))

    

##if __name__=="__main__":
##    app = LoLTeamCheckerController()
##    app.gui.mainloop()
