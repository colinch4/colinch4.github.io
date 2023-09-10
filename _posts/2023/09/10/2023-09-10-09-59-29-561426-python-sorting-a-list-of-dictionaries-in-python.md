---
layout: post
title: "[Python] Sorting a list of dictionaries in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Sorting a list of dictionaries based on a key

Let's assume we have a list of dictionaries representing employees, and we want to sort this list based on the employees' names. Here's an example list:

```python
employees = [
    {'name': 'John', 'age': 35, 'salary': 50000},
    {'name': 'Alice', 'age': 28, 'salary': 45000},
    {'name': 'Bob', 'age': 42, 'salary': 60000},
    {'name': 'Megan', 'age': 31, 'salary': 55000}
]
```

To sort this list based on the `name` key, we can use the `sorted()` function with a lambda function as the `key` parameter:

```python
sorted_employees = sorted(employees, key=lambda emp: emp['name'])
print(sorted_employees)
```

Output:

```plaintext
[{'name': 'Alice', 'age': 28, 'salary': 45000},
 {'name': 'Bob', 'age': 42, 'salary': 60000},
 {'name': 'John', 'age': 35, 'salary': 50000},
 {'name': 'Megan', 'age': 31, 'salary': 55000}]
```

In this example, the lambda function `key=lambda emp: emp['name']` is used to specify that the sorting should be based on the `name` key of each dictionary. The `sorted()` function returns a new sorted list while leaving the original list unchanged.

## Sorting in descending order

By default, `sorted()` sorts in ascending order. If we want to sort the list in descending order based on the `name` key, we can use additional parameters in the `sorted()` function:

```python
sorted_employees_desc = sorted(employees, key=lambda emp: emp['name'], reverse=True)
print(sorted_employees_desc)
```

Output:

```plaintext
[{'name': 'Megan', 'age': 31, 'salary': 55000},
 {'name': 'John', 'age': 35, 'salary': 50000},
 {'name': 'Bob', 'age': 42, 'salary': 60000},
 {'name': 'Alice', 'age': 28, 'salary': 45000}]
```

Here, the `reverse=True` parameter is used to sort the list in descending order.

## Sorting based on multiple keys

Sometimes, we need to sort the list based on multiple keys. For example, let's say we want to sort the employees first by their salaries and then by their ages. We can achieve this by providing a tuple as the `key` parameter:

```python
sorted_employees_multi = sorted(employees, key=lambda emp: (emp['salary'], emp['age']))
print(sorted_employees_multi)
```

Output:

```plaintext
[{'name': 'Alice', 'age': 28, 'salary': 45000},
 {'name': 'John', 'age': 35, 'salary': 50000},
 {'name': 'Megan', 'age': 31, 'salary': 55000},
 {'name': 'Bob', 'age': 42, 'salary': 60000}]
```

In this example, the `sorted()` function sorts the list first by the `salary` key and then by the `age` key.

## Conclusion

In this blog post, we explored different ways to sort a list of dictionaries in Python based on specified keys. The `sorted()` function in combination with the `key` parameter allows us to easily sort the list based on single or multiple keys. Sorting lists of dictionaries in Python is a powerful technique that can be used in a variety of scenarios and make our code more efficient and organized.