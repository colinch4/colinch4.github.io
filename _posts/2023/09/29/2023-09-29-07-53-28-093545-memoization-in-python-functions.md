---
layout: post
title: "Memoization in Python functions"
description: " "
date: 2023-09-29
tags: [python, memoization]
comments: true
share: true
---

When working with recursive functions, it is common to encounter repetitive calculations that can significantly slow down the program. One way to optimize these calculations is by implementing memoization.

Memoization is a technique that stores the results of expensive function calls and retrieves them when the same inputs occur again. By doing so, we can avoid redundant evaluations and improve the overall performance of our code.

In Python, we can easily implement memoization using decorators. Let's take a look at an example.

```python
import functools

@functools.lru_cache()
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
```

In the code above, we define a `fibonacci` function that calculates the nth Fibonacci number recursively. By using the `@functools.lru_cache()` decorator, we enable memoization for this function.

The `lru_cache()` function is a built-in memoization decorator in Python. It stands for "Least Recently Used Cache" and automatically caches function results using a dictionary. It also takes care of handling function arguments and hashing them correctly.

Once the memoization is enabled, subsequent calls to the `fibonacci` function with the same inputs will return the cached result instead of recalculating it. This drastically improves the performance of the function, especially for larger values of `n`.

Memoization is not only limited to recursive functions like the Fibonacci sequence. It can be applied to any function that has repetitive computations or expensive function calls. Just wrap the function with the `@functools.lru_cache()` decorator, and you're good to go.

In conclusion, memoization is a powerful technique to optimize the performance of recursive functions in Python. By storing and reusing calculated results, we can reduce the time complexity of our code and improve its efficiency. So, the next time you encounter repetitive calculations, think about incorporating memoization into your Python functions to boost their speed.

#python #memoization