from flask import Flask
from flask import json
import logging

FORMAT = '%(asctime)s %(endpoint)s %(message)s'
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({'status': 'success', 'code': 0, 'data': {'UserCount': 140, 'UserCountActive': 23}}),
            status=200,
            mimetype='application/json'
    )
    extra={'endpoint': '/metrics'}
    logger.debug('endpoint was reached', extra=extra)
    return response

@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    extra={'endpoint': '/status'}
    logger.debug('endpoint was reached', extra=extra)
    return response

@app.route("/")
def hello():
    extra={'endpoint': '/'}
    logger.debug('endpoint was reached', extra=extra)
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=FORMAT)
    app.run(host='0.0.0.0')
