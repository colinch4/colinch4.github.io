---
layout: post
title: "Working with databases using functions in Python"
description: " "
date: 2023-09-29
tags: [python, databases]
comments: true
share: true
---

In modern applications, databases play a critical role in storing and managing data. Python provides various libraries and modules to interact with databases and perform operations such as CRUD (Create, Read, Update, Delete). 

In this blog post, we will explore how to work with databases using functions in Python, focusing on the popular library `sqlite3`.

## Installing sqlite3

Before we start, ensure that you have `sqlite3` installed. If not, you can install it using the following command:

```shell
pip install pysqlite3
```

## Connecting to the Database

To connect to a database using `sqlite3`, we need to first import the module and establish a connection. Here's an example:

```python
import sqlite3

def connect_to_database():
    conn = sqlite3.connect("example.db")
    print("Connected to the database successfully.")
    return conn

```

In the above code, we import the `sqlite3` library and define a function `connect_to_database()` which establishes a connection to a database file named `example.db`. The `connect()` function returns a connection object that we can use to interact with the database.

## Creating a Table

Once we have connected to the database, we can create tables to store our data. Here's an example of creating a table in a database:

```python
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")
    conn.commit()
    print("Table created successfully.")

```

In the above code, we define a function `create_table()` that takes a connection object as a parameter. Inside the function, we use the `cursor()` method to create a cursor object, which allows us to execute SQL queries. We use the `execute()` method to execute the SQL statement to create a table named `users` with columns `id`, `name`, and `email`. We then commit the changes to the database using the `commit()` method.

## Inserting Data

To insert data into the table, we can define a function like this:

```python
def insert_data(conn, name, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("Data inserted successfully.")

```

In the above code, we define a function `insert_data()` that takes the connection object, `name`, and `email` as parameters. Inside the function, we use the `execute()` method to insert data into the `users` table. We use placeholders (`?`) to prevent SQL injection, and the values are passed as a tuple.

## Fetching Data

To retrieve data from the table, we can create a function like this:

```python
def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

```

In the above code, we define a function `fetch_data()` that takes the connection object as a parameter. Inside the function, we use the `execute()` method to execute the `SELECT` statement to fetch all rows from the `users` table. We then use the `fetchall()` method to retrieve all rows and iterate over them to print the data.

## Closing the Connection

Finally, when we are done working with the database, we need to close the connection. Here's an example of closing the connection:

```python
def close_connection(conn):
    conn.close()
    print("Connection closed.")

```

In the above code, we define a function `close_connection()` that takes the connection object as a parameter. We use the `close()` method to close the connection, preventing any further interaction with the database.

## Conclusion

Working with databases in Python using functions can help make your code more modular and reusable. In this blog post, we explored connecting to a database, creating tables, inserting and retrieving data, and closing the connection.

By leveraging the power of Python and libraries like `sqlite3`, you can efficiently work with databases and build robust applications that can store and manipulate data effectively.

Happy coding! 😊

#python #databases