---
layout: post
title: "[Python] Summing elements of corresponding indices in two lists in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can easily sum the elements of corresponding indices in two lists by using a combination of `zip()` function and list comprehension.

Here is an example code that demonstrates how to do this:

```python
# Two example lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Summing elements of corresponding indices using zip() and list comprehension
result = [x + y for x, y in zip(list1, list2)]

# Displaying the result
print(result)
```

In the code above, we have two lists: `list1` and `list2`. Each list contains integers. We use the `zip()` function to iterate over the corresponding elements of `list1` and `list2` simultaneously. Then, we use list comprehension to add the elements of the corresponding indices together and create a new list called `result`. Finally, we print the `result` list to see the output.

The output of the above code will be:

```
[6, 8, 10, 12]
```

This indicates that the sum of corresponding elements at index 0 is 6, at index 1 is 8, at index 2 is 10, and at index 3 is 12.

This technique can be useful when you need to perform element-wise operations between two lists of the same length, such as adding or subtracting corresponding elements.

You can also extend this approach to more than two lists. For example, if you have three lists `list1`, `list2`, and `list3`, you can modify the code as follows:

```python
# Three example lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]

# Summing elements of corresponding indices using zip() and list comprehension
result = [x + y + z for x, y, z in zip(list1, list2, list3)]

# Displaying the result
print(result)
```

This will give you the sum of corresponding elements in all three lists.