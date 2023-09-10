---
layout: post
title: "[Python] Checking if two lists are equal in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can use the `==` operator to check if two lists are equal. However, this comparison only checks whether the two lists have the same elements in the same order.

If you want to check if two lists are equal regardless of their order, you can sort the lists and then compare them.

Here's an example that demonstrates both methods:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

# Using the `==` operator to check equality
if list1 == list2:
    print("The lists are equal (in the same order)")
else:
    print("The lists are not equal")

# Sorting the lists and comparing
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

if sorted_list1 == sorted_list2:
    print("The lists are equal (regardless of order)")
else:
    print("The lists are not equal")
```

In this example, both `list1` and `list2` have the same elements in the same order, so the output will be:

```
The lists are equal (in the same order)
The lists are equal (regardless of order)
```

If the lists had different elements, or if the order of the elements differed, the output would be:

```
The lists are not equal
```