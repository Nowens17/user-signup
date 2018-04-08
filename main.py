from flask import Flask, request, redirect, render_template
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

#TODO: Tasks to finish:
#Email verification
#Preserve user input in the username and e-mail fields
#Develop the Welcome HTML page

@app.route("/welcome")
def welcome_form():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)

@app.route("/", methods=['POST'])
def check_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    errors = False
    username_message = ""   
    password_message = ""
    verify_message = ""
    email_message = ""   

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_message = "Please enter a valid username."
        errors = True     
    
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_message = "Please enter a valid password."
        errors = True

    
    if password != verify or ' ' in verify:
        verify_message = "Passwords do not match"
        errors = True

    if len(email) > 0:
        if email.count('@') != 1 or email.count('.') != 1:
            email_message = "Please enter a valid email."
            errors = True
        if len(email) < 3 or len(email) > 20:
            email_message = "Please enter a valid email."
            errors = True

    if errors == True:
        return render_template("signup_form.html", username = username, username_message = username_message, password_message = password_message, verify_message = verify_message, email_message = email_message, email = email)
    else:
        return redirect('/welcome?username={0}'.format(username))

    

@app.route('/')
def index():
    return render_template('signup_form.html')


app.run()