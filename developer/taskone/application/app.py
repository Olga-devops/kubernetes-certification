from flask import Flask, jsonify, json
import time
app = Flask(__name__)


## Ready page for application
@app.route('/started')
def started():
    return jsonify({"message": "started"})


## healthy page for application
@app.route('/healthz')
def healthz():
    return jsonify({"message": "healthy"})


if __name__ == '__main__':
    time.sleep(10)
    app.run(port=8080, debug=True, host='0.0.0.0')
