---
layout: post
title: "Class attributes and methods in Python"
description: " "
date: 2023-09-13
tags: [programming]
comments: true
share: true
---

In Python, classes are used to define objects with specific attributes and behaviors. These attributes and behaviors can be defined as either instance attributes/methods or class attributes/methods. Class attributes and methods are shared among all instances of the class and can be accessed without creating an instance of the class.

## Class Attributes

Class attributes are variables that are shared by all instances of a class. They are defined within the class but outside of any methods. Class attributes are accessed using the class name followed by the attribute name.

```python
class Car:
    # Class attribute
    manufacturer = "Toyota"

    def __init__(self, model):
        self.model = model

car1 = Car("Corolla")
car2 = Car("Camry")

print(car1.manufacturer)  # Output: Toyota
print(car2.manufacturer)  # Output: Toyota
```

In the above example, the `manufacturer` attribute is a class attribute because it is defined outside of any methods. It is shared by all instances of the `Car` class.

## Class Methods

Class methods are methods that are bound to the class and not the instances of the class. They are defined using the `@classmethod` decorator and have the first parameter as the class itself, conventionally named as `cls`. Class methods can access and modify class attributes but not instance attributes.

```python
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

dog1 = Dog("Max")
dog2 = Dog("Bella")

print(Dog.get_species())  # Output: Canine
print(dog1.get_species())  # Output: Canine
print(dog2.get_species())  # Output: Canine
```

In the above example, the `get_species` method is a class method as it is decorated with `@classmethod`. It can be called both from the class itself and from instances of the class.

## Conclusion

Understanding class attributes and methods in Python allows you to define shared properties and behaviors among all instances of a class. Class attributes are variables shared by all instances, while class methods are methods bound to the class itself. They provide flexibility and extensibility to your Python classes. #python #programming