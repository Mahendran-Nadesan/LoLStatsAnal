# LoLStatsAnal
# kda_graph_panel.py
# Small gui to show champ picks and kda graph when clicked


'''
A small gui with several rows (1 per champ), each with a square button/pic of the champ, with 
buttons next to it, several dummies, one of which is "kda graph"

Currently, pics are from:
C:/Riot Games/League of Legends/RADS/projects/lol_air_client/releases/0.0.1.83/deploy/assets/images/champions

Bugs/Specials:
- Current name representation is as per the picture directory, i.e. not "Dr. Mundo", but "DrMundo", 
not "Wukong", but "MonkeyKing".
- Currently some games in the csv have no champion attached to them, and need to be "removed" (they 
show up as "-").
'''

# Imports
import Tkinter as tk
import tkFileDialog
import os
from PIL import Image, ImageTk
from matplotlib import pyplot
from operator import itemgetter

# GUI Class
class GraphGui(tk.Frame):
	def __init__(self, picdir, champlist, kdalist, wrlist, brprlist, title, master=None):
		tk.Frame.__init__(self)
		# self.master = master
		self.picdir = picdir
		self.champlist = champlist
		self.kdalist = kdalist
		self.wrlist = wrlist
		self.brprlist = brprlist
		self.master.title(title)
		
		self.generate_pics()
		self.new_frame = []
		self.new_label = []
		self.text_label = []
		self.wr_label = []
		self.side_wr_label = []
		
		for i, j in enumerate(self.champlist):
			self.create_entry(i)
		# self.pic_label = tk.Button(self.master, image=self.newpic,borderwidth=0, command=self.on_click)
		# self.pic_label.pack(side="left")
		# self.text_label = tk.Label(self.master, text=self.champlist[0])
		# self.text_label.pack(side="left")
		# self.pic_canvas = tk.Canvas(self.master, bd=0)
		# self.pic_canvas.create_image(0, 0, image = self.newpic, tags="IMG")
		# self.pic_canvas.pack()
		
	def on_click(self, i):
		pyplot.plot(self.kdalist[i])	
		pyplot.title(self.champlist[i])
		pyplot.show()

	def on_click_wr(self, i):
                pyplot.plot(self.wrlist[i])
                pyplot.title(self.champlist[i] + " win rate")
                pyplot.show()
	
	# def find_champ(self, i):
		# return self.champ(i[0])
		
	def generate_pics(self):
		self.pics = []
		for i, j in enumerate(self.champlist):
			if j != "-":
				self.pic = Image.open(os.path.join(self.picdir, j + "_Square_0.png"))
				self.pic = self.pic.resize((40,40),Image.ANTIALIAS)
				self.pics.append(ImageTk.PhotoImage(self.pic))
			else:
				self.pics.append(ImageTk.PhotoImage(self.pic))
		
		# return self.pics
		
	def create_entry(self, i):
	# Consider redoing this with insert as per
	# http://stackoverflow.com/questions/7040172/python-tk-multiple-buttons-creation-problem/7040309#7040309
		f = i / 3
		if i % 3 == 0:
			
			self.new_frame.append(tk.Frame(self.master))
			self.new_frame[f].pack(side="top", pady=5)
		
		self.new_label.append(tk.Button(self.new_frame[f], image=self.pics[i], command=lambda i=i : self.on_click(i)))
		# Note on above line:
		# This passes the value of i to the lambda as a local variable. Without this, you are using a reference to the original
		# variable which will, of course, always resolve to whatever is stored in the original variable.
		self.new_label[i].pack(side="left", padx=5)
		
		self.wr_label.append(tk.Button(self.new_frame[f], text="WR", command=lambda i=i : self.on_click_wr(i)))
		self.wr_label[i].pack(side="left", padx=5)
		
		self.text_label.append(tk.Label(self.new_frame[f], width=10, text=self.champlist[i]))
		self.text_label[i].pack(side="left", padx=5)
		
		self.side_wr_label.append(tk.Label(self.new_frame[f], width=20, relief="sunken", text=self.brprlist[i]))
		self.side_wr_label[i].pack(side="left", padx=5)
		
		return self.new_frame[f]
		
