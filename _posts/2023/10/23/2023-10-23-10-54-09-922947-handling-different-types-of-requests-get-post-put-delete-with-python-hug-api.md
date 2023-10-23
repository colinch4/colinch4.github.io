---
layout: post
title: "Handling different types of requests (GET, POST, PUT, DELETE) with Python Hug API"
description: " "
date: 2023-10-23
tags: [HugAPI]
comments: true
share: true
---

In this blog post, we will explore how to handle different types of HTTP requests (GET, POST, PUT, DELETE) using Python Hug API. Python Hug is a lightweight framework that makes it easy to build APIs.

## Table of Contents
- [Introduction](#introduction)
- [Setting up the Environment](#setting-up-the-environment)
- [Handling GET Requests](#handling-get-requests)
- [Handling POST Requests](#handling-post-requests)
- [Handling PUT Requests](#handling-put-requests)
- [Handling DELETE Requests](#handling-delete-requests)
- [Conclusion](#conclusion)

## Introduction
Python Hug is a great choice for building APIs due to its simplicity and efficiency. It provides decorators for different HTTP methods, allowing us to handle different types of requests easily.

## Setting up the Environment
Before getting started, make sure you have Python and Hug installed on your system. You can install Hug by using pip:

```python
pip install hug
```

## Handling GET Requests
To handle GET requests, we can use the `@hug.get` decorator. Here's an example:

```python
import hug

@hug.get('/hello')
def say_hello():
    return {'message': 'Hello, World!'}
```

In the above example, we define a function `say_hello()` and decorate it with `@hug.get('/hello')`. This decorator tells Hug to map this function to the `/hello` endpoint for GET requests.

## Handling POST Requests
To handle POST requests, we can use the `@hug.post` decorator. Here's an example:

```python
import hug

@hug.post('/users')
def create_user(name):
    # Logic to create a new user
    return {'message': f'User {name} created successfully!'}
```

In this example, we use the `create_user()` function decorated with `@hug.post('/users')` to handle POST requests sent to the `/users` endpoint. The `name` parameter is received from the request body.

## Handling PUT Requests
To handle PUT requests, we can use the `@hug.put` decorator. Here's an example:

```python
import hug

@hug.put('/users/{id}')
def update_user(id, name):
    # Logic to update user with given ID
    return {'message': f'User {id} updated successfully!'}
```

In this example, we define the `update_user()` function and decorate it with `@hug.put('/users/{id}')`. The `{id}` parameter in the URL path is received as an argument, along with the `name` parameter from the request body.

## Handling DELETE Requests
To handle DELETE requests, we can use the `@hug.delete` decorator. Here's an example:

```python
import hug

@hug.delete('/users/{id}')
def delete_user(id):
    # Logic to delete user with given ID
    return {'message': f'User {id} deleted successfully!'}
```

In this example, we define the `delete_user()` function and decorate it with `@hug.delete('/users/{id}')`. The `{id}` parameter in the URL path is received as an argument.

## Conclusion
With Python Hug API, handling different types of requests becomes straightforward. By utilizing the appropriate decorators, we can easily define functions to handle GET, POST, PUT, and DELETE requests. This flexibility makes Python Hug a powerful tool for building APIs efficiently.

# References
- [Python Hug Documentation](https://www.hug.rest/)
- [Python Hug GitHub Repository](https://github.com/timothycrosley/hug)

#hashtags: #Python #HugAPI