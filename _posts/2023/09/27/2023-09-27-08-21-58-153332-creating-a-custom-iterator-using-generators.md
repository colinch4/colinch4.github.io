---
layout: post
title: "Creating a custom iterator using generators"
description: " "
date: 2023-09-27
tags: [generators, iterators]
comments: true
share: true
---

Generators are a powerful feature of Python that allow us to create iterators in a simple and elegant way. In this blog post, we will explore how to create a custom iterator using generators.

## What is an Iterator?

An iterator is an object that can be iterated (looped) over. It returns data values one at a time, which allows us to iterate over a collection of items or elements. For example, iterating over a list or a dictionary.

## Generators in Python

Generators are functions that use the `yield` keyword instead of `return` to generate a sequence of values. They can be paused and resumed, which makes them ideal for creating iterable objects.

To create a generator, we define a function that uses the `yield` keyword to return a value. When the generator is called, it returns an iterator object that can be iterated over using a loop, like a `for` loop.

Here's an example of a simple generator that generates a sequence of numbers:

```python
def number_generator(n):
    for i in range(n):
        yield i

# Using the number_generator
numbers = number_generator(5)
for num in numbers:
    print(num)
```

Output:
```
0
1
2
3
4
```

## Creating a Custom Iterator using Generators

To create a custom iterator using generators, we define a generator function that generates the values we want to iterate over. The generator function can have any logic we want, such as filtering or transforming data.

Here's an example of a custom iterator using generators that generates a sequence of even numbers:

```python
def even_number_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Using the even_number_generator
even_numbers = even_number_generator(10)
for num in even_numbers:
    print(num)
```

Output:
```
0
2
4
6
8
```

In this example, the `even_number_generator` function generates a sequence of numbers from 0 to `n` (exclusive), but only yields the numbers that are divisible by 2 (i.e., even numbers).

## Conclusion

Generators provide a convenient way to create custom iterators in Python. They allow us to generate values on the fly, which can be useful for iterating over large data sets or generating sequences based on specific conditions.

By using generators, we can make our code more readable, concise, and memory-efficient. So the next time you need to create an iterator, consider using generators to simplify the process.

#python #generators #iterators