---
layout: post
title: "Builder pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Builder pattern is a creational design pattern that allows you to construct complex objects step by step. It provides a way to create an object using a builder class, which is responsible for creating the product object and setting its properties.

## Why use the Builder pattern?

The Builder pattern is useful in situations where you need to create an object that requires a complex initialization process. It helps to separate the construction of an object from its representation, making the code cleaner and easier to maintain. It also allows you to build different variations of an object using the same construction process.

## Implementation in Python

To implement the Builder pattern in Python, you can create a builder class that encapsulates the construction logic. Here's an example implementation of the Builder pattern using Python:

```python
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.processor = processor
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card
        return self

    def build(self):
        return self.computer


class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None

    def __str__(self):
        return f"Processor: {self.processor}, Memory: {self.memory}, Storage: {self.storage}, Graphics Card: {self.graphics_card}"
```

In this example, we have a `ComputerBuilder` class that allows us to set different properties of the `Computer` object. The `Computer` class represents the product that we want to build. The `ComputerBuilder` class has methods to set each property of the `Computer` object and returns `self` to enable method chaining.

To use the Builder pattern to construct a `Computer` object, you can follow the following steps:

```python
builder = ComputerBuilder()
computer = builder.set_processor("Intel Core i7").set_memory("16GB").set_storage("1TB SSD").set_graphics_card("NVIDIA GeForce RTX 3070").build()
print(computer)
```

Output:
```
Processor: Intel Core i7, Memory: 16GB, Storage: 1TB SSD, Graphics Card: NVIDIA GeForce RTX 3070
```

In this example, we create a `ComputerBuilder` instance and use its methods to set the different properties of the `Computer` object. Finally, we call the `build` method to get the constructed `Computer` object.

## Summary

The Builder pattern is a useful design pattern for creating complex objects step by step. It helps separate the construction process from the final object representation, making the code more modular and easier to maintain. In Python, you can implement the Builder pattern by creating a builder class that encapsulates the construction logic and provides methods for setting the properties of the object being built.