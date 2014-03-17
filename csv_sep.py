# Main Class for opening csv and separating

'''
Written 16/03/2014
	- created main class


'''




import csv

class csv_file:
	def __init__(self, csv_dir, csv_txt):
		self.csv_dir = csv_dir
		self.csv_txt = csv_txt
		self.stats = []
		print self.csv_dir
		print self.csv_txt
		
	def open(self):
		with open(self.csv_dir+self.csv_txt,'r') as f:	# eventually change how we get the file
			reader = csv.reader(f)
			for row in reader:
				self.stats.append(row)

		# delete initial line
		self.stats.pop(0)

