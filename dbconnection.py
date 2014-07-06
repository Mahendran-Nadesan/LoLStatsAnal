#
# Test host: 127.0.0.1
# Test db name: test_lolstatsanal_1
# Test table: champ_basics
# Class aux_db:
# Handles string formation for eventual input into database.
# Specifically, handles column name creation, and hopefully, later, also formats data for input
#
# To do:
#
# 1. Is there any reason to have dicts over lists?
# 2. Make some allowance for "VARCHAR(30)"
# 3. I don't think formatting the data will work here if this class stays as is (too specific)

import MySQLdb
import collections


##db = MySQLdb.connect("127.0.0.1","root","","test_lolstatsanal_2") # old db
##cur = db.cursor()

# Do a check to see if the db exists, if not, create it.
# Then check for the table, if it doesn't exist, create it.
# Note, tables must be created with columns, or at least one.
##db_name = "LoLStatsApp"
##db_cur.execute("CREATE DATABASE IF NOT EXISTS {s}".format(s=db_name))
##cur.execute("USE {s}".format(s=db_name)) # switch to current db




##cur.execute("create database test_lolstatsanal_2")
##cur.execute("create table test_1 (test_column varchar(20))") 
##
##table_names = {}
##pr = 'champ'
##for x in range(10):
##	prn = 'pr{n}_'.format(n=str(x))
##	for i in match['stats']:
##		table_names['{s}'.format(s=prn+i)] = []
		

class aux_db:
        """ Assumes db - i.e. db isn't specified, but the cursor is!
        """
        def __init__(self, table_name, db_cursor):
##                self.example_match = example_match
                self.table_name = table_name
                self.db_cursor = db_cursor
                self.sql_command_history = []
                self.arg_history = []
                self.strings = {}
                # self.initial_column_names = {'gameId': [], 'createDate': [], 'gameMode': [], 'mapId': [], 'gameType': [], 'subType': [], 'gameResult': []}
                # self.list_initial_column_names = list(self.initial_column_names)

##        def make_db_string(self, column_names):
##                self.base_string = str()
##                self.col_names = str()
##                for i in column_names:
##                        self.col_names = self.col_names + " {a} {col_name},".format(a="ADD COLUMN", col_name=i) 
##                        
##                return "CREATE TABLE {table} {exec_string}".format(table=self.table_name, exec_string=self.col_names)

        def check_type(self, var, var_type):
                return str(type(var)) == "<type \'{var_type}\'>".format(var_type=var_type)

##        def create_string(self, sql_command, in_arg):
##                self.sql_command_history.append(sql_command)
##                self.arg_history.append(in_arg)
##                self.sql_command = sql_command
##                self.arg = in_arg
##                return "{sqlcomm} {table} {exec_string}".format(sqlcomm=self.sql_command, table=self.table_name, exec_string=self.arg)
##
        def create_insert_string(self, val_string, string_name="insert_string"):
##                self.strings[string_name] = "INSERT INTO {table_name} VALUES ({val_string}) ".format(table_name=self.table_name, val_string=val_string)
                return "INSERT INTO {table_name} VALUES ({val_string}) ".format(table_name=self.table_name, val_string=val_string)
                               
        def create_colname_strings(self):
                # Put in initial column names with champ number modifiers
                self.temp_column_names = {}
                self.list_initial_column_names = ['gameID', 'createDate', 'gameMode', 'mapID', 'gameType', 'subType', 'gameResult']
                c_string = "champ"
                bool_type = "<type \'bool\'>"
                int_type = "<type \'int\'>"
                for champ_num in range(10):
                        ch_string = '{name}{num}_'.format(name=c_string, num=str(champ_num))
                        for i in range(2):
                                self.temp_column_names['{s}spell{n}'.format(s=ch_string, n=i)] = [] # add 2 spells
                                self.temp_column_names['{s}ID'.format(s=ch_string, n=i)] = []   # add champ ID
                        for col_name in self.example_match['stats']:
                                if str(type(col_name)) == bool_type:
                                        var_type = "BOOL"
                                else:
                                        var_type = "INT(10)"
                                self.temp_column_names['{s} {t}'.format(s=ch_string+col_name, t=var_type)] = [] # add other Riot JSON data

                # Change to lists (why the hell did I make them dicts anyway?).
                # Order them by name.
                self.list_temp_column_names = sorted(self.temp_column_names)

                # Remove excess "champx_win" names.
                for col_name in self.list_temp_column_names:
                        if col_name[-4:] == "_win":
                                self.list_temp_column_names.remove(col_name)

                # Add initial list and sorted one
                for col_name in self.list_temp_column_names:
                        self.list_initial_column_names.append(col_name)
                
                # Iterate and add to string
                self.base_string = str()
                self.col_names = str()
                for i in self.list_initial_column_names:
                        self.col_names = self.col_names + " {a} {col_name},".format(a="ADD COLUMN", col_name=i)

                return self.col_names
##                return self.make_db_string(self.list_initial_column_names)

        def write_to_db(self, string_name, target_data):
                """ Writes the data to the table according to its
                column length. Target data must be a list/dict?? of
                integers/booleans (combined). For now, this assumes
                we're only writing an INSERT MySQL command."""
##                if self.check_type(target_data, "list"):
                val_string = ", ".join(["%s" for i in range(len(target_data))])
                self.db_cursor.execute(self.create_insert_string(val_string, string_name), target_data.values())
                
                        
                                
                        
                        
                        
                

                
                
                
##for i in all_stats:
##	x = ', '.join('?' * len(i))
####	var_string = "INSERT INTO MatchPlayerDetails VALUES (%s);" % x
##	cursor.execute(x, i.values())
##
##for i in all_stats:
##	x = ", ".join("?" * len(i))
##	y = ", ".join([str(j) for j in i.values()])
##	var_string = "INSERT INTO MatchPlayerDetails VALUES (x);".format(x=x)
##	cursor.execute(var_string, y)


# Data entry stuff 2/7/2014
##db_name = "LoLStatsApp"
##db = MySQLdb.connect("127.0.0.1","root","","") 
##cursor = db.cursor()
##cursor.execute("USE {s}".format(s=db_name))
##
##z = all_stats[1].values()
##news = ", ".join(["%s" for i in range(56)])
##newstring = "insert into MatchPlayerDetails VALUES ({s}) ".format(s=news)
##cursor.execute(newstring, z)
##db.commit()
