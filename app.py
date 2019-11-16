from flask import Flask, Response, request, jsonify, render_template, session, redirect, url_for
from database import DatabaseConnection
import datetime, bcrypt
import os
import datetime as DT
import random
from pprint import pprint
import json

app = Flask(__name__)
db = DatabaseConnection()

@app.route("/", methods=["GET"])
# home page 
def index(): 
    return render_template("index.html")

if __name__ == "__main__":
    app.secret_key = "secretkey"
    app.run(host="localhost", port=4000, debug=True)
