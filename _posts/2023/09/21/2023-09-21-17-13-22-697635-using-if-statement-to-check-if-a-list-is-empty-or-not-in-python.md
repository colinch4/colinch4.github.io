---
layout: post
title: "Using if statement to check if a list is empty or not in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

To check if a list is empty, you can use the `len()` function to get the length of the list and compare it to zero. If the length is zero, it means the list is empty. Here's an example:

```python
my_list = []

if len(my_list) == 0:
    print("The list is empty")
else:
    print("The list is not empty")
```

In the above code, we create an empty list `my_list`. The `len(my_list)` returns the number of elements in the list. If the length is equal to zero, we print "The list is empty". Otherwise, we print "The list is not empty".

Another way to check if a list is empty is by using the `not` operator along with the list variable. This is possible because an empty list is considered as a "False" value in Python. Here's an alternative example:

```python
my_list = []

if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")
``` 

In this code, we use `not my_list` to check if the list is empty. If the list is empty, it will evaluate to `True` and we print "The list is empty". Otherwise, we print "The list is not empty".

Using `if` statements to check if a list is empty or not allows you to handle different scenarios based on the presence or absence of elements in the list.