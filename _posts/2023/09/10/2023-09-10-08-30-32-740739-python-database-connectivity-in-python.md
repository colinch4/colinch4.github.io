---
layout: post
title: "[Python] Database connectivity in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore how to establish database connectivity in Python. Python provides a variety of libraries and modules that allow us to interact with different databases efficiently. We will cover two popular options: **SQLite** and **MySQL**.

## SQLite Connectivity

SQLite is a lightweight and serverless database engine that is widely used for local storage. Python has built-in support for SQLite connectivity through the **sqlite3** module.

Here's an example of how to establish a connection with an SQLite database using Python:

```python
import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries
# Example: create a new table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
```

In the above code snippet, we import the `sqlite3` module and establish a connection with the SQLite database file `example.db`. We then create a cursor object to execute SQL queries. Finally, we execute an SQL query to create a new table named "users" if it does not already exist.

## MySQL Connectivity

MySQL is a popular open-source relational database management system that is widely used in web and application development. To establish connectivity with MySQL in Python, we can use the **mysql-connector-python** library.

To use **mysql-connector-python**, you need to install it first via pip:

```bash
pip install mysql-connector-python
```

Here's an example of how to establish a connection with a MySQL database using Python:

```python
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries
# Example: create a new table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
```

In the above code snippet, we import the `mysql.connector` module and establish a connection with the MySQL database using the provided host, username, password, and database name. We then create a cursor object to execute SQL queries. Finally, we execute an SQL query to create a new table named "users" if it does not already exist.

## Conclusion

In this blog post, we explored how to establish database connectivity in Python using two popular options: SQLite and MySQL. With the help of the `sqlite3` module, we can easily connect to and interact with SQLite databases. Additionally, the `mysql-connector-python` library provides a convenient way to establish connectivity with MySQL databases. By leveraging these tools, you can efficiently work with databases in your Python projects.