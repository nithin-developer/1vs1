from flask import Flask, render_template, request, redirect, session, send_file, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '1vs1-gaming'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sonabai2009@gmail.com'
app.config['MAIL_PASSWORD'] = 'pmtpzjnmszyuboxy'

mysql = MySQL(app)
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        enc_pass = password
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', (email, enc_pass))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            session['name'] = account['username']

            return redirect('/home')
        else:
            msg = 'Incorrect Email / password!'

    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phno = request.form['phno']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'INSERT INTO users (username, password, email, phone_number) VALUES (%s, %s, %s, %s)',
                (username, password, email, phno)
            )
            mysql.connection.commit()

            return redirect('/auth')

    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('login.html', msg=msg)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'name' in session and 'email' in session:
        name = session['name']
        email = session['email']
        islogin = session['loggedin']
        return render_template('index.html', name=name, email=email, islogin=islogin)
    else:
        return redirect('/auth')


@app.route('/auth/logout')
def logout():
    if 'email' in session:
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        session.pop('name', None)
        return redirect('/auth')
    else:
        return redirect('/auth')


if __name__ == '__main__':
    app.run(debug=True)
