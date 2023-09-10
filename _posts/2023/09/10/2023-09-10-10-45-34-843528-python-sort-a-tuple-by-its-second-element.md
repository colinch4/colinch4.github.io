---
layout: post
title: "[Python] Sort a Tuple by its Second Element"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Here's an example of how to sort a tuple by its second element:

```python
# Define a tuple
my_tuple = [('apple', 10), ('banana', 5), ('orange', 7), ('kiwi', 3)]

# Sort the tuple by the second element
sorted_tuple = sorted(my_tuple, key=lambda x: x[1])

# Print the sorted tuple
print(sorted_tuple)
```

In this example, we have a tuple `my_tuple` containing a list of fruit names and their corresponding quantities. To sort the tuple based on the second element (quantity), we use the `sorted()` function with a lambda function as the `key` parameter.

The lambda function `lambda x: x[1]` specifies that the sorting should be based on the second element of each tuple. The `x[1]` index retrieves the second element of the tuple `x`.

After sorting, the `sorted()` function returns a new sorted list. In this case, it returns `sorted_tuple`, which will contain the tuples sorted based on their second element.

Finally, we print the `sorted_tuple` to see the sorted result.

The output of the above code will be:

```
[('kiwi', 3), ('banana', 5), ('orange', 7), ('apple', 10)]
```

As you can see, the tuples are sorted based on the second element (quantity), with the lowest quantity appearing first and the highest quantity appearing last.

By using the `sorted()` function along with a lambda function, you can easily sort a tuple based on any specific element or attribute you desire.