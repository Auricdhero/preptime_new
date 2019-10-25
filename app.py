import os
import json

from flask import Flask, flash, url_for, redirect, render_template, request, session
from passlib.hash import sha256_crypt
from flask_pymongo import PyMongo
from flask import request
import yaml

app = Flask(__name__)
#usr = os.environ['MONGO_DB_USER']
#pwd = os.environ['MONGO_DB_PASS']

#db1
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/admin_db")

#db2
mongo2 = PyMongo(app, uri="mongodb://localhost:27017/school_admin_db")

#db3
mongo3 = PyMongo(app, uri="mongodb://localhost:27017/student_db")


mongo = PyMongo(app)




#run home termplate
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", name=NameError)

    

#payment run templates
def visa():
    return render_template('visa.htm', name=NameError)
def mastercard():
    return render_template('mastercard.htm', name=NameError)
def momo():
    return render_template('momo.htm', name=NameError)
def vfcash():
    return render_template('vfcash.htm', name=NameError)
def atmoney():
    return render_template('atm.htm', name=NameError)


#prepadmin portal
def prepdashboard():
    online_users =  mongo.db.users.find_one_or_404({"online": True})
    return render_template("prepdashboard.html", user=user)

#schooladmin portal
def schdashboard():
    online_users =  mongo.db.users.find_one_or_404({"online": True})
    return render_template("schdashboard.html", user=user)


#for student portal
def students():
    online_users =  mongo.db.users.find_one_or_404({"online": True})
    return render_template("student.html", user=user)






if __name__== "__main__":
    app.run(debug=True)

