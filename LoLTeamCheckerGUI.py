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
        self.user_values = {}
        self.row_buttons = []
        # Please check how to code this by PEP standards
        self.default_values = {'ln': ["Summoner Name", "Champion Name"],
                               'rn': ["Total Games", "Win Rate", "Ave "
                                      "Kills", "Ave Deaths", "Ave "
                                      "Assists", "Ave CS", "Ave Towers",
                                      "KDA", "Prediction"],
                               'li': {"Names":['{s}'.format(s="Summoner"
                                                            " ") + str(i)
                                               for i in range(1, 6)],
                                      "Champs": ['{s}'.format(s="Champ ")
                                                 + str(i) for i in
                                                 range(1,6)]},
                               'ri':['-' if i==8 else '0' for i in
                                     range(9) for j in range(5)]}
        self.header_values = []
##        self.pack(side="top", expand=False, fill="x")

        # Create various frames
##        self._create_headers(0)
##        for i in range(1, 6):
##            self._create_summoner_row(i)
        self._create_left_name_frame(self.default_values['ln'])
##        self._create_mid
        self._create_right_name_frame(self.default_values['rn'])
        self._create_left_info_frame(self.default_values['ln'])
        self._create_button_frame()
        self._create_right_info_frame(self.default_values['rn'])

##        self.master.grid()
        top = self.winfo_toplevel()
##        top.grid(0, "ew")
        top.columnconfigure(0, weight=1, minsize=100)
        top.columnconfigure(1, weight=1, minsize=50)
        top.columnconfigure(2, weight=2, minsize=100)
##        top.rowconfigure(0, weight=1)
        top.rowconfigure(1, weight=1)
##        self.columnconfigure(0, weight=1)
##        self.columnconfigure(1, weight=1)
##        self.rowconfigure(0, weight=0)
        self.grid(sticky="ew")
##        self.master.title("jkshd")
        

    def _create_summary(self):
        pass

        
    def _create_left_name_frame(self, headers):
        """Creates a left, top, frame, for the headers."""
        self.frames.append(tk.LabelFrame(self.master, bg="red"))
        self.labels.append([])
        
        for i, name in enumerate(headers):
            self.labels[0].append(tk.Label(self.frames[0], text=name,
                                           relief="groove"))
            self.labels[0][i].grid(column=i, row=0, sticky="ew")
            self.frames[0].columnconfigure(i, weight=1, minsize=100)

        # For .grid one must modify their positions by referencing
        # their parents. Here: the LabelFrame is self.frames[0], and
        # in order to modify the positions, etc. of the Labels *IN*
        # the LabelFrame, one must modify the relevant coordinates in
        # the LabelFrame, not by referencing the Labels:
        # x = Label(parent, ...) {parent=LabelFrame}
        # x.grid(column_in_parent, row_in_parent)
        
        # For .columnconfigure one must modify the column within its
        # parent widget, not by referencing its parents. Here, the

        self.frames[0].grid(column=0, row=0, sticky="ew", columnspan=1)
        
    def _create_right_name_frame(self, headers):
        self.frames.append(tk.LabelFrame(self.master, bg="blue"))
        self.labels.append([])

        for i, name in enumerate(headers):
            self.labels[1].append(tk.Label(self.frames[1], text=name,
                                           relief="sunken"))
            self.labels[1][i].grid(column=i, row=0, sticky="ew")
            self.frames[1].columnconfigure(i, weight=1)

        self.frames[1].grid(column=2, row=0, sticky="ew")
            
    def _create_left_info_frame(self, headers):
        self.frames.append(tk.Frame(self.master, bg="green"))
        self.entries.append([])

        for column, name in enumerate(headers):
            self.frames[2].columnconfigure(column, weight=1)
            self.user_values[name] = []
            for row in range(5):
                self.user_values[name].append(tk.StringVar())
                self.user_values[name][row].set(self.default_values
                                                ['li']
                                                [self.default_values
                                                 ['li'].keys()[column]]
                                                [row])
                self.entries[0].append(tk.Entry(self.frames[2],
                                                textvariable=self.
                                                user_values[name][row]))
                self.entries[0][(column*5)+row].grid(column=column,
                                                     row=row, sticky="ew")
                self.frames[2].rowconfigure(row, weight=1, minsize=50)
                

        self.frames[2].grid(column=0, row=1, sticky="ew")

    def _create_button_frame(self):
        self.frames.append(tk.Frame(self.master, bg="yellow"))
        self.row_buttons.append([])

        for row in range(5):
            self.row_buttons[0].append(tk.Button(self.frames[3],
                                                 text="Go!", command=
                                                 lambda x=row: self.
                                                 _test_get(x)))
            self.row_buttons[0][row].grid(column=0, row=row)
            self.frames[3].rowconfigure(row, weight=1, minsize=50)
        
        self.frames[3].grid(column=1, row=1, sticky="ew")
        self.frames[3].columnconfigure(0, weight=1, minsize=50)
                           
    def _create_right_info_frame(self, headers):
        self.frames.append(tk.Frame(self.master, bg="blue"))
        self.labels.append([])

        for column, name in enumerate(headers):
            self.frames[4].columnconfigure(column, weight=1)
            for row in range(5):
                self.labels[2].append(tk.Label(self.frames[4], text=
                                               (self.default_values
                                                ['ri'][(column*5)+row]), relief="ridge"))
                self.labels[2][(column*5)+row].grid(column=column, row=row, sticky="ew")
                self.frames[4].rowconfigure(row, weight=1, minsize=50)
        self.frames[4].grid(column=2, row=1, sticky="ew")

    def _test_get(self, row):
        print self.entries[0][row].get()
        
    
                             
            
        
