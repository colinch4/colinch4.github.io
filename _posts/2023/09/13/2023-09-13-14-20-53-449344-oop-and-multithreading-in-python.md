---
layout: post
title: "OOP and multithreading in Python"
description: " "
date: 2023-09-13
tags: [multithreading]
comments: true
share: true
---

Python is a versatile programming language widely used for various applications, including object-oriented programming (OOP) and multithreading. In this blog post, we'll explore how Python supports OOP and multithreading and discuss their benefits.

## Object-Oriented Programming (OOP) in Python

OOP is a programming paradigm that organizes code into objects, which are instances of classes. Python fully supports OOP and provides several features that make it easy to implement. Let's look at some key concepts in Python OOP.

### Classes and Objects

In Python, a class is a blueprint for creating objects. It defines the attributes (variables) and methods (functions) that the objects of the class will have. To create an object, we instantiate the class using the `class_name()` syntax.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
      
    def get_details(self):
        return f"{self.make} {self.model}"
      
my_car = Car("Toyota", "Corolla")
print(my_car.get_details())  # Output: Toyota Corolla
```

### Inheritance

Python supports inheritance, allowing classes to inherit attributes and methods from other classes. The `super()` keyword is used to refer to the parent class.

```python
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
      
    def get_details(self):
        return f"{super().get_details()}, {self.battery_capacity} kWh"
      
my_electric_car = ElectricCar("Tesla", "Model S", 75)
print(my_electric_car.get_details())  # Output: Tesla Model S, 75 kWh
```

### Encapsulation

Python allows encapsulation by using access modifiers (`public`, `protected`, and `private`) to control the visibility of attributes and methods.

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self._age = age  # protected attribute
        self.__grade = grade  # private attribute
      
    def __get_grade(self):
        return self.__grade
      
    def display_details(self):
        return f"{self.name}, {self._age}, {self.__get_grade()}"
      
my_student = Student("John", 18, "A")
print(my_student.display_details())  # Output: John, 18, A
```

## Multithreading in Python

Multithreading allows concurrent execution of multiple threads within a single process. It enables efficient utilization of CPU resources and improves the performance of certain applications. Python provides a built-in threading module to support multithreading.

### Creating Threads

To create a new thread, we need to define a function that will be executed concurrently and use the `Thread` class from the `threading` module.

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

def print_letters():
    for letter in "abcdefghij":
        print(letter)
      
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### Synchronization

In multithreaded programs, threads may access shared resources simultaneously, leading to race conditions. Python provides synchronization primitives like locks and semaphores to prevent such conflicts.

```python
import threading

x = 0
lock = threading.Lock()

def increment():
    global x
    for _ in range(100000):
        with lock:
            x += 1
      
def decrement():
    global x
    for _ in range(100000):
        with lock:
            x -= 1
      
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(x)  # Output: 0
```

## Conclusion

Python's support for OOP and multithreading provides developers with powerful tools for building complex and efficient applications. By leveraging the object-oriented paradigm and embracing the benefits of multithreading, Python programmers can design scalable, maintainable, and high-performance systems. #python #OOP #multithreading