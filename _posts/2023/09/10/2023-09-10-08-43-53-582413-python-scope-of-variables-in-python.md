---
layout: post
title: "[Python] Scope of variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, the **scope** of a variable determines the region of the program where the variable can be accessed. There are three main levels of variable scope in Python:

1. **Local Scope**: Variables declared inside a function have local scope. They can only be accessed within the function.

2. **Global Scope**: Variables declared outside of any function, at the top-level of the program, have **global scope**. They can be accessed from anywhere in the program.

3. **Built-in Scope**: Python comes with a set of built-in functions and modules that have a predefined scope.

Let's explore each scope in detail.

### Local Scope

Variables defined inside a function are considered to have **local scope**. They are accessible only within that function. Once the function finishes running, the variables are destroyed.

Example:

```python
def my_function():
    x = 10
    print(x)  # Output: 10

my_function()
print(x)  # Error: NameError: name 'x' is not defined
```

### Global Scope

Variables declared outside of any function, at the top-level of the program, have **global scope**. They can be accessed from anywhere in the program, including inside functions.

Example:

```python
x = 10  # Global variable

def my_function():
    print(x)  # Output: 10

my_function()
print(x)  # Output: 10
```

In the example above, `x` is declared outside of any function and can be accessed both inside and outside of the `my_function()`.

### Built-in Scope

Python provides a set of built-in functions and modules that have a predefined **built-in scope**. These functions and modules are always available and can be used in any part of the program.

Example:

```python
import math

def calculate_square_root(number):
    return math.sqrt(number)

print(calculate_square_root(25))  # Output: 5.0
```

In this example, the `math` module is imported, giving access to the `sqrt()` function, which is part of the built-in scope.

### Shadowing Variables

When a variable with the same name is declared inside a nested scope, it **shadows** or overrides the variable with the same name in the outer scope. This means that the inner variable takes precedence over the outer one within the nested scope.

Example:

```python
x = 10

def my_function():
    x = 5
    print(x)  # Output: 5

my_function()
print(x)  # Output: 10
```

In this example, the variable `x` is shadowed in the `my_function()`, and the inner value of `x` is printed within the function. However, outside of the function, the global value of `x` is still accessible and remains unchanged.

Understanding the scope of variables in Python is essential when writing code to ensure proper variable access and prevent variable conflicts. By following the rules of variable scope, you can write clean and maintainable Python code.