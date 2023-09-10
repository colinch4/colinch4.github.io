---
layout: post
title: "[Python] Tuple Membership and Identity Operators"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, tuples are an immutable sequence type that can store multiple values. They are very similar to lists, but the main difference is that tuples cannot be modified after they are created. In this blog post, we will explore the concepts of **membership operators** and **identity operators** in relation to tuples in Python.

## Tuple Membership Operators

Python provides two membership operators to check if a value is present in a tuple:

- `in`: Returns `True` if the value is found in the tuple.
- `not in`: Returns `True` if the value is not found in the tuple.

Let's take a look at an example to understand how these operators work:

```python
fruits = ('apple', 'banana', 'cherry', 'date')

print('banana' in fruits)  # Output: True
print('grape' not in fruits)  # Output: True
```

In the above example, we have a tuple named `fruits` that contains four elements. By using the `in` operator, we check if the value `'banana'` is present in the tuple, which returns `True`. Similarly, we use the `not in` operator to check if the value `'grape'` is not present in the tuple, which also returns `True`.

## Tuple Identity Operators

Python provides two identity operators to compare the **identity** of two objects:

- `is`: Returns `True` if both objects are the same.
- `is not`: Returns `True` if both objects are not the same.

When working with tuples, the identity operators are useful to check if two tuples refer to the same object or have the same values.

Let's illustrate this with an example:

```python
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = tuple1

print(tuple1 is tuple2)  # Output: False
print(tuple1 is tuple3)  # Output: True
print(tuple1 is not tuple2)  # Output: True
```

In the above example, we have three tuples: `tuple1`, `tuple2`, and `tuple3`. `tuple1` and `tuple2` have the same values, but they are distinct objects, so the `is` operator returns `False`. On the other hand, `tuple1` and `tuple3` refer to the same object, so the `is` operator returns `True`. Finally, the `is not` operator confirms that `tuple1` and `tuple2` are indeed not the same object.

## Conclusion

In this blog post, we explored the concepts of tuple membership operators and identity operators in Python. We saw how the `in` and `not in` operators can be used to check if a value exists in a tuple. We also discussed how the `is` and `is not` operators compare the identity of two tuples. Understanding these operators will help you write more efficient and concise code when working with tuples in Python.