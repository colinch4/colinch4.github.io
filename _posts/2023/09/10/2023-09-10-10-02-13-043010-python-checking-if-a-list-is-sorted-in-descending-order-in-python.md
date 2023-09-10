---
layout: post
title: "[Python] Checking if a list is sorted in descending order in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Checking if a list is sorted in descending order in Python

def is_sorted_descending(lst):
    """
    Check if a given list is sorted in descending order.
    
    Parameters:
    lst (list): The input list.
    
    Returns:
    bool: True if the list is sorted in descending order, False otherwise.
    """
    return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    
# Test Cases
print(is_sorted_descending([5, 4, 3, 2, 1]))  # True
print(is_sorted_descending([1, 2, 3, 4, 5]))  # False
print(is_sorted_descending([5, 3, 1, 2, 4]))  # False
print(is_sorted_descending([100, 50, 25, 10]))  # True
print(is_sorted_descending([5]))  # True
print(is_sorted_descending([]))  # True

```
In the above code, we are implementing a function `is_sorted_descending` which takes a list as input and checks if the list is sorted in descending order. 

The function uses the `all` function with a generator expression to check if every adjacent element in the list satisfies the condition `lst[i] >= lst[i+1]`. This condition ensures that each element is greater than or equal to the next element, maintaining the descending order.

We have provided some test cases to demonstrate the functionality of the `is_sorted_descending` function. The test cases cover scenarios where the list is sorted in descending order (`[5, 4, 3, 2, 1]`, `[100, 50, 25, 10]`, `[5]`, `[]`) and where the list is not sorted in descending order (`[1, 2, 3, 4, 5]`, `[5, 3, 1, 2, 4]`).