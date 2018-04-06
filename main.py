from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    username_error = ''
    password_error = ''
    email_error = ''
    return render_template('index.html', username_error=username_error, password_error=password_error, email_error=email_error)

@app.route('/welcome', methods=['POST'])
def welcome():
    #username = request.form['username']
    return render_template('welcome.html')

@app.route('/', methods=['POST'])
def display_form():
    return render_template('index.html', username='', username_error='', password='', password_error='', email='', email_error='')

def validate_signin():
    username = render_template('index.html')
    password = render_template('index.html')
    email = render_template('index.html')

    if username=="":
        username_error="Username cannot be blank."
    elif " " in username:
        username_error="Username cannot contain a space."
    elif len(username) <3 or len(username) >20:
        username_error="Username must be 3-20 characters in length."

    if password=="":
        password_error="Password cannot be blank."
        password=""
    elif " " in password:
        password_error="Password cannot contain a space."
        password=""
    elif len(password) <3 or len(password) >20:
        password_error="Password must be 3-20 characters in length."
        password=""
    elif password != password_verify:
        password_error="Password must match password verification."

    if " " in email:
        email_error="Email cannot contain a space."
    elif len(email) <3 or len(email) >20:
        email_error="Email must be 3-20 characters in length."
    elif "@" not in email:
        email_error="Email not valid (must contain @)."
    elif "." not in email:
        email_error="Email not valid (must contain . [dot])."

    else:
        return "redirect('/welcome={username}'.format(username))"

app.run()
