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
        data = flask.request.json
        address = data['address']

        # exp = subprocess.run(['export WEB3_PROVIDER_URI=https://eth-mainnet.g.alchemy.com/v2/gOSHH4ng6NXaQA7zPRT1pBAQ5srcXtt0'], capture_output=True, shell=True)
        # command = f"panoramix {address}"
        # process = subprocess.check_output(command.split()).decode('ascii').split('\n')
        # print(exp)
        # print(process)
        return os.environ
    except Exception as e:
        return flask.Response(status=400)


