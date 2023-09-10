---
layout: post
title: "[Python] Decorators in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, *decorators* are a powerful feature that allow you to modify the behavior of functions or classes without changing their source code. They provide a clean and concise way to add additional functionality to existing code.

## What are Decorators?

In simple terms, decorators are functions that take another function as input and extend its behavior. They are defined using the `@` symbol followed by the decorator function name, placed above the function or class to be decorated.

## Creating a Decorator

To create a decorator, you define a function that takes a function as input, modifies it, and returns the modified function. Here's an example of a simple decorator that adds a greeting message before a function is called:

```python
def greeting_decorator(func):
    def wrapper():
        print("Hello, I'm a decorator!")
        func()
    return wrapper

@greeting_decorator
def greet():
    print("Hello, world!")

greet()
```

In the example above, the `greeting_decorator` function is defined with a nested function called `wrapper`. The `greet` function is decorated by placing `@greeting_decorator` above its definition. When `greet` is called, it actually calls the `wrapper` function, which first prints the greeting message and then calls the original `greet` function.

## Decorators with Arguments

Decorators can also take arguments to customize their behavior. In this case, we need an extra level of nesting to properly pass and accept arguments. Let's modify our previous example to accept a custom greeting message:

```python
def greeting_decorator(message):
    def decorator(func):
        def wrapper():
            print(message)
            func()
        return wrapper
    return decorator

@greeting_decorator("Welcome!")
def greet():
    print("Hello, world!")

greet()
```

Now, the `greeting_decorator` function takes a `message` argument and returns a decorator function. This decorator function then takes the `func` argument, and in the `wrapper` function, it uses the custom greeting message.

## Class Decorators

In addition to functions, decorators can also be used with classes. The process is similar, where the decorator function wraps around the class definition. Here's an example of a class decorator that adds a simple logging functionality:

```python
def logging_decorator(cls):
    class LoggerWrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.log("Object created")

        def log(self, message):
            print(f"Logging: {message}")

        def __getattr__(self, name):
            attr = super().__getattr__(name)
            if callable(attr):
                return lambda *args, **kwargs: (self.log(f"Calling {name}"), attr(*args, **kwargs))
            return attr

    return LoggerWrapper

@logging_decorator
class ExampleClass:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello, {self.name}!")

example = ExampleClass("Alice")
example.greeting()
```

In this case, the `logging_decorator` wraps around the class `ExampleClass`, creating a new class `LoggerWrapper` that extends and modifies its behavior. The logging functionality is added to the class by overriding the `__init__` method and adding a custom `log` method. In addition, the `__getattr__` method is overridden to log the method calls made on the class.

## Conclusion

Decorators are a powerful tool in Python that allow you to modify the behavior of functions and classes without altering their source code. They provide a flexible and elegant way to add or extend functionalities. By understanding decorators, you can write cleaner and more reusable code.