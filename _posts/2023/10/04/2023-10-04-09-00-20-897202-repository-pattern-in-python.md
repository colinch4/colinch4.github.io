---
layout: post
title: "Repository pattern in Python"
description: " "
date: 2023-10-04
tags: [repository, concrete]
comments: true
share: true
---

The Repository pattern is a design pattern that helps to abstract the data access layer in an application. It provides a set of interfaces or classes that define the CRUD operations (Create, Read, Update, Delete) for working with a specific data model. By using the Repository pattern, we can separate the business logic from the details of how the data is stored and accessed.

In this blog post, we will explore how to implement the Repository pattern in Python. We will start by defining the interfaces for our repository, and then we will create concrete implementations for working with a specific data storage mechanism.

## Table of Contents
- [Repository Interfaces](#repository-interfaces)
- [Concrete Repository Implementation](#concrete-repository-implementation)
- [Usage Example](#usage-example)
- [Conclusion](#conclusion)

## Repository Interfaces

The first step in implementing the Repository pattern is to define the interfaces that will be used for interacting with the data model. Each entity or data model should have its own interface that specifies the methods for CRUD operations.

Here is an example of a `Repository` interface for a `User` entity:

```python
# user_repository.py

from abc import ABC, abstractmethod
from typing import List
from models import User

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass
```

In this example, we define a `UserRepository` interface that provides methods for getting a user by ID, creating a user, updating a user, deleting a user, and getting a list of all users.

## Concrete Repository Implementation

Once we have defined the repository interfaces, we can create concrete implementations for working with a specific data storage mechanism. Let's say we want to implement a `UserRepository` that uses a SQLite database as the data storage.

Here's an example of a `SQLiteUserRepository` implementation:

```python
# sqlite_user_repository.py

import sqlite3
from typing import List
from models import User
from repositories.user_repository import UserRepository

class SQLiteUserRepository(UserRepository):
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def get_user(self, user_id: int) -> User:
        query = "SELECT id, name, age FROM users WHERE id = ?"
        result = self.cursor.execute(query, (user_id,))
        row = result.fetchone()
        if row is None:
            return None
        return User(row[0], row[1], row[2])

    def create_user(self, user: User) -> User:
        query = "INSERT INTO users (name, age) VALUES (?, ?)"
        self.cursor.execute(query, (user.name, user.age))
        self.connection.commit()
        return user

    def update_user(self, user: User) -> User:
        query = "UPDATE users SET name = ?, age = ? WHERE id = ?"
        self.cursor.execute(query, (user.name, user.age, user.id))
        self.connection.commit()
        return user

    def delete_user(self, user_id: int) -> None:
        query = "DELETE FROM users WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()

    def get_all_users(self) -> List[User]:
        query = "SELECT id, name, age FROM users"
        result = self.cursor.execute(query)
        rows = result.fetchall()
        users = []
        for row in rows:
            users.append(User(row[0], row[1], row[2]))
        return users
```

In this example, we create a `SQLiteUserRepository` class that extends the `UserRepository` interface. We initialize a SQLite database connection and create a table for storing the users if it doesn't already exist. Each method in the repository implementation corresponds to a CRUD operation.

## Usage Example

To use the `SQLiteUserRepository`, we can create an instance of the repository and call its methods to interact with the users:

```python
from models import User
from repositories.sqlite_user_repository import SQLiteUserRepository

repository = SQLiteUserRepository("users.db")

user1 = User(1, "John Doe", 25)
repository.create_user(user1)

user2 = User(2, "Jane Smith", 30)
repository.create_user(user2)

updated_user = User(1, "John Doe", 26)
repository.update_user(updated_user)

user = repository.get_user(1)
print(user)  # Output: User(id=1, name='John Doe', age=26)

users = repository.get_all_users()
print(users)  # Output: [User(id=1, name='John Doe', age=26), User(id=2, name='Jane Smith', age=30)]

repository.delete_user(1)
```

In this example, we create a `SQLiteUserRepository` instance with the name of the SQLite database file. We then create and manipulate user objects using the repository methods.

## Conclusion

The Repository pattern is a powerful design pattern for decoupling the data access layer from the business logic of an application. By defining repository interfaces and providing concrete implementations, we can easily switch between different data storage mechanisms without affecting the rest of the codebase.

In this blog post, we explored how to implement the Repository pattern in Python using an example repository for working with user data. You can use this pattern as a starting point for structuring the data access layer in your own Python applications.

**#python #repositorypattern**

I hope you found this blog post helpful in understanding the Repository pattern in Python. If you have any questions or feedback, please let me know in the comments below.