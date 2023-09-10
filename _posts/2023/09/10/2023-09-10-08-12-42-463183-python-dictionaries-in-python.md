---
layout: post
title: "[Python] Dictionaries in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Dictionaries are a powerful data structure in Python that allow you to store and manipulate data in key-value pairs. They are sometimes referred to as associative arrays, hashes, or hash maps in other programming languages.

## Creating a Dictionary
To create a dictionary in Python, you can use curly braces `{}` or the built-in `dict()` function. Each key-value pair is separated by a colon `:` and multiple pairs are separated by commas.

```python
# Create an empty dictionary
empty_dict = {}

# Create a dictionary with some initial data
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

## Accessing Values
You can access the values in a dictionary by providing the corresponding key in square brackets `[]`.

```python
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 25
print(my_dict['city'])  # Output: New York
```

If a key doesn't exist in the dictionary, it will raise a `KeyError`. You can use the `get()` method to avoid this and return a default value instead.

```python
print(my_dict.get('country'))     # Output: None
print(my_dict.get('country', '')) # Output: '' (empty string)
```

## Updating and Adding Elements
To update the value of an existing key in a dictionary, you can simply assign a new value to it.

```python
my_dict['age'] = 30
print(my_dict['age'])  # Output: 30
```

To add a new key-value pair to a dictionary, you can use the same syntax.

```python
my_dict['occupation'] = 'Software Engineer'
print(my_dict['occupation'])  # Output: Software Engineer
```

## Removing Elements
You can remove an element from a dictionary using the `del` keyword followed by the key.

```python
del my_dict['age']
print(my_dict.get('age', ''))  # Output: '' (empty string)
```

## Iterating Over a Dictionary
You can iterate over the keys, values, or both using the `keys()`, `values()`, and `items()` methods, respectively.

```python
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
```

## Dictionary Methods
Dictionaries come with other useful methods for manipulating and inspecting the data. Some commonly used methods include:

- `clear()`: Removes all the items from the dictionary
- `copy()`: Returns a shallow copy of the dictionary
- `pop(key)`: Removes an item with the specified key and returns its value. Raises a `KeyError` if the key is not found.
- `update(dictionary)`: Updates the dictionary with the key-value pairs from another dictionary

These methods can be accessed using dot notation like `my_dict.clear()` or `my_dict.update()`, where `my_dict` is the name of your dictionary.

Dictionaries are an essential part of Python programming and are widely used due to their flexibility and efficiency. They provide a convenient way to store, access, and manipulate data in a structured manner.

Remember to use dictionaries when you have a set of related data that is best represented as key-value pairs.