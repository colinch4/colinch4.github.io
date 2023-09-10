---
layout: post
title: "[Python] Constants and immutable variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
<!-- Bold: Python -->
<!-- Italicize: variables -->

In Python, **constants** and **immutable variables** play an important role in maintaining data integrity and reducing unexpected bugs. In this blog post, we'll dive into the concept of constants and immutable variables in the **Python** programming language.

## Constants in Python

Constants are **variables** whose values remain the same throughout the program's execution. They are typically used to represent fixed values that should not be modified. In Python, while there is no explicit way to define constants, a common convention is to write them in **uppercase** with underscores (_) separating words. This convention indicates to other developers that the variable's value should not be changed.

Here's an example of defining a constant in Python:

```python
PI = 3.14159
```

In the code snippet above, `PI` is a constant representing the value of pi. By convention, we use uppercase letters to clearly distinguish it as a constant.

Attempting to modify the value of a constant will raise a `SyntaxError`. For example, the following code will result in an error:

```python
PI = 3.14159
PI = 3.14  # Throws a SyntaxError
```

It's important to note that Python does not enforce immutability for constants. It is up to the programmer to follow the convention and avoid modifying their values.

## Immutable Variables in Python

In Python, some **variables** are **immutable**, meaning their values cannot be changed after assignment. Immutable objects cannot be modified once created, although you can reassign a new value to the variable.

Python provides several built-in types that are immutable, such as **numbers**, **strings**, and **tuples**. When you assign a new value to an immutable variable, Python creates a new object and assigns it to the variable.

Let's look at some examples of immutable variables in Python:

**Numbers:**
```python
x = 5
x = 10  # Reassigning the variable to a new value is allowed
```

**Strings:**
```python
name = "John"
name = "Jane"  # Similarly, reassigning the variable to a new string is allowed
```

**Tuples:**
```python
point = (1, 2)
point = (4, 5)  # Reassigning the variable to a new tuple is allowed
```

On the other hand, **lists** and **dictionaries** are examples of **mutable** objects. Their values can be modified even after assignment.

Understanding the difference between immutable and mutable variables is crucial to avoid unexpected behavior in your Python programs. Immutable variables ensure that the data remains constant and can be safely shared between different parts of your code.

To summarize, constants and immutable variables in Python allow us to establish and maintain fixed values, ensuring data integrity and reducing bugs. It's good practice to follow the naming conventions for constants and be mindful of using immutable objects when appropriate.

I hope this blog post helps you understand the concept of constants and immutable variables in Python! Happy coding!