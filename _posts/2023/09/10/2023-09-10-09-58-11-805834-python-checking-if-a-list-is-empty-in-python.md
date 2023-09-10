---
layout: post
title: "[Python] Checking if a list is empty in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

When working with lists in Python, it is often necessary to check if a list is empty before performing any further operations. A common scenario where this check might be required is when processing user input or handling data retrieved from a database.

## Using the `len()` function

One way to check if a list is empty in Python is by using the `len()` function. The `len()` function returns the number of elements in a list. If the length of the list is `0`, it means the list is empty.

```python
my_list = []

if len(my_list) == 0:
    print("The list is empty.")
else:
    print("The list contains elements.")
```

In the code above, we first create an empty list called `my_list`. Then, we use an `if` statement to check if the length of `my_list` is `0`. If it is, we print a message indicating that the list is empty. Otherwise, we print a message indicating that the list contains elements.

## Using the `not` operator

Another way to check if a list is empty is by using the `not` operator. This approach leverages the concept of truthiness and falsiness in Python. In Python, an empty list is considered falsy, meaning it evaluates to `False` in a boolean context. Therefore, we can use the `not` operator to negate the truthiness of the list.

```python
my_list = []

if not my_list:
    print("The list is empty.")
else:
    print("The list contains elements.")
```

In the code above, we create an empty list called `my_list`. Then, we use an `if` statement along with the `not` operator to check if `my_list` is falsy. If it is, we print a message indicating that the list is empty. Otherwise, we print a message indicating that the list contains elements.

Both of these approaches will yield the same result - determining whether a list is empty or not. Choose the one that suits your coding style and preferences. Remember that it is always a good practice to check if a list is empty before performing any operations on it to avoid unforeseen errors.

Hope you found this tutorial helpful for checking if a list is empty in Python!