from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# db
db = yaml.safe_load(open('db.yaml'))
app.config[MYSQL_HOST] = db['mysql_host']
app.config[MYSQL_USER] = db['mysql_user']
app.config[MYSQL_PASSWORD] = db['mysql_password']
app.config[MYSQL_DB] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        indexnumber = userDetails['name']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, password) VALUES(%s, %c)", (name, passord))
        mysql.connection.commit()
        cur.close()
        return render_template('students.html', name=NameError)

    return render_template('index.html', name=NameError)

def visa():
    return render_template('visa.htm', name=NameError)


def question():
    return render_template()
if __name__== "__main__":
    app.run(debug=True)

