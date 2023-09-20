---
layout: post
title: "Using MyPy annotations with Python decorators"
description: " "
date: 2023-09-20
tags: [python, decorators]
comments: true
share: true
---

Python decorators are a powerful feature that allow you to modify the behavior of functions or classes by wrapping them with another function. Decorators are commonly used in frameworks such as Flask and Django to modify the behavior of routes or views.

However, when using decorators, it can be challenging to preserve type annotations and ensure type safety. This is where MyPy comes in. MyPy is a static type checker for Python that can help catch type errors before your code is executed.

In this blog post, we will explore how to use MyPy annotations with Python decorators to enforce type checking and ensure that our code is free of type errors.

## Installing MyPy
First, you need to install MyPy. You can install it using pip:

````shell
pip install mypy
````

## Adding MyPy Annotations
To use MyPy annotations with your Python decorators, you need to add type hints to your code. Type hints allow MyPy to infer the types of variables, arguments, and return values.

Let's start with a simple example. Suppose we have a decorator called `validate_input` that verifies if a function's arguments satisfy certain conditions. We want to ensure that the function works with integers only.

``` python
from typing import Callable

def validate_input(func: Callable[..., int]) -> Callable[..., int]:
    def wrapper(*args: int, **kwargs: int) -> int:
        # Validate input here
        return func(*args, **kwargs)
    return wrapper

@validate_input
def add_numbers(a: int, b: int) -> int:
    return a + b
```

In the example above, we have added type hints `int` to the decorator's inner function `wrapper`, as well as the decorated function `add_numbers`. This allows MyPy to perform type checks on the arguments and return value of the decorated function.

## Running MyPy
Once we have added MyPy annotations to our code, we can run MyPy to perform static type checking. Open your terminal, navigate to your project directory, and run the following command:

````shell
mypy your_script.py
````

MyPy will analyze your code and output any type errors it encounters. In our example, if there are any type errors in `add_numbers` or `wrapper`, MyPy will report them.

## Conclusion
In this blog post, we learned how to use MyPy annotations with Python decorators to enforce type checking in our code. By adding type hints to our decorated functions and running MyPy, we can catch type errors early and improve the robustness of our code.

Using MyPy with decorators helps maintain code quality and readability, especially in larger projects. Start using MyPy in your Python codebase today to catch type errors and ensure your code is type-safe.

#python #decorators