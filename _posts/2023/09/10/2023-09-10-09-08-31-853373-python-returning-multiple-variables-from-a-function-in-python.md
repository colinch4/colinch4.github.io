---
layout: post
title: "[Python] Returning multiple variables from a function in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Returning multiple variables from a function in Python

In Python, a function can return multiple values using various methods. Let's explore some of these methods.

## Method 1: Using a Tuple

A tuple is an ordered sequence of values that can be accessed using indexing. To return multiple values from a function, you can create a tuple and assign the values to it.

Here's an example:

```python
def get_user_info():
    name = "John"
    age = 25
    location = "New York"
    return name, age, location

user_info = get_user_info()
print(user_info)
```

Output:
```
('John', 25, 'New York')
```

In this example, the `get_user_info()` function returns a tuple containing three values: the name, age, and location. We then assign the returned tuple to the `user_info` variable and print its value.

## Method 2: Using a List

Similar to a tuple, a list can also be used to return multiple values from a function. Instead of using parentheses to create a tuple, you can use square brackets to create a list.

Here's an example:

```python
def get_user_info():
    name = "John"
    age = 25
    location = "New York"
    return [name, age, location]

user_info = get_user_info()
print(user_info)
```

Output:
```
['John', 25, 'New York']
```

In this example, the `get_user_info()` function returns a list containing three values: the name, age, and location. We assign the returned list to the `user_info` variable and print its value.

## Method 3: Using a Dictionary

A dictionary is a collection of key-value pairs. You can use a dictionary to return multiple values from a function by assigning each value to a specific key.

Here's an example:

```python
def get_user_info():
    user_info = {
        "name": "John",
        "age": 25,
        "location": "New York"
    }
    return user_info

user_info = get_user_info()
print(user_info)
```

Output:
```
{'name': 'John', 'age': 25, 'location': 'New York'}
```

In this example, the `get_user_info()` function returns a dictionary containing the name, age, and location as key-value pairs. We assign the returned dictionary to the `user_info` variable and print its value.

These are three common methods to return multiple variables from a function in Python. Depending on your use case, you can choose the method that best suits your needs and coding style.

Remember, when using tuples or lists to return multiple values, you can access each individual value using indexing. When using dictionaries, you can access each value using its corresponding key.