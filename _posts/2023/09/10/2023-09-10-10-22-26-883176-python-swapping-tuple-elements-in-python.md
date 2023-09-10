---
layout: post
title: "[Python] Swapping Tuple elements in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Let's get started with an example:

```python
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a list
my_list = list(my_tuple)

# Swap elements at index 1 and 2
my_list[1], my_list[2] = my_list[2], my_list[1]

# Convert the list back to a tuple
swapped_tuple = tuple(my_list)

# Print the original and swapped tuple
print("Original tuple:", my_tuple)
print("Swapped tuple:", swapped_tuple)
```

In the above code, we create a tuple `my_tuple` with elements `(1, 2, 3, 4, 5)`. We then convert the tuple to a list using the `list()` function. The elements can now be swapped using the indexing technique of Python lists. In this example, we swap the elements at index 1 and 2 using a single line of code:

```python
my_list[1], my_list[2] = my_list[2], my_list[1]
```

After swapping the elements, we convert the list back to a tuple using the `tuple()` function and assign it to `swapped_tuple`.

Finally, we print both the original and the swapped tuple using `print()` statements.

When you run this code, the output will be:

```
Original tuple: (1, 2, 3, 4, 5)
Swapped tuple: (1, 3, 2, 4, 5)
```

As you can see, the elements at indices 1 and 2 have been successfully swapped in the tuple.

Swapping elements in a tuple can be useful when dealing with different types of data or when reordering elements based on certain conditions without changing the tuple's overall structure.

I hope this blog post has helped you understand how to swap elements in a tuple using Python. Happy coding!