---
layout: post
title: "Static methods and variables in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

### Static Methods
A static method is a method that belongs to the class itself, rather than an instance of the class. It does not have access to the instance or class variables and does not need to be instantiated to be called.

To define a static method in Python, you can use the `@staticmethod` decorator. Here's an example:

```python
class MathUtils:
    @staticmethod
    def add_numbers(a, b):
       return a + b

# Calling the static method without creating an instance of the class
result = MathUtils.add_numbers(5, 10)
print(result)  # Output: 15
```

In the above example, the `add_numbers` method is defined as a static method using the `@staticmethod` decorator. It can be called directly on the class itself without creating an instance of the `MathUtils` class.

### Static Variables
Static variables, also known as class variables, are shared among all instances of a class. They are defined within the class but outside any methods.

To define a static variable in Python, simply declare it inside the class, before any methods. Here's an example:

```python
class Circle:
    pi = 3.14  # Static variable

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.pi * (self.radius ** 2)

# Creating instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(10)

# Accessing the static variable
print(circle1.pi)  # Output: 3.14
print(circle2.pi)  # Output: 3.14

# Calling the instance method that uses the static variable
print(circle1.calculate_area())  # Output: 78.5
print(circle2.calculate_area())  # Output: 314.0
```

In the above example, the `pi` variable is declared as a static variable within the `Circle` class. It can be accessed using either an instance of the class or the class itself. The `calculate_area` method uses the `pi` variable to calculate the area of the circle based on the given radius.

Static methods and variables provide a way to organize and encapsulate functionality that is shared among all instances of a class in Python. They offer flexibility and convenience when you don't need to access instance-specific data or behavior.