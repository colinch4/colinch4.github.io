---
layout: post
title: "[Python] Splitting a list into equal-sized sublists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Sometimes, we may need to split a list into smaller sublists of equal size in Python. This can be useful when working with large datasets or when performing parallel operations on smaller portions of a list. In this blog post, we will explore various methods to achieve this in Python.

## Method 1: Using List Slices

The most straightforward way to split a list into equal-sized sublists is by using list slices. We can calculate the size of each sublist based on the length of the original list and the desired number of sublists. Here's an example:

```python
def split_list_into_sublists(lst, num_sublists):
    sublist_size = len(lst) // num_sublists
    sublist_remainder = len(lst) % num_sublists
    
    sublists = []
    start = 0
    for i in range(num_sublists):
        sublist_length = sublist_size + (1 if i < sublist_remainder else 0)
        sublist = lst[start : start + sublist_length]
        sublists.append(sublist)
        start += sublist_length
    
    return sublists

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = split_list_into_sublists(my_list, 3)
print(result)
```

Output:
```
[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
```

This code snippet defines the `split_list_into_sublists` function that takes in a list `lst` and the number of sublists `num_sublists` as parameters. It first calculates the size of each sublist using integer division (`//`) and the remainder using the modulo operator (`%`). Then, it iterates over the range of `num_sublists` to create sublists of equal size and adds them to a new list `sublists`. Finally, it returns the sublists as the result.

## Method 2: Using NumPy

Another efficient way to split a list into equal-sized sublists is by using the NumPy library. NumPy provides an `array_split()` function that can split an array into multiple subarrays of equal or almost equal size. Here's an example:

```python
import numpy as np

def split_list_into_sublists(lst, num_sublists):
    return np.array_split(lst, num_sublists)

# Example Usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = split_list_into_sublists(my_list, 3)
print(result)
```

Output:
```
[array([1, 2, 3, 4]), array([5, 6, 7]), array([8, 9, 10])]
```

In this example, we import the NumPy library and define the `split_list_into_sublists` function that takes in a list `lst` and the number of sublists `num_sublists`. We use the `np.array_split()` function to split the list into subarrays of equal or almost equal size. The function returns a list of NumPy arrays, which serves as our result.

Both of these methods provide efficient ways to split a list into equal-sized sublists in Python. Choose the method that best suits your needs and enjoy working with smaller and manageable portions of your list!