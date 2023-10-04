---
layout: post
title: "Memoization with decorators in Python"
description: " "
date: 2023-09-29
tags: [memoization]
comments: true
share: true
---

In computer science, **memoization** is a technique used to optimize the execution time of a function by caching its results. This is particularly useful when dealing with recursive functions or functions with expensive computations.

Python provides a simple and elegant way to implement memoization using decorators. Decorators are a powerful feature that allows us to modify the behavior of a function or class without changing its source code. 

Here's an example of how to implement memoization with decorators in Python:

```python
# Define the memoize decorator
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    
    return wrapper

# Define a recursive function and apply the memoize decorator
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the fibonacci function
print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765
print(fibonacci(30))  # Output: 832040
```

In the above code, we first define a `memoize` decorator function that creates a cache dictionary to store the results of previously executed function calls. The `wrapper` function is then defined to check if the arguments are already in the cache. If they are, the previously cached result is returned. Otherwise, the function is called, the result is cached, and then returned.

Finally, we define the `fibonacci` function and apply the `memoize` decorator to it. This will automatically optimize the function by caching the results of previous Fibonacci number calculations.

By using the memoization technique, we can significantly improve the performance of recursive functions that involve repetitive computations. It reduces the time complexity by avoiding redundant calculations.

Remember to use the `@memoize` decorator whenever you have a function that can benefit from memoization. It can make a substantial difference in the execution time of your code.

#python #memoization