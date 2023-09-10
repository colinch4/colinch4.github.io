---
layout: post
title: "[Python] Class variables vs instance variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Class Variables

Class variables are shared among all instances of a class. They are defined within the class, but outside any methods or constructors. Class variables are accessed using the class name and can be modified globally.

```python
class Car:
    wheels = 4  # This is a class variable

    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable
```

As shown in the example above, the `wheels` variable is a class variable. It is shared by all instances of the `Car` class. If we were to create multiple instances of the `Car` class, they would all have access to the same `wheels` value.

```python
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

Car.wheels = 6

print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6
```

Modifying the class variable `wheels` will affect all instances of the class. It is important to note that if we modify the value of the class variable using an instance, it creates a new instance variable with the same name that shadows the class variable.

```python
car1.wheels = 5

print(car1.wheels)  # Output: 5
print(car2.wheels)  # Output: 6
```

In the above example, `car1.wheels` creates a new instance variable `wheels` for the `car1` instance. `car2.wheels` still refers to the class variable `wheels`, as it has not been modified.

## Instance Variables

Instance variables are unique to each instance of a class. They are defined within the class's methods, typically in the `__init__` constructor method. Instance variables belong to the specific object instance and are accessed using the `self` keyword.

```python
class Car:
    def __init__(self, make, model):
        self.make = make  # Instance variable
        self.model = model  # Instance variable
```

In the example above, `make` and `model` are instance variables. Each instance of the `Car` class will have its own unique values for these variables.

```python
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.make)  # Output: Toyota
print(car2.make)  # Output: Honda
```

Instance variables are specific to the instance they belong to. Modifying the value of an instance variable for one instance doesn't affect the value of the same variable for other instances.

```python
car1.make = "Ford"

print(car1.make)  # Output: Ford
print(car2.make)  # Output: Honda
```

In the above example, `car1.make` is modified to "Ford," but `car2.make` remains unchanged.

## Conclusion

Understanding the difference between class variables and instance variables is important when designing classes in Python. Class variables are shared among all instances of a class and can be modified globally. Instance variables are unique to each instance and belong to that specific object instance. Both types of variables have their own use cases and play a significant role in object-oriented programming.