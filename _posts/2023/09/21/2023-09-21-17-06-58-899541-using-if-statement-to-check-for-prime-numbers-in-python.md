---
layout: post
title: "Using if statement to check for prime numbers in Python"
description: " "
date: 2023-09-21
tags: [primenumbers]
comments: true
share: true
---

Prime numbers are an essential concept in mathematics and can be useful in various programming tasks. In this article, we will explore how to determine whether a number is prime or not using an `if` statement in Python.

In mathematics, a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers.

To check whether a number is prime or not, we can use the following logic:

1. Start with a number, let's call it `num`.
2. Iterate from 2 to the square root of `num` (inclusive) and check if any number evenly divides `num`.
3. If a divisor is found, the number is not prime. Otherwise, it is prime.

Let's implement this in Python:

```python
import math

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

# Testing the function
number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```

In the above code, we use the `math.sqrt()` function from the `math` module to calculate the square root of `num`. By converting it to an integer using `int()`, we ensure that the iteration range is correct.

The `is_prime()` function takes a number as input and checks if it is less than 2. If it is, the function immediately returns `False`. Otherwise, it iterates from 2 to the square root of `num` and checks if any number evenly divides `num`. If a divisor is found, it returns `False`, indicating that the number is not prime. If no divisor is found, it returns `True`, indicating that the number is prime.

Finally, we test the function with a sample number (`17` in this case) using an `if` statement. If the number is prime, it prints that it is a prime number. Otherwise, it prints that it is not a prime number.

By using the `is_prime()` function, we can easily check for prime numbers in Python.

#python #primenumbers