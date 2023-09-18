---
layout: post
title: "Classes and objects in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

In Python, **classes** are used to define *blueprints* for creating objects. Objects are *instances* of a class, and they have attributes (variables) and methods (functions) associated with them. This concept is known as **object-oriented programming (OOP)**.

## Creating a Class
To create a class in Python, we use the `class` keyword followed by the class name. By convention, class names are written in **CamelCase**.

```python
class Car:
    pass
```

In the above example, we have defined a simple class called `Car` using the `class` keyword. The `pass` statement is used as a placeholder when there are no attributes or methods defined within the class.

## Creating Objects (Instances)
Once we have a class, we can create objects or instances of that class using the class name followed by parentheses.

```python
my_car = Car()
```

In this example, `my_car` is an object of the `Car` class. We can create multiple objects from the same class, each with its own set of attributes and methods.

## Class Attributes and Instance Attributes
Classes can have **attributes** associated with them. These attributes can be accessed using dot notation.

```python
class Car:
    # Class Attribute
    category = 'Automobile'

my_car = Car()
print(my_car.category)  # Output: Automobile
```

In the above example, `category` is a **class attribute**. It is shared among all instances of the `Car` class.

In addition to class attributes, objects can have **instance attributes** that are specific to each instance of the class. These attributes are defined within the `__init__` method of the class.

```python
class Car:
    # Class Attribute
    category = 'Automobile'
    
    # Instance Attribute
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Tesla", "Model S")
print(my_car.brand)  # Output: Tesla
print(my_car.model)  # Output: Model S
```

In this code snippet, `brand` and `model` are instance attributes. They are unique to each instance created from the `Car` class.

## Class Methods and Instance Methods
Classes can also have **methods** associated with them. Methods are functions defined within a class and are used to perform actions on objects.

```python
class Car:
    # Class Attribute
    category = 'Automobile'
    
    # Instance Attribute
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # Instance Method
    def start_engine(self):
        print("Engine started")

my_car = Car("Tesla", "Model S")
my_car.start_engine()  # Output: Engine started
```

In the above example, `start_engine` is an instance method. It is defined within the class and can be called on any object of that class.

## Conclusion
Classes and objects are fundamental concepts in object-oriented programming. They provide a way to structure and organize code, making it more maintainable and reusable. By understanding classes and objects in Python, you can take advantage of the power of OOP and create robust and scalable applications.