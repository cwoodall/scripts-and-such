#!/usr/bin/python

import csv
from operator import itemgetter

## CURENT STATUS: FAIL
#class Album(object):
#	'''Album object: REVISE DOCSTRING'''
#	def __init__(self, title, votes=0):
#		self.title = title
#		self.votes = votes
	
class Voter(object):
	# Revise DOCSTRING
	'''Assigns a voter with his votes and multiplier'''
	def __init__(self, name, multiplier, albums):
		self.name = name
		self.multiplier = multiplier
		self.albums = albums

def filterAlbumString(album_string):
	# for this situation only
	album_string = album_string.replace('Beatiful', 'Beautiful')
	album_string = album_string.replace('Deehunter', 'Deerhunter')
	album_string = album_string.replace('Monae, Janelle', 'Janelle Monae' )
	
	# General cleanup
	album_string = album_string.replace('\xe2\x80\x93', '-')
	album_string = album_string.replace('?', '')
	album_string = album_string.replace('\t', '')
	album_string = album_string.replace('The', '')
	album_string = album_string.replace('  ', ' ')
	album_string = album_string.title()
	album_string = album_string.split(':')[0]
	album_string = album_string.rstrip()	
	album_string = album_string.lstrip()		
	
	return album_string
				
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
			album = filterAlbumString(album)
			if album:
				try:
					album_list[album] = int(album_list[album] + (int(voter.multiplier) * int(vote_score)))
				except:
					album_list[album] = int(voter.multiplier) * int(vote_score)
			vote_score -= 1
	
	# Print out a sorted table of votes and albums
	print "Votes | Album"
	print "------|-------------------------------------------------------------"		
	for album in reversed(sorted(album_list.items(), key=itemgetter(1))):
		print "%5s | %s" % (album[1], album[0])
