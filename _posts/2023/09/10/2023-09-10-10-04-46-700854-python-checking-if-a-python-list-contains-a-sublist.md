---
layout: post
title: "[Python] Checking if a Python list contains a sublist"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Method 1: Using the `in` keyword

The simplest way to check if a Python list contains a sublist is by using the `in` keyword. This method is intuitive and readable.

```python
def sublist_exists(list1, list2):
    return list2 in list1
```

In the above example, `list1` represents the main list, and `list2` represents the sublist we want to search for. The `in` keyword checks if `list2` is present in `list1` and returns `True` or `False` accordingly.

Let's see an example:

```python
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4, 5]

print(sublist_exists(main_list, sub_list))   # Output: True
```

## Method 2: Using list slicing

Another approach is to use list slicing to compare sublists. In Python, we can use slicing to extract a portion of a list and then compare it with another list.

```python
def sublist_exists(list1, list2):
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i + len(list2)] == list2:
            return True
    return False
```

In the above code snippet, we iterate over `list1` using a loop and compare the sliced portion with `list2`. This approach checks if a sublist exists and returns `True` or `False` accordingly.

Here's an example:

```python
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4, 5]

print(sublist_exists(main_list, sub_list))   # Output: True
```

## Method 3: Using the `any` function with list comprehension

We can also utilize the `any` function along with list comprehension to check if a sublist exists in a list.

```python
def sublist_exists(list1, list2):
    return any(list1[i:i + len(list2)] == list2 for i in range(len(list1) - len(list2) + 1))
```

In the above code, we create a list of `True` or `False` values using a list comprehension. The `any` function checks if any of the elements in the list are `True` and returns the result accordingly.

Let's see it in action:

```python
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4, 5]

print(sublist_exists(main_list, sub_list))   # Output: True
```

In conclusion, we have explored three different methods to check if a Python list contains a sublist. Each approach has its advantages and may be suitable for different scenarios. It is important to choose the appropriate method based on the size of the list and the efficiency required for the task at hand.

By having these techniques in our arsenal, we can efficiently search and manipulate lists in Python.