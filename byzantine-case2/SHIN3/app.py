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
	
	if lead is not None: # message from Leader
		try:
			# send FAULT value (BYZANTINE)
			response = requests.get('http://SHIN2:5001/?value=' + 'Oowgnod')
			response = requests.get('http://SHIN4:5003/?value=' + 'Oowgnod')
		except requests.exceptions.RequestException as e:
			return 'ERROR\n'
	return ''
		
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5002, debug = True)
