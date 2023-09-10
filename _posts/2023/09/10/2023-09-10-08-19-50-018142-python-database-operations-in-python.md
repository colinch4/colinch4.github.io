---
layout: post
title: "[Python] Database operations in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Python is a versatile programming language that is widely used for various applications, including database operations. In this blog post, we will explore how to perform database operations using Python.

## Connecting to a Database

To interact with a database using Python, we first need to establish a connection. Python provides several libraries to connect to different types of databases such as **MySQL**, **PostgreSQL**, **SQLite**, and more. In this example, we will use the `sqlite3` library to connect to an SQLite database.

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')
```

## Creating a Table

Once the connection is established, we can create a table in the database. A table consists of columns, each representing a specific type of data. We use the SQL `CREATE TABLE` statement to define the structure of the table.

```python
# Create a table
conn.execute('''CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                salary REAL
                )''')
```

## Inserting Data

To insert data into a table, we use the SQL `INSERT` statement. We can execute the statement with the `execute()` method of the connection object.

```python
# Insert data into the table
conn.execute("INSERT INTO employees (name, age, salary) VALUES ('John Doe', 30, 5000.00)")
```

## Retrieving Data

To retrieve data from a table, we use the SQL `SELECT` statement. The `fetchall()` method of the cursor object allows us to retrieve all the records.

```python
# Retrieve data from the table
cursor = conn.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

## Updating Data

To update data in a table, we use the SQL `UPDATE` statement. We can modify the desired records based on certain conditions.

```python
# Update data in the table
conn.execute("UPDATE employees SET salary = 5500.00 WHERE id = 1")
```

## Deleting Data

To delete data from a table, we use the SQL `DELETE` statement. We can remove the records based on specific conditions.

```python
# Delete data from the table
conn.execute("DELETE FROM employees WHERE id = 1")
```

## Closing the Connection

After performing the necessary database operations, it is important to close the connection to free up resources.

```python
# Close the connection
conn.close()
```

In this blog post, we looked at how to perform database operations in Python. We covered connecting to a database, creating tables, inserting, retrieving, updating, and deleting data. Python provides easy-to-use libraries for interacting with different databases, making it a powerful tool for handling database tasks.

With Python's simplicity and flexibility, you can create robust applications that interact with databases efficiently and effortlessly. It's worth exploring the various database libraries available in Python to enhance your database operations.