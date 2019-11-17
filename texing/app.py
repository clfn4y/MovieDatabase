# /usr/bin/env python
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
		resp.message('Hello, you are looking for: {}'.format(message_body[7:]))
	elif message_body[0:4].lower() == "get:":
		resp.message("In get")
	elif message_body[0:5].lower() == "send:":
		resp.message("Send will send the movie to your email or wherever you want it")
	elif message_body[0:8].lower() == "commands":
		intructions = "Welcome to sNetflix"
		intructions += "\n   -- check: movie,...,... \n    -(This will see if you have any of those movies.)"
		intructions += "\n   -- get: movie,...,... \n    -(This will get whatever movies you want. Will send back what it couldnt get or if you have it.)"
		intructions += "\n   -- send: movie \n    -(This will send you a movie to where you want.)"
		resp.message(intructions)
	else:
		resp.message("Not an actuall instruction")

	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)