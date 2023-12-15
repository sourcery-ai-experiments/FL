from flask import Flask
from time import time

app = Flask(__name__)


@app.route("/")
def tested_fog():
    return "THE FOG IS COMING" * int(time()/100000)

app.run(port=9002)
