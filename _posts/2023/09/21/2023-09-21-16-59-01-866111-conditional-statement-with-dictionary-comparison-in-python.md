---
layout: post
title: "Conditional statement with dictionary comparison in Python"
description: " "
date: 2023-09-21
tags: [dictionaries]
comments: true
share: true
---

In Python, dictionaries are a useful data structure for storing key-value pairs. They allow efficient lookup and retrieval of values based on a unique key. In this blog post, we will explore how to use conditional statements to compare dictionaries in Python.

To compare two dictionaries, we need to check if they have the same keys and if the corresponding values for each key are equal. Here's an example of a conditional statement that compares two dictionaries:

```python
# Example dictionaries
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict2 = {'name': 'John', 'age': 30, 'city': 'Chicago'}

# Compare dictionaries
if dict1 == dict2:
    print("The dictionaries are equal")
else:
    print("The dictionaries are not equal")
```

In this example, we have two dictionaries `dict1` and `dict2` with the same keys and values, except for the value associated with the key 'city'. The output of the conditional statement is "The dictionaries are not equal" because the values for the key 'city' are different.

We can also use the `!=` operator to check if two dictionaries are not equal. Here's an example:

```python
# Example dictionaries
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict2 = {'name': 'John', 'age': 30, 'city': 'Chicago'}

# Compare dictionaries
if dict1 != dict2:
    print("The dictionaries are not equal")
else:
    print("The dictionaries are equal")
```

In this case, the output of the conditional statement is "The dictionaries are not equal" because the values for the key 'city' are different.

It's important to note that the ordering of the keys in the dictionaries does not matter for comparison. As long as the keys and their corresponding values are the same, the dictionaries are considered equal.

In conclusion, comparing dictionaries in Python is straightforward using conditional statements. By checking if two dictionaries have the same keys and the values for each key are equal, we can determine if they are equal or not.

#python #dictionaries