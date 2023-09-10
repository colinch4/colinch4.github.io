---
layout: post
title: "[Python] Check if a Tuple Contains Only Positive/Negative Numbers"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, tuples are immutable sequences that can contain elements of different data types. Sometimes, we may need to check if a tuple contains only positive or negative numbers. In this blog post, we will explore a few ways to accomplish this task using Python.

## Method 1: Loop through the Tuple

One way to check if a tuple contains only positive or negative numbers is by looping through the tuple's elements and checking their sign. Here's an example code snippet that demonstrates this approach:

```python
def is_all_positive(numbers):
    for num in numbers:
        if num <= 0:
            return False
    return True

def is_all_negative(numbers):
    for num in numbers:
        if num >= 0:
            return False
    return True

# Example usage
tuple1 = (1, 2, 3, 4)
tuple2 = (-1, -2, -3, -4)
tuple3 = (1, -2, 3, -4)

print(is_all_positive(tuple1))  # Output: True
print(is_all_negative(tuple1))  # Output: False

print(is_all_positive(tuple2))  # Output: False
print(is_all_negative(tuple2))  # Output: True

print(is_all_positive(tuple3))  # Output: False
print(is_all_negative(tuple3))  # Output: False
```

In the above code, the functions `is_all_positive()` and `is_all_negative()` iterate through the given tuple using a `for` loop. They check if each number fulfills the condition of being positive (greater than zero) or negative (less than zero) respectively. If any element fails the condition, the function returns `False`. If all elements pass the condition, the function returns `True`.

## Method 2: Using `all()` and List Comprehension

Another approach is to use the `all()` function along with list comprehension to check if all elements of the tuple satisfy the desired condition. Here's how we can implement this method:

```python
def is_all_positive(numbers):
    return all(num > 0 for num in numbers)

def is_all_negative(numbers):
    return all(num < 0 for num in numbers)

# Example usage
tuple1 = (1, 2, 3, 4)
tuple2 = (-1, -2, -3, -4)
tuple3 = (1, -2, 3, -4)

print(is_all_positive(tuple1))  # Output: True
print(is_all_negative(tuple1))  # Output: False

print(is_all_positive(tuple2))  # Output: False
print(is_all_negative(tuple2))  # Output: True

print(is_all_positive(tuple3))  # Output: False
print(is_all_negative(tuple3))  # Output: False
```

This code snippet uses list comprehension to create a boolean list based on the given condition (`num > 0` or `num < 0`). The `all()` function then checks if all elements of the boolean list are `True`. If they are, it returns `True`; otherwise, it returns `False`.

## Conclusion

In this blog post, we explored two different methods to check if a tuple contains only positive or negative numbers. The first method involved looping through the tuple's elements and checking their sign individually. The second method utilized the `all()` function along with list comprehension to create a boolean list and check if all elements are `True`. Both methods provide efficient ways to solve this problem in Python.