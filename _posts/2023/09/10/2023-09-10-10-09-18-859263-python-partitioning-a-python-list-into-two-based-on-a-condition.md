---
layout: post
title: "[Python] Partitioning a Python list into two based on a condition"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, there may be situations where you need to partition a list into two separate lists based on a specific condition. This can be done using list comprehensions or the `filter()` function. This blog post will explore both approaches and provide examples on how to achieve this task.

## Using List Comprehensions

List comprehensions offer a concise way to create new lists by filtering and transforming existing lists. Here's an example of using list comprehensions to partition a Python list into two based on a condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
```

In the above code snippet, we have a list called `numbers` containing integers from 1 to 10. We use two list comprehensions to create the `even_numbers` and `odd_numbers` lists. The condition `num % 2 == 0` filters out even numbers from the `numbers` list, whereas the condition `num % 2 != 0` filters out odd numbers.

The output of the above code will be:

```
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
```

## Using the filter() Function

The `filter()` function is another way to partition a list based on a condition. It takes two arguments: the filtering condition and the list to apply the filter to. Here's an example of using the `filter()` function:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
```

In the above code, we use the `filter()` function along with a lambda function to specify the filtering condition. The `lambda x: x % 2 == 0` filters out even numbers, whereas `lambda x: x % 2 != 0` filters out odd numbers.

The output of the above code will be the same as the previous example:

```
Even numbers: [2, 4, 6, 8, 10]
Odd numbers: [1, 3, 5, 7, 9]
```

Both the list comprehension and `filter()` approaches achieve the same result. The choice between them depends on personal preference and the specific requirements of your project.

In conclusion, partitioning a Python list into two based on a condition is straightforward using list comprehensions or the `filter()` function. These techniques provide flexibility and allow you to efficiently manipulate lists in Python.