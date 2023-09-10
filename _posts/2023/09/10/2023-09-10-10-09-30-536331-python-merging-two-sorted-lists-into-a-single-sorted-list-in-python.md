---
layout: post
title: "[Python] Merging two sorted lists into a single sorted list in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Merging two sorted lists into a single sorted list is a common operation in many programming tasks. Python provides an efficient way to accomplish this using the built-in `merge` function from the `heapq` module.

## Using the `merge` function from the `heapq` module

The `heapq.merge` function efficiently merges multiple sorted iterables into a single sorted iterator. To merge two sorted lists, you can convert them into iterables and pass them as arguments to `heapq.merge`. Here's an example:

```python
import heapq

def merge_sorted_lists(list1, list2):
    merged_list = list(heapq.merge(list1, list2))
    return merged_list

# Example usage
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

merged_list = merge_sorted_lists(list1, list2)
print(merged_list)
```

Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

In the example above, we define a function `merge_sorted_lists` that takes two sorted lists as input. Inside the function, we use `heapq.merge` to merge the lists into an iterator and convert it back to a list.

The merged list is assigned to the variable `merged_list`, which is then printed to the console. The output shows the result of merging `list1` and `list2` into a single sorted list.

## Conclusion

Merging two sorted lists into a single sorted list in Python is a simple task thanks to the `heapq.merge` function. By utilizing this efficient built-in function, you can easily handle the merging process without the need for complex algorithms or extensive code.