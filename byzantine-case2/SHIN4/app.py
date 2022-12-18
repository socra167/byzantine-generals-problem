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
		# save lead
		if(values.get(lead)):
			values[lead] = values[lead] + 1
		else:
			values[lead] = 1
		received = received + 1
		try:
			# send lead value to others
			response = requests.get('http://SHIN2:5001/?value=' + lead)
			response = requests.get('http://SHIN3:5002/?value=' + lead)
		except requests.exceptions.RequestException as e:
			return 'ERROR\n'
	else:
		if(values.get(value)):
			values[value] = values[value] + 1
		else:
			values[value] = 1
		received = received + 1
		
	if(received == 3):
		print('Every message is received...', file=sys.stderr)
		# list comprehension
		maxVal = [k for k, v in values.items() if max(values.values()) == v]
		print(maxVal, file=sys.stderr)
		received = 0
		values = dict()
		if(len(maxVal) == 1):
			print('[SHIN4] possible : ' + maxVal[0], file=sys.stderr)
			return '[SHIN4] possible : ' + maxVal[0]
		else:
			print('[SHIN4] impossible!', file=sys.stderr)
			return '[SHIN4] impossible!'
	return ''
	
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5003, debug = True)
