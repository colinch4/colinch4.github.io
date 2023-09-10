---
layout: post
title: "[Python] Nested Tuples in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a tuple is an immutable sequence of elements enclosed in parentheses. It is commonly used to represent a collection of related values. But did you know that you can also have nested tuples in Python? This means that a tuple can contain other tuples as its elements. In this article, we will explore how to work with nested tuples in Python.

## Creating Nested Tuples

To create a nested tuple, simply enclose multiple tuples within a larger tuple. Here's an example:

```python
nested_tuple = (("apple", "banana"), ("cherry", "durian"), ("elderberry", "fig"))
```

In this example, `nested_tuple` contains three tuples, each with two elements. You can visualize it as a table with rows and columns:

```
[("apple", "banana"), 
 ("cherry", "durian"), 
 ("elderberry", "fig")]
```

## Accessing Elements of Nested Tuples

To access elements in a nested tuple, you can use indexing. The first index will refer to the outer tuple, and the second index will refer to the inner tuple. Here's how you can access specific elements in the `nested_tuple`:

```python
print(nested_tuple[0])            # Output: ("apple", "banana")
print(nested_tuple[1][0])         # Output: "cherry"
print(nested_tuple[2][1])         # Output: "fig"
```

In the first example, we retrieve the entire first tuple from the `nested_tuple`. In the second example, we access the first element of the second tuple. In the third example, we access the second element of the third tuple.

## Modifying Elements in Nested Tuples

Since tuples are immutable, you cannot modify the individual elements directly. However, you can create a new tuple by concatenating or replacing elements. Let's see an example:

```python
nested_tuple = (("apple", "banana"), ("cherry", "durian"), ("elderberry", "fig"))
new_tuple = nested_tuple[0] + ("grape",) + nested_tuple[2][1:]
print(new_tuple)          # Output: ("apple", "banana", "grape", "fig")
```

In this example, we create a new tuple `new_tuple` by concatenating the elements from the original nested tuple and inserting a new element "grape" between them.

## Iterating through Nested Tuples

To iterate through a nested tuple, you can use nested loops or list comprehension. Here's an example using nested loops to print all the elements of the `nested_tuple`:

```python
for inner_tuple in nested_tuple:
    for element in inner_tuple:
        print(element)
```

This will output all the elements of the nested tuple, one element per line.

## Conclusion

Nested tuples in Python allow you to represent complex data structures efficiently. You can access and modify elements using indexing and concatenate or replace elements to create new tuples. Iterating through nested tuples can be achieved using nested loops or list comprehension. With these techniques, you can harness the power of nested tuples in your Python programs.