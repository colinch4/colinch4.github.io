---
layout: post
title: "[Python] Finding the sum of elements in a Python list"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can easily find the sum of elements in a list using the `sum()` function. The `sum()` function takes an iterable as its argument and returns the sum of all the elements in that iterable.

Here's an example of how you can use the `sum()` function to find the sum of elements in a Python list:

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("The sum of elements in the list is:", total)
```

Output:
```
The sum of elements in the list is: 15
```

In this example, we have a list of numbers `[1, 2, 3, 4, 5]`. We pass this list as an argument to the `sum()` function, which calculates the sum of all the elements in the list. The result is then stored in the `total` variable.

Finally, we use the `print()` function to display the result, which in this case is `15`, as the sum of all the numbers in the list.

You can also use the `sum()` function on other iterables such as tuples or sets. For example:

```python
numbers = (1, 2, 3, 4, 5)
total = sum(numbers)
print("The sum of elements in the tuple is:", total)

numbers_set = {1, 2, 3, 4, 5}
total = sum(numbers_set)
print("The sum of elements in the set is:", total)
```

Output:
```
The sum of elements in the tuple is: 15
The sum of elements in the set is: 15
```

As you can see, the `sum()` function can be used to find the sum of elements in various types of iterables, making it a convenient tool in Python for performing summation operations.