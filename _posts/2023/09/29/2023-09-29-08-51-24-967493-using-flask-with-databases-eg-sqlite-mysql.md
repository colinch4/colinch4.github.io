---
layout: post
title: "Using Flask with databases (e.g., SQLite, MySQL)"
description: " "
date: 2023-09-29
tags: [Flask, Databases]
comments: true
share: true
---

Flask is a popular Python web framework that allows you to build web applications quickly and easily. One of the essential components of many web applications is a database for storing and retrieving data. Flask seamlessly integrates with various databases, such as SQLite and MySQL, making it a powerful choice for building database-driven web applications.

## SQLite

SQLite is a lightweight, serverless database engine that is widely used for small-scale applications and prototyping. Flask provides a simple interface to work with SQLite databases using the built-in SQLite library.

To use SQLite with Flask, you need to import the `sqlite3` module and establish a connection to the database. Here's an example of connecting to an SQLite database and executing a query:

```python
import sqlite3
from flask import Flask, g

app = Flask(__name__)
app.config['DATABASE'] = 'path_to_database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM table_name')
    result = cursor.fetchall()
    return str(result)

if __name__ == '__main__':
    app.run()
```

In this example, we define a Flask application and configure the path to the SQLite database file. The `get_db` function establishes a connection to the database, and the `close_db` function ensures the connection is closed after each request.

## MySQL

MySQL is a robust and widely-used relational database management system. Flask provides an extension called Flask-MySQL to work with MySQL databases seamlessly.

To use Flask-MySQL, you first need to install the extension using `pip`. Here's an example of using Flask-MySQL with Flask:

```python
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM table_name")
    result = cur.fetchall()
    return str(result)

if __name__ == '__main__':
    app.run()
```

In this example, we import the `MySQL` class from the `flask_mysqldb` module and create an instance of it by passing in the Flask application object. We configure the MySQL connection details, such as the host, username, password, and database name.

We then define a route in Flask and execute a SELECT query on the MySQL database using the `cur` cursor object. The query result is returned as a string.

These examples demonstrate how Flask can be used with SQLite and MySQL databases. Depending on your application's requirements, you can choose the appropriate database engine and configure Flask accordingly. Flask's flexibility and extensive ecosystem make it an excellent choice for developing database-driven web applications.

[#Flask #Databases]