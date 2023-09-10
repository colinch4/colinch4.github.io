---
layout: post
title: "[Python] Sort a Tuple by its Absolute Values"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Let's say we have a tuple that looks like this:

```python
my_tuple = (-3, 5, -1, 2, -4)
```

We want to sort this tuple in ascending order based on the absolute values of its elements. The expected output should be:

```python
(-1, 2, -3, -4, 5)
```

To achieve this, we can use the `sorted()` function along with the `key` parameter. The `key` parameter allows us to provide a custom sorting criterion.

```python
sorted_tuple = sorted(my_tuple, key=abs)
```

In this case, `abs` is the built-in Python function that returns the absolute value of a number. We pass `abs` as the `key` to the `sorted()` function, which tells Python to sort the tuple based on the absolute values of its elements.

Now, let's see the complete code:

```python
my_tuple = (-3, 5, -1, 2, -4)
sorted_tuple = sorted(my_tuple, key=abs)
print(sorted_tuple)
```

When you run this code, you should see the sorted tuple printed to the console:

```
(-1, 2, -3, -4, 5)
```

By utilizing the `key` parameter in the `sorted()` function, we can easily sort tuples based on their absolute values in Python. This technique can be extended to sorting lists or other iterable data structures as well.

Keep in mind that the `sorted()` function creates a new sorted list, so if you want to modify the original tuple, you can reassign the sorted list back to the tuple variable:

```python
my_tuple = tuple(sorted_tuple)
```

This allows you to keep the original data structure as a tuple while still having it sorted based on the absolute values of its elements.

I hope this blog post has been helpful in showing you how to sort a tuple by its absolute values in Python. Happy coding!