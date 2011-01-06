#!/usr/bin/python
##
# Name: Vote Counter (vote_counter.py)
# Purpose: To calculate a sorted list of album rankings for 130BPM's year-end
#		   rankings (and any other ranking).
# Date: January 5, 2011
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: Apache License 2.0
##
import csv
from operator import itemgetter
from optparse import OptionParser
import sys

# Filters
from vote_filters import *

class Voter(object):
	'''Assigns a voter with his albums and multiplier'''
	def __init__(self, name, multiplier, albums):
		self.name = name
		self.multiplier = multiplier
		self.albums = albums

def generateAlbums(voters):
	albums = {} # Dictionary in the format {"Album Title": number_of_votes}
	# Populate album_list
	for voter in voters:
		for (score, album) in enumerate(reversed(voter.albums)):
			album = filterAlbumString(album, filters)
			
			# If the album is not a blank string then try to add it to album_list
			# but if it already exists just add the albums calculate score (not 
			# album_score) to the value.
			if album:
				try:
					albums[album] = int(albums[album]) + int(voter.multiplier) * int(score)
				except:
					albums[album] = int(voter.multiplier) * int(score)						
	return albums

def main():
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename", default="./test.csv",
		help="The location of the csv file", metavar="FILE")
	(options, args) = parse.parse_args()
	
	reader = csv.reader(open(options.filename, "rb")) # import the csv file
	reader.next() # Skip the header information in the csv file

	voters = [Voter(row[2], row[1], row[3:]) for row in reader]
	albums = generateAlbums(voters)
	
	# Print out a sorted table of votes and albums
	print "Votes | Album"
	print "------|-------------------------------------------------------------"		
	# sort and reverse list for easier reading
	for album in reversed(sorted(albums.items(), key=itemgetter(1))):
		print "%5s | %s" % (album[1], album[0])			
			
if __name__ == '__main__':
	main()
