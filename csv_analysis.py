#!/usr/bin/python

import csv
from operator import itemgetter

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
	voter_list = []
	album_list = {}
	reader.next()
	for row in reader:
		voter = Voter(row[2], row[1], row[3:])		
		voter_list.append(voter)
	for voter in voter_list:
		vote_score = 50
		for album in voter.albums:
			album = album.replace('\xe2\x80\x93', '-')
			album = album.replace('?', '')
			album = album.replace('Beatiful', 'Beautiful')
			album = album.replace('\t', '')
			album = album.replace('Deehunter', 'Deerhunter')
			album = album.replace('The', '')
			album = album.replace('  ', ' ')
			album = album.replace('Monae, Janelle', 'Janelle Monae' )
			album = album.title()
			album = album.split(':')[0]
			album = album.rstrip()	
			album = album.lstrip()		
#			album = album.replace(' ','')
			
			if album:
				try:
					album_list[album] = int(album_list[album] + (int(voter.multiplier) * int(vote_score)))
				except:
					album_list[album] = int(voter.multiplier) * int(vote_score)
			vote_score -= 1
	
	print "Votes | Album"
	print "------|-------------------------------------------------------------"		
	for album in sorted(album_list.items(), key=itemgetter(1)):
		print "%5s | %s" % (album[1], album[0])
