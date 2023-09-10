---
layout: post
title: "[Python] Combining multiple lists into a single list in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Combining multiple lists into a single list is a common operation in Python. It can be done using various approaches, such as using the `extend()` method, the `+` operator, or by converting the lists to sets and back to lists.

In this blog post, we will explore these different methods and provide examples for each.

## 1. Using the `extend()` method

The `extend()` method is used to add individual elements or another list to the end of an existing list. It is a simple and efficient way to combine multiple lists into a single list.

Here's an example:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined_list = list1.copy()  # Create a copy of list1
combined_list.extend(list2)  # Extend the copy with list2
combined_list.extend(list3)  # Extend the copy with list3

print(combined_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In the example above, we create a copy of `list1` using the `copy()` method. Then, we use the `extend()` method to combine `list1`, `list2`, and `list3` into `combined_list`. Finally, we print the result.

## 2. Using the `+` operator

Python provides an overloaded `+` operator that can concatenate two lists. This operator allows us to combine multiple lists into a single list.

Here's an example:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined_list = list1 + list2 + list3

print(combined_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

In the example above, we simply use the `+` operator to concatenate `list1`, `list2`, and `list3` into `combined_list`. This method provides a concise way to combine lists.

## 3. Converting lists to sets

Another approach to combine multiple lists into a single list is by converting the lists to sets and then back to lists. This method eliminates any duplicate elements in the final combined list.

Here's an example:

```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [5, 6, 7]

# Convert lists to sets and use the union operator |
combined_list = list(set(list1) | set(list2) | set(list3))

print(combined_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
```

In the example above, we convert each list to a set using the `set()` function. Then, we use the union operator `|` to combine the sets. Finally, we convert the combined set back to a list using the `list()` function.

These are three different approaches you can use to combine multiple lists into a single list in Python. Choose the method that best suits your needs based on the specific requirements of your project.

Remember to consider the size of the lists and the potential presence of duplicate elements when deciding which method to use.