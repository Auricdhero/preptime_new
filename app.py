import os
import json

from flask import Flask, flash, url_for, redirect, render_template, request, session
from passlib.hash import sha256_crypt
from flask_pymongo import PyMongo
from flask import request
import yaml

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/preptime_db"
mongo = PyMongo(app)

# db



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        return render_template('students.html', name=NameError)

    return render_template('index.html', name=NameError)

def visa():
    return render_template('visa.htm', name=NameError)


def question():
    return render_template()
if __name__== "__main__":
    app.run(debug=True)

