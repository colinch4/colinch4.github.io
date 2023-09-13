---
layout: post
title: "Access specifiers in Python"
description: " "
date: 2023-09-13
tags: [python]
comments: true
share: true
---

Access specifiers in programming languages determine the level of access or visibility to class members (variables and methods) from different parts of the program. Python doesn't have explicit access specifiers like public, private, or protected, as seen in some other object-oriented programming languages. However, Python provides a convention to achieve similar behavior using naming conventions.

## Public Access

In Python, by convention, all class members are **public** by default. This means that they can be accessed from anywhere, both inside and outside the class. Public members are not prefixed with any special characters or keywords to indicate their visibility. For example, let's declare a class with a public member:

```python
class MyClass:
    def __init__(self):
        self.public_var = 10

my_obj = MyClass()
print(my_obj.public_var)  # Output: 10
```

In the code above, `public_var` is a public variable, so it can be accessed using the `my_obj` object from outside the class.

## Private Access

Even though Python doesn't have private access like other languages, it uses a naming convention to indicate a variable or method as **private**. By convention, a private member's name starts with a single underscore `_`. However, private members can still be accessed from outside the class, but it is considered bad practice.

```python
class MyClass:
    def __init__(self):
        self._private_var = 20

    def _private_method(self):
        return "This is a private method"

my_obj = MyClass()
print(my_obj._private_var)  # Output: 20
print(my_obj._private_method())  # Output: This is a private method
```

In the above code, `_private_var` and `_private_method` are considered private, but they can still be accessed directly. It's important to note that the leading underscore `_` is more of a convention to indicate the intended visibility and serve as a reminder to not access them directly.

## Protected Access

Python doesn't have a true protected access specifier like some other languages. However, it uses a naming convention to indicate a variable or method as **protected**. According to convention, a protected member's name starts with a single underscore `_`, but it is also accessible outside the class.

```python
class MyClass:
    def __init__(self):
        self._protected_var = 30

    def _protected_method(self):
        return "This is a protected method"

my_obj = MyClass()
print(my_obj._protected_var)  # Output: 30
print(my_obj._protected_method())  # Output: This is a protected method
```

In the above code, `_protected_var` and `_protected_method` are considered protected, but they can still be accessed directly. Again, the leading underscore `_` serves as a convention to indicate the intended visibility.

## Usage Guidelines

While Python provides the above naming conventions for achieving access specifiers, it's essential to understand the guidelines for accessing these members:

1. **Public members** can be accessed from anywhere in the program without restrictions.
2. **Private members** are conventionally considered non-public, but they can still be accessed directly. It's best to treat them as if they were private and avoid accessing them from outside the class.
3. **Protected members** are also conventionally considered non-public, but they are accessible outside the class. However, it is generally suggested to treat them as if they were private and refrain from direct access outside the class.

Following these guidelines helps maintain clean and encapsulated code, promoting better code organization and reducing potential dependencies and bugs.

In conclusion, Python's access specifiers are achieved through naming conventions rather than explicit keywords. While public members are straightforward, private and protected members are denoted by a leading underscore `_`, with the understanding that direct access should be avoided. Adhering to these conventions promotes code readability and encapsulation while maintaining flexibility.