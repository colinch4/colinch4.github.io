---
layout: post
title: "[Python] Checking for Duplicates in Tuples"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Checking for Duplicates in Tuples

Tuples are an immutable collection of elements in Python. Each element in a tuple can be of different data types such as integers, strings, or even other tuples. Sometimes, it becomes necessary to check if there are any duplicates present in a tuple.

Here's a simple Python function that can be used to check for duplicates in a tuple:

```python
def check_for_duplicates(tuple):
    """
    Function to check for duplicates in a tuple
    """

    # Create an empty set to store unique elements
    unique_elements = set()

    # Iterate through the tuple
    for element in tuple:
        # If the element is already present in the set, it is a duplicate
        if element in unique_elements:
            return True
        # Otherwise, add the element to the set
        else:
            unique_elements.add(element)

    # If no duplicates are found, return False
    return False
```

Let's test the function with some examples:

```python
# Test case 1: Tuple with no duplicates
tuple1 = (1, 2, 3, 4, 5)
print(check_for_duplicates(tuple1))  # Output: False

# Test case 2: Tuple with duplicates
tuple2 = (1, 2, 3, 2, 4, 5)
print(check_for_duplicates(tuple2))  # Output: True
```

In the first test case, the tuple `(1, 2, 3, 4, 5)` does not contain any duplicates, so the output is `False`. In the second test case, the tuple `(1, 2, 3, 2, 4, 5)` contains the duplicate element `2`, so the output is `True`.

By using this function, you can easily check for duplicates in a tuple and take appropriate actions based on the results.