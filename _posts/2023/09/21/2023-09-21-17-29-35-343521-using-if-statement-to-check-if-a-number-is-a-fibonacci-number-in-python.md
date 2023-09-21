---
layout: post
title: "Using if statement to check if a number is a Fibonacci number in Python"
description: " "
date: 2023-09-21
tags: [python, fibonacci]
comments: true
share: true
---
title: "Checking if a Number is a Fibonacci Number in Python"
date: "2022-07-04"
categories:
  - Python
tags:
  - Fibonacci
  - Number
---

In this tutorial, we will learn how to check if a given number is a Fibonacci number using an `if` statement in Python.

## Fibonacci Sequence

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It starts with 0 and 1. Here is the Fibonacci sequence for reference:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```

## Using an `if` Statement

To check if a number is a Fibonacci number, we need to iterate until we find a number that is equal to or greater than the given number. Then, we check if the last two numbers in the sequence are equal to the given number.

Here's the code to check if a number is a Fibonacci number:

```python
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

# Example Usage
number = 55
if is_fibonacci(number):
    print(number, "is a Fibonacci number")
else:
    print(number, "is not a Fibonacci number")
```

In this code, we initialize the variables `a` and `b` to 0 and 1 respectively, which represent the first two Fibonacci numbers. We then use a `while` loop to generate the Fibonacci sequence until `b` becomes equal to or greater than the given number.

Finally, we check if `b` is equal to the given number. If it is, we return `True` indicating that the number is a Fibonacci number. Otherwise, we return `False`.

You can try running the above code with different values of `number` to check if they are Fibonacci numbers.

That's it! You now know how to use an `if` statement to check if a number is a Fibonacci number in Python.

#python #fibonacci