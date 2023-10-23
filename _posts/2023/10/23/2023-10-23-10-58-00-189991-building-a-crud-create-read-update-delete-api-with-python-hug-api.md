---
layout: post
title: "Building a CRUD (Create, Read, Update, Delete) API with Python Hug API"
description: " "
date: 2023-10-23
tags: []
comments: true
share: true
---

In this tutorial, we will learn how to build a CRUD (Create, Read, Update, Delete) API using the Python Hug API framework. Hug is a powerful and flexible framework that allows us to quickly and easily create and deploy APIs.

## Table of Contents
- [Introduction to Hug](#introduction-to-hug)
- [Setting Up the Project](#setting-up-the-project)
- [Creating the API Endpoints](#creating-the-api-endpoints)
- [Testing the API](#testing-the-api)
- [Conclusion](#conclusion)

## Introduction to Hug

Hug is a Python framework for building APIs that focuses on being simple, scalable, and fast. It is designed to be developer-friendly and requires minimal code to get started. Hug provides a set of decorators and functions that allow us to define API endpoints and handle HTTP requests and responses.

## Setting Up the Project

Before we start building the API, let's set up our project. We will assume that you have Python and pip installed on your system.

1. Create a new directory for your project and navigate to it in your terminal.
2. Create a virtual environment by running the following command:

```bash
python -m venv env
```
3. Activate the virtual environment:

For Windows:
```bash
.\env\Scripts\activate
```

For Linux/macOS:
```bash
source env/bin/activate
```

4. Install the required dependencies:

```bash
pip install hug
```

## Creating the API Endpoints

Now that we have our project set up, let's create the API endpoints. In this example, we will create endpoints for managing users.

First, let's create a `main.py` file and import the necessary modules:

```python
import hug

@hug.get('/users')
def get_users():
    # Logic to fetch all users
    pass

@hug.get('/users/{id}')
def get_user(id: int):
    # Logic to fetch a single user by ID
    pass

@hug.post('/users')
def create_user(name: str, email: str):
    # Logic to create a new user
    pass

@hug.put('/users/{id}')
def update_user(id: int, name: str, email: str):
    # Logic to update a user by ID
    pass

@hug.delete('/users/{id}')
def delete_user(id: int):
    # Logic to delete a user by ID
    pass
```

In the above code, we define five endpoints: `get_users`, `get_user`, `create_user`, `update_user`, and `delete_user`. Each endpoint is decorated with the appropriate HTTP method decorator (`@hug.get`, `@hug.post`, `@hug.put`, `@hug.delete`), and we define the required parameters for each endpoint.

## Testing the API

To test our API, we can run a local development server using the following command:

```bash
hug -f main.py
```

This will start the server, and we can now make requests to `http://localhost:8000` using a tool like cURL or a web browser.

For example, to fetch all users, we can make a GET request to `http://localhost:8000/users`. To create a new user, we can make a POST request to `http://localhost:8000/users` with the required parameters in the request body.

## Conclusion

In this tutorial, we learned how to build a CRUD API using the Python Hug API framework. We set up our project, created the API endpoints, and tested the API using a local development server. Hug provides a simple and convenient way to build APIs in Python, and its developer-friendly design makes it a great choice for rapid API development.

For more information, you can refer to the [Hug documentation](https://www.hug.rest/).

Make sure to check out the code repository on [GitHub](https://github.com/your-username/your-repo).

Happy coding! #python #api