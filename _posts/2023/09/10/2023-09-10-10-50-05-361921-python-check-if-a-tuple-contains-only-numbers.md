---
layout: post
title: "[Python] Check if a Tuple Contains Only Numbers"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

To solve this problem, we can iterate over each element in the tuple and use the `isinstance()` function to check if it is of type `int` or `float`. If any element fails this check, we can conclude that the tuple contains non-numeric values.

Here's an example implementation of how you can check if a tuple contains only numbers in Python:

```python
def is_numeric_tuple(input_tuple):
    for element in input_tuple:
        if not isinstance(element, (int, float)):
            return False
    return True
```

In the above code, we define a function called `is_numeric_tuple()` that takes an input tuple as a parameter. We iterate over each element of the input tuple and use the `isinstance()` function to check if the element is an `int` or `float`. If any element fails this check, we immediately return `False`. If all elements pass the check, we return `True` at the end.

Now, let's test our function with a few examples:

```python
tuple1 = (4, 2, 1, 3)
print(is_numeric_tuple(tuple1))  # Output: True

tuple2 = (4, 2, 'a', 3)
print(is_numeric_tuple(tuple2))  # Output: False

tuple3 = (1.5, 2.8, 3.6)
print(is_numeric_tuple(tuple3))  # Output: True

tuple4 = (1.5, 2.8, '3.6')
print(is_numeric_tuple(tuple4))  # Output: False
```

In the above examples, `is_numeric_tuple()` is called with different tuples as input. The function correctly identifies whether the tuples contain only numbers or not.

By using this simple approach, you can easily check if a tuple contains only numbers in Python. This can be applied to various scenarios, such as data validation or filtering out non-numeric values from a tuple.