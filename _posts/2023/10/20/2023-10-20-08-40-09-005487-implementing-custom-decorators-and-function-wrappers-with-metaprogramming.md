---
layout: post
title: "Implementing custom decorators and function wrappers with metaprogramming"
description: " "
date: 2023-10-20
tags: [decorators]
comments: true
share: true
---

Decorators and function wrappers are powerful tools in Python that allow you to modify the behavior of a function at runtime. With metaprogramming, you can go beyond the basic decorators provided by Python and create your own custom decorators. In this article, we will explore how to implement custom decorators and function wrappers using metaprogramming techniques.

## Table of Contents
- [What are Decorators?](#what-are-decorators)
- [Implementing Custom Decorators](#implementing-custom-decorators)
   - [Using Class-based Decorators](#using-class-based-decorators)
   - [Using Function-based Decorators](#using-function-based-decorators)
- [Function Wrappers with Metaprogramming](#function-wrappers-with-metaprogramming)
- [Conclusion](#conclusion)
- [References](#references)

## What are Decorators?

In Python, a decorator is a function or class that takes a function as input and returns a modified or enhanced version of that function. It allows you to wrap or decorate a function with additional functionality without modifying the original function's code. Decorators are commonly used for tasks such as logging, caching, authentication, and more.

## Implementing Custom Decorators

Python provides a built-in syntax `@` to apply decorators to functions. However, we can also create our own custom decorators using metaprogramming techniques. Let's explore two common approaches to implementing custom decorators: class-based decorators and function-based decorators.

### Using Class-based Decorators

A class-based decorator is a class that implements the `__call__` method. This method is called when the decorated function is called. Here's an example of a class-based decorator that logs the name and arguments of a function before it is executed:

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Calling function: {self.func.__name__}')
        print(f'Arguments: {args}, {kwargs}')
        return self.func(*args, **kwargs)

@Logger
def greet(name):
    print(f'Hello, {name}!')

greet('John')
```

Output:
```
Calling function: greet
Arguments: ('John',), {}
Hello, John!
```

In the above example, the `Logger` class is defined as a decorator, and the `greet` function is decorated with the `@Logger` syntax. When `greet` is called, the `__call__` method of the `Logger` class is invoked, which logs the function call details before executing the original function.

### Using Function-based Decorators

Function-based decorators are simpler to implement than class-based decorators. They are defined as regular functions that take a function as input and return a modified version of that function. Here's an example of a function-based decorator that adds a timer to a function:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time: {end_time - start_time} seconds')
        return result
    return wrapper

@timer
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
```

Output:
```
Execution time: 8.821487426757812e-06 seconds
120
```

In the above example, the `timer` function is defined as a decorator. It creates a wrapper function that measures the execution time of the decorated function. The `factorial` function is decorated with `@timer`, and when called, the wrapper function measures the execution time and executes the original function.

## Function Wrappers with Metaprogramming

In addition to decorators, metaprogramming allows you to create function wrappers that modify function behavior by wrapping the function in another function. This is achieved by manipulating function objects at runtime. Here's an example of creating a function wrapper using metaprogramming techniques:

```python
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f'Calling function: {func.__name__}')
        print(f'Arguments: {args}, {kwargs}')
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    print(f'Hello, {name}!')

greet = log_arguments(greet)
greet('John')
```

Output:
```
Calling function: greet
Arguments: ('John',), {}
Hello, John!
```

In the above example, the `log_arguments` function takes a function as input and returns a wrapper function that logs the function call details. The wrapper function is then assigned to the `greet` function, effectively modifying its behavior.

## Conclusion

Custom decorators and function wrappers are powerful tools in Python that allow you to modify the behavior of functions at runtime. By leveraging metaprogramming techniques, you can create your own custom decorators and function wrappers to add additional functionality and flexibility to your code.

In this article, we explored two common approaches to implementing custom decorators: class-based decorators and function-based decorators. We also discussed how function wrappers can be created using metaprogramming techniques. By using these techniques, you can enhance the capabilities of your functions and make your code more versatile.

## References

- [Python Decorators - Real Python](https://realpython.com/primer-on-python-decorators/)
- [Python Metaprogramming - Real Python](https://realpython.com/python-metaclasses/)
- [The Hitchhiker's Guide to Python - Decorators](https://docs.python-guide.org/writing/style/#decorators)