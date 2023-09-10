---
layout: post
title: "[Python] Checking the length of a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

### Using the `len()` function

The most common and straightforward way to check the length of a Python list is by using the built-in `len()` function. This function returns the number of items present in the list.

Here's an example of how to use the `len()` function to determine the length of a list:

```python
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(f"The length of the list is {length}")
```

Output:
```
The length of the list is 5
```

### Using the `__len__` method

In Python, the `len()` function actually calls the `__len__` method of an object internally. So, you can directly use the `__len__` method to get the length of a list, bypassing the function call. This method returns the same result as the `len()` function.

Here's an example of how to use the `__len__` method to check the length of a list:

```python
my_list = [1, 2, 3, 4, 5]
length = my_list.__len__()
print(f"The length of the list is {length}")
```

Output:
```
The length of the list is 5
```

### Conclusion

These are the two common ways to determine the length of a Python list. Both the `len()` function and the `__len__` method are efficient and give you the same result. Choose the one that you find more readable and cohesive with your code style.

Remember, understanding the length of a list can be crucial when performing various operations or iterating through its elements.