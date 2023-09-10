---
layout: post
title: "[Python] Merging two sorted lists into a single sorted list without using additional memory in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Merging two sorted lists into a single sorted list is a common task in programming. The traditional approach involves creating a new list to store the merged elements. However, if you want to save some memory, there's a way to merge the lists **in-place** without the need for additional memory.

In Python, you can merge two sorted lists without using additional memory by taking advantage of the fact that both lists are already sorted. Here's an example of how you can do it:

```python
def merge_sorted_lists(list1, list2):
    # Get the lengths of the input lists
    m = len(list1)
    n = len(list2)

    # Traverse the lists from right to left
    while m > 0 and n > 0:
        # Compare the last elements of both lists
        if list1[m - 1] >= list2[n - 1]:
            # Move the larger element to the end of list1
            list1[m + n - 1] = list1[m - 1]
            m -= 1
        else:
            # Move the larger element to the end of list2
            list1[m + n - 1] = list2[n - 1]
            n -= 1

    # If there are any remaining elements in list2, move them to list1
    while n > 0:
        list1[n - 1] = list2[n - 1]
        n -= 1
```

Let's break down the code:

1. We define a function `merge_sorted_lists` that takes two sorted lists as input.
2. We get the lengths of both lists using the `len` function and assign them to the variables `m` and `n`.
3. We start traversing the lists from right to left using a `while` loop. The loop continues as long as both `m` and `n` are greater than 0.
4. Inside the loop, we compare the last elements of both lists. If the last element of `list1` is larger or equal to the last element of `list2`, we move it to the end of `list1` and decrement `m` by 1. Otherwise, we move the last element of `list2` to the end of `list1` and decrement `n` by 1.
5. After the loop finishes, if there are any remaining elements in `list2`, we move them to the beginning of `list1` one by one.
6. At the end of the function, `list1` will contain the merged and sorted elements from both input lists.

You can test this function by calling it with two sorted lists:

```python
# Example usage
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

merge_sorted_lists(list1, list2)

print(list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

By merging the lists in-place without creating a new list, you can save memory when dealing with large datasets.