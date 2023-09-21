---
layout: post
title: "Conditional statement with multiple identity operators in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

The identity operators in Python are `is` and `is not`. The `is` operator returns True if two variables refer to the same object, while the `is not` operator returns True if two variables refer to different objects.

Here's an example of a conditional statement with multiple identity operators in Python:

```python
x = 10
y = 20

if x is not None and y is not None:
    print("Both x and y have a valid value.")
else:
    print("At least one of x or y is None.")
```

In the above example, we are checking if both `x` and `y` are not None using the `is not` operator. If both variables have a valid value, the first block of code will be executed, printing "Both x and y have a valid value." Otherwise, if either `x` or `y` is None, the second block of code will be executed instead.

You can also use the `is` operator to check if two variables refer to the same object. For example:

```python
list1 = [1, 2, 3]
list2 = list1

if list1 is list2:
    print("list1 and list2 refer to the same object.")
```

In the above example, we are checking if `list1` is the same as `list2` using the `is` operator. Since both variables refer to the same list object, the conditional statement evaluates to True, and the corresponding message is printed.

Using multiple identity operators in your conditional statements allows you to check specific object identities and make decisions based on their relation to each other. Just remember to use the `is` operator to check if two variables refer to the same object, and the `is not` operator to check if they refer to different objects.