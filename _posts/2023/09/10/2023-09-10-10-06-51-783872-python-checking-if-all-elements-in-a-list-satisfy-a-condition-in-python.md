---
layout: post
title: "[Python] Checking if all elements in a list satisfy a condition in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Let's say we have a list of numbers and we want to check if all elements in the list are even. Here's how we can do it:

```python
numbers = [2, 4, 6, 8, 10]

# Method 1: Using a for loop
all_even = True
for num in numbers:
    if num % 2 != 0:
        all_even = False
        break
if all_even:
    print("All elements are even")
else:
    print("There are odd elements in the list")

# Method 2: Using the all() function with a generator expression
all_even = all(num % 2 == 0 for num in numbers)
if all_even:
    print("All elements are even")
else:
    print("There are odd elements in the list")
```

In Method 1, we iterate over each element in the list using a for loop. If any element is not even, we set the `all_even` variable to `False` and break out of the loop. Finally, we check the value of `all_even` to determine if all elements are even or not.

Method 2 uses the `all()` function along with a generator expression. The generator expression `(num % 2 == 0 for num in numbers)` generates a series of `True` or `False` values indicating whether each number in the list is even. The `all()` function returns `True` if all values in the generator expression are `True`, and `False` otherwise.

Both methods produce the same result, but using the `all()` function with a generator expression provides a more concise and pythonic way to check if all elements satisfy a condition.

Remember to choose the method that suits your specific requirement and coding style.