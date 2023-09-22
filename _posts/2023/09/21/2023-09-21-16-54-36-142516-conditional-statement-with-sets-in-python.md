---
layout: post
title: "Conditional statement with sets in Python"
description: " "
date: 2023-09-21
tags: [sets]
comments: true
share: true
---

In Python, conditional statements allow us to dictate the flow of our program based on certain conditions. We can use sets to represent collections of unique items, and perform conditional checks on these sets.

Consider a scenario where we have two sets: `set1` and `set2`. Let's explore how we can use conditional statements to compare these sets and perform different actions based on the comparison result.

```python
# Define sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Check if set1 is a subset of set2
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

# Check if set1 and set2 have any common elements
if set1.intersection(set2):
    print("set1 and set2 have common elements")
else:
    print("set1 and set2 have no common elements")

# Check if set1 and set2 have no common elements
if set1.isdisjoint(set2):
    print("set1 and set2 have no common elements")
else:
    print("set1 and set2 have common elements")
```

Output:
```
set1 is not a subset of set2
set1 and set2 have common elements
set1 and set2 have common elements
```

In the above example, we used the following conditional statements to compare the sets:

- The `issubset()` method checks if `set1` is a subset of `set2`.
- The `intersection()` method checks if `set1` and `set2` have any common elements.
- The `isdisjoint()` method checks if `set1` and `set2` have no common elements.

These conditionals help us make decisions based on the relationships between sets, and perform different actions accordingly.

By utilizing conditional statements with sets in Python, we can dynamically control the behavior of our program based on the contents of these sets, enhancing the flexibility and functionality of our code.

#python #sets