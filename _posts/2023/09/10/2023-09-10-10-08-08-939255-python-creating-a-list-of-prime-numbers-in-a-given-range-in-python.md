---
layout: post
title: "[Python] Creating a list of prime numbers in a given range in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will discuss how to create a list of prime numbers within a given range in Python.

A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. To determine if a number is prime, we will use the trial division method.

Let's start by writing a Python function that checks whether a number is prime or not.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The `is_prime` function takes an integer `n` as input and returns `True` if it is prime, and `False` otherwise. It checks for divisors up to the square root of `n` to optimize the process.

Now, let's write another function that generates a list of prime numbers within a given range.

```python
def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
```

The `generate_primes` function takes two integers `start` and `end` as input and returns a list of prime numbers between `start` and `end`. It uses the `is_prime` function to determine if a number is prime and adds it to the `primes` list if it is.

Let's test our functions by generating a list of prime numbers between 1 and 100.

```python
start = 1
end = 100

prime_list = generate_primes(start, end)

print(prime_list)
```

Running this code will output `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]`, which are all the prime numbers within the range 1 to 100.

In conclusion, we have learned how to create a list of prime numbers within a given range in Python. The `is_prime` function checks if a number is prime, and the `generate_primes` function generates a list of prime numbers within a specified range.

Happy coding!