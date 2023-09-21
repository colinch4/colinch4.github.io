---
layout: post
title: "Conditional statement with list comparison in Python"
description: " "
date: 2023-09-21
tags: [python, listcomparison]
comments: true
share: true
---

In Python, you can use conditional statements to compare lists and perform specific actions based on the comparison result. By comparing lists, you can check if they are equal, partially equal, or have specific elements. Let's dive into some examples!

## Checking if two lists are equal

To check if two lists are equal, you can use the equality (`==`) operator. This operator compares the elements of the two lists and returns `True` if all elements are the same, and `False` otherwise.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not equal")

# Output: Lists are equal
```

## Checking if lists have partially equal elements

If you want to check if two lists share some common elements, you can use the `in` operator in combination with a `for` loop. The `in` operator checks if a specific value is present in a list.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

for element in list1:
    if element in list2:
        print(f"{element} is present in both lists")

# Output: 4 is present in both lists
#         5 is present in both lists
```

## Checking if a list contains specific elements

To check if a list contains specific elements, you can use conditional statements in combination with the `all()` function. The `all()` function returns `True` if all elements in an iterable object evaluate to `True`, and `False` otherwise.

```python
my_list = [10, 20, 30, 40, 50]

# Check if the list contains 20 and 40
if all(element in my_list for element in [20, 40]):
    print("List contains both 20 and 40")
else:
    print("List does not contain both 20 and 40")

# Output: List contains both 20 and 40
```

## Summary

In Python, you can use conditional statements to compare lists and perform specific actions based on the comparison result. Whether you want to check if two lists are equal, have partially equal elements, or contain specific elements, Python offers multiple ways to achieve this. Understanding list comparison techniques can help you write more efficient and dynamic code. 

#python #listcomparison