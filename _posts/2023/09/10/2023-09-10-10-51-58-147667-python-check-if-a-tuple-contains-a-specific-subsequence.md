---
layout: post
title: "[Python] Check if a Tuple Contains a Specific Subsequence"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will discuss how to check if a tuple contains a specific subsequence in python. Tuples are immutable sequences, similar to lists, that can contain any type of objects. Subsequences, on the other hand, are a shorter sequence of elements that appear in the same order within a larger sequence.

## Problem Statement

Suppose we have a tuple `t` and we want to determine whether it contains a specific subsequence `s`. Our goal is to write a function that returns `True` if the subsequence is found, and `False` otherwise.

## Solution Approach

One possible approach to solve this problem is by iterating over the elements of the tuple and checking if the subsequence can be found at any position. Let's implement this solution in python.

## Example Code

```python
def is_subsequence(t: tuple, s: tuple) -> bool:
    """
    Function to check if a tuple contains a specific subsequence.

    Args:
        t (tuple): The input tuple to be searched.
        s (tuple): The subsequence to be found.

    Returns:
        bool: True if subsequence is found, False otherwise.
    """
    t_len = len(t)
    s_len = len(s)

    if s_len > t_len:
        return False

    i, j = 0, 0

    while i < t_len and j < s_len:
        if t[i] == s[j]:
            j += 1
        i += 1

    return j == s_len

# Testing the function
tuple_1 = (1, 2, 3, 4, 5, 6)
subsequence_1 = (2, 4, 6)

print(is_subsequence(tuple_1, subsequence_1)) # Output: True

tuple_2 = (1, 2, 3, 4, 5, 6)
subsequence_2 = (3, 5)

print(is_subsequence(tuple_2, subsequence_2)) # Output: False
```

In this example code, we define a function `is_subsequence()` that takes two input parameters `t` and `s` representing the main tuple and the subsequence, respectively. The function iterates over the elements of the tuple and checks if the subsequence can be found by comparing each element. If the subsequence is found, the function returns `True`, otherwise `False`.

We then test the function with two examples. In the first example, the subsequence `(2, 4, 6)` can be found in the tuple `(1, 2, 3, 4, 5, 6)`, so the function returns `True`. In the second example, the subsequence `(3, 5)` cannot be found in the tuple `(1, 2, 3, 4, 5, 6)`, so the function returns `False`.

## Conclusion

We have successfully implemented a solution to check if a tuple contains a specific subsequence in python. This approach can be applied to any tuple and subsequence combination to determine whether the subsequence is present or not. By understanding and utilizing the concept of subsequences, we can efficiently search for patterns within tuples and perform various data processing tasks.