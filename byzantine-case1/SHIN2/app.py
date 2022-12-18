from flask import Flask
from flask import request
import requests
import sys
app = Flask(__name__)

received = 0
values = {}

@app.route('/')
def send():
	global received
	global values
	lead = request.args.get('lead')
	value = request.args.get('value')
	
	if lead is not None:
		try:
			# send FAULT value (BYZANTINE)
			response = requests.get('http://SHIN3:5002/?value=' + 'Oowgnod')
		except requests.exceptions.RequestException as e:
			return 'ERROR\n'
		if(values.get(lead)):
			values[lead] = values[lead] + 1
		else:
			values[lead] = 1
		received = received + 1
		return ''
	else:
		if(values.get(value)):
			values[value] = values[value] + 1
		else:
			values[value] = 1
		received = received + 1
		
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5001, debug = True)
