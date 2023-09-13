---
layout: post
title: "Recursive inheritance in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

In object-oriented programming, inheritance allows a class to inherit properties and methods from another class. In Python, it is possible to have recursive inheritance, where a class inherits from itself or one of its subclasses. This can be a powerful technique, but it needs to be used carefully to avoid infinite loops.

## Understanding Recursive Inheritance

Recursive inheritance occurs when a class extends or inherits from itself. This means that a class is both the base class and the derived class at the same time. This concept can be useful in certain scenarios where we want to create a hierarchy of classes that share some common functionality.

## Example of Recursive Inheritance

Let's consider a scenario where we have a base class called `Shape`, and we want to create subclasses for different geometric shapes such as `Circle`, `Rectangle`, and `Triangle`. However, we also want to have a generic `Shape` subclass to represent an abstract shape.

```python
class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")
```

Now, let's say we want to create another class called `CompositeShape` that represents a shape composed of multiple smaller shapes. This `CompositeShape` class can inherit from the `Shape` class recursively.

```python
class CompositeShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def draw(self):
        for shape in self.shapes:
            shape.draw()
```

In this example, the `CompositeShape` class inherits from the `Shape` class and overrides the `draw()` method to iterate over its list of shapes and call the `draw()` method for each shape.

## Avoiding Infinite Loops

When using recursive inheritance, it is important to be cautious to avoid infinite loops. Since a class inherits from itself or its subclass, we need to ensure that there is an exit condition to break the recursion.

In the example above, we have an exit condition in the `Shape` class by raising a `NotImplementedError` if the `draw()` method is called directly on the `Shape` class. This forces subclasses to implement their own `draw()` method, breaking the recursion.

## Conclusion

Recursive inheritance can be a powerful tool in Python for creating class hierarchies. It allows a class to inherit properties and methods from itself or its subclasses. However, it should be used carefully to avoid infinite loops and ensure that there is an exit condition in the recursion.