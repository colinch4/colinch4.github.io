---
layout: post
title: "Layer Supertype pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The **Layer Supertype** pattern is a design pattern used to separate a common set of functionalities or responsibilities of multiple classes into a shared base class. It aims to reduce code duplication and improve maintainability by promoting the reuse of common code.

## Overview of the Layer Supertype Pattern

In object-oriented programming, a layer represents a group of related classes that share similar behavior or responsibilities. The Layer Supertype pattern introduces a common base class for these classes, known as the supertype. This supertype contains the common attributes and methods that are shared among the classes within the layer.

By implementing the Layer Supertype pattern, you can:

- Centralize common code: By moving the common code to a single base class, you reduce code duplication and create a single point of maintenance.
- Simplify future changes: When a change is required in the shared functionalities, modifying the supertype class will automatically reflect the changes in all the classes that inherit from it.
- Improve readability: By having a clear separation of common code, the responsibilities of each class become more apparent.

## Implementation Example in Python

Let's demonstrate the Layer Supertype pattern in Python with a simple example. Suppose we have two classes, `Square` and `Rectangle`, which require a common `calculate_area` method. To avoid duplicated code, we can create a supertype class called `Shape`, which will contain the common code.

```python
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side
```

In the above example, we define the `Shape` class as the supertype, which includes a `calculate_area` method that raises a `NotImplementedError`. This ensures that the subclasses must implement their own `calculate_area` method.

The `Rectangle` and `Square` classes inherit from the `Shape` class and override the `calculate_area` method with their own implementation. This way, the common code for calculating the area is centralized in the `Shape` class, promoting code reuse.

## Conclusion

The Layer Supertype pattern provides a way to extract common functionality from multiple classes into a shared base class. By implementing this pattern, you can reduce code duplication, improve maintainability, and enhance readability in your Python code.