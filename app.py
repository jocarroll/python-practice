#!/usr/bin/python
import time;
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    localtime = time.asctime( time.localtime(time.time()) )
    return(f"Current date/time: {localtime}")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
