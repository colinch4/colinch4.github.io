---
layout: post
title: "Building a food delivery platform with Flask"
description: " "
date: 2023-09-29
tags: []
comments: true
share: true
---

In today's fast-paced world, the demand for food delivery platforms has skyrocketed. Many businesses are leveraging technology to streamline the food ordering and delivery process. In this blog post, we will explore how to build a food delivery platform using Flask, a popular Python web framework.

## Getting Started with Flask

To start building our food delivery platform, we need to set up a Flask project. First, we need to install Flask using pip:

```bash
$ pip install flask
```

Next, let's create a new Flask application by creating a new Python file, `app.py`, and import Flask:

```python
from flask import Flask

app = Flask(__name__)
```

## Database Setup

One crucial aspect of a food delivery platform is managing data, such as users, restaurants, menus, and orders. We can use a relational database to store this information. For this example, we will use SQLite, but you can use any database of your choice.

To get started, we need to install SQLAlchemy, a Python library for working with databases:

```bash
$ pip install SQLAlchemy
```

Let's create a `models.py` file where we define our database models. Here's an example of a `User` model:

```python
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"
```

Make sure to also update your `app.py` to include the database configuration:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_delivery.db'
db.init_app(app)
```

## User Registration and Login

Next, we need to implement user registration and login functionality. We can create routes for these actions using Flask's routing system.

```python
from flask import request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # User authenticated, redirect to dashboard
            return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html')
```

## Building the Dashboard

Once users are registered and logged in, they should be redirected to their respective dashboard. Here, they can view restaurants, menus, place orders, and manage their profile. We can create a dashboard route and implement the necessary logic.

```python
@app.route('/dashboard')
def dashboard():
    # Fetch user details and display dashboard
    return render_template('dashboard.html')
```

## Conclusion

In this blog post, we explored how to build a food delivery platform using Flask. We covered setting up the Flask project, database configuration using SQLAlchemy, user registration and login functionality, and building the dashboard.

By following this guide, you should have a solid foundation to start developing a food delivery platform. Feel free to extend the functionality and add more features to suit your specific needs. Happy coding!