from flask import Flask, flash, url_for, redirect, render_template, request, session
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, SQLAlchemyAdapter, UserManager, UserMixin
#from flask import roles_required
from passlib.hash import sha256_crypt
import mysql.connector

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MYSQL_HOST'] = '35.187.117.190'
app.config['MYSQL_USER'] = 'auric'
app.config['MYSQL_PASSWORD'] = 'auric'
app.config['MYSQL_DB'] = 'preptime_db'

#mysql = MySQL(app)
mydb = mysql.connector.connect(
  host="35.187.117.190",
  user="auric",
  passwd="auric",
  database="preptime_db"
)

print(mydb)

#run home template
@app.route('/', methods=['GET', 'POST'])
#@roles_required('sch_Admin')
def index():
    if request.method == "POST":
        details = request.form
        print('Hello POST')
        name = details['name']
        email = details['email']
        password = details['psw']
        repeat_password = details['psw-repeat']
        #cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO preptime_users(email, password) VALUES (%c, %c)", (email, password, repeat_pasword))
        
        #cur.execute("INSERT INTO preptime_users(email, password) VALUES ('hello', 'home')")
        #mysql.connection.commit()
        #cur.close()
        mycursor = mydb.cursor()

        sql = "INSERT INTO preptime_users(name, email, password) VALUES (%c, %c, %c)"
        val = (name, email, password)
        mycursor.execute("INSERT INTO preptime_users(email, password) VALUES ('hello', 'home')")

        mydb.commit()
        return 'done'
    print('Hello GET')
    return render_template('index.html')

#prepadmin portal
#@roles_required('Admin')

#schooladmin portal
#@roles_required('sch_Admin')


#for student portal
#@roles_required('student')




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




if __name__== "__main__":
    app.run(debug=True)

