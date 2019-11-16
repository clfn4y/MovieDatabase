# # This code is for sending and reciving text messages
# # +12054987110

# from flask import Flask, request
# from twilio import twiml


# app = Flask(__name__)

# @app.route('/sms', methods=['POST'])
# def sms():
# 	number = request.form['From']
# 	message_body = request.form['Body']

# 	resp = twiml.Response()
# 	resp.message('Hello {}, you said: {}'.format(number, message_body))
# 	return str(resp)


# if __name__ == '__main__':
#     app.run()














# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'AC9708c90eeb68f98cfd555714ae656458'
# auth_token = '17806343c634d1fdd24f49f1d4cf9e7e'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Yo this is caleb and this is my ython script to send messages!!\nWorking on reciving now",
#                      from_='+12054987110',
#                      to='+14174139906'
#                  )

# print(message.sid)


# EXAMPLE JSON API RESPONSE
# {
#   "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
#   "api_version": "2010-04-01",
#   "body": "Join Earth's mightiest heroes. Like Kevin Bacon.",
#   "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
#   "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
#   "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
#   "direction": "outbound-api",
#   "error_code": null,
#   "error_message": null,
#   "from": "+15017122661",
#   "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
#   "num_media": "0",
#   "num_segments": "1",
#   "price": null,
#   "price_unit": null,
#   "sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
#   "status": "sent",
#   "subresource_uris": {
#     "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
#   },
#   "to": "+14178337395",
#   "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
# }













# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():

	number_person = request.form['From']
	number_server = request.form['To']
	message_body = request.form['Body']
	# name_person = request.form['friendlyName']
	resp = MessagingResponse()


	if message_body[0:6].lower() == "check:":
		# f = open("MovieProject/tKinter/MovieDatabase/Flash_drive/index.txt", "r")
		resp.message('Hello, you are looking for: {}'.format(message_body[:7]))
	else:
		# resp.message('Hello {}, you said on else: {}'.format(number_person, message_body))
		resp.message("Do not have that movie: {}".format(name_person))

	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)