# -*- coding: latin-1 -*-

"""The GUI for LoLTeamChecker

The GUI has rows for each champ, allowing for entry of summoner name
and champion. When appropriate buttons are pressed, average/relevant
data is returned."""

import Tkinter as tk
import tkFileDialog

class LoLTeamCheckerGUI(tk.Frame):
    """Main GUI frame, which loads individual frames."""
    def __init__(self, master=None):
        """Initialises class, runs the methods for loading in
        frames."""

        # Initialise variables
        tk.Frame.__init__(self)
        self.frames = []
        self.labels = []
        self.entries = []
        self.user_values = {}
        self.header_values = {}
        self.row_buttons = []
        self.master.title("LoL Team Checker")

        # Please check how to code this by PEP standards
        self.default_values = {'ln': ["Summoner Name", "Champion Name"],
                               'rn': ["Games", "Win Rate", "Kills",
                                      "Deaths", "Assists", "CS",
                                      "Towers", "Gold", "KDA",
                                      "Prediction"],
                               'li': {"Names":['{s}'.format(s="Summoner"
                                                            " ") + str(i)
                                               for i in range(1, 6)],
                                      "Champs": ['{s}'.format(s="Champ ")
                                                 + str(i) for i in
                                                 range(1,6)]},
                               'ri': ['-' if i==9 else '0' for i in
                                      range(10) for j in range(5)],
                               'rv': [tk.StringVar() if i==9 else
                                      tk.DoubleVar() for i in
                                      range(10) for j in range(5)]}

        # Create Frames
        self._create_left_name_frame(self.default_values['ln'])
        self._create_right_name_frame(self.default_values['rn'])
        self._create_left_info_frame(self.default_values['ln'])
        self._create_button_frame()
        self._create_right_info_frame(self.default_values['rn'])
        self._create_mid_region_frame() # mid, top, frame created by column
        self._create_summary_frame()
##        configuration, not explicitly.
        # Configure frames  
##        self.master.grid()
        top = self.winfo_toplevel()
##        top.grid(0, "ew")
        top.columnconfigure(0, weight=1, minsize=100)
        top.columnconfigure(1, weight=1, minsize=75)
        top.columnconfigure(2, weight=1, minsize=100)
##        top.rowconfigure(0, weight=1)
        top.rowconfigure(1, weight=1)
        top.rowconfigure(2, weight=2)
##        self.columnconfigure(0, weight=1)
##        self.columnconfigure(1, weight=1)
##        self.rowconfigure(0, weight=0)
        self.grid(sticky="ew")
##        self.master.title("jkshd")

    def _create_frames(self, column, rows):
        """Empty method for now, but might be more general. Need to
        decide whether I need more than columns/rows as arguments -
        what **kwargs?"""
        pass
        

    def _create_left_name_frame(self, headers):
        """Creates a left, top, frame, for the name headers."""
        
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
        """Creates a right, top, frame for the data headers."""

        self.frames.append(tk.LabelFrame(self.master, bg="blue"))
        self.labels.append([])

        for i, name in enumerate(headers):
            self.labels[1].append(tk.Label(self.frames[1], text=name,
                                           relief="sunken"))
            self.labels[1][i].grid(column=i, row=0, sticky="ew")
            self.frames[1].columnconfigure(i, weight=1, minsize=50)

        self.frames[1].grid(column=2, row=0, sticky="ew")

    def _create_mid_region_frame(self):
        """Creates a middle, top, frame, which Will list the regions
        the app works in"""
        self.region_option = tk.StringVar()
        self.region_option.set("euw")
        
        self.frames.append(tk.LabelFrame(self.master))
        self.option_menu = tk.OptionMenu(self.frames[5], self.region_option, "euw", "na", "eune")
        self.option_menu.grid(sticky="ew")

        self.frames[5].grid(column=1, row=0, sticky="ew")
        self.frames[5].columnconfigure(0, weight=1, minsize=100)
        
            
    def _create_left_info_frame(self, headers):
        """Creates a left, middle, frame, with 5 entry widgets, which
        the user will fill."""
        
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
        """Creates a middle, middle, frame, with a "Go!" button."""
        
        self.frames.append(tk.Frame(self.master, bg="yellow"))
        self.row_buttons.append([])

        for row in range(5):
            self.row_buttons[0].append(tk.Button(self.frames[3], text="Go"))
            self.row_buttons[0][row].grid(column=0, row=row)
            self.frames[3].rowconfigure(row, weight=1, minsize=50)
        
        self.frames[3].grid(column=1, row=1, sticky="ew")
        self.frames[3].columnconfigure(0, weight=1, minsize=50)
                           
    def _create_right_info_frame(self, headers):
        """Creates a right, middle, frame, with "empty" labels for the
        data."""

        self.frames.append(tk.Frame(self.master, bg="blue"))
        self.labels.append([])

        for column, name in enumerate(headers):
            self.frames[4].columnconfigure(column, weight=1, minsize=50)
            self.header_values[name] = []
            for row in range(5):
                self.header_values[name].append(self.default_values
                                                ['rv']
                                                [(column*5)+row])
                self.header_values[name][row].set(self.default_values
                                                  ['ri']
                                                  [(column*5)+row])
##                self.labels[2].append(tk.Label(self.frames[4], text=
##                                               (self.default_values
##                                                ['ri'][(column*5)+row]), relief="ridge"))
                self.labels[2].append(tk.Label(self.frames[4],
                                               textvariable=self.
                                               header_values[name]
                                               [row], relief="ridge"))
                self.labels[2][(column*5)+row].grid(column=column, row=row, sticky="ew")
                self.frames[4].rowconfigure(row, weight=1, minsize=50)
        self.frames[4].grid(column=2, row=1, sticky="ew")

    def _create_summary_frame(self):
        """Creates the summary frame, bottom, total, frame."""
        self.frames.append(tk.Frame(self.master))

        self.frames[6].grid(column=0, row=2, sticky="ew")
        self.go_button = (tk.Button(self.frames[6], text="Get Summary Stats"))
        self.go_button.grid(column=0, row=0)
        self.getall_button = (tk.Button(self.frames[6], text="Get all indiv stats"))
        self.getall_button.grid(column=1, row=0)

    def _set_right_info_row_values(self, row, values):
        """Takes a values dict from the controller, and lays it into
        those labels."""
        for name in values.keys():
            self.header_values[name][row].set(values[name])

    def _get_user_values(self, row):
        """Gets the user values (summoner and champ names)."""
        return [self.user_values['Summoner Name'][row].get(), self.user_values['Champion Name'][row].get()]

    def _get_all_summoners(self):
        """Gets all current summoner names. Useful for snapshots."""
        return [self.user_values['Summoner Name'][row].get() for row, obj in enumerate(self.user_values['Summoner Name'])]

    def _get_all_champs(self):
        """Gets all current champion names."""
        return [self.user_values['Champion Name'][row].get() for row, obj in enumerate(self.user_values['Champion Name'])]
    
    def _get_region_value(self):
        """Gets the region value."""
        return self.region_option.get()

    def _show_error_message(self, error_code):
        """Method for creating error message boxes."""
        print error_code
        self.error_box = tk.Toplevel()
        self.error_box.title("Error!")
        self.error_frame = tk.Frame(self.error_box)
        self.error_frame.grid(column=0, row=0, sticky="ew")
        self.error_frame.columnconfigure(0, weight=1, minsize=100)
        self.error_message = tk.Message(self.error_frame, text=error_code)
        self.error_message.grid(column=0, row=0, sticky="ew")



        
    
                             
            
        
