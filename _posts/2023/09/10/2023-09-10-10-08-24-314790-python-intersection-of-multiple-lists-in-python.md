---
layout: post
title: "[Python] Intersection of multiple lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Here are a few approaches to accomplish this task:

### Using the `set` data structure

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

intersection = set(list1).intersection(list2, list3)
print(intersection)  # Output: {5}
```

In this approach, we first convert each list to a set using the `set()` function. Then, we can use the `intersection()` method to find the common elements among the sets. Finally, we print the resulting set, which contains the intersection of the lists.

### Using the `&` operator

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

intersection = set(list1) & set(list2) & set(list3)
print(intersection)  # Output: {5}
```

Similar to the previous approach, we convert each list to a set. Then, we use the `&` operator to find the intersection of the sets. The resulting set contains the common elements among all the lists.

### Using list comprehension

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

intersection = [value for value in list1 if value in list2 and value in list3]
print(intersection)  # Output: [5]
```

In this approach, we iterate through each element of `list1` using list comprehension. We check whether the current element is present in both `list2` and `list3`. If it is, we add it to the `intersection` list. Finally, we print the `intersection` list, which contains the common elements.

These are just a few approaches to find the intersection of multiple lists in Python. Depending on your specific requirements and the size of the lists, one approach may be more efficient than the others.