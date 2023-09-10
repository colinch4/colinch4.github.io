---
layout: post
title: "[Python] Checking if a list contains only unique elements in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Method 1: Using the set() function

One simple way to check for uniqueness in a list is by converting the list into a set. The set data structure in Python only allows unique elements. Thus, if the length of the set is equal to the length of the original list, it means that all elements in the list are unique.

Here's an example implementation using this method:

```python
def has_unique_elements(lst):
    return len(lst) == len(set(lst))

# Testing the function
numbers = [1, 2, 3, 4, 5]
print(has_unique_elements(numbers))  # Output: True

fruits = ['apple', 'banana', 'apple', 'orange']
print(has_unique_elements(fruits))  # Output: False
```

In this example, `has_unique_elements()` is a function that takes a list `lst` as input and returns `True` if the list contains only unique elements, and `False` otherwise. We use the `len()` function to compare the lengths of the original list and the set created from the list.

## Method 2: Using a loop

Another approach is to use a loop to iterate over the elements of the list and check if there are any duplicates. We can maintain a set to keep track of the already encountered elements and return `False` as soon as we find a duplicate.

Here's an example implementation using this method:

```python
def has_unique_elements(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return False
        seen.add(element)
    return True

# Testing the function
numbers = [1, 2, 3, 4, 5]
print(has_unique_elements(numbers))  # Output: True

fruits = ['apple', 'banana', 'apple', 'orange']
print(has_unique_elements(fruits))  # Output: False
```

In this example, we initialize an empty set `seen` to keep track of the elements seen so far. We iterate over each element in the list and use an `if` condition to check if the element is already present in the set. If it is, we return `False`, indicating that the list contains duplicates. Otherwise, we add the element to the set and continue the loop. If no duplicates are found, we return `True`.

## Conclusion

Checking if a list contains only unique elements is a common task in Python. In this blog post, we explored two different methods to accomplish this task, using the `set()` function and using a loop with a set. Both methods are efficient and provide a straightforward solution.

You can choose the method that best suits your requirement or personal preference. Keep in mind that the `set()` function method is shorter and more concise, whereas the loop method allows you to perform additional operations or checks during the iteration process.