from flask import Flask, flash, url_for, redirect, render_template, request, session
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# db


mysql = MySQL(app)

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

