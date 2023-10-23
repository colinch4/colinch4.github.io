---
layout: post
title: "Using decorators in Python Hug API"
description: " "
date: 2023-10-23
tags: []
comments: true
share: true
---

In Python, decorators are a powerful tool that allow you to modify the behavior of functions or classes without directly changing their code. They provide a way to "wrap" or modify the functionality of a function, providing additional features or functionality.

Python Hug is a modern and lightweight web framework that makes it easy to build APIs. It emphasizes simplicity and usability, while still providing powerful features. One of the key features of Python Hug is its support for decorators, which can be used to add functionality to your API endpoints.

## What are Decorators?

Decorators in Python are functions that take in another function as an argument and extend its behavior without modifying its source code. They are denoted by the `@` symbol followed by the decorator function.

Here's a simple example of a decorator in Python:

```python
def decorator_function(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator_function
def hello_world():
    print("Hello, World!")

hello_world()
```

In this example, the `decorator_function` is a decorator that wraps the `hello_world` function. It adds additional functionality by printing a message before and after the execution of the function.

## Using Decorators in Python Hug API

Python Hug provides built-in decorators that can be used to add functionality to your API endpoints. These decorators can be used to handle request methods, route parameters, input validation, and more.

Here's an example of using decorators in Python Hug API:

```python
import hug

@hug.get('/hello')
def hello_world():
    return {'message': 'Hello, World!'}

@hug.get('/greet/{name}')
def greet(name):
    return {'message': f'Hello, {name}!'}

@hug.post('/add')
def add_numbers(a: int, b: int):
    return {'result': a + b}
```

In this example, the `@hug.get` decorator is used to handle GET requests for the `/hello` and `/greet/{name}` endpoints. The `@hug.post` decorator is used to handle POST requests for the `/add` endpoint. These decorators make it easy to define the behavior of each endpoint in a concise and readable way.

## Conclusion

Decorators are a powerful feature in Python that can be used to extend the functionality of functions or classes. In Python Hug, decorators are used to add functionality to API endpoints, making it easy to define the behavior of each endpoint. By using decorators in Python Hug API, you can write clean and modular code, making it easier to develop and maintain your API.

#python #hug