#!/usr/bin/python
import gdata.docs.data
import gdata.docs.client

# set the metadata for the program connecting to the google docs server
company = 'onethirtybpm'
app = 'listcruncher'
version = 'v1'

def setup_gdocs(company_name, app_name, version, ssl=True, debug=False):
	'''Setup connection to gdocs'''
	source_string = company_name + '-' + app_name + '-' + version
	client = gdata.docs.client.DocsClient(source=source_string)
	client.ssl = ssl
	client.http_client.debug = False
	return client
	
if __name__ == '__main__':
	setup_gdocs(company, app, version)
