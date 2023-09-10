---
layout: post
title: "[Python] Data types of Python variables"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, variables are dynamically typed, which means that you don't have to explicitly declare the data type of a variable. The data type is automatically inferred based on the value assigned to it.

Python supports multiple built-in data types that you can use to store different kinds of values. Here, we will explore some of the most commonly used data types in Python.

## Numeric data types

Python provides different numeric data types to handle numerical values. The main numeric data types in Python are:

1. **Integer (int):** Integers are whole numbers without any fractional part. They can be positive, negative, or zero.
   
    ```python
    age = 25
    price = -9
    quantity = 0
    ```

2. **Floating-point (float):** Floating-point numbers represent real numbers with decimal points. They can be positive, negative, or zero.
   
    ```python
    height = 1.75
    temperature = -3.5
    pi = 3.14159
    ```

## Text data types

Textual data in Python is represented using strings. Strings are sequences of characters enclosed within single quotes (' ') or double quotes (" ").

```python
name = 'John Doe'
address = "123 Main Street"
message = "It's a beautiful day!"
```

## Boolean data type

Boolean data type is used to represent truth values. It can have two possible values: True and False. It is commonly used in conditional statements and logic operations.

```python
is_raining = True
is_sunny = False
```

## Collection data types

Python provides various collection data types to store multiple values. Some commonly used collection data types in Python are:

1. **List:** A list is an ordered collection of values enclosed within square brackets ([]). It can store values of different data types, and the elements can be accessed by their index.

    ```python
    numbers = [1, 2, 3, 4, 5]
    fruits = ['apple', 'banana', 'orange']
    ```

2. **Tuple:** A tuple is similar to a list, but it is immutable, meaning its elements cannot be modified once it is created. It is enclosed within round brackets (()).
   
    ```python
    coordinates = (55.756, 37.617)
    rgb_color = (255, 0, 0)
    ```

3. **Dictionary:** A dictionary is an unordered collection of key-value pairs enclosed within curly braces ({}). Each value is accessed using its corresponding key.

    ```python
    person = {'name': 'John', 'age': 30, 'city': 'New York'}
    student = {'id': 12345, 'name': 'Alice', 'grade': 'A'}
    ```

These are just a few examples of the data types available in Python. Understanding the different data types is essential for effective programming in Python.