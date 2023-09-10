---
layout: post
title: "[Python] Static variables in Python classes"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, we can define static variables in classes. These variables belong to the class itself rather than any particular instance of the class. Static variables are shared among all instances of the class and can be accessed using the class name.

To define a static variable in Python, we can simply declare a variable outside of any method within a class definition. Let's take a look at an example:

```python
class Car:
    # Static variable
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
```

In the above example, we have a `Car` class with a static variable `wheels` set to `4`. We then create two instances of the `Car` class (`car1` and `car2`). Even though `wheels` is a static variable, we can access it using the instance names `car1` and `car2`.

Static variables can also be accessed using the class name itself. Let's take a look at an example:

```python
class Car:
    # Static variable
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

print(Car.wheels)  # Output: 4
```

In this example, we directly access the static variable `wheels` using the class name `Car`. 

Static variables are useful when you have data that should be shared among all instances of a class. They can be used to store characteristics or properties that should remain constant for every object of that class.

Remember that when a static variable is modified, the change will be reflected in all instances of the class. This behavior should be taken into account when working with static variables in Python.

Overall, static variables provide a way to store shared data within a class and can be accessed using the class name or any instance of the class.