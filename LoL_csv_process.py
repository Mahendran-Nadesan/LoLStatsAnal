# Python script for LoL stats
# Uses a csv file, computes and presents data
#
# To do:
# Add a predictor (maybe like the twitter project)
# http://fantasy.lolesports.com/en-US/join/league/41985/0wgEsQ5IgRf2Pc4n1eTQ
# http://fantasy.lolesports.com/en-US/join/league/41985/0wgEsQ5IgRf2Pc4n1eTQ

'''
CSV Columns: 
01 Game Number
02 Champion Played
03 Side Played
04 Duration (minutes)
05 Duration (seconds)
06 Result
07 Kills
08 Deaths
09 Assists
10 Creep Score
11 Gold Earned
12 Team Kills
13 Team Deaths
14 Team Assists
15 Team Creep Score
16 Team Gold
17 Enemy Kills
18 Enemy Deaths
19 Enemy Assists
20 Enemy Creep Score
21 Enemy Gold
22 LP Gained/Lost
23 Team Mate 1
24 Team Mate 2
25 Team Mate 3
26 Team Mate 4
27 Enemy 1
28 Enemy 2
29 Enemy 3
30 Enemy 4
31 Enemy 5

Extra Data Computed (per game):
01 KDA
02 Team KDA
03 % of Team Kills
04 % of Team Deaths
05 % of Team Assists
06 Kill Participation (%/1)
07 KDA > Team KDA
08 Enemy KDA
09 G/M
10 CS/M
11 CS Differential as %
12 CS Differential/M
13 Gold Differential as %
14 Gold Differential/M

Extra Data Computed (cumulative + average):
01 KDA
02 Team KDA
03 % of Team Kills
04 % of Team Deaths
05 % of Team Assists
06 Kill Participation (%/1)
07 Side Win %
08 G/M
09 Game Duration
10 CS/M
'''       
from __future__ import division # must be first import
import csv
import math
import numpy
from matplotlib import pyplot
from operator import itemgetter
from kda_graph_panel import GraphGui

# import csv
csv_dir = "C:\Users\Mahen\Documents\LOLStats"
csv_file = "EUW_S4_Stats.csv"

all_stats = []
with open("C:\Users\Mahen\My Documents\\LOLStats\EUW_S4_Stats.csv",'r') as f:
        reader = csv.reader(f)
        for row in reader:
                all_stats.append(row)
                
# delete initial line
all_stats.pop(0)

# do some conversions
# for num in all_stats:
        # for col in num:
                # check for string/type
                # make int if it's a num
                
kda = []
team_kdas = []
team_kda = []
champs = []
champ_allies = []

# Add champs played
for game in all_stats:
        if game[1] in champs:
                pass
        else:
                champs.append(game[1])
                
# Add allied champs, enemy champs (totals) - later per champ
        # if game[] in champ_allies:
                # pass
        # else:
                # champ_allies

side_purple = []
side_blue = []                  
tblue_wins = 0
tpurple_wins = 0
tblue_losses = 0
tpurple_losses = 0
unknown = 0
total_wl = []
total_wl_blue = []
total_wl_purple = []
wl = 0
blue_wl = 0
purple_wl = 0
wins = 0
cumwinperc = []

# Add side stats, team total and average kdas
for i, game in enumerate(all_stats):
        
        team_kdas.append([game[11],game[12], game[13]])
        if game[11] == '-':
                team_kda.append([])
        else:   
                # kdat = ((int(game[11])+int(game[13]))/int(game[12]))
                # kdad = round(((int(game[11]) + int(game[13])) % max(int(game[12]), 1))/(max(int(game[12]),1)*0.01)/100, 2) # THIS FORMULA IS CORRECT
                kdad = round((int(game[11])+int(game[13]))/(int(game[12])),2)
                team_kda.append([kdad])
        
        if game[2] == 'blue' and game[5] != "lossprevented":
                side_blue.append(game)
                if game[5] == 'win':
                        tblue_wins += 1
                        blue_wl += 1
                        wl += 1
                        wins += 1
                elif game[5] == 'loss':
                        tblue_losses += 1
                        blue_wl -= 1
                        wl -= 1
                total_wl_blue.append(blue_wl)   
        elif game[2] == 'purple' and game[5] != "lossprevented":
                side_purple.append(game)
                if game[5] == 'win':
                        tpurple_wins += 1
                        purple_wl += 1
                        wl += 1
                        wins += 1
                elif game[5] == 'loss':
                        tpurple_losses += 1     
                        purple_wl -= 1
                        wl -= 1
                total_wl_purple.append(purple_wl)
        elif game[2] == '-':
                unknown += 1
                if game[5] == 'win':
                        wl += 1
                elif game[5] == 'loss':
                        wl -= 1
        total_wl.append(wl)
        cumwinperc.append((round((wins/(i+1))*100),2))
print "TOTALS:"
print "Blue wins: %i, blue losses: %i" %(tblue_wins, tblue_losses)
print "Purple wins: %i, purple losses: %i" %(tpurple_wins, tpurple_losses)
print ""

champ_games = []                                # all info, per champ
champ_all_participation = []                                    # participation per game
champ_totals = []                               # all kills, deaths, assists, per game, per champ
champ_kda = []                                  # kda per champ
ew_kdas = []                                    # equally weighted kdas, per game, per champ
ew_kda = []                                     # equally weighted kda per champ
champ_basics = []                               # totals kills, deaths, assists, per champ
champ_total_kda = []                                                    # cumulative kda per champ
num_champ_games = []
champ_participation = []
champ_all_death_perc = []
champ_all_kill_perc = []
champ_death_perc = []
champ_kill_perc = []
champ_all_wl = []
champ_wl = []
champ_time_m = []
champ_time_s = []
champ_time_all = []
champ_time_ave = []
champ_time_cum = []
champ_wr = []
br = []
pr = []
brpr_text = []
champ_enemies = {}

total_kda = []
totals_kda = []
kills = 0
deaths = 0
assists = 0
missing = 0
# Add champ side stats, KDAs, participation rates, win:loss data
for champ_num, champ in enumerate(champs):
        blue_wins = 0
        blue_losses = 0
        purple_wins = 0
        purple_losses = 0
        wl = 0
        lp = 0
        cumwins = 0
##        br.append([])
##        pr.append([])
##        brpr_text.append([])
        cgames = 0
        champ_wr.append([])
        champ_games.append([])
        champ_all_death_perc.append([])
        champ_all_kill_perc.append([])
        champ_all_participation.append([])
        champ_totals.append([])
        champ_total_kda.append([])
        ew_kdas.append([])
        champ_all_wl.append([])
        champ_time_m.append([])
        champ_time_s.append([])
        champ_time_all.append([])
        champ_time_ave.append([])
        champ_time_cum.append([])
        champ_enemies[champ] = {}
                
                
        # champ_basics.append([])
        for game in all_stats:
                
                # champ win/losses based on side
                if game[1] == champ and game[5] != "lossprevented":
                        champ_games[champ_num].append(game)
                        cgames += 1
                        if game[2] == 'blue' and game[5] == 'win':
                                blue_wins += 1
                                wl += 1
                                cumwins += 1
                        elif game[2] == 'blue' and game[5] == 'loss':
                                blue_losses += 1
                                wl -= 1
                        elif game[2] == 'purple' and game[5] == 'win':
                                purple_wins += 1
                                wl += 1
                                cumwins += 1
                        elif game[2] == 'purple' and game[5] == 'loss':
                                purple_losses += 1
                                wl -= 1
                        elif game[5] == 'lossprevented':
                                lp += 1
                        
                        champ_all_wl[champ_num].append(wl)
                        champ_wr[champ_num].append((cumwins/cgames)*100)

                                        
                        if game[6] != '-' and game[11] != '-':
                                champka = int(game[6])+int(game[8])             # champ kills + assists
                                champd = max(int(game[7]),1)                    # champ deaths
                                kdat = round(champka/champd,2)                                  # unit kda
                                # kdad = round(((champka) % max(champd, 1))/(max(champd,1)*0.01)/100, 2) # THIS FORMULA IS CORRECT - decimal kda
                                ew_kdas[champ_num].append(kdat)
                                pt = round((champka*100)/int(game[11]),2)
                                
                                champ_all_participation[champ_num].append(pt)
                                champ_totals[champ_num].append([int(game[6]),int(game[7]),int(game[8])])
                                
                                dperc = round((int(game[7])*100) / int(game[12]), 2)            # death percentage
                                kperc = round((int(game[6])*100) / int(game[11]), 2)            # kill percentage
                                champ_all_death_perc[champ_num].append(dperc)
                                champ_all_kill_perc[champ_num].append(kperc)
                                
                                kills += int(game[6])
                                deaths += int(game[7])
                                assists += int(game[8])
                                currkdat = round((kills + assists)/deaths, 2)
                                total_kda.append(currkdat)
                        else:
                                missing += 1
                
                        if game[3] != '-':
                                champ_time_s[champ_num].append(game[4])
                                champ_time_m[champ_num].append(game[3])
                                
                                champ_time_all[champ_num].append(int(game[3])*60 + int(game[4]))
                                champ_time_cum[champ_num].append(sum(champ_time_all[champ_num]))
                                champ_time_ave[champ_num].append(round((champ_time_cum[champ_num][-1])/len(champ_time_cum[champ_num]),2))
                        
        
        ckills = 0
        cdeaths = 0
        cassists = 0
        for game in champ_games[champ_num]:
                if game[6] != '-' and game[5] != "lossprevented":
                        ckills += int(game[6])
                        cdeaths += int(game[7])
                        cassists += int(game[8])
                        cumkdat = round((ckills + cassists)/cdeaths, 2)
                        champ_total_kda[champ_num].append(cumkdat)
        kdat = round((ckills + cassists)/max(cdeaths, 1), 2)
        champ_kda.append(kdat)
        ew_kda.append(round(((sum(ew_kdas[champ_num]))/max(len(ew_kdas[champ_num]),1)),2))

        for game in champ_games[champ_num]:
                if game[26] != '-':
                        for i in range(26,31):
                                if game[i] not in champ_enemies[champ].keys():
                                        champ_enemies[champ][game[i]] = {'games': 0, 'wins': 0, 'losses': 0}

        
        for game in champ_games[champ_num]:
                if game[26] != '-':
                        if game[5] != 'lossprevented':
                                for i in range(26,31):
                                        champ_enemies[champ][game[i]]['games'] += 1
                                        if game[5] == 'win':
                                                champ_enemies[champ][game[i]]['wins'] += 1
                                        else:
                                                champ_enemies[champ][game[i]]['losses'] += 1


        
        # for game in champ_time_s[champ_num]:

        if (blue_wins + blue_losses) != 0:
                br.append(str(round((blue_wins*100/(blue_wins + blue_losses)),2)))
        else:
##                br.append(round((blue_wins/(blue_wins + blue_losses)),2))
                
                br.append(str(0))                        
        if (purple_wins + purple_losses) == 0:
                pr.append(str(0))
        else:
##                pr.append(round((purple_wins/(purple_wins + purple_losses)),2))
                pr.append(str(round((purple_wins*100/(purple_wins + purple_losses)),2)))
        brprstring = "b: "+(br[champ_num])+"% p: "+(pr[champ_num])+"%"        
        brpr_text.append(brprstring)
        games = len(champ_games[champ_num])             
        cwins = (blue_wins + purple_wins)
        wr = round(cwins / (games*0.01), 2)
        champ_basics.append([ckills, cdeaths, cassists])
        champ_participation.append(round(sum(champ_all_participation[champ_num])/max(len(champ_all_participation[champ_num]),1), 2))
        champ_kill_perc.append(round(sum(champ_all_kill_perc[champ_num])/max(len(champ_all_kill_perc[champ_num]),1), 2))
        champ_death_perc.append(round(sum(champ_all_death_perc[champ_num])/max(len(champ_all_death_perc[champ_num]),1), 2))
        num_champ_games.append(len(champ_games[champ_num]))
        print "%s: %i, win rate: %r" % (champ, len(champ_games[champ_num]), wr)
        print "Blue wins: %i, blue losses: %i, Purple wins: %i, purple losses: %i" % (blue_wins, blue_losses, purple_wins, purple_losses)
        print "br: ",br[champ_num]," pr: ",pr[champ_num]
##        print round((blue_wins/(blue_wins + blue_losses)),2)
        print "Champ KDA: ", champ_kda[champ_num]
        # print "Equally Weighted KDA: ", ew_kda[champ_num], ew_kdas[champ_num]
        print "Participation: ", round(sum(champ_all_participation[champ_num])/max(len(champ_all_participation[champ_num]),1), 2)
        # print "Total kills: ",ckills,"Total deaths: ",cdeaths,"Total Assists: ",cassists
        # print "Champ w/l trend: ", champ_all_wl[champ_num]
        print "Cumulative KDA: ", champ_total_kda[champ_num]
        # print champ_totals[champ_num]
        # print "Kill percentages: ",champ_all_kill_perc[champ_num]
        # print "Death percentages: ",champ_all_death_perc[champ_num]
        print ""
        
minutes = []    
seconds = []

for game in all_stats:
        if game[3] == '-' or game[3] == None or game[4] == '-' or game[4] == None:
                pass
        else:   
                minutes.append(int(game[3]))
                seconds.append(int(game[4]))
secs = sum(seconds)
avg_game_time = (sum(minutes) + sum(seconds)/60 + (sum(seconds) % 60)*0.1)/(len(all_stats)-unknown)

# print avg_game_time
# print team_kda
# print len(team_kda)

print num_champ_games


'''
Tables

KDA - H > L


'''

all_champs = zip(champs,num_champ_games,champ_basics,champ_kda, champ_participation, champ_kill_perc, champ_death_perc)
# print all_champs

# by_overall_kda, namelist = zip(*sorted(enumerate(champ_kda), key=itemgetter(1), reverse=True))

temp = sorted(all_champs, key=lambda x: x[3], reverse=True)
namelist, num_games, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
print "Best KDA"
for i, j in enumerate(namelist):
        print i, ": ", j, " = ", by_overall_kda[i]
print   

temp = sorted(all_champs, key=lambda x: x[4], reverse=True)
namelist, num_games, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
print "Best Participation"
for i, j in enumerate(namelist):
        print i, ": ", j, " = ", by_participation[i]
print

temp = sorted(all_champs, key=lambda x: x[1], reverse=True)
namelist, num_games, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
print "Most Played"
for i, j in enumerate(namelist):
        print i, ":", j, " = ", num_games[i]
print
# temp = sorted(all_champs, key=lambda x: x[4], reverse=True)
# namelist, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
# print "Best Kill Perc"
# for i, j in enumerate(namelist):
        # print i, ": ", j, " = ", by_kill_perc[i]
# print

# temp = sorted(all_champs, key=lambda x: x[5], reverse=False)
# namelist, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
# print "Best Death Perc"
# for i, j in enumerate(namelist):
        # print i, ": ", j, " = ", by_death_perc[i]
# print

temp = sorted(all_champs, key=lambda x: x[0], reverse=False)
namelist, num_games, basics, by_overall_kda, by_participation, by_kill_perc, by_death_perc = map(list, zip(*temp))
print "Overall"
for i, j in enumerate(namelist):
        print "%i: \t%s \n\t%r \t%r \t%r \t%r" % (i, j, by_overall_kda[i], by_participation[i], by_kill_perc[i], by_death_perc[i])
        # print i, ": ", j, " : ", basics[i], " "by_death_perc[i]
print


the_champ = 'Rumble'
for i in sorted(champ_enemies[the_champ]):
        print "{c}: games {g} wins: {w} losses: {l}".format(c=i, g=champ_enemies[the_champ][i]['games'],w=champ_enemies[the_champ][i]['wins'], l=champ_enemies[the_champ][i]['losses'])



# print total_wl
# print total_kda
print "kda: ",total_kda[-1]
print "Totals: ", kills, deaths, assists
print len(total_wl)
print len(total_kda)
print missing
# total_wl.insert(0,0)
print "Blue wr%: ",round((tblue_wins*100)/(len(total_wl_blue)),2)
print "Purple wr%: ",round((tpurple_wins*100)/(len(total_wl_purple)),2)
##pyplot.plot(total_wl_blue,'b')
##pyplot.plot(total_wl_purple,'r')
##pyplot.show()

picdir = "C:/Riot Games/League of Legends/RADS/projects/lol_air_client/releases/0.0.1.91/deploy/assets/images/champions"
##print champ_
mygui = GraphGui(picdir, champs, champ_total_kda, champ_wr, brpr_text, champ_time_ave, "GUI")
mygui.mainloop()
