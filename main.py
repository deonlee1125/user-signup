from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_signin():
    username = request.form["username"]
    password = request.form['password']
    password_verify= request.form['password_verify']
    email = request.form['email']
    username_error=""
    password_error=""
    email_error=""

    if username=="":
        username_error="Username cannot be blank."
    elif " " in username:
        username_error="Username cannot contain a space."
    elif len(username) <3 or len(username) >20:
        username_error="Username must be 3-20 characters long."

    if password=="":
        password_error="Password cannot be blank."
    elif " " in password:
        password_error="Password cannot contain a space."
    elif len(password) <3 or len(password) >20:
        password_error="Password must be 3-20 characters in length."
    elif password != password_verify:
        password_error="Password must match password verification."

    if email != "":
        if " " in email:
            email_error="Email cannot contain a space."
        elif len(email) <3 or len(email) >20:
            email_error="Email must be 3-20 characters in length."
        elif "@" not in email:
            email_error="Email not valid (must contain @)."
        elif "." not in email:
            email_error="Email not valid (must contain . [dot])."
    
    if not username_error and not password_error and not email_error:
       return render_template('welcome.html', username=username)
     
    else:
       return render_template('index.html', username_error=username_error, password_error=password_error, email_error=email_error )

app.run()