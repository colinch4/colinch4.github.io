---
layout: post
title: "[Python] Tuple as Dictionary Keys"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, dictionaries are a powerful data structure that allows us to store key-value pairs. The keys in a dictionary are typically **immutable** data types like strings or numbers. However, there are cases where we might want to use a **tuple** as a dictionary key.

A tuple is an ordered collection of elements, enclosed in parentheses and separated by commas. Unlike lists, tuples are **immutable**, which means they cannot be modified after they are created.

Let's look at an example of how we can use a tuple as a dictionary key:

```python
# Create a dictionary with tuples as keys and their corresponding values
student_scores = {('John', 'Doe'): 85, ('Jane', 'Smith'): 92, ('Mike', 'Johnson'): 78}

# Accessing values using tuple keys
score1 = student_scores[('John', 'Doe')]
score2 = student_scores[('Jane', 'Smith')]

print(score1)  # Output: 85
print(score2)  # Output: 92
```

In the example above, we have created a dictionary called `student_scores` where the keys are tuples representing the names of the students. Each tuple key is associated with a corresponding score.

To access the values in the dictionary, we use the tuple keys inside the square brackets `[]`. We can access the values just like we would with any other dictionary using string or number keys.

Using tuples as dictionary keys can be useful in situations where we need to uniquely identify an element based on multiple values. For example, in a student database, we can use a tuple of first name and last name as a key to store and retrieve student information efficiently.

It is important to remember that the elements of the tuple used as a key must be **hashable**. Mutable objects like lists cannot be used as dictionary keys since they can be modified, which would break the hashability requirement.

In conclusion, using tuples as dictionary keys allows us to store and access values based on multiple values efficiently. This can be handy when we need to uniquely identify elements in complex data structures.

I hope this article helps you understand how to use tuples as dictionary keys in Python. Happy coding!