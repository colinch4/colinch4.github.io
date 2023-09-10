---
layout: post
title: "[Python] Data types in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, data types define the kind of values that can be stored and manipulated within a program. Python provides a number of built-in data types, each with its own characteristics and uses. In this blog post, we will explore some commonly used data types in Python.

## 1. Numeric Types

Python supports several numeric types, including integers, floats, and complex numbers.

### Integers

Integers are whole numbers, both positive and negative, without any decimal point. They are represented by the `int` data type in Python. For example:

```python
num = 42
print(type(num))  # Output: <class 'int'>
```

### Floats

Floats or floating-point numbers are numbers with a decimal point. They are represented by the `float` data type in Python. For example:

```python
num = 3.14
print(type(num))  # Output: <class 'float'>
```

### Complex Numbers

Complex numbers consist of a real part and an imaginary part. They are represented by the `complex` data type in Python. For example:

```python
num = 2 + 3j
print(type(num))  # Output: <class 'complex'>
```

## 2. Strings

Strings are sequences of characters enclosed within single quotes `'` or double quotes `"`. They are represented by the `str` data type in Python. For example:

```python
name = "Python"
print(type(name))  # Output: <class 'str'>
```

Python provides a wide range of operations and methods to manipulate strings, such as concatenation, slicing, and formatting.

## 3. Booleans

Booleans represent the truth values `True` and `False`. They are often used in logical expressions and control flow statements. Booleans are represented by the `bool` data type in Python. For example:

```python
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
```

## 4. Lists

Lists are ordered collections of items that can be of different data types. They are represented by the `list` data type in Python. Lists are mutable, meaning their elements can be modified. For example:

```python
fruits = ["apple", "banana", "orange"]
print(type(fruits))  # Output: <class 'list'>
```

Python provides various list operations and methods to add, remove, access, and manipulate list elements.

## 5. Tuples

Tuples are similar to lists but are immutable, meaning their elements cannot be modified once defined. They are represented by the `tuple` data type in Python. For example:

```python
person = ("John", 25, "New York")
print(type(person))  # Output: <class 'tuple'>
```

Tuples are often used when you want to store a collection of related but unchangeable values.

## 6. Dictionaries

Dictionaries are key-value pairs, where each value is associated with a unique key. They are represented by the `dict` data type in Python. For example:

```python
person = {"name": "John", "age": 25, "city": "New York"}
print(type(person))  # Output: <class 'dict'>
```

Dictionaries allow you to access and manipulate values based on their keys, making them useful for storing and retrieving data in a structured manner.

These are just a few of the many data types available in Python. Understanding the different data types and how to use them effectively is essential for writing efficient and robust Python programs.

In future blog posts, we will delve deeper into each data type, explore advanced data structures, and learn how to work with them effectively. Stay tuned for more Python goodies!