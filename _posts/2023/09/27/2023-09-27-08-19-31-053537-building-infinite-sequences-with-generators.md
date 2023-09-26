---
layout: post
title: "Building infinite sequences with generators"
description: " "
date: 2023-09-27
tags: [generators]
comments: true
share: true
---

Generators in Python are a powerful tool for creating infinite sequences of data. They allow us to generate values on the fly, saving memory and computation time. In this blog post, we will explore how to use generators to build infinite sequences.

## What are generators?

Generators in Python are a type of iterator, a special kind of object that can be iterated over. Unlike lists or tuples, generators do not store all values in memory at once. Instead, they generate the next value in the sequence each time they are iterated over. This makes them memory-efficient, especially when working with large sequences or infinite streams of data.

To create a generator, we use a function that contains the `yield` keyword. The `yield` statement pauses the function's execution and "yields" a value to the caller. The function can then be resumed later, starting from where it left off.

## Generating an infinite sequence

To build an infinite sequence, we can use a while loop inside a generator function. The loop generates a new value in the sequence on each iteration and yields it to the caller. Here's an example of a generator function that generates an infinite sequence of natural numbers:

```python
def natural_numbers():
    number = 1
    while True:
        yield number
        number += 1
```

In this example, the generator function `natural_numbers` starts from 1 and generates an incremented value on each iteration indefinitely. We can use this generator to create an infinite sequence of natural numbers:

```python
numbers = natural_numbers()
for i in range(10):
    print(next(numbers))
```

The output will be:

```
1
2
3
4
5
6
7
8
9
10
```

## Infinite sequences with conditions

We can also add conditions to our generator functions to generate infinite sequences that match specific criteria. For example, let's create a generator that generates an infinite sequence of even numbers:

```python
def even_numbers():
    number = 0
    while True:
        yield number
        number += 2
```

In this generator, we start from 0 and generate the next even number on each iteration. We can use this generator to create an infinite sequence of even numbers:

```python
even_nums = even_numbers()
for i in range(10):
    print(next(even_nums))
```

The output will be:

```
0
2
4
6
8
10
12
14
16
18
```

## Conclusion

Generators are a powerful feature in Python that allow us to create infinite sequences of data. They are memory-efficient and provide a convenient mechanism to generate values on the fly. By using generator functions and the `yield` keyword, we can easily build infinite sequences that match specific criteria. This makes generators a valuable tool for working with large datasets, data streams, or any situation where we need to generate data dynamically.

#python #generators