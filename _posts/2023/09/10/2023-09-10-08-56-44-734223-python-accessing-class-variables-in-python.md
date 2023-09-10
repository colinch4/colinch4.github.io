---
layout: post
title: "[Python] Accessing class variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, class variables are variables that are shared among all instances of a class. They are defined within the class definition, but outside of any methods or constructors. Class variables can be accessed by all the objects created from the class, including both instance methods and class methods.

Here's an example to demonstrate how to access class variables in Python:

```python
class Car:
    # class variable
    top_speed = 200
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def drive(self):
        # accessing class variable within an instance method
        print(f"The {self.make} {self.model} is driving at {Car.top_speed} mph.")
        
    @classmethod
    def set_top_speed(cls, speed):
        # accessing class variable within a class method
        cls.top_speed = speed
        
    @staticmethod
    def beep():
        # accessing class variable within a static method
        print(f"Beep beep! The top speed is {Car.top_speed} mph.")
        

# create instances of Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

# access class variable using object instance
print(car1.top_speed)  # Output: 200
print(car2.top_speed)  # Output: 200

# access class variable using class name
print(Car.top_speed)   # Output: 200

# change the class variable using class method
Car.set_top_speed(250)

# accessing class variable within an instance method
car1.drive()  # Output: The Toyota Camry is driving at 250 mph.
car2.drive()  # Output: The Honda Accord is driving at 250 mph.

# accessing class variable within a static method
Car.beep()    # Output: Beep beep! The top speed is 250 mph.
```

In the above example, the `top_speed` is a class variable that is shared by all instances of the `Car` class. We can access this variable both through the object instances and through the class name itself.

We can also modify the value of the class variable using a class method, as demonstrated in the `set_top_speed` method. Changes made to the class variable using a class method will affect all instances created from the class.

Moreover, we can access the class variable within instance methods, as shown in the `drive` method, and within static methods, as shown in the `beep` method.

Remember that class variables should be used when you want to share data among all instances of a class. If you need variables that are specific to each instance, you should use instance variables.