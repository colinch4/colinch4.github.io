---
layout: post
title: "Abstract classes and interfaces in Python"
description: " "
date: 2023-09-13
tags: [Abstraction]
comments: true
share: true
---

Python is a versatile and dynamically-typed programming language that supports object-oriented programming (OOP) concepts. In addition to classes and objects, Python also provides mechanisms for defining abstract classes and interfaces. Abstract classes and interfaces allow developers to define common methods and attributes that can be inherited by other classes. This blog post will explore the concepts of abstract classes and interfaces in Python and how they can be used effectively in your code.

## Abstract Classes

An abstract class in Python is a class that cannot be instantiated but can contain abstract methods. Abstract methods are methods that have no implementation and must be implemented by the derived classes. Abstract classes act as blueprints for concrete classes and provide a common interface for all its subclasses.

To define an abstract class in Python, we need to use the `abc` module (Abstract Base Classes). Let's consider an example:

```python
import abc

class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def talk(self):
        pass
```

In the above example, we have defined an abstract class called `Animal`. The `@abc.abstractmethod` decorator indicates that the `talk` method is an abstract method and should be implemented by any class that inherits from `Animal`. 

To create a concrete class that inherits from the abstract class, we need to provide an implementation for all the abstract methods:

```python
class Dog(Animal):

    def talk(self):
        return "Woof!"
```

In this case, the `Dog` class inherits from the `Animal` class and provides an implementation for the `talk` method.

## Interfaces

Unlike some other programming languages, Python does not have a built-in keyword for interfaces. However, we can achieve similar functionality by using abstract classes and inheriting from multiple abstract classes.

By convention, an interface in Python is identified by a class that contains only abstract methods. Any class that implements all the abstract methods of the interface is considered to implement that interface.

Let's consider an example of how we can define an interface in Python:

```python
import abc

class AnimalInterface(abc.ABC):

    @abc.abstractmethod
    def talk(self):
        pass

    @abc.abstractmethod
    def move(self):
        pass
```

In this example, we have defined an interface called `AnimalInterface`. It contains two abstract methods, `talk` and `move`. Any class that implements both these methods can be considered as implementing the `AnimalInterface`.

```python
class Dog(AnimalInterface):

    def talk(self):
        return "Woof!"

    def move(self):
        return "Running"
```

The `Dog` class in this case implements the `AnimalInterface` by providing implementations for both the `talk` and `move` methods.

## Conclusion

Abstract classes and interfaces are powerful tools in Python to define common behavior that can be inherited by multiple classes. Abstract classes with abstract methods provide a blueprint for derived classes, while interfaces help define the contract that any implementing class must follow. By making use of abstract classes and interfaces, you can write cleaner and more organized code by promoting code reuse and ensuring consistent behavior across classes.

#Python #OOP #Abstraction