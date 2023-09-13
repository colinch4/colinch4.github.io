---
layout: post
title: "Data hiding and abstraction in Python"
description: " "
date: 2023-09-13
tags: [datahiding, abstraction]
comments: true
share: true
---

In object-oriented programming, data hiding and abstraction are important concepts that allow developers to encapsulate the implementation details of a class and provide a simplified interface for using and interacting with the class. 

## Data Hiding

Data hiding refers to the practice of hiding the internal state and implementation details of a class from the outside world. It helps in creating a clear separation between the public interface of a class and its internal representation. In Python, data hiding is achieved using name mangling.

### Name Mangling

Name mangling is a technique where attribute names are prefixed with double underscore "__" in order to make them private. This means that these attributes are not directly accessible from outside the class. However, they can still be accessed using a specific syntax. 

Let's take a look at an example:

```python
class MyClass:
    def __init__(self):
        self.__private_attr = "This is a private attribute"

obj = MyClass()
print(obj.__private_attr)  # Raises an AttributeError
```
In the above example, trying to access `__private_attr` outside the class will result in an `AttributeError`. However, the attribute can still be accessed using the mangled name `obj._MyClass__private_attr`.

## Abstraction

Abstraction is the process of defining a class or interface in such a way that it hides the complex details and only exposes the essential features or behavior. It helps in simplifying the interaction with an object by providing a high-level interface that focuses on the "what" rather than the "how". 

In Python, abstraction can be achieved by using abstract base classes (ABCs) provided by the `abc` module.

### Abstract Base Classes

An abstract base class is a class that cannot be instantiated and typically defines an interface for its subclasses. Subclasses of an abstract base class must implement all its abstract methods.

Let's see an example of creating an abstract base class in Python:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")

# Cannot instantiate an abstract class
vehicle = Vehicle()  # Raises a TypeError

car = Car()
car.start()
car.stop()
```

In the above example, `Vehicle` is an abstract base class with two abstract methods: `start` and `stop`. The `Car` class inherits from `Vehicle` and implements these methods. Trying to instantiate `Vehicle` directly will result in a `TypeError`.

By using abstract base classes, we can define a common interface that all subclasses must adhere to, promoting code reusability and allowing for polymorphism.

#datahiding #abstraction