---
layout: post
title: "Bridge design pattern in Python"
description: " "
date: 2023-09-13
tags: [Bridge, DesignPattern, Python]
comments: true
share: true
---

The **Bridge design pattern** is a structural design pattern that decouples an abstraction from its implementation, allowing them to vary independently. This pattern is useful when there are multiple dimensions in an application that can vary independently, and we want to avoid a situation where a large number of classes are created to handle all possible combinations.

## Implementation

To explain the Bridge design pattern, let's consider an example where we have a **Shape** hierarchy which has various subclasses like **Circle** and **Square**. Additionally, there are different rendering options available, such as **RasterRenderer** and **VectorRenderer**. Without using the Bridge pattern, we would end up with multiple classes for each combination (CircleRasterRenderer, CircleVectorRenderer, SquareRasterRenderer, etc.), which could quickly become unmanageable.

To solve this problem, we can utilize the Bridge design pattern. We'll define an **AbstractRenderer** interface that all rendering classes will implement. Then, we'll create a **Shape** class that maintains a reference to an **AbstractRenderer** object, allowing the shape to be rendered with different renderers without the need for subclassing.

Let's see the implementation in Python:

```python
class AbstractRenderer:
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass

class RasterRenderer(AbstractRenderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using raster renderer.")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using raster renderer.")

class VectorRenderer(AbstractRenderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vector renderer.")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using vector renderer.")

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)
```

## Usage

Now, let's see how we can use the Bridge design pattern to draw different shapes using different renderers:

```python
raster_renderer = RasterRenderer()
vector_renderer = VectorRenderer()

circle = Circle(raster_renderer, 5)
circle.draw()  # Output: "Drawing a circle with radius 5 using raster renderer."

square = Square(vector_renderer, 10)
square.draw()  # Output: "Drawing a square with side 10 using vector renderer."
```

By using the Bridge design pattern, we can easily switch between different renderers without modifying the shape classes. This promotes code flexibility and reduces the need for excessive subclassing.

## Conclusion

The Bridge design pattern in Python allows us to separate the abstraction from its implementation. It provides a way to handle multiple dimensions of an application independently and avoids an explosion of subclasses. By decoupling the abstraction and implementation, we can easily add new dimensions or modify existing ones without affecting the other. The Bridge pattern promotes loose coupling, which leads to more flexible and maintainable code.

#Bridge #DesignPattern #Python