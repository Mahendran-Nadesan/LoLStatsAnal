# script to check LoLTeamCheckerGUI

from riotapi_py import RiotApiPy
from rankeddata import GrabRankedData
from staticdata import GrabStaticData
from LoLTeamCheckerGUI import LoLTeamCheckerGUI
from LoLTeamCheckerController import LoLTeamCheckerController

api_key = "e20154f8-3601-40ac-ae35-5af13e62cc8c" 
region = "euw" 
versions = {"gsbn": "v1.4", "gsbid": "v1.4", "ggbid": "v1.3", "grsbid": "v1.3", "sgcbid": "v1.2"} 



# Explicitly initialise arguments to controller

api_instance = RiotApiPy(api_key, versions, region)
my_gui = LoLTeamCheckerGUI(api_instance)

##data_model = LoLTeamCheckerModel()
##myapp = LoLTeamCheckerController(my_gui, api_instance)
my_gui.mainloop()

