#!/usr/bin/python
##
# Name: Vote Filters (vote_filters.py)
# Purpose: Contains the filters for vote_counter
# Date: January 5, 2011
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: Apache License 2.0
##

filters = [('Beatiful', 'Beautiful'), ('Deehunter', 'Deerhunter'), 
	('Monae, Janelle', 'Janelle Monae')] # Filters to make calculations more accurate

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

if __name__ == '__main__':
	for filter in filters:
		print filter