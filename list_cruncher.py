#!/usr/bin/python
import gdata.docs.data
import gdata.docs.client
import gdata.service

# set the metadata for the program connecting to the google docs server
company = 'onethirtybpm'
app = 'listcruncher'
version = 'v1'
application = company + '-' + app + '-' + version

def setup_gdocs(application_string, ssl=True, debug=False):
	'''Setup connection to gdocs'''
	client = gdata.docs.client.DocsClient(source=application_string)
	client.ssl = ssl
	client.http_client.debug = False
	return client
	
def main():
	# initialize gd_client
	gd_client = setup_gdocs(application)
	
	email = raw_input("Email: ")
	password = raw_input("Password: ")
	
	# handle captcha challenges
	try:
		gd_client.ClientLogin(email, password, source=application)
	except gdata.service.CaptchaRequired:
		print('Please visit ' + gd_client.captcha_url)
		answer = raw_input('Answer to the challenge? ')
		gd_client.ClientLogin(email, password, source=application,
			captcha_token=client.captcha_token, captcha_response=answer)
	except gdata.client.BadAuthentication:
		exit('Users credentials were unrecognized')
	except gdata.client.Error:
		exit('Login Error')
		
if __name__ == '__main__':
	main()