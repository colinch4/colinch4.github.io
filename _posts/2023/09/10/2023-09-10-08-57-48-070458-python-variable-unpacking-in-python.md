---
layout: post
title: "[Python] Variable unpacking in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Python offers a convenient way to **unpack variables** assigned to a sequence or iterable. This feature allows you to assign values to multiple variables at once, making your code cleaner and more efficient. In this blog post, we will explore how variable unpacking works in Python and discuss its various use cases.

## Basic Syntax

The basic syntax for variable unpacking in Python involves using the assignment operator (`=`) along with a comma-separated list of target variables on the left, and a sequence or iterable on the right. 

Here's an example:

```python
a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

In the above code, the sequence `[1, 2, 3]` is unpacked into the variables `a`, `b`, and `c`. Each variable receives a respective value from the sequence.

## Unpacking with Multiple Assignments

Variable unpacking in Python not only works with lists but with other iterable objects like tuples and strings as well. Let's take a look at a few examples:

### Unpacking a tuple

```python
my_tuple = (10, 20, 30)
x, y, z = my_tuple
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30
```

### Unpacking a string

```python
my_string = "abc"
x, y, z = my_string
print(x)  # Output: a
print(y)  # Output: b
print(z)  # Output: c
```

### Unpacking a nested sequence

```python
my_list = ["apple", [1, 2], ("x", "y")]
fruit, numbers, xy = my_list
print(fruit)   # Output: apple
print(numbers) # Output: [1, 2]
print(xy)      # Output: ('x', 'y')
```

## Ignoring Values

Sometimes, you might want to unpack only a few values from a sequence and ignore the rest. In such cases, you can use the underscore (`_`) as a placeholder for the values you want to disregard.

Here's an example:

```python
numbers = [1, 2, 3, 4, 5]
x, _, y, _, z = numbers
print(x)  # Output: 1
print(y)  # Output: 3
print(z)  # Output: 5
```

In the above code, we are unpacking the first, third, and fifth values from `numbers` and ignoring the others.

## Swapping Variables

One of the useful applications of variable unpacking is swapping the values of two variables without using a temporary variable. This can be done with just a single line of code in Python.

```python
a = 10
b = 20

a, b = b, a
print(a)  # Output: 20
print(b)  # Output: 10
```

By leveraging variable unpacking, we can directly assign the new values to `a` and `b` simultaneously, effectively swapping their values.

## Conclusion

Variable unpacking in Python provides a powerful and efficient way to assign values to multiple variables at once. It simplifies your code, improves readability, and enables various operations like unpacking nested data structures and swapping variable values. By leveraging this feature, you can write cleaner and more concise code in Python.