from flask import Flask
from flask import request
import requests
import sys
app = Flask(__name__)

@app.route('/')
def send():
	try:
		response = requests.get('http://SHIN2:5001/?lead=' + 'Dongwoo')
		response = requests.get('http://SHIN3:5002/?lead=' + 'Dongwoo')
		response = requests.get('http://SHIN4:5003/?lead=' + 'Dongwoo')
	except requests.exceptions.RequestException as e:
		print('\n Cannot reach the service. \n', file=sys.stderr)
		return 'ERROR\n'
	return 'SHIN1 : \'Dongwoo\' sent to others!\n'
	
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 5000, debug = True)
