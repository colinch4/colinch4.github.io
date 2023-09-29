---
layout: post
title: "Creating a crowdfunding platform with Flask"
description: " "
date: 2023-09-29
tags: [flask, crowdfunding]
comments: true
share: true
---

Crowdfunding has become an increasingly popular way to raise funds for projects, businesses, and social causes. In this tutorial, we will leverage Flask, a web framework written in Python, to create a basic crowdfunding platform.

## Setting Up the Project

To begin, make sure you have Python and Flask installed on your machine. You can install Flask using pip:

```python
pip install flask
```

Once Flask is installed, create a new Flask project by running the following commands:

```bash
mkdir crowdfunding-platform
cd crowdfunding-platform
```

Next, create a virtual environment to manage project dependencies:

```bash
python -m venv env
```

Activate the virtual environment:

```bash
source env/bin/activate  # for Linux/macOS
env\Scripts\activate  # for Windows
```

## Creating the Flask Application

Create a new file called `app.py` and open it in a text editor. Begin by importing Flask and initializing the Flask application:

```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
```

## Setting Up the Database

We will use SQLite as our database for simplicity. Flask provides an extension called Flask-SQLAlchemy, which simplifies the interaction with databases. Install Flask-SQLAlchemy using pip:

```bash
pip install flask-sqlalchemy
```

In `app.py`, import `SQLAlchemy` and configure the database connection:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crowdfunding.db'
db = SQLAlchemy(app)
```

Next, define the database models, such as `User`, `Project`, and `Contribution`, by creating new classes:

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('projects', lazy=True))

    def __repr__(self):
        return f'<Project {self.title}>'

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('contributions', lazy=True))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('contributions', lazy=True))
```

Run the following command in the terminal to create the database:

```bash
python app.py
```

## Building the User Interface

For simplicity, we will focus on building a basic user interface using HTML templates. Create a new directory called `templates` and within it, create `index.html`:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Crowdfunding Platform</title>
    </head>
    <body>
        <h1>Welcome to the Crowdfunding Platform</h1>
    </body>
</html>
```

In `app.py`, render the `index.html` template by modifying the root route:

```python
@app.route('/')
def index():
    return render_template('index.html')
```

## Conclusion

In this tutorial, we have set up a basic Flask application for a crowdfunding platform. We created a SQLite database and defined the necessary models. Additionally, we built a basic user interface using HTML templates. This is just a starting point, and you can further enhance the platform by adding features like user authentication, project creation, and contribution functionality.

#flask #crowdfunding