---
layout: post
title: "[Python] Variables as function arguments in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can pass variables as arguments to functions. This allows you to reuse and manipulate data within your functions. In this blog post, we will explore how to use variables as function arguments in Python.

### Positional Arguments

In Python, you can pass variables to a function as **positional arguments**. Positional arguments are arguments that are passed to a function in the order they are defined. Let's see an example:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

In the above example, we define a function called `add` which takes two positional arguments `a` and `b`. We then call the `add` function with the values `5` and `3`, and it returns the sum of `5` and `3`, which is `8`.

### Keyword Arguments

Python also allows you to pass variables as **keyword arguments**. By providing the argument name along with its value, you can pass arguments to a function in any order. Let's see an example:

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(name="John", age=25)
```

In the above example, we define a function called `greet` with two keyword arguments `name` and `age`. We then call the `greet` function and pass the values `"John"` and `25` using keyword arguments. The function prints the greeting message with the provided values.

### Default Arguments

Python also supports **default arguments**. Default arguments are arguments that take a default value if no value is provided when calling the function. Let's see an example:

```python
def power(base, exponent=2):
    return base ** exponent

result = power(3, 4)
print(result)  # Output: 81

result = power(5)
print(result)  # Output: 25 (default exponent of 2 is used)
```

In the above example, we define a function called `power` with a default argument `exponent` value of `2`. When calling the `power` function, if the `exponent` value is not provided, it will default to `2`. We can see that when we call `power(3, 4)`, it returns `81`, and when we call `power(5)`, it returns `25` using the default exponent value.

### Variable number of arguments

Python also allows you to pass a **variable number of arguments** to a function using the `*args` syntax. This is useful when you don't know the number of arguments in advance. Let's see an example:

```python
def sum_all(*args):
    total = sum(args)
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

In the above example, we define a function called `sum_all` with `*args` as the argument. This allows us to pass any number of arguments to the function. Inside the function, we calculate the sum of all the arguments using the `sum` function and return the result.

In conclusion, Python provides several ways to pass variables as function arguments. By understanding the different types of arguments and their syntax, you can write more flexible and reusable code.