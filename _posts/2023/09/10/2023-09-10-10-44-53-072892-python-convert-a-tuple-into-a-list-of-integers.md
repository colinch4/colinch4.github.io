---
layout: post
title: "[Python] Convert a Tuple into a List of Integers"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Convert a Tuple into a List of Integers

# Example Tuple
tuple_example = (1, 2, 3, 4, 5)

# Using the `map()` function and `list()` function
list_example = list(map(int, tuple_example))

# Print the converted list
print(list_example)
```

In Python, a tuple is an immutable sequence, meaning its values cannot be changed. However, if you need to perform operations like modifying or iterating over the elements, it can be useful to convert the tuple into a mutable list. 

To convert a tuple into a list of integers, you can use the `map()` function along with the `int()` function. The `map()` function applies the `int()` function to each element of the tuple, and the `list()` function is then used to convert the resulting map object into a list.

In the example code above, we have a tuple `tuple_example` containing integers. We use the `map()` function with the `int()` function to convert each element of the tuple into an integer. Then, we pass the result to the `list()` function to convert the map object into a list. Finally, we print the converted list. 

Running this code will give the following output:
```
[1, 2, 3, 4, 5]
```

Now, you have successfully converted a tuple into a list of integers in Python. This can be useful when you need to perform operations that are only possible with lists, such as sorting, appending, or modifying the elements.