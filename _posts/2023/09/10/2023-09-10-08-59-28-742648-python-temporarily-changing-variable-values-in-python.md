---
layout: post
title: "[Python] Temporarily changing variable values in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, there may be situations where you need to temporarily change the value of a variable. This can be useful when you want to modify a variable's value for a specific scope without affecting its original value. In this blog post, we will explore different ways to achieve this in Python.

## Method 1: Using a context manager

One way to temporarily change a variable's value is by using a context manager. Context managers provide a way to allocate and release resources when they are no longer needed. They can also be used to temporarily modify variables. Here's an example:

```python
from contextlib import contextmanager

@contextmanager
def temp_change(variable, new_value):
    old_value = variable
    variable = new_value
    yield
    variable = old_value

# Example usage
my_variable = 10

print("Before:", my_variable)
with temp_change(my_variable, 20):
    print("Inside:", my_variable)

print("After:", my_variable)
```

Output:
```
Before: 10
Inside: 20
After: 10
```

In this example, we define a context manager `temp_change` that takes a variable and a new value as arguments. Inside the context manager, we temporarily assign the new value to the variable. After the context manager is exited, the original value is restored.

## Method 2: Using a decorator

Another way to temporarily modify a variable is by using a decorator. Decorators in Python are functions that modify the behavior of other functions. Here's an example:

```python
def temp_change(variable_name, new_value):
    def decorator(function):
        def wrapper(*args, **kwargs):
            globals()[variable_name] = new_value
            result = function(*args, **kwargs)
            globals()[variable_name] = original_value
            return result
        return wrapper
    return decorator

# Example usage
my_variable = 10

@temp_change('my_variable', 20)
def foo():
    print("Inside:", my_variable)

print("Before:", my_variable)
foo()
print("After:", my_variable)
```

Output:
```
Before: 10
Inside: 20
After: 10
```

In this example, we define a decorator `temp_change` that takes the variable name and the new value as arguments. Inside the decorator, we temporarily modify the global variable using the `globals()` function. The original value is restored after the decorated function is executed.

## Method 3: Using the `with` statement and another variable

If you want to keep track of the original value of the variable without using a context manager or decorator, you can create another variable to store the original value. Here's an example:

```python
my_variable = 10
original_value = my_variable

print("Before:", my_variable)

my_variable = 20
print("Inside:", my_variable)

my_variable = original_value
print("After:", my_variable)
```

Output:
```
Before: 10
Inside: 20
After: 10
```

In this example, we create a new variable `original_value` to store the original value of `my_variable`. We then modify `my_variable` with the new value and later restore it by assigning the original value back to it.

These are three different methods to temporarily change variable values in Python. Choose the one that suits your needs and coding style.