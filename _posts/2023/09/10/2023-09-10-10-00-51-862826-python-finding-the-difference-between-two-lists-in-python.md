---
layout: post
title: "[Python] Finding the difference between two lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
## Finding the difference between two lists in Python ##

In Python, finding the difference between two lists is a common task that may arise in various scenarios. One such scenario is when comparing two datasets or sets of values to identify the elements that are present in one list but not in the other.

There are several approaches to solve this problem, each with its own advantages and use cases. Here, we will discuss three common methods to find the difference between two lists in Python.

1. Using list comprehension:
   ```python
   list1 = [1, 2, 3, 4, 5]
   list2 = [3, 4, 5, 6, 7]
   
   difference = [x for x in list1 if x not in list2]
   print(difference)  # Output: [1, 2]
   ```
   In this method, we iterate over each element in `list1` and check if it exists in `list2`. If it does not, we add it to the `difference` list using a list comprehension.

2. Using the set() function:
   ```python
   list1 = [1, 2, 3, 4, 5]
   list2 = [3, 4, 5, 6, 7]
   
   difference = list(set(list1) - set(list2))
   print(difference)  # Output: [1, 2]
   ```
   In this method, we convert both lists into sets using the `set()` function. Then, we use the set difference operator `-` to find the elements that are in `list1` but not in `list2`. Finally, we convert the resulting set back into a list.

3. Using the difference() method of set objects:
   ```python
   list1 = [1, 2, 3, 4, 5]
   list2 = [3, 4, 5, 6, 7]
   
   set1 = set(list1)
   set2 = set(list2)
   
   difference = list(set1.difference(set2))
   print(difference)  # Output: [1, 2]
   ```
   In this method, we convert both lists into sets, similar to the previous method. Then, we use the `difference()` method of set objects to find the elements that are in `set1` but not in `set2`. Finally, we convert the resulting set back into a list.

Each of these methods has its own advantages depending on the size of the lists and the specific requirements of your task. You can choose the method that best suits your needs.