---
layout: post
title: "[Python] Classes and objects in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Python is an object-oriented programming language, which means it supports the concept of **classes** and **objects**. Classes are blueprint or templates for creating objects, while objects are instances of those classes.

## Creating a Class

To create a class in Python, you can use the `class` keyword, followed by the name of the class. Class names, by convention, should start with a capital letter.

```python
class Car:
    pass
```

The `pass` keyword is used as a placeholder for empty classes. You can define attributes and methods inside the class to give it functionality.

## Creating Objects

To create an object of a class, you can simply call the class name as if it were a function. This process is called **instantiation**.

```python
my_car = Car()
```

By doing this, `my_car` becomes an instance of the `Car` class. Now you can access the attributes and methods of the class through this object.

## Class Attributes and Instance Attributes

Attributes are variables that hold data associated with a class or an instance of a class. There are two types of attributes in Python: class attributes and instance attributes.

**Class attributes** are shared by all instances of a class. They are defined inside the class but outside any methods.

```python
class Car:
    # Class attribute
    wheels = 4
```

You can access class attributes using the class name or any instance of the class.

```python
print(Car.wheels)  # Output: 4
print(my_car.wheels)  # Output: 4
```

**Instance attributes** are unique to each instance of a class. They are defined inside the `__init__` method of the class. This method is called when an object is created.

```python
class Car:
    def __init__(self, color):
        self.color = color
```

You can pass arguments to the `__init__` method when creating an object to initialize its instance attributes.

```python
my_car = Car("blue")
print(my_car.color)  # Output: blue
```

## Class Methods and Instance Methods

Methods are functions associated with a class or an instance of a class. Like attributes, there are class methods and instance methods.

**Class methods** are defined using the `@classmethod` decorator and take the class itself as the first argument. They can access and modify class attributes but not instance attributes.

```python
class Car:
    @classmethod
    def get_wheels(cls):
        return cls.wheels
```

You can call a class method using the class name or any instance of the class.

```python
print(Car.get_wheels())  # Output: 4
print(my_car.get_wheels())  # Output: 4
```

**Instance methods** are defined without decorators and take the instance itself as the first argument. They can access and modify both class attributes and instance attributes.

```python
class Car:
    def __init__(self, color):
        self.color = color

    def honk(self):
        print("Beep beep!")
```

You can call an instance method using any instance of the class.

```python
my_car = Car("blue")
my_car.honk()  # Output: Beep beep!
```

## Conclusion

Classes and objects are fundamental concepts in object-oriented programming, and Python provides a clean and simple syntax to work with them. By understanding how to create classes, objects, attributes, and methods, you can build powerful and modular code in Python.