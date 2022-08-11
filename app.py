# app.py
import flask
import subprocess
import json
app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    try:
        data = flask.request.json
        address = data['address']
        command = f"panoramix {address}"
        process = subprocess.check_output(command.split()).decode('ascii').split('\n')
        print(process)
        return address
    except Exception as e:
        return flask.Response(status=400)


