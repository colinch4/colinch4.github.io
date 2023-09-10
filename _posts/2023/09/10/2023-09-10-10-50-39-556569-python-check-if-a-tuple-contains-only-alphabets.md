---
layout: post
title: "[Python] Check if a Tuple Contains Only Alphabets"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Tuples are immutable sequences in Python that can store multiple items. Sometimes, you may need to check whether a tuple contains only alphabets or not. In this blog post, we will explore a simple and efficient way to accomplish this task in Python.

## Approach

To check if a tuple contains only alphabets, we can iterate over each element in the tuple and use the `isalpha()` method of strings. This method returns `True` if all the characters in the string are alphabets; otherwise, it returns `False`. By applying this method to each element of the tuple, we can determine if the tuple contains only alphabetic values.

Let's see the code in action:

```python
def check_tuple_contains_only_alphabets(tuple):
    for item in tuple:
        if not item.isalpha():
            return False
    return True

# Test Cases
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = ('123', 'pencil', 'book')
tuple3 = ('orange', 'grape', '5')

print(check_tuple_contains_only_alphabets(tuple1))  # Output: True
print(check_tuple_contains_only_alphabets(tuple2))  # Output: False
print(check_tuple_contains_only_alphabets(tuple3))  # Output: False
```

In this example, we define a function `check_tuple_contains_only_alphabets` that takes a tuple as input and iterates over each item in the tuple. Inside the loop, we use the `isalpha()` method to check if the item contains only alphabets. If any item does not satisfy this condition, the function immediately returns `False`. If all items pass the check, the function returns `True` at the end.

## Summary

By using the `isalpha()` method in a loop, we can efficiently check if a tuple contains only alphabetic values in Python. This approach is simple and can be easily applied to any tuple containing strings. Remember to take care of any special cases, such as empty tuples or tuples containing non-string values, if necessary.

I hope you found this blog post helpful. Happy coding!