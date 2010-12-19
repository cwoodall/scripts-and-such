#!/usr/bin/python

import csv

## CURENT STATUS: FAIL
class Album(object):
	'''Album object: REVISE DOCSTRING'''
	def __init__(self, title, votes=0):
		self.title = title
		self.votes = votes
	
class Voter(object):
	# Revise DOCSTRING
	'''Assigns a voter with his votes and multiplier'''
	def __init__(self, name, multiplier, albums):
		self.name = name
		self.multiplier = multiplier
		self.albums = albums
		
if __name__ == '__main__':
	reader = csv.reader(open("test.csv", "rb"))
	album_list = {}
	reader.next()
	for row in reader:
#		voter = Voter(row[2], row[1], row[3:])
#		print "Name: " + voter.name
#		print "Multiplier: " + voter.multiplier
#		print "Votes: ",
		for album in row[3:]:
			a = True
			for i, v in album_list.iteritems():
				if i.find('The National') == -1:
					a = False
			if a == True:
				album_list.update({album: 0})
	print album_list