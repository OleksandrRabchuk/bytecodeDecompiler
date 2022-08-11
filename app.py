# app.py
import flask
import subprocess
import json
app = flask.Flask(__name__)

@app.route("/", methods=["Get"])
def index():
    return "Hi"
@app.route("/", methods=["POST"])
def index():
    try:
        data = flask.request.json
        address = data['address']
        process = subprocess.run(['panoramix', address], shell=True)
        print(process)
        return address
    except Exception as e:
        return flask.Response(status=400)

