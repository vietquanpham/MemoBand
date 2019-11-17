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

@app.route("/medication", methods=["GET", "POST"])
def medication():
    if request.method == 'POST':
        document = {
            "label": request.form['label'],
            "day": request.form.getlist('day[]'),
            "time": request.form['time'],
            "location": request.form['location'],
            "notes": request.form['notes'],
        }
        db.insert("medication", document)
        return render_template("medication.html")
    else:
        return render_template("medication.html")

@app.route("/meal", methods=["GET", "POST"])
def meal():
    if request.method == 'POST':
        document = {
            "meal": request.form['meal'],
            "time": request.form['time'],
            "notes": request.form['notes'],
        }
        db.insert("meal", document)
        return render_template("meal.html")
    else:
        return render_template("meal.html")

@app.route("/sleep", methods=["GET", "POST"])
def sleep():
    if request.method == 'POST':
        document = {
            "time": request.form['time'],
        }
        db.insert("sleep", document)
        return render_template("sleep.html")
    else:
        return render_template("sleep.html")

@app.route("/hydration", methods=["GET", "POST"])
def hydration():
    if request.method == 'POST':
        document = {
            "time": request.form['time'],
        }
        db.insert("hydration", document)
        return render_template("hydration.html")
    else:
        return render_template("hydration.html")

if __name__ == "__main__":
    app.secret_key = "secretkey"
    app.run(host="localhost", port=4000, debug=True)
