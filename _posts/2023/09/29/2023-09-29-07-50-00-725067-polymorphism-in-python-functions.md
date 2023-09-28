---
layout: post
title: "Polymorphism in Python functions"
description: " "
date: 2023-09-29
tags: [techblog, python]
comments: true
share: true
---

Polymorphism is one of the fundamental concepts in object-oriented programming. It allows you to use a single interface to represent different data types or objects. In Python, polymorphism is implemented through function overloading and function overriding.

## Function Overloading
Function overloading refers to defining multiple functions with the same name but with different parameters or different combinations of parameters. Python does not support function overloading out of the box, but you can achieve similar behavior using default arguments or by using the `*args` and `**kwargs` parameters.

Here's an example of function overloading using default arguments:

```python
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))      # Output: 5
print(add(2, 3, 4))   # Output: 9
```

In this example, the `add()` function is defined with two parameters `x` and `y`, and an optional parameter `z` with a default value of 0. You can call the function with two or three arguments, and the behavior will change accordingly.

## Function Overriding
Function overriding occurs when a derived class defines a method with the same name as a method in its base class. The derived class can provide a different implementation for the method.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
```

In this example, the `Shape` class is a base class, and the `Rectangle` and `Circle` classes are derived classes. Each derived class overrides the `area()` method inherited from the `Shape` class with its own implementation.

```python
rectangle = Rectangle(5, 4)
circle = Circle(3)

print(rectangle.area())   # Output: 20
print(circle.area())      # Output: 28.26
```

Here, calling the `area()` method on an instance of `Rectangle` or `Circle` will return the area specific to that shape.

## Conclusion
Polymorphism in Python functions allows you to write more flexible and reusable code by providing different behaviors based on the input. You can achieve polymorphism through function overloading and function overriding, allowing you to work with different data types or objects using a common interface.

#techblog #python