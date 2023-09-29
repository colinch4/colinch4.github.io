---
layout: post
title: "User authentication and login in Flask"
description: " "
date: 2023-09-29
tags: [WebDevelopment, Flask]
comments: true
share: true
---

In any web application, user authentication and login is a critical component. In this blog post, we will explore how to implement user authentication and login functionality in a Flask application.

## Prerequisites
To follow along with this tutorial, you should have basic knowledge of Flask and Python. Additionally, make sure you have Flask installed on your system.

## Setting up the Flask Application
First, let's create a Flask application by following these steps:

1. Create a new directory for your project.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment by running the command `python3 -m venv venv`.
4. Activate the virtual environment using the appropriate command for your operating system.
5. Install Flask by running `pip install flask`.
6. Create a new file called `app.py` and open it in your preferred text editor.

## Creating a User Model
Next, let's create a user model to represent our users. This model will typically store user information such as the username, email, and hashed password.

```python
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```

In the above code, we define a User class that extends the `db.Model` class from SQLAlchemy. It has attributes for id, username, email, and password_hash. We also define methods to set and check the hashed password.

## Creating Routes for User Authentication
Now, let's create the routes for user authentication. We will need routes for user registration, login, and logout.

```python
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new user
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Find the user by username
        user = User.query.filter_by(username=username).first()
        
        # Check if the user exists and the password is correct
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect('/dashboard')
        
        return redirect('/login')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
```

In the above code, we define routes for user registration, login, and logout. On registration, we create a new user and save it to the database. On login, we find the user by the provided username and check the password. If the user exists and the password is correct, we store the user's id in the session and redirect them to the dashboard. On logout, we simply clear the session and redirect the user to the home page.

## Summary
In this blog post, we looked at how to implement user authentication and login functionality in a Flask application. We created a user model, defined routes for registration, login, and logout, and added the necessary database operations. By following this tutorial, you now have a solid foundation for implementing user authentication in your Flask applications.

#WebDevelopment #Flask