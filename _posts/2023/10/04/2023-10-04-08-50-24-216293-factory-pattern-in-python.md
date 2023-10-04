---
layout: post
title: "Factory pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In software development, the **Factory Pattern** is a creational design pattern that provides an interface for creating objects but allows subclasses to decide which class to instantiate. It encapsulates object creation by hiding the logic and details from the client.

## Benefits of using the Factory Pattern

- **Encapsulation**: The client code does not need to know the specific class of the object it is creating. It only needs to use the factory method to create the object.
- **Flexible**: It allows easy extensibility by adding new product classes without modifying the client code.
- **Decoupling**: It decouples the client code from the concrete implementation of the object, providing loose coupling and better maintainability.

## Example: Shape Factory

Let's consider a simple example of a shape factory that can create different types of shapes. We'll demonstrate how the factory pattern can be implemented in Python.

```python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Usage
shape_factory = ShapeFactory()
circle = shape_factory.create_shape("circle")
circle.draw()  # Output: "Drawing a circle"

rectangle = shape_factory.create_shape("rectangle")
rectangle.draw()  # Output: "Drawing a rectangle"

square = shape_factory.create_shape("square")
square.draw()  # Output: "Drawing a square"
```

In the above example, we have an abstract `Shape` class that defines the `draw` method. We have three concrete shape classes: `Circle`, `Rectangle`, and `Square`, which implement the `draw` method. 

The `ShapeFactory` class acts as the factory and provides a `create_shape` method that takes a `shape_type` parameter and returns the appropriate shape object based on the type.

By using the factory pattern, the client code can create different types of shapes without knowing the specific implementation details. This allows for easy extensibility if new shape classes are added in the future.

## Conclusion

The Factory Pattern is a useful design pattern that provides a way to create objects without exposing the creation logic to the client code. It promotes encapsulation, flexibility, and decoupling of the client code from concrete implementations. In Python, using the Factory Pattern can enhance the maintainability and extensibility of your codebase.