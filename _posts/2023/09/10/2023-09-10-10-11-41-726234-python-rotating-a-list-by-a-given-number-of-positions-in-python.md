---
layout: post
title: "[Python] Rotating a list by a given number of positions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, there are different ways to rotate a list by a certain number of positions. In this blog post, we will explore a few approaches to achieve this.

## Method 1: Using Slicing 

One simple way to rotate a list is by using **slicing**. You can use the slice notation with the starting and ending indices to rearrange the elements of the list.

```python
def rotate_list_by_positions(lst, positions):
    positions = positions % len(lst)  # handle cases where positions > len(lst)
    return lst[positions:] + lst[:positions]
```

In the above code snippet, we define a function `rotate_list_by_positions` that takes two arguments: `lst` (the list to be rotated) and `positions` (the number of positions to rotate the list by). We calculate the actual number of positions to rotate by using `positions % len(lst)` to handle cases where `positions` is greater than the length of the list.

The list is rotated by splitting it into two parts using slicing: `lst[positions:]` represents the elements from `positions` onwards, and `lst[:positions]` represents the elements from the beginning of the list until `positions`. By concatenating these two parts using the `+` operator, we obtain the rotated list.

## Method 2: Using the `deque` class from the `collections` module

Another approach is to use the `deque` class from the `collections` module, which provides methods for rotating elements.

```python
from collections import deque

def rotate_list_by_positions(lst, positions):
    d = deque(lst)
    d.rotate(positions)
    return list(d)
```

In this code snippet, we import the `deque` class from the `collections` module. We convert the input list `lst` into a deque object `d`. The `rotate` method of the deque object allows us to rotate the elements by the specified number of positions. Finally, we convert the deque back into a list using the `list()` function and return the rotated list.

## Example usage

Let's try out our `rotate_list_by_positions` function with an example:

```python
my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list_by_positions(my_list, 2)
print(rotated_list)
```

Output:
```
[4, 5, 1, 2, 3]
```

In this example, we have a list `[1, 2, 3, 4, 5]` and we want to rotate it by 2 positions. The resulting `rotated_list` will be `[4, 5, 1, 2, 3]`.

By using the provided methods, you can easily rotate a list by a given number of positions in Python. Whether you prefer slicing or the `deque` class from the `collections` module, both approaches offer an efficient solution to accomplish this task.

Try experimenting with different input lists and rotation positions to further explore the capabilities of rotation in Python!