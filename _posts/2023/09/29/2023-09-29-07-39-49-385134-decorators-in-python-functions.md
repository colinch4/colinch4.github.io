---
layout: post
title: "Decorators in Python functions"
description: " "
date: 2023-09-29
tags: [Decorators]
comments: true
share: true
---

Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes without directly changing their source code. They provide a way to wrap or decorate a function, adding additional functionality before or after it executes, or even modifying its behavior altogether.

## How Decorators Work

Decorators are implemented as functions themselves, which take the function they are decorating as an argument and return a modified or wrapped version of that function. They are defined using the `@` symbol, followed by the name of the decorator function.

## Examples of Decorators

Let's look at a few examples to understand how decorators work in Python.

### Example 1: Timing Execution

```python
import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")
    return wrapper

@timer_decorator
def my_function():
    # Code to be timed
    time.sleep(1)

my_function()
```

In this example, we create a decorator `timer_decorator` that measures the execution time of a function. We use the `time` module to calculate the time difference between the start and end of the function execution. The wrapped function, `wrapper()`, is responsible for timing the execution and displaying the result.

### Example 2: Logging

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@log_decorator
def my_function(message):
    print(f"Function called with message: {message}")

my_function("Hello, decorators!")
```

In this example, we create a decorator `log_decorator` that logs the function call and completion. The `wrapper()` function not only calls the decorated function but also adds logging before and after execution. It accepts any arguments and keyword arguments and passes them to the decorated function.

## Conclusion

Decorators in Python provide a powerful way to enhance the functionality of functions or classes without modifying their source code. They allow you to add additional behavior, such as timing, logging, caching, or authentication, to your functions or classes. Understanding and mastering decorators can greatly improve the versatility and maintainability of your Python code.

#Python #Decorators