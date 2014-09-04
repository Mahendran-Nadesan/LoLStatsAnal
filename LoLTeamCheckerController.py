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
        # Check region info
        if self.model.region != self.gui._get_region_value():
            self.model.region = self.gui._get_region_value()
            self.model._update()
        # Error checking
        try:
            self.model._get_champ_stats(summoner_name, champ_name)
        except:
            self.gui._show_error_message(self.model.error)
        
        # Update GUI
        if summoner_name in self.model.final_stats:
            self.gui._set_right_info_row_values(line, self.model.final_stats[summoner_name])
        
    def _process_all(self):
        """Runs all methods for getting data for all rows, plus the
        summary stats."""
        summoner_names = self.gui._get_all_summoners()
        champ_names = self.gui._get_all_champs()
        row = int()
        for summoner, champ in zip(summoner_names, champ_names):
            try:
                self.model._get_champ_stats(summoner, champ)
            except:
                self.gui._show_error_message(self.model.error)

            if summoner in self.model.final_stats:
                print
                print "Setting values for {s}: {c}.".format(s=summoner, c=champ)
                print "Values are: ", self.final_stats[summoner]
                print
                self.gui._set_right_info_row_values(summoner_names.index(summoner), self.model.final_stats[summoner])
                

    def _process_summary(self):
        """Runs the methods for processing the average/summary
        pane."""
        self._process_all()
        self.model._get_summary_stats(self.gui._get_all_summoners(), self.gui._get_all_champs())
        
    def _set_bindings(self):
        """Set bindings for buttons in GUI."""
        for i, button in enumerate(self.gui.row_buttons[0]):
            button.config(command=lambda row=i: self._process_line(row))
        self.gui.go_button.config(command=lambda i=i: self._process_summary())
        self.gui.getall_button.config(command=lambda i=i: self._process_all())

    

##if __name__=="__main__":
##    app = LoLTeamCheckerController()
##    app.gui.mainloop()
