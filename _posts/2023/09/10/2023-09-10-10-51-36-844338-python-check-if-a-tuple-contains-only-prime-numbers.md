---
layout: post
title: "[Python] Check if a Tuple Contains Only Prime Numbers"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

To start, let's define what a prime number is. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are all prime numbers.

Now, let's create a function in Python to check if a tuple contains only prime numbers:

```python
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def tuple_contains_only_primes(t):
    for num in t:
        if not is_prime(num):
            return False
    return True
```

Here, we first define the `is_prime` function, which checks if a given number is prime. It uses a simple loop to iterate from 2 to the square root of the number and checks if any of the numbers evenly divide the given number. If no divisors are found, the number is prime.

Next, we define the `tuple_contains_only_primes` function, which takes a tuple `t` as an input. It iterates over each element in the tuple and checks if it is prime using the `is_prime` function. If any element is found to be non-prime, the function returns `False`. However, if all elements in the tuple are prime, the function returns `True`.

Let's test our function with some examples:

```python
t1 = (2, 3, 5, 7)
print(tuple_contains_only_primes(t1))  # Output: True

t2 = (2, 4, 7, 11)
print(tuple_contains_only_primes(t2))  # Output: False

t3 = (13, 17, 19, 23)
print(tuple_contains_only_primes(t3))  # Output: True

t4 = ()
print(tuple_contains_only_primes(t4))  # Output: True, as an empty tuple is considered to contain only prime numbers
```

In the above example, `t1` contains only prime numbers, so our function returns `True`. `t2` contains a non-prime number (`4`), so the function returns `False`. `t3` contains only prime numbers, so the function returns `True`. Lastly, `t4` is an empty tuple, and since it doesn't contain any numbers (prime or not), the function also returns `True`.

In conclusion, we have explored how to check if a tuple in Python contains only prime numbers. This can be useful when dealing with lists or sets of numbers and filtering out non-prime numbers. Understanding prime numbers and how to work with them is a fundamental concept in programming and mathematics.