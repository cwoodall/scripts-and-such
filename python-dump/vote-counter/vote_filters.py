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

def filterAlbumString(title, filters=[]):
	''' filterAlbumString: Filters the title of an album with standard filters 
		so that common typos are corrected and they can be compared more 
		appropriately.
		
		title
		filters: A list of tuples in the format (old,new) for replacement
			string.replace(old,new)
	'''
	# Add in custom filters
	for filter in filters:
		title = title.replace(filter[0], filter[1])

	# for this situation only
	title = title.replace('Beatiful', 'Beautiful')
	title = title.replace('Deehunter', 'Deerhunter')
	title = title.replace('Monae, Janelle', 'Janelle Monae' )

	# General cleanup
	title = title.replace('\xe2\x80\x93', '-')
	title = title.replace('?', '')
	title = title.replace('\t', '')
	title = title.replace('The', '')
	title = title.replace('  ', ' ')
	title = title.title()
	title = title.split(':')[0]
	title = title.rstrip()	
	title = title.lstrip()		

	return title

if __name__ == '__main__':
	for filter in filters:
		print filter