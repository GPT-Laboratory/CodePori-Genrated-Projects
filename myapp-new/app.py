from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import re
import os
app = Flask(__name__)

app.secret_key = 'thisismysecretkey'
app.config["SESSION_PERMANENT"] = False

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg= ""
    user_check = False
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        
        if username != "" and password != "":
            myfile = open("user_info.txt", "r")
            user_list = myfile.readlines()
            myfile.close()
            
            uname = ""
            upass = ""
            
            for uinfo in user_list:
                uname = uinfo.split("-")[0]
                upass = uinfo.split("-")[1].strip("\n")
                
                if username == uname and password == upass: # if condition is valid then continue
                    user_check = True
                    session['loggedin'] = True
                    # session['username'] = uname
                    continue
            
            if user_check:
                return redirect(url_for('index'))
            else:
                msg = 'Incorrect E-mail / Password!'
        else:
            msg = "Email / Password Missing!"

    return render_template('login.html', msg = msg)


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ""
    user_exist = False
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        
        if username != "" and password != "":
            
            myfile = open("user_info.txt", "r")
            user_list = myfile.readlines()
            myfile.close()

            for uinfo in user_list:
                uname = uinfo.split("-")[0]
                if uname == username:
                    user_exist = True
                    continue
            if user_exist:
                msg = "User Already Exist!"
            else: # user does not exist .. so create new user.
                uinfo_temp = username +"-"+ password
                myfile = open("user_info.txt", "a") # append mode
                myfile.write(f'\n{uinfo_temp}')
                myfile.close()
                msg = "User Registerd Sucessfully."
        else:
            msg = "Email / Password Missing!"
    
    return render_template('register.html', msg = msg)


@app.route('/index', methods = ['POST', 'GET'])
def index():
    
    if session['loggedin'] == None:
        return redirect(url_for('login'))
    
    return render_template('index.html', **locals())

@app.route("/logout", methods = ["GET"])
def logout():
    
    # on logout set session to None and redirect to login page
    session['loggedin'] = None
    
    return redirect(url_for('login'))

if __name__ == '__main__':  
    app.run()