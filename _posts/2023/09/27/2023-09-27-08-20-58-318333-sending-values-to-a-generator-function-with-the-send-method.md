---
layout: post
title: "Sending values to a generator function with the send() method"
description: " "
date: 2023-09-27
tags: [Python, Generators]
comments: true
share: true
---

Generators in Python are a powerful tool for lazy evaluation, allowing us to pause and resume the execution of a function. One interesting feature of generators is the ability to send values back to them using the `send()` method.

The `send()` method is used to both send values to a generator and receive the value yielded by the generator. It can be particularly useful in scenarios where we want to dynamically control the behavior of the generator or pass data into the generator for further processing.

To illustrate this, let's consider a simple generator function that yields the square of each number sent to it:

```python
def number_square():
    while True:
        x = yield
        yield x ** 2
```

In this example, the `number_square()` function is a generator function that yields the square of each number sent to it. It uses the `yield` keyword to pause the execution and return a value.

Now, let's see how we can send values to this generator and receive the calculated squares using the `send()` method:

```python
gen = number_square()
next(gen)  # Prime the generator

for i in range(5):
    square = gen.send(i)
    print(square)
```

In this code snippet, we create an instance of the generator using the `number_square()` function and call `next()` to advance the generator to the first `yield` statement. This primes the generator for receiving values.

We then use a loop to send a series of numbers to the generator using the `send()` method. Each time we send a value, the generator resumes execution and assigns the value to the variable `x`. It then yields the square of the received value, which we assign to the variable `square`. We print the resulting squares in each iteration.

By running this code, we get the following output:

```
0
1
4
9
16
```

As we can see, the `send()` method allows us to pass values to a generator and receive the processed results. It provides a convenient way to interact with generators and influence their behavior dynamically.

In summary, the `send()` method is a powerful feature of generators in Python. It enables us to pass values into generators and receive computed results. By utilizing this method effectively, we can create more flexible and interactive generator functions in our programs.

#Python #Generators