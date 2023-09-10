---
layout: post
title: "[Python] Scope resolution in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, scope refers to the **visibility** and **accessibility** of variables, objects, and functions within a program. It determines where a certain entity can be referenced and used. Python follows a set of rules known as **LEGB** to search and define the scope of a variable.

LEGB stands for:
- **L**ocal
- **E**nclosing
- **G**lobal
- **B**uilt-in

Let's take a closer look at each scope level and how they affect variable resolution in Python.

## Local Scope (L)

Variables defined inside a function or a method have **local scope**. They are only accessible within the block where they are defined. Once the function or method ends execution, the local variables are destroyed and cannot be accessed anymore.

```python
def do_something():
    x = 10  # local variable
    print(x)

do_something()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined
```

## Enclosing Scope (E)

Enclosing scope, also known as **function scope**, refers to variables that are defined in a nested function, which encloses the current function. The enclosing function can access variables from the outer function but not vice versa.

```python
def outer_function():
    x = 10
    
    def inner_function():
        print(x)  # Access variable from the enclosing scope
    
    inner_function()

outer_function()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined
```

## Global Scope (G)

Variables defined at the **module level** have global scope. They are accessible throughout the entire module. Global variables can be accessed and modified from any function or method within the module. Moreover, they can also be accessed from other modules within the same program.

```python
x = 10  # global variable

def do_something():
    print(x)  # Access global variable

do_something()  # Output: 10
print(x)  # Output: 10
```

## Built-in Scope (B)

The built-in scope refers to the **built-in functions**, **keywords**, and **constants** provided by Python. These entities are available in every Python program without having to import any external modules.

```python
print("Hello, World!")  # Output: Hello, World!
```

## Local Variables vs Global Variables

When there is a variable with the same name in both the local and global scope, Python gives preference to the local variable.

```python
x = 10  # global variable

def do_something():
    x = 5  # local variable
    print(x)  # Access local variable

do_something()  # Output: 5
print(x)  # Output: 10
```

If you want to modify the value of a global variable inside a function, you can use the `global` keyword to **explicitly specify** that you want to use the global variable instead of creating a new local variable.

```python
x = 10  # global variable

def do_something():
    global x  # Access the global variable
    x = 5
    print(x)

do_something()  # Output: 5
print(x)  # Output: 5
```

Understanding scope resolution in Python is crucial for writing clean, efficient, and bug-free code. By following the LEGB rule, you can ensure that variables are used in the intended scope, minimizing confusion and potential errors.