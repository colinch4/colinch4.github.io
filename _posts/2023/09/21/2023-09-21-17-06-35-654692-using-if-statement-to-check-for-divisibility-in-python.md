---
layout: post
title: "Using if statement to check for divisibility in Python"
description: " "
date: 2023-09-21
tags: [Divisibility]
comments: true
share: true
---

Here's an example code snippet that demonstrates how to check for divisibility in Python:

```python
def is_divisible(dividend, divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False

# Example usage
num1 = 15
num2 = 3

if is_divisible(num1, num2):
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")
```

In the above code, we define a function called `is_divisible` that takes two parameters - `dividend` and `divisor`. Inside the function, we use the modulo operator `%` to check if the remainder is equal to 0. If it is, we return `True`, indicating that the dividend is divisible by the divisor. Otherwise, we return `False`.

In the example usage part, we create two variables `num1` and `num2` with values 15 and 3 respectively. We then call the `is_divisible` function with these two numbers as arguments. If the function returns `True`, we print that `num1` is divisible by `num2`. Otherwise, we print that `num1` is not divisible by `num2`.

By using the modulo operator and an "if" statement in Python, you can easily check for divisibility between two numbers. This can be useful in various situations, such as checking if a number is even or odd, determining if a number is a multiple of another, or validating input in a program. #Python #Divisibility