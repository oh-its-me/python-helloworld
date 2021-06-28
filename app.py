from flask import Flask
from flask import json
import logging
app = Flask(__name__)

logging.basicConfig(
	filename='app.log',
	level=logging.DEBUG,
	# format='[%(asctime)s] %(message)s'
	# datefmt='%H:%M:%S'
)

@app.route("/")
def hello():
	app.logger.info("Hello request successful")
	return "Hello World!"

@app.route("/status")
def healthCheck():
	data = {"result":"OK - healthy"}	
	response = app.response_class(
		response = json.dumps(data),
		status = 200,
		mimetype = 'application/json'
	)
	app.logger.info("Status request successful")
	return response

@app.route("/metrics")
def metric():
	data = {
		"status": "success",
		"code": 0,
		"data": {
			"UserCount":140,
			"UserCountActive":23
		}
	}	
	response = app.response_class(
		response = json.dumps(data),
		status = 200,
		mimetype = 'application/json'
	)
	app.logger.info("Metric request successful")
	return response

if __name__ == "__main__":
	app.logger = logging.getLogger(__name__)
	# logger.setLevel(logging.DEBUG)

	app.run(host='0.0.0.0')
