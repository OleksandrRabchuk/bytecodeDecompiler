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
        process = subprocess.run(['panoramix', address], shell=True)
        print(process)
        return json.loads(process.stdout)
    except Exception as e:
        return flask.Response(status=400)

