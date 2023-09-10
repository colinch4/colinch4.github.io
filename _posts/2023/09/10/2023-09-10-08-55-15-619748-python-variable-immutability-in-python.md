---
layout: post
title: "[Python] Variable immutability in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, variables can be categorized as either **mutable** or **immutable**. This distinction refers to whether the value of a variable can be changed after it has been assigned. Understanding the concept of variable immutability is crucial for efficient programming in Python.

### Immutable Variables

Immutable variables are those whose value cannot be modified once they are assigned. When you try to modify the value of an immutable variable, a new object is created with the updated value instead.

The following are some examples of immutable variable types in Python:
- **int**: integer values
- **float**: floating-point values
- **str**: string values

```python
# Immutable variables
age = 25
pi = 3.14
name = "John"

# Trying to modify immutable variables
age = 26  # creates a new int object with value 26
pi = 3.14159  # creates a new float object with value 3.14159
name = "John Doe"  # creates a new str object with value "John Doe"
```
In the code snippet above, you can see that when we try to modify the value of our immutable variables, new objects are created with the updated values.

### Mutable Variables

Mutable variables, on the other hand, can have their values modified after they are assigned. Unlike immutable variables, the objects themselves are modified instead of creating new objects.

Some examples of mutable variable types in Python include:
- **list**: ordered collection of items
- **dictionary**: collection of key-value pairs
- **set**: collection of unique items

```python
# Mutable variables
numbers = [1, 2, 3, 4, 5]
student = {"name": "Alice", "age": 20, "grade": "A"}
fruits = {"apple", "banana", "orange"}

# Modifying mutable variables
numbers.append(6)  # modifies the list by adding a new element
student["age"] = 21  # modifies the value associated with the "age" key
fruits.remove("apple")  # modifies the set by removing an item
```
In the code snippet above, you can see that we can modify the values of our mutable variables directly without creating new objects.

### Benefits of Variable Immutability

Understanding the concept of variable immutability can lead to several benefits in your Python programming:
- **Predictability**: Immutable objects ensure that their values can't be accidentally changed, leading to more predictable behavior.
- **Hashability**: Immutable objects can be used as dictionary keys or elements of sets, as their values won't change.
- **Thread-safety**: Immutable objects are inherently thread-safe, as multiple threads can access them without worrying about concurrent modifications.

By leveraging the immutability of variables when appropriate, you can write more reliable and efficient code in Python.

In conclusion, Python provides both mutable and immutable variable types. Immutable variables prevent accidental changes, are hashable, and thread-safe. Understanding the concept of variable immutability helps in writing robust and efficient Python code.