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
        process = subprocess.Popen(['panoramix', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        print('works')
        print(out)
        return address
    except Exception as e:
        return flask.Response(status=400)

