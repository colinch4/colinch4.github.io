---
layout: post
title: "[Python] Sort a Tuple by its Last Element"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Method 1: Using the sorted() Function

The simplest and most straightforward way to sort a tuple by its last element is by using the built-in `sorted()` function. We can pass a custom key function to the `sorted()` function to tell it to use the last element of each tuple for comparison.

```python
# Original unsorted tuple
my_tuple = [('apple', 5), ('orange', 10), ('banana', 3)]

# Sorting the tuple by last element
sorted_tuple = sorted(my_tuple, key=lambda x: x[-1])

print(sorted_tuple)
```

Output:
```
[('banana', 3), ('apple', 5), ('orange', 10)]
```

In this example, the `key` argument inside the `sorted()` function specifies a **lambda** function that extracts the last element of each tuple (`x[-1]`) for comparison.

## Method 2: Using the itemgetter() Function from the operator module

Another way to sort a tuple by its last element is by using the `itemgetter()` function from the **operator** module. This function returns a getter function that retrieves the specified item from its operand.

```python
from operator import itemgetter

# Original unsorted tuple
my_tuple = [('apple', 5), ('orange', 10), ('banana', 3)]

# Sorting the tuple by last element
sorted_tuple = sorted(my_tuple, key=itemgetter(-1))

print(sorted_tuple)
```

Output:
```
[('banana', 3), ('apple', 5), ('orange', 10)]
```

In this example, the `key` argument inside the `sorted()` function takes the **itemgetter** function as the value. The `itemgetter(-1)` returns a callable that extracts the last element of each tuple for comparison.

Both methods mentioned above will give the same output, which is the sorted tuple based on the last element of each tuple.

By utilizing these techniques, you can easily sort a tuple by its last element in Python. Whether using the `sorted()` function with a lambda function or the `itemgetter()` function from the operator module, you have the flexibility to achieve a sorted result based on your specific requirements.