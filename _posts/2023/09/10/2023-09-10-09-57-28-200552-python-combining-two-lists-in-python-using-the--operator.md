---
layout: post
title: "[Python] Combining two lists in Python using the '+' operator"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Lists are an essential data structure in Python that allow you to store and manipulate multiple values. Combining two lists can be useful in many scenarios, such as merging data from different sources or creating a single list from multiple smaller ones.

In Python, you can easily combine two lists using the '+' operator. The '+' operator is known as the concatenation operator, and when applied to lists, it merges the elements of the two lists into a new list.

Here's an example to demonstrate how to combine two lists using the '+' operator:

```python
# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine the two lists using the '+' operator
combined_list = list1 + list2

# Print the combined list
print(combined_list)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

In the example above, we have two lists: `list1` and `list2`. We use the '+' operator to combine these two lists and assign the result to the variable `combined_list`. Finally, we print the `combined_list`, which contains all the elements of `list1` followed by all the elements of `list2`.

It's important to note that merging lists using the '+' operator creates a new list and does not modify the original lists.

You can also combine more than two lists by using the '+' operator multiple times. Here's an example:

```python
# Define three lists
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]

# Combine three lists using the '+' operator
combined_list = list1 + list2 + list3

# Print the combined list
print(combined_list)
```

Output:
```
[1, 2, 3, 4, 5, 6]
```

In the example above, we have three lists: `list1`, `list2`, and `list3`. We use the '+' operator to combine these three lists and assign the result to the variable `combined_list`. The resulting list contains all the elements from the three original lists.

In conclusion, combining two or more lists in Python using the '+' operator is a straightforward way to merge their elements into a new list. This can be useful in various scenarios where you need to consolidate data from multiple sources.