---
layout: post
title: "[Python] Common operations on Python lists"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Lists are one of the most versatile data types in Python. They allow you to store and manipulate a collection of elements. In this blog post, we will explore some common operations that you can perform on Python lists.

## Creating a List

To create a list in Python, simply enclose the elements within square brackets `[]`, separated by commas. Here's an example:

```python
fruits = ['apple', 'banana', 'orange', 'mango']
```

## Accessing Elements in a List

You can access individual elements in a list using indexing. The index starts from 0 for the first element. Here's how you can access elements from the `fruits` list:

```python
print(fruits[0])    # Output: 'apple'
print(fruits[2])    # Output: 'orange'
```

You can also use negative indexing to access elements from the end of the list. For example:

```python
print(fruits[-1])   # Output: 'mango'
print(fruits[-2])   # Output: 'orange'
```

## Modifying List Elements

Lists are mutable, which means you can modify their elements. You can assign a new value to a specific index in the list. Here's an example:

```python
fruits[1] = 'grape'
print(fruits)    # Output: ['apple', 'grape', 'orange', 'mango']
```

## Slicing a List

Python allows you to extract a portion of a list using slicing. Slicing creates a new list containing the selected elements. Here's how you can slice the `fruits` list:

```python
sliced_list = fruits[1:3]
print(sliced_list)    # Output: ['grape', 'orange']
```

Slicing notation includes the start index (inclusive) and the end index (exclusive). You can also omit the start or end index to slice from the beginning or up to the end of the list respectively.

## Adding Elements to a List

You can append new elements to the end of a list using the `append()` method:

```python
fruits.append('strawberry')
print(fruits)   # Output: ['apple', 'grape', 'orange', 'mango', 'strawberry']
```

You can also insert elements at a specific index using the `insert()` method:

```python
fruits.insert(2, 'kiwi')
print(fruits)   # Output: ['apple', 'grape', 'kiwi', 'orange', 'mango', 'strawberry']
```

## Removing Elements from a List

To remove an element from a list, you can use the `remove()` method. It removes the first occurrence of the specified value from the list:

```python
fruits.remove('orange')
print(fruits)   # Output: ['apple', 'grape', 'kiwi', 'mango', 'strawberry']
```

If you know the index of the element you want to remove, you can use the `del` keyword:

```python
del fruits[1]
print(fruits)   # Output: ['apple', 'kiwi', 'mango', 'strawberry']
```

## Conclusion

Python lists offer a wide range of functions and methods for performing common operations. In this blog post, we covered creating lists, accessing elements, modifying elements, slicing, adding elements, and removing elements. These operations are fundamental to working with lists in Python and will help you efficiently manipulate your data.