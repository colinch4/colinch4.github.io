---
layout: post
title: "[Python] Dictionary variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a **dictionary** is a built-in data structure that allows you to store data as key-value pairs. It is an unordered collection of elements where each element is indexed by a unique key. Dictionaries are a powerful tool in Python and can be used in various scenarios to store, retrieve, and manipulate data efficiently.

## Creating a dictionary

To create a dictionary variable in Python, you can use curly braces `{}` or the `dict()` constructor. Here's an example:

```python
# Using curly braces
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Using dict() constructor
my_dict = dict(name='John', age=25, city='New York')
```

In the above examples, we have created a dictionary `my_dict` with three key-value pairs: `'name': 'John'`, `'age': 25`, and `'city': 'New York'`.

## Accessing values in a dictionary

To access the values in a dictionary, you can use the key as an index. Here's an example:

```python
# Accessing values
print(my_dict['name'])  # Output: John

# Getting all keys
keys = my_dict.keys()
print(keys)  # Output: ['name', 'age', 'city']

# Getting all values
values = my_dict.values()
print(values)  # Output: ['John', 25, 'New York']
```

In the above code, we accessed the value associated with the key `'name'` using `my_dict['name']`. We also retrieved all keys and values using the `keys()` and `values()` methods, respectively.

## Modifying a dictionary

To modify the value associated with a key in a dictionary, you can assign a new value to that key. Here's an example:

```python
# Modifying value
my_dict['age'] = 30
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

In the above code, we modified the value associated with the key `'age'` to 30.

## Adding and removing items from a dictionary

To add a new item to a dictionary or remove an existing item, you can use the `update()` method or the `del` keyword, respectively. Here's an example:

```python
# Adding a new item
my_dict['occupation'] = 'Developer'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Developer'}

# Removing an item
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'occupation': 'Developer'}
```

In the above code, we added a new item `'occupation': 'Developer'` to the dictionary using the `update()` method. We also removed the item with the key `'city'` using the `del` keyword.

## Conclusion

Python dictionaries are a versatile data structure that allows you to store and manipulate data as key-value pairs. They are incredibly useful when working with complex data and can significantly simplify your code. Understanding how to create, access, modify, and manipulate dictionaries is crucial for any Python programmer.