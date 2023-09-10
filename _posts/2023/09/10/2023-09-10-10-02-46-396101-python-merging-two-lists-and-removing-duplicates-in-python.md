---
layout: post
title: "[Python] Merging two lists and removing duplicates in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Merging two lists and removing duplicates is a common task in Python. In this blog post, we will explore different methods to achieve this using Python.

Let's start by creating two lists that we want to merge and remove duplicates from:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
```

### Method 1: Using the `set` data type

One straightforward way to merge two lists and remove duplicates is by converting them into sets. Sets are unordered collections of unique elements. By merging the lists and converting them back to lists, we can remove any duplicate values.

```python
merged_list = list(set(list1 + list2))
print(merged_list)
```

### Method 2: Using the `+=` operator and `not in` condition

Another approach is to iterate over the second list and append its elements to the first list, but only if they are not already present in the first list. We can achieve this by using the `+=` operator to concatenate the lists and `not in` condition to check for duplicates.

```python
for item in list2:
    if item not in list1:
        list1.append(item)
print(list1)
```

### Method 3: Using list comprehension and `not in` condition

List comprehension is a concise way to create new lists based on existing ones. We can apply list comprehension to merge the lists and remove duplicates by using the `not in` condition.

```python
merged_list = list1 + [item for item in list2 if item not in list1]
print(merged_list)
```

### Method 4: Using the `extend()` method

The `extend()` method allows us to add multiple elements to a list. We can use it to extend the first list with the elements from the second list if they are not already present.

```python
for item in list2:
    if item not in list1:
        list1.extend([item])
print(list1)
```

These are a few ways to merge two lists and remove duplicates in Python. You can choose the method that suits your needs and preferences.

Remember that the ordering of the elements may differ depending on the method used since sets and lists have different behavior when it comes to preserving the order of elements.

I hope you found this blog post helpful in understanding various methods to merge lists and remove duplicates in Python!