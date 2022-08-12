# app.py
import flask
import subprocess
import json
import os
import platform
app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    try:
        os.environ["WEB3_PROVIDER_URI"] = "https://eth-mainnet.g.alchemy.com/v2/gOSHH4ng6NXaQA7zPRT1pBAQ5srcXtt0"
        data = flask.request.json
        address = data['address']
        for item, value in os.environ.items():
            print('{}: {}'.format(item, value))
        command = f"panoramix {address}"
        process = subprocess.check_output(command.split()).decode('ascii').split('\n')
        print(process)
        return address
    except Exception as e:
        return flask.Response(status=400)


