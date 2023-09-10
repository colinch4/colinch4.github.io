---
layout: post
title: "[Python] Checking if a list is sorted in ascending order in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you might come across situations where you need to check if a list is sorted in ascending order. Whether you're dealing with numerical or string values, Python provides an easy way to determine whether a list is sorted or not.

## Using the `sorted()` function

One approach to checking if a list is sorted in ascending order is by using the `sorted()` function. The `sorted()` function takes a list and returns a new sorted list. By comparing this new sorted list with the original list, we can determine if the list is sorted in ascending order.

Here's an example:

```python
def is_sorted_ascending(lst):
    # Create a sorted version of the list
    sorted_lst = sorted(lst)
    
    # Compare the original list with the sorted list
    if lst == sorted_lst:
        return True
    else:
        return False

# Example usage
numbers = [1, 2, 3, 4, 5]
is_sorted = is_sorted_ascending(numbers)
print(is_sorted)  # Output: True
```

In this example, we define a function `is_sorted_ascending()` that takes a list as input. Inside the function, we create a sorted version of the list using the `sorted()` function. We then compare the original list with the sorted list using the equality operator (`==`) and return `True` if they are the same, indicating that the list is sorted in ascending order.

## Implementing a manual check

If you prefer not to use the `sorted()` function, you can also implement a manual check to verify if a list is sorted in ascending order. This approach involves iterating over each element in the list and comparing it with the next element in the sequence.

Here's an example:

```python
def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage
numbers = [1, 2, 3, 4, 5]
is_sorted = is_sorted_ascending(numbers)
print(is_sorted)  # Output: True
```

In this example, we define a function `is_sorted_ascending()` that takes a list as input. We use a `for` loop to iterate over each element in the list up to the second-to-last element. Inside the loop, we compare the current element with the next element. If we find an element that is greater than the next element, we return `False`, indicating that the list is not sorted in ascending order. If the loop completes without finding any out-of-order elements, we return `True`.

Both the `sorted()` function and the manual check approach give us the same result, indicating whether a list is sorted in ascending order or not. Choose the approach that suits your needs and coding style.

That's it! With these methods, you'll be able to easily check if a list is sorted in ascending order in Python.