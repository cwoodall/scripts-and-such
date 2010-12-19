#!/usr/bin/python
##
# Name: List Cruncher
# Purpose: Crunch lists for OneThirtyBPMs end of year list
# Date: December 16, 2010
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: MIT/BSD License
##

import gdata.docs
import gdata.docs.service
import gdata.service
import gdata.spreadsheet.service
import csv

# set the metadata for the program connecting to the google docs server
company = 'onethirtybpm'
app = 'listcruncher'
version = 'v1'
# Produce the source_string/application name sent to google for connection
application = company + '-' + app + '-' + version

# Print feed information to the console
def PrintFeed(feed):
	'''Prints out the contents of a feed to the console.'''
	print '\n'
	if not feed.entry:
		print 'No entries in feed.\n'
	for entry in feed.entry:
		print '%s' % (entry.title.text.encode('UTF-8'))			


def main():
	# Input
	email = raw_input("Email: ")
	password = raw_input("Password: ")
	
	# Initialize DocService class on client gd_client
	gd_client = gdata.docs.service.DocsService(source=application)
	spreadsheets_client = gdata.spreadsheet.service.SpreadsheetsService()
	
	# Handle captcha challenges on login
	try:
		gd_client.ClientLogin(email, password)
	except gdata.service.CaptchaRequired:
		print('Please visit ' + gd_client.captcha_url)
		answer = raw_input('Answer to the challenge? ')
		gd_client.ClientLogin(email, password, source=application,
			captcha_token=client.captcha_token, captcha_response=answer)
	except gdata.service.BadAuthentication:
		exit('Users credentials were unrecognized')
	except gdata.service.Error:
		exit('Login Error')
	
	document_title = ''
	q = gdata.docs.service.DocumentQuery()
	while not document_title:
		# Query for spreadsheet
		document_title = raw_input('Spreadsheet (Press ENTER for a list of spreadsheets): ')	
		if not document_title:
			q.categories=['spreadsheet']
		else:
			q['title'] = document_title
			q['title-exact'] = 'true'
		feed = gd_client.Query(q.ToUri())	
		PrintFeed(feed)
	
	file_path = raw_input('File Path: ')
	
	# Login to spreadsheet
	spreadsheets_client.ClientLogin(email, password)
	# substitute the spreadsheets token into our gd_client
	docs_auth_token = gd_client.GetClientLoginToken()
	gd_client.SetClientLoginToken(spreadsheets_client.GetClientLoginToken())
	
	# download spreadsheet
	for entry in feed.entry:
		gd_client.Export(entry, file_path, gid=0)
		print "Downloading spreadsheet to %s" % (file_path)
	
	# add in functionality to work with csv
		
if __name__ == '__main__':
	main()
