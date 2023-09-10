---
layout: post
title: "[Python] NoSQL databases in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In recent years, NoSQL databases have gained popularity due to their ability to handle large volumes of data and flexible schema. Python, being a versatile and powerful programming language, offers various libraries and frameworks to work with NoSQL databases. In this blog post, we will explore some of the popular NoSQL databases and how to use them in Python.

## MongoDB

MongoDB is one of the most widely used NoSQL databases that stores data in a flexible, document-like format called BSON (Binary JSON). With Python, you can interact with MongoDB using the `pymongo` library.

To get started with MongoDB in Python, you need to install the `pymongo` library using pip:

```python
pip install pymongo
```

Once installed, you can connect to a MongoDB instance and perform various operations using the following code:

```python
import pymongo

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["mydatabase"]

# Access a collection (similar to a table in SQL)
collection = db["mycollection"]

# Insert a document
document = {"name": "John", "age": 25}
collection.insert_one(document)

# Find documents
query = {"name": "John"}
result = collection.find(query)

for document in result:
    print(document)

# Update a document
query = {"name": "John"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)

# Delete a document
query = {"name": "John"}
collection.delete_one(query)
```

## Cassandra

Cassandra is a highly scalable and distributed NoSQL database known for its ability to handle massive amounts of data across multiple servers. To work with Cassandra in Python, you can use the `cassandra-driver` library.

To install the `cassandra-driver` library, use pip:

```python
pip install cassandra-driver
```

Here is an example of how to use Cassandra with Python:

```python
from cassandra.cluster import Cluster

# Connect to a Cassandra cluster
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create a keyspace
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS mykeyspace
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
""")

# Use the keyspace
session.set_keyspace('mykeyspace')

# Create a table
session.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id UUID PRIMARY KEY,
        name TEXT,
        age INT
    );
""")

# Insert data
id = uuid.uuid1()
session.execute("""
    INSERT INTO users (id, name, age)
    VALUES (%s, %s, %s);
""", (id, "John", 25))

# Query data
result = session.execute("SELECT * FROM users WHERE name = 'John'")
for row in result:
    print(row)

# Update data
session.execute("UPDATE users SET age = 26 WHERE name = 'John';")

# Delete data
session.execute("DELETE FROM users WHERE name = 'John';")
```

## Redis

Redis is an in-memory data structure store known for its simplicity, performance, and versatility. Python provides a library called `redis` that allows you to interact with Redis in Python.

To install the `redis` library, use pip:

```python
pip install redis
```

Here is an example of how to use Redis in Python:

```python
import redis

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('name', 'John')

# Get a value by key
name = r.get('name')
print(name)  # b'John'

# Increment a value
r.incr('counter')

# Delete a key
r.delete('name')
```

In conclusion, Python offers a wide range of options when it comes to working with NoSQL databases. From MongoDB to Cassandra and Redis, you can choose the database that best suits your needs and leverage Python's libraries to interact with them efficiently. Whether you're handling large volumes of data or need a fast and scalable solution, Python has got you covered.