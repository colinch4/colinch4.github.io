---
layout: post
title: "Type hints for complex generics in MyPy for Python"
description: " "
date: 2023-09-20
tags: [typing]
comments: true
share: true
---

In Python, type hints allow us to annotate our code with information about the expected data types of variables and function return values. This can improve the readability, maintainability, and correctness of our code. MyPy is a popular static type checker for Python that can analyze our code and report any type errors.

When working with complex data structures, such as lists, dictionaries, or nested types, we may encounter situations where simple type hinting may not be sufficient. In these cases, we can leverage complex generics to provide more precise type information to MyPy.

## List of Tuples Example

Let's say we have a list that contains tuples with a fixed number of elements, and we want to provide type hints for each element of the tuple.

```python
from typing import List, Tuple

# A list of tuples where the first element is a string and the second element is an integer
data: List[Tuple[str, int]] = [("apple", 1), ("banana", 2), ("cherry", 3)]

for item in data:
    fruit: str = item[0]
    quantity: int = item[1]
    print(f"Fruit: {fruit}, Quantity: {quantity}")
```

In the above example, we use `List[Tuple[str, int]]` to specify that `data` is a list of tuples where the first element is a string and the second element is an integer. This provides precise type information to MyPy, allowing it to perform more accurate type checking.

## Dictionary Example

Next, let's consider a dictionary that maps strings to lists of integers.

```python
from typing import Dict, List

# A dictionary with string keys and list of integers as values
grades: Dict[str, List[int]] = {
    "Alice": [90, 95, 80],
    "Bob": [85, 70, 75],
    "Charlie": [95, 90, 92]
}

for student, marks in grades.items():
    total_marks: int = sum(marks)
    average_marks: float = total_marks / len(marks)
    print(f"Student: {student}, Total Marks: {total_marks}, Average Marks: {average_marks}")
```

Here, we utilize `Dict[str, List[int]]` to indicate that `grades` is a dictionary that has string keys and values that are lists of integers. This helps MyPy understand the structure of the data and perform targeted type checking.

## Conclusion

Type hints and static type checking with MyPy can greatly enhance the reliability and maintainability of our Python code. When dealing with complex data structures, we can employ complex generics to provide richer type information to MyPy. This ensures that our code is more self-documenting and helps catch type errors early on during development.

#python #typing