---
layout: post
title: "[Python] List manipulation exercises in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this blog post, we will explore some exercises related to list manipulation in Python. Lists are a versatile and widely used data structure in Python, and being able to manipulate them effectively is an important skill for any Python developer. So, let's dive into these exercises and enhance our list manipulating skills!

## Exercise 1: Reversing a List

To reverse a list in Python, you can use the `reverse()` method or the slicing technique. Here's an example using the `reverse()` method:

```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]
```

And here's an example using the slicing technique:

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```

## Exercise 2: Removing Duplicates from a List

To remove duplicates from a list in Python, you can use the `set()` function or a list comprehension. Here's an example using the `set()` function:

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5]
```

And here's an example using a list comprehension:

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = [x for i, x in enumerate(my_list) if x not in my_list[:i]]
print(unique_list)  # Output: [1, 2, 3, 4, 5]
```

## Exercise 3: Flattening a List of Lists

To flatten a list of lists in Python, you can use the `itertools.chain.from_iterable()` function or a list comprehension. Here's an example using the `itertools.chain.from_iterable()` function:

```python
import itertools

my_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = list(itertools.chain.from_iterable(my_list))
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
```

And here's an example using a list comprehension:

```python
my_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [x for sublist in my_list for x in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
```

## Conclusion

In this blog post, we explored some exercises related to list manipulation in Python. We learned how to reverse a list, remove duplicates from a list, and flatten a list of lists. List manipulation is a fundamental skill in Python programming, and by practicing these exercises, you can enhance your understanding and proficiency in this area. So, keep practicing and happy coding!