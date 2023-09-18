---
layout: post
title: "Builder design pattern in Python"
description: " "
date: 2023-09-13
tags: [DesignPatterns]
comments: true
share: true
---

The Builder design pattern is a creational design pattern that focuses on separating the construction of complex objects from their representation. It allows the same construction process to create different representations.

## Why use the Builder design pattern?

The Builder design pattern is useful in scenarios where an object requires multiple steps and configurations to be constructed. Rather than having a complex constructor or multiple constructors with different parameter combinations, the Builder pattern provides a cleaner solution.

## Implementing the Builder design pattern in Python

To implement the Builder pattern, we'll need to create the following components:

1. **Product**: This represents the final object that is built. It will have various properties and methods.

2. **Builder**: This abstract class defines the different steps required to build the product. Each step is represented by a method in the Builder class.

3. **ConcreteBuilder**: This class inherits from the Builder class and implements the step methods. It keeps track of the product being built and returns the final product when requested.

4. **Director**: This class controls the order in which the step methods are called to construct the product. It takes an instance of the ConcreteBuilder and calls the steps in a specific sequence.

Here's an example implementation of the Builder design pattern in Python:

```python
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None

    def __str__(self):
        return f"Part A: {self.part_a}, Part B: {self.part_b}, Part C: {self.part_c}"


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_b = "Part B"

    def build_part_c(self):
        self.product.part_c = "Part C"

    def get_product(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


# Usage Example
builder = ConcreteBuilder()
director = Director(builder)
director.construct_product()
product = builder.get_product()
print(product)
```

In the above example, we have a Product class that represents the final object being built. The Builder class defines the necessary steps to build the product. The ConcreteBuilder class implements the step methods and returns the final product. The Director class controls the construction by calling the steps in the desired sequence.

## Benefits of the Builder design pattern

- **Separates the construction logic**: The Builder pattern separates the construction logic from the product, allowing for clear separation of concerns.

- **Allows complex object creation**: With the Builder pattern, you can create complex objects step by step, providing flexibility and reusability.

- **Provides control over construction**: The Director class gives more control over the construction process, allowing for different variations of the final product.

## Conclusion

The Builder design pattern is a valuable tool in software development, particularly when dealing with complex object creation. It helps to separate the construction logic and provides a clear and reusable way to build objects. Consider using the Builder pattern when you have objects that require multiple steps and configurations during construction.

#Python #DesignPatterns