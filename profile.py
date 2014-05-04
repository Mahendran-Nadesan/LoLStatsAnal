# LoL App profile class

import os

class profile:
    def __init__(self):
        self.profile_filename = "C:\lolappprofile.lap"
        if self.has_default():
            self.get_default()
        else:
            self.default_profile = []
            
    def has_default(self):
        # check for text file
        if os.path.isfile(self.profile_filename):
            return True
        return False
        

    def get_default(self):
        # load the profile
        self.profile_file = open(self.profile_filename, "r")
        self.default_profile = self.profile_file.readline()
        self.default_region = self.profile_file.next()

        
    def make_new(self):
        # make a new profile, add the lines, make sure to add newlines.
        pass
        
        

            
