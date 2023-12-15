from flask import Flask
from time import time

app = Flask(__name__)


@app.route("/")
def tested_fog():
    return "THE FOG IS COMING" * int(time()/100000)

if __name__ == "__main__":
    app.run(port=90145)
