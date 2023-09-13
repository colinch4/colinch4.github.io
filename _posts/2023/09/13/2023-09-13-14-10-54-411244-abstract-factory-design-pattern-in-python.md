---
layout: post
title: "Abstract factory design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Abstract Factory design pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is useful in scenarios where we want to create different objects that belong to the same family or have similar properties. By using the Abstract Factory pattern, we can dynamically create objects with a common interface.

## Implementation

To implement the Abstract Factory pattern in Python, we can start by defining an abstract factory class that declares the methods for creating different types of objects. Each method in the factory class corresponds to a different product that the factory can create. These methods are usually abstract, meaning they don't have an implementation in the factory class.

```python
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass
```

Next, we can define concrete factory classes that inherit from the abstract factory class and implement the methods to create specific types of products.

```python
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()
```

In this example, we have two concrete factory classes `ConcreteFactory1` and `ConcreteFactory2` that create different implementations of `ProductA` and `ProductB`.

We also need to define the abstract product classes and their concrete implementations. These product classes provide a common interface for the products created by the concrete factories.

```python
class AbstractProductA(ABC):
    @abstractmethod
    def perform_operation(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def perform_operation(self):
        pass

class ProductA1(AbstractProductA):
    def perform_operation(self):
        print("Performing operation from ProductA1")

class ProductA2(AbstractProductA):
    def perform_operation(self):
        print("Performing operation from ProductA2")

class ProductB1(AbstractProductB):
    def perform_operation(self):
        print("Performing operation from ProductB1")

class ProductB2(AbstractProductB):
    def perform_operation(self):
        print("Performing operation from ProductB2")
```

## Usage

To use the Abstract Factory pattern in Python, we can create an instance of a concrete factory and use its methods to create objects of different types.

```python
factory = ConcreteFactory1()

product_a = factory.create_product_a()
product_b = factory.create_product_b()

product_a.perform_operation()  # Output: Performing operation from ProductA1
product_b.perform_operation()  # Output: Performing operation from ProductB1
```

In this example, we use `ConcreteFactory1` to create `ProductA1` and `ProductB1` objects. We can also switch to `ConcreteFactory2` to create `ProductA2` and `ProductB2` objects.

## Conclusion

The Abstract Factory design pattern provides a way to create families of related objects without specifying their concrete classes. It promotes loose coupling and allows for easy interchangeability of objects created by different factories. By using this pattern, we can write code that is more flexible, extensible, and maintainable.