---
layout: post
title: "[Python] Variable mutation in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, variables are mutable, which means their value can be changed after they have been assigned. This flexibility allows us to modify and update variables throughout our code. In this blog post, we will explore the concept of variable mutation in Python and see how it works.

## Understanding Variable Mutation

Variable mutation involves modifying the value of a variable after it has been assigned. Unlike **immutable** objects, such as strings or tuples, where a new object is created when a modification is made, **mutable** objects like lists or dictionaries can be modified directly without creating a new object.

Let's dive into some examples to understand how variable mutation works in Python.

## Lists - Mutable Objects

Lists are one of the most commonly used mutable objects in Python. We can easily modify the elements of a list.

```python
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]

# Modifying the first element
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Appending new element
my_list.append(4)
print(my_list)  # Output: [10, 2, 3, 4]

# Extending the list
my_list.extend([5, 6])
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
```

As you can see from the examples above, we can easily modify the list by assigning new values to its elements, appending new elements, or extending it with other lists.

## Dictionaries - Mutable Objects

Dictionaries are another common data structure in Python that allow for variable mutation. We can modify existing key-value pairs or add new ones.

```python
my_dict = {'name': 'John', 'age': 25}
print(my_dict)  # Output: {'name': 'John', 'age': 25}

# Modifying the value of an existing key
my_dict['age'] = 30
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# Adding a new key-value pair
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

In the code snippet above, we can see how the values of the dictionary can be easily modified by assigning new values to existing keys or by adding new key-value pairs.

## Variables and References

It is important to understand the concept of **references** when working with variable mutation. In Python, variables are references to objects stored in memory. When we mutate a variable, we are actually modifying the value of the referenced object, not the variable itself.

```python
a = [1, 2, 3]
b = a  # b now references the same list as a
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3]

# Modifying the list through variable b
b.append(4)
print(a)  # Output: [1, 2, 3, 4]
print(b)  # Output: [1, 2, 3, 4]
```

In the example above, both variables `a` and `b` reference the same list object. When we modify the list through variable `b`, the change is reflected in the value of variable `a` as well.

## Conclusion

Variable mutation is a powerful concept in Python that allows us to modify the value of variables, especially with mutable objects like lists and dictionaries. Understanding how references work helps us grasp the behavior of variable mutation and utilize it effectively in our programs.

By being aware of the mutability of variables, we can write more flexible and concise Python code.