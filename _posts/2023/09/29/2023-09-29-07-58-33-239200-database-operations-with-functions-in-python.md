---
layout: post
title: "Database operations with functions in Python"
description: " "
date: 2023-09-29
tags: []
comments: true
share: true
---

In this blog post, we will explore how to perform database operations using functions in Python. We will use the `sqlite3` module to interact with SQLite, a lightweight relational database management system. 

## Prerequisites

Before we begin, make sure you have SQLite and the `sqlite3` module installed. You can install the module by running the following command:

```bash
pip install sqlite3
```

## Connecting to the Database

To connect to a SQLite database, we need to create a connection object using the `connect()` function from the `sqlite3` module. We can specify the database file path as a parameter to the function. Here's an example:

```python
import sqlite3

def connect_to_database(database_file):
    connection = sqlite3.connect(database_file)
    return connection
```

## Executing Queries

Once connected to the database, we can execute SQL queries using the `execute()` function of the connection object. This function takes an SQL statement as a parameter. Here's an example of executing a simple query to create a table:

```python
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
```

## Querying Data

To retrieve data from the database, we can use the `fetchall()` method of the cursor object. This method returns all rows from the result set as a list of tuples. Here's an example of querying all rows from the `users` table:

```python
def get_all_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return rows
```

## Inserting Data

To insert data into the database, we can use the `execute()` method with an `INSERT` statement. We can use parameterized queries and pass the values as a tuple or a dictionary to prevent SQL injection attacks. Here's an example of inserting a user record:

```python
def insert_user(connection, name, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connection.commit()
```

## Updating Data

To update data in the database, we can use the `execute()` method with an `UPDATE` statement. We can use parameterized queries to specify the new values and the condition. Here's an example of updating a user's age:

```python
def update_user_age(connection, user_id, new_age):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    connection.commit()
```

## Deleting Data

To delete data from the database, we can use the `execute()` method with a `DELETE` statement. We typically specify the condition based on which the records should be deleted. Here's an example of deleting a user by their ID:

```python
def delete_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    connection.commit()
```

## Closing the Connection

After performing all the necessary database operations, it's important to close the connection to free up resources. Here's an example of a function that closes the connection:

```python
def close_connection(connection):
    connection.close()
```

## Conclusion

In this blog post, we explored how to perform database operations using functions in Python. We covered connecting to a database, executing queries, querying data, inserting data, updating data, deleting data, and closing the connection. By encapsulating these operations in functions, we can enhance the reusability and readability of our code.