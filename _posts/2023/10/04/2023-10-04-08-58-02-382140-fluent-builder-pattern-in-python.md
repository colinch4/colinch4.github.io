---
layout: post
title: "Fluent Builder pattern in Python"
description: " "
date: 2023-10-04
tags: [designpattern]
comments: true
share: true
---

In object-oriented programming, the builder pattern is a creational design pattern that allows an object to be constructed in a step-by-step manner. It separates the construction of an object from its representation, enabling the same construction process to create different representations.

A fluent builder pattern is a variation of the traditional builder pattern, where the builder methods are chained together in a more readable and expressive way.

Let's see an example of how to implement a fluent builder pattern in Python.

## Step 1: Define the Product Class

First, we need to define the class that we want to build using the fluent builder pattern. For the sake of this example, let's consider a `Car` class with properties like `make`, `model`, `year`, `color`, etc.

```python
class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
```

## Step 2: Implement the Builder Class

Next, we need to implement the builder class that constructs the `Car` object step by step. The builder class will have methods for setting the car's properties and a final `build` method that returns the constructed car object.

```python
class CarBuilder:
    def __init__(self):
        self.car = Car()
    
    def set_make(self, make):
        self.car.make = make
        return self
    
    def set_model(self, model):
        self.car.model = model
        return self
    
    def set_year(self, year):
        self.car.year = year
        return self
    
    def set_color(self, color):
        self.car.color = color
        return self
    
    def build(self):
        return self.car
```

## Step 3: Using the Fluent Builder Pattern

Now, let's see how we can use the fluent builder pattern to create a car object.

```python
car = CarBuilder().set_make("Tesla").set_model("Model S").set_year(2021).set_color("Red").build()
```

Here, we chain the builder methods to set the car's properties one by one, and finally, call the `build` method to get the constructed `Car` object.

Using the fluent builder pattern, we can easily create a car object with a concise and readable syntax.

## Conclusion

The fluent builder pattern is a useful variation of the traditional builder pattern that allows for more readable and expressive code. It separates the construction of an object from its representation and provides a step-by-step approach to build objects. By using method chaining, the fluent builder pattern can make code more concise and easier to understand.

#python #designpattern