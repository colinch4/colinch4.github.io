---
layout: post
title: "[Python] Get the Index of a Tuple Element from the Right Side"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Tuples are immutable sequences in Python that can store a collection of elements. They are similar to lists, but unlike lists, tuples cannot be modified once created.

In some scenarios, you may need to retrieve the index of a tuple element from the right side. By default, Python provides the `index()` method to find the index of an element from the left side. However, there is no built-in method to find the index from the right side. In this blog post, we will explore a simple solution to achieve this functionality.

### Approach Using Reversed Tuple

One way to find the index from the right side is to reverse the tuple and then find the index using the `index()` method. Here is an example:

```python
def get_index_from_right(tuple_data, element):
    reversed_tuple = tuple(reversed(tuple_data))
    return len(reversed_tuple) - reversed_tuple.index(element) - 1

# Example usage
my_tuple = (10, 20, 30, 40, 50)
element_to_find = 30

index = get_index_from_right(my_tuple, element_to_find)
print(f"The index of {element_to_find} from the right side is {index}")
```

In the above example, we define a function `get_index_from_right()` that takes a tuple and the element to find. The function first reverses the tuple using the `reversed()` function and converts it back to a tuple using `tuple()`. Then, it finds the index of the element using the `index()` method and subtracts it from the total length of the reversed tuple. Finally, it subtracts 1 to get the correct index from the right side.

### Output

```
The index of 30 from the right side is 2
```

### Conclusion

Although Python doesn't provide a built-in method to find the index of a tuple element from the right side, we can achieve this functionality by reversing the tuple and using the `index()` method. By using the approach mentioned in this blog post, you can easily get the index of any element from the right side of a tuple in Python.