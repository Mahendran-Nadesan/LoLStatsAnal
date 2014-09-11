"""Test stuff for filling in frames."""

import Tkinter as tk

default_values = {'ln': ["Summoner Name", "Champion Name"],
                  'rn': ["Games", "Win Rate", "Kills", "Deaths",
                         "Assists", "CS", "Towers","Gold", "KDA",
                         "Prediction"],
                  'li': {"Names":['{s}'.format(s="Summoner") +
                                  str(i) for i in range(1, 6)],
                         "Champs": ['{s}'.format(s="Champ ") +
                                     str(i) for i in range(1,6)]},
                  'ri': ['-' if i==9 else '0' for i in range(10)
                         for j in range(5)],
                  'rv': [str() if i==9 else float() for i in
                         range(10) for j in range(5)]}

header_values = {}
summary_values = {"EWA": {}, "Ave": {}}

