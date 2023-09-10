---
layout: post
title: "[Python] Tuple Sorting in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a **tuple** is an immutable sequence of elements, enclosed in parentheses `()`. Tuples are commonly used to group related information together.

Sorting tuples can be useful, especially when you want to order them based on a specific criteria. In this blog post, we will explore different methods to sort tuples in Python.

## Sorted() Function

The simplest way to sort tuples is by using the built-in `sorted()` function. The `sorted()` function takes an iterable as input and returns a new list containing the sorted elements.

```python
fruits = ('apple', 'orange', 'banana', 'pear')
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'orange', 'pear']
```

In the example above, the `fruits` tuple is sorted in alphabetical order using the `sorted()` function. The resulting sorted list is assigned to the `sorted_fruits` variable.

## Sort Method

Another approach to sort tuples is by using the `sort()` method. However, unlike the `sorted()` function, the `sort()` method can only be used with **lists**, not tuples, **because tuples are immutable**.

To sort a tuple using the `sort()` method, you need to convert the tuple into a list, sort it, and then convert it back to a tuple using the `tuple()` function.

```python
fruits = ('apple', 'orange', 'banana', 'pear')
sorted_fruits = tuple(sorted(list(fruits)))
print(sorted_fruits)  # Output: ('apple', 'banana', 'orange', 'pear')
```

In the example above, we first convert the `fruits` tuple into a list using `list(fruits)`. Then, the `sorted()` function is called on the list, and finally, the sorted list is converted back to a tuple using `tuple()`.

## Using a Custom Key Function

Sometimes, you may want to sort tuples based on a specific key or a particular element within each tuple. In such cases, you can pass a custom key function to the `sorted()` function or `sort()` method.

Let's say we have a list of tuples representing students' names and their corresponding scores. We want to sort the tuples based on the scores in ascending order.

```python
students = [('John', 80), ('Alice', 95), ('Bob', 75), ('Charlie', 90)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sorting by second element of each tuple
print(sorted_students)
```

In the example above, we used a lambda function as the key argument to access the second element of each tuple. The tuples are sorted based on the scores, resulting in the sorted list of `students`.

## Conclusion

Sorting tuples in Python is straightforward using built-in functions like `sorted()` or `sort()`. Additionally, you can customize the sorting order by providing a custom key function.

Understanding how to sort tuples is essential when working with data that needs to be ordered based on specific criteria.