---
layout: post
title: "[Python] Sorting a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Sorting in Ascending Order

To sort a list in ascending order, you can simply call the `sort()` function without any arguments. Let's take a look at an example:

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]
```

In this example, the `sort()` function is called on the `numbers` list, which contains some random numbers. After sorting the list, we can see that the elements are arranged in ascending order.

## Sorting in Descending Order

If you want to sort the list in descending order, you can pass an argument `reverse=True` to the `sort()` function. Here's an example:

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 8, 5, 2, 1]
```

In this case, the `sort()` function sorts the `numbers` list in descending order based on the values of its elements.

## Sorting Complex Objects

The `sort()` function can also be used to sort lists of complex objects, such as dictionaries or custom objects. To do this, you need to specify a key function that returns the value to be used for comparison. Here's an example using dictionary objects:

```python
students = [
    { "name": "Alice", "age": 20 },
    { "name": "Bob", "age": 18 },
    { "name": "Charlie", "age": 22 },
]

students.sort(key=lambda student: student["age"])
print(students)
```

In this example, the `sort()` function sorts the `students` list of dictionaries based on the "age" key. The resulting list will have the dictionaries arranged in ascending order of age.

## Conclusion

Sorting a list is made easy with the built-in `sort()` function in Python. Whether you need to sort a list of integers, strings, or complex objects, the `sort()` function provides a convenient way to accomplish this task.