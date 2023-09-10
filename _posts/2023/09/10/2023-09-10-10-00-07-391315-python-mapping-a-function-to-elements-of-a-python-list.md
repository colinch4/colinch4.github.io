---
layout: post
title: "[Python] Mapping a function to elements of a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

The `map()` function takes two arguments - the function you want to apply and the list you want to apply it to. It returns a new list with the function applied to each element of the original list.

Here's an example to demonstrate how to use the `map()` function in Python:

```python
# Define a function
def square(x):
    return x ** 2

# Define a list
numbers = [1, 2, 3, 4, 5]

# Apply the function to each element of the list using map()
result = map(square, numbers)

# Print the result
print(list(result))  # Output: [1, 4, 9, 16, 25]
```

In this example, we first define a function `square()` that takes a number as input and returns its square. Then, we create a list of numbers. 

Next, we use the `map()` function to apply the `square()` function to each element of the `numbers` list. The result is an iterable object, so we convert it to a list using the `list()` function.

Finally, we print the resulting list, which contains the squares of the original numbers.

You can use any valid Python function as an argument to `map()`, allowing you to perform a wide range of operations on the elements of a list.

Using the `map()` function can be an efficient and elegant way to apply a function to multiple elements of a list in Python. It saves you from writing explicit loops and reduces code duplication.