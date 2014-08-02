"""The GUI for LoLTeamChecker

The GUI has rows for each champ, allowing for entry of summoner name
and champion. When appropriate buttons are pressed, average/relevant
data is returned."""

import Tkinter as tk
import tkFileDialog

class LoLTeamChecker(tk.Frame):
    """Main GUI frame, which loads individual frames."""
    def __init__(self, master=None):
        """Initialises class, runs the method for loading in frames."""
        tk.Frame.__init__(self)
        self.frames = []
        self.labels = []
        self.entries = []
        self.entry_values = []
        self.row_buttons = []
        self.default_values = {}
        self.header_values = []

        self._create_headers(0)
##        self.frames[0].pack(side="top", pady=5)

        for i in range(1, 6):
            
            self._create_summoner_row(i)
##            self.frames[i].pack(side="top", pady=5)

        print self.frames

##        self._create_summary()


    def _create_headers(self, row):
        """Creates the headings for the stats."""
        # Add the frame
        self.frames.append(tk.Frame(self.master))
        self.frames[row].pack(side="top", pady=5)
        
        # Add the label list
        self.labels.append([])

        self.default_values['Headers'] = ["Summoner Name", "Champion \
        Name", "Total Games", "Win Rate", "Ave Kills", "Ave Deaths",
        "Ave Assists", "Ave CS", "Ave Towers", "KDA", "Prediction"]
        
        for i, heading in enumerate(self.default_values['Headers']):
            self.labels[row].append(tk.Label(self.frames[row], width=10, text=heading))
            self.labels[row][i].pack(side="left", padx=5)
            print heading

        self.labels
        
        return self.frames[row]
            

    def _create_summary(self):
        pass

        
    def _create_summoner_row(self, row):
        """Creates a summoner row with the following types/attributes:
        Entries: summoner_name, champ_name
        Dynamic Labels: num_games, win_rate, ave_kills, ave_deaths,
        ave_assists, ave_kda, ave_cs, ave_turrets, ave_gold"""
        self.frames.append(tk.Frame(self.master))
        self.frames[row].pack(side="top", pady=5)

        self.default_values['Entries'] = ["Summoner ", "Champion"]
        self.entries.append([])
##        self.labels.append([])
        self.entry_values.append([])
        print self.entry_values
        
        for entry in range(2):
            print row
            self.entry_values[row-1].append(tk.StringVar)
            self.entries[row-1].append(tk.Entry(self.frames[row], textvariable=self.entry_values[row-1][entry]))
            self.entry_values[row-1][entry] = str(self.default_values['Entries'][entry]) + str(row)
            self.entries[row-1][entry].pack(side="left", padx=5)

        print self.frames
        return self.frames[row]

        
        
    
    
                             
            
        
