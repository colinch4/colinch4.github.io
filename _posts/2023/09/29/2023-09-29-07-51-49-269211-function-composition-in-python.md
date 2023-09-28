---
layout: post
title: "Function composition in Python"
description: " "
date: 2023-09-29
tags: [Python, FunctionComposition]
comments: true
share: true
---

Function composition is an important concept in functional programming that allows us to create new functions by combining existing functions. In Python, we can achieve function composition in different ways, using built-in functions or libraries.

## Using the `compose` function from the `functools` module

The `compose` function from the `functools` module is a convenient way to compose functions in Python. It takes two or more functions as arguments and returns a new function that is the composition of those functions.

```python
from functools import compose

# Functions to be composed
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

# Compose the functions
composed_function = compose(multiply_by_two, add_one)

# Call the composed function
result = composed_function(3)
print(result)  # Output: 8
```

In the example above, the `compose` function takes `multiply_by_two` and `add_one` functions as arguments and returns a new function that first applies `add_one` and then applies `multiply_by_two` to the result.

## Using lambda functions

Another way to achieve function composition in Python is by using lambda functions. Lambda functions are anonymous functions that can be defined and used inline.

```python
# Functions to be composed (as lambda functions)
add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2

# Compose the functions
composed_function = lambda x: multiply_by_two(add_one(x))

# Call the composed function
result = composed_function(3)
print(result)  # Output: 8
```

In this example, we define the `add_one` and `multiply_by_two` functions as lambda functions and then compose them using another lambda function `composed_function`. The result is the same as in the previous example.

## Conclusion

Function composition is a powerful technique that allows us to create complex functions by combining simpler functions. In Python, we can achieve function composition using the `compose` function from the `functools` module or by using lambda functions. Choose the method that suits your preference and coding style. 

#Python #FunctionComposition