from flask import Flask, flash, url_for, redirect, render_template, request, session
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'preptime_admin, preptime_students, preptime_school'

mysql = MySQL(app)


#run home termplate
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        email = details['email']
        password = details['pswd']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO preptime_school(email, password) VALUES (%c, %c)", (email, password))
        mysql.connection.commit()
        cur.close()
        return render_template("schdashboard.html", name=NameError)
    return render_template('index.html')

    

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
    if request.method == "POST":
        details = request.form
        
    return render_template("index.html", user=user)

#schooladmin portal
def schdashboard():
    
    return render_template("schdashboard.html", user=user)


#for student portal
def students():
    
    return render_template("student.html", user=user)






if __name__== "__main__":
    app.run(debug=True)

