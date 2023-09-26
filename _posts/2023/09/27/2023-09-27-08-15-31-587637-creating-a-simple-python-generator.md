---
layout: post
title: "Creating a simple Python generator"
description: " "
date: 2023-09-27
tags: [generators]
comments: true
share: true
---

Generators in Python are a powerful tool for creating iterators. They allow us to generate a sequence of values on-the-fly, without storing them in memory. This can be useful when working with large datasets or when we only need to iterate through a portion of a sequence.

In this blog post, we'll explore how to create a simple generator in Python using the `yield` keyword.

## What is a Generator?

A generator is a special type of function that returns an iterator. It allows us to iterate through a sequence of values one at a time, rather than generating the entire sequence upfront.

To create a generator, we use the `yield` keyword instead of `return` in a normal function. When the `yield` keyword is encountered, the current state of the function is saved, and the yielded value is returned. The next time the function is called, it resumes execution from where it left off, allowing us to generate the next value in the sequence.

## Example: Generating Even Numbers

Let's start by creating a simple generator that generates even numbers. We'll define a function called `even_numbers()` and use the `yield` keyword inside a loop to generate each even number.

```python
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2
```

In this example, the `even_numbers()` function is an infinite generator that produces even numbers. We initialize `num` to 0 and then use an infinite loop (`while True`) to generate each even number. We yield `num` before incrementing it by 2, producing the next even number when the generator is iterated.

## Using the Generator

Now that we have our `even_numbers()` generator, let's use it to print the first 10 even numbers.

```python
even_gen = even_numbers()

for _ in range(10):
    print(next(even_gen))
```

In this code snippet, we first create an instance of the `even_numbers()` generator and assign it to the variable `even_gen`. We then use a `for` loop to iterate 10 times and print each generated even number by calling `next(even_gen)`.

## Conclusion

Generators are a useful feature in Python for generating sequences of values on-demand. They allow us to create memory-efficient iterators and can be especially handy when working with large datasets or when we only need to iterate through a portion of a sequence.

In this post, we created a simple Python generator that generates even numbers using the `yield` keyword. We also demonstrated how to use the generator to print the first 10 even numbers.

By using generators, we can write more efficient code that consumes less memory and provides a more elegant way of working with iterable data.

#python #generators