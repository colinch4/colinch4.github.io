---
layout: post
title: "Instance variables vs class variables in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

## Instance Variables

Instance variables are variables that are unique to each instance of a class. They hold data that is specific to an object and can be accessed and modified using the instance of the class. Instance variables are declared within the constructor method (`__init__()`) and are prefixed with the `self` keyword.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Tesla", "red")
car2 = Car("BMW", "blue")

print(car1.brand)  # output: Tesla
print(car2.color)  # output: blue
```

In the above code, `brand` and `color` are instance variables. Each instance of the `Car` class can have different values for these variables. When we create `car1` and `car2`, we pass different values for `brand` and `color`, and the instance variables are set accordingly.

## Class Variables

Class variables, on the other hand, are variables that are shared among all instances of a class. They are declared outside any method within the class and are prefixed with the class name. Unlike instance variables, class variables are not unique to each object but are shared across all objects of the class.

```python
class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Tesla", "red")
car2 = Car("BMW", "blue")

print(car1.wheels)  # output: 4
print(car2.wheels)  # output: 4

Car.wheels = 5  # Change the value of class variable

print(car1.wheels)  # output: 5
print(car2.wheels)  # output: 5
```

In the above code, the `wheels` variable is declared as a class variable, and its initial value is 4. Both `car1` and `car2` share the same `wheels` value. If we change the value of `wheels` using the class name (`Car.wheels = 5`), it will be reflected in all instances of the class.

## When to use Instance Variables and Class Variables

Understanding when to use instance variables and class variables is crucial for writing efficient and maintainable code.

- Use instance variables when you need different values for each instance of the class. For example, if you have a `Person` class and each person has a unique name and age, you would use instance variables for `name` and `age`.

- Use class variables when you want to share a value among all instances of the class or when the value is constant across all objects. For example, if you have a `Circle` class and want to declare the value of `pi` as a class variable, as it is constant and the same for all circles.

By properly choosing between instance variables and class variables, you can organize your code effectively and ensure that each piece of data is stored in the most appropriate way.

In conclusion, instance variables are unique to each instance of a class, while class variables are shared among all instances. Understanding the differences between the two is crucial for writing clean and efficient object-oriented code in Python.