---
layout: post
title: "Function arguments in Python"
description: " "
date: 2023-09-29
tags: [Python, FunctionArguments]
comments: true
share: true
---

In Python, function arguments are values that are passed into a function when it is called. Arguments allow us to provide data to a function so that it can perform a specific task.

## Positional Arguments
Positional arguments are the most basic type of function arguments. They are passed into a function in the order they are defined.

```python
def greet(name, age):  # name and age are positional arguments
    print(f"Hello {name}, you are {age} years old!")

greet("John", 25)  # Call the greet() function with positional arguments
```
Output:
```
Hello John, you are 25 years old!
```

## Keyword Arguments
Keyword arguments are passed into a function with a keyword and a corresponding value. The order of the arguments does not matter when using keyword arguments.

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet(age=30, name="Alice")  # Call the greet() function with keyword arguments
```
Output:
```
Hello Alice, you are 30 years old!
```

## Default Arguments
Default arguments are defined with a default value. If a corresponding argument is not passed when calling the function, the default value is used.

```python
def greet(name, age=18):  # age has a default value of 18
    print(f"Hello {name}, you are {age} years old!")

greet("Sarah")  # Call the greet() function without passing age argument
```
Output:
```
Hello Sarah, you are 18 years old!
```

## Variable Length Arguments
Python provides two special symbols `*` (asterisk) and `**` (double asterisk) to indicate variable-length arguments.

### Variable-length Positional Arguments
A single asterisk `*` is used to pass a variable number of positional arguments into a function.

```python
def greet(*names):  # *names allows any number of positional arguments
    for name in names:
        print(f"Hello {name}!")

greet("John", "Alice", "Bob")  # Call the greet() function with multiple positional arguments
```
Output:
```
Hello John!
Hello Alice!
Hello Bob!
```

### Variable-length Keyword Arguments
A double asterisk `**` is used to pass a variable number of keyword arguments into a function.

```python
def greet(**person):  # **person allows any number of keyword arguments
    for key, value in person.items():
        print(f"{key}: {value}")

greet(name="John", age=25)  # Call the greet() function with multiple keyword arguments
```
Output:
```
name: John
age: 25
```

With these different types of function arguments, Python provides us with flexibility in how we pass data to functions and customize their behavior. Understanding these argument types is essential for writing clean and reusable code. #Python #FunctionArguments