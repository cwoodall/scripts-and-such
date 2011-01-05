#!/usr/bin/python
import csv
from operator import itemgetter

class Voter(object):
	'''Assigns a voter with his albums and multiplier'''
	def __init__(self, name, multiplier, albums):
		self.name = name
		self.multiplier = multiplier
		self.albums = albums


def filterAlbumString(album_string, filters=[]):
	''' Filters the title of an album with standard filters so that common
		typos are corrected and they can be compared more appropriately
		
		Takes an argument filters which is a list of tuples in (old, new) 
		format for repalces:
			string.replace(old, new)		
	'''
	# Add in custom filters
	for filter in filters:
		album_string = album_string.replace(filter[0], filter[1])

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


def main():
	reader = csv.reader(open("test.csv", "rb")) # import the csv file
	voter_list = []
	album_list = {} # Dictionary in the format {"Album Title": number_of_votes}
	filters = [('Beatiful', 'Beautiful'), ('Deehunter', 'Deerhunter'), 
		('Monae, Janelle', 'Janelle Monae')] # Filters to make calculations more accurate
	reader.next() # Skip the header information in the csv file

	# Fill voter_list with list of Voter objects
	for row in reader:
		voter = Voter(row[2], row[1], row[3:])		
		voter_list.append(voter)
	
	for voter in voter_list:
		# Start vote_score at 50 and decrement to 1 to adjust the weight on the albums
		album_score = 50
		for album in voter.albums:
			album = filterAlbumString(album, filters)
			
			# if the album is not a blank string then try to add it to album_list
			# but if it already exists just add the albums calculate score (not 
			# album_score) to the value.
			if album:
				try:
					# make sure everythign is an int
					album_list[album] = int(album_list[album]) + int(voter.multiplier) * int(album_score)
				except:
					album_list[album] = int(voter.multiplier) * int(album_score)
						
			album_score -= 1
	
	# Print out a sorted table of votes and albums
	print "Votes | Album"
	print "------|-------------------------------------------------------------"		
	# sort and reverse list for easier reading
	for album in reversed(sorted(album_list.items(), key=itemgetter(1))):
		print "%5s | %s" % (album[1], album[0])			
			
if __name__ == '__main__':
	main()
