import os
import smtplib
import requests
import time
import datetime
from datetime import datetime
from django.http import HttpResponse
# import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# from ArubaCloud.PyArubaAPI import CloudInterface
# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# ARUBA_NAME = os.environ.get('ARUBA_NAME')
# ARUBA_PASS = os.environ.get('ARUBA_PASS')


EMAIL_HOST_USER = 'mava.monitor@gmail.com'
EMAIL_HOST_PASSWORD = 'Mavabc@1234'
EMAIL_ADDRESS = EMAIL_HOST_USER
EMAIL_PASSWORD = EMAIL_HOST_PASSWORD


APP_NAME = "MAVA Server Monitoring Platform"
MAVA_TITLE_PREFIX = "MAVA IMPORTANT: Server ALERT"
MESSAGE_PREFIX = ""
MESSAGE_SALUTE = "Hello,\n"
MESSAGE_ALERT = "' is NOT accessible from the Monitoring applicaton. Something\'s terribly wrong.\nPlease check the server and application immediatley.\n"
MESSAGE_FOOTER = "\nSent by : " + APP_NAME


TARGET_DICT = { 'MGSOSA': 'http://mavapartnersin.pythonanywhere.com',
				'NCGA': 'http://gims.ncga.com/Mobile/',
				'Blackswan Staging': 'http://blackswanstaging.black-swan-insurance.com/login',
				}

def notify():
	print('Something\'s terribly wrong.')


def send_gmail(email_to,title , message):
	msg = MIMEMultipart()
	# message = "This is an email"

	password = EMAIL_PASSWORD
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = email_to
	msg['Subject'] = title

	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()

def format_message(server_name,url, status_code):
	# print(server_name,url, status_code)
	now = datetime.now()
	cur_time = now.strftime("%B  %d %Y %H:%M:%S")

	message = "\nServer ' " + server_name + MESSAGE_ALERT
	message = MESSAGE_PREFIX +  MESSAGE_SALUTE + message
	message =   message + "\nURL: " + url + " . Status :  " + str(status_code)     +"\n"
	message =   message + "\nAlert time: " + cur_time + "\n"
	message =  message + MESSAGE_FOOTER
	return message

def monitor(server_name, url,to_email):
	status = ''
	try:
	    r = requests.get(url, timeout=15)
	    status = r.status_code
	    if  status != 200 :
	    	print(status)
	    	message = format_message(server_name, url, status ) # , url, r.status_code
	    	# print(message)
	    	send_gmail(to_email,MAVA_TITLE_PREFIX, message)
	    	print('Mail Sent')

	    else :
	     	print('Everything is fine for {} ,  {}'.format(server_name ,datetime.now().strftime("%d-%m-%Y %H:%M")))
	     	# message = format_message(server_name, url, status ) # , url, r.status_code
	     	# print(message)

	     	# send_gmail(to_email,MAVA_TITLE_PREFIX, message)
	     	# print('Mail Sent')


	except Exception as e:
		status = ''
		print(e)
		error = str(e)
		if  ( error.find("Max retries exceeded ") != -1 ) :
			# print(status)
			message = format_message(server_name, url, status ) # , url, r.status_code
			print(message)
			send_gmail(to_email,MAVA_TITLE_PREFIX, message)
			print('Mail Sent')

	    # print('Unable to connect to server!' + str(e))





# message = format_message('server_name', 'url', 200 ) # , url, r.status_code
# print(message)

def check_server_status(request):
    for svr in TARGET_DICT :
        name=svr
        # print(name)
        url = TARGET_DICT.get(name)
        # print(url + '\n')
        to_email =  'anoob.vm@mavapartners.com' # 'kishore.george@mavapartners.com'
        # to_email =  'kishore.george@mavapartners.com' # 'kishore.george@mavapartners.com'
        print('\n*** Monitoring : ', url + ' ...')
        result = monitor(name, url,to_email)
        return HttpResponse('success')
