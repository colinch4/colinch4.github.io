---
layout: post
title: "[Python] Nested lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

A nested list is a list that contains other lists as its elements. Each element can also be a nested list, creating a hierarchical structure. This allows you to represent multi-dimensional data or create more advanced data structures.

Creating a nested list is straightforward. You can simply include lists as elements of a master list:

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

In this example, `nested_list` is a list containing three sub-lists. Each sub-list represents a row of numbers. You can access individual elements within the nested list using indexing:

```python
print(nested_list[0])    # Output: [1, 2, 3]
print(nested_list[1][2]) # Output: 6
```

Here, `nested_list[0]` returns the first sub-list `[1, 2, 3]`, and `nested_list[1][2]` returns the value `6` from the second sub-list.

You can also modify elements within a nested list by assigning new values:

```python
nested_list[1][0] = 10
print(nested_list) # Output: [[1, 2, 3], [10, 5, 6], [7, 8, 9]]
```

In this example, the value at index `[1][0]` is changed to `10`, resulting in `[[1, 2, 3], [10, 5, 6], [7, 8, 9]]`.

Iterating over a nested list follows a similar approach to regular lists. You can use loops to access each element within the nested list:

```python
for lst in nested_list:
    for item in lst:
        print(item)
```

This will print all the elements of the nested list individually.

Nested lists provide a flexible and powerful way to work with complex data structures in Python. They allow you to represent and manipulate multi-dimensional data easily. Whether you are dealing with matrices, trees, or any other hierarchical data, nested lists can be a useful tool in your Python programming arsenal.