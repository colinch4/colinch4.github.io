---
layout: post
title: "Half-Object + Protocol metaclass pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In Python, the **Half-Object + Protocol (HOP) metaclass** pattern is a powerful way to handle object initialization and provide default behavior for methods. This pattern combines the concept of **Half-Object** (an object that has default implementations for some methods) and **Protocol** (a set of methods that an object must implement).

Let's understand this pattern with an example.

## Example Scenario: Building a Vehicle Inventory System

Suppose we are building a vehicle inventory system that can manage different types of vehicles. We want to define a base class `Vehicle` that provides default implementations for common methods like `start_engine` and `stop_engine`. However, we don't want `Vehicle` to be instantiated directly; instead, we want to define subclasses for specific vehicle types (e.g., Car, Truck) that provide the necessary implementations for vehicle-specific methods.

To achieve this, we can apply the HOP metaclass pattern. Here's how it can be implemented in Python:

### Step 1: Define the `Vehicle` Base Class

```python
class Vehicle:
    def __init__(self, color):
        self.color = color

    def start_engine(self):
        raise NotImplementedError("start_engine method not implemented")

    def stop_engine(self):
        raise NotImplementedError("stop_engine method not implemented")

    # Other common methods...
```

In this step, we define the `Vehicle` base class that provides default implementations for `start_engine` and `stop_engine` methods. We raise `NotImplementedError` to indicate that these methods should be implemented by subclasses.

### Step 2: Implement the HOP Metaclass

```python
class HOPMeta(type):
    def __new__(cls, clsname, bases, attrs):
        if not any('start_engine' in base.__dict__ for base in bases):
            attrs['start_engine'] = lambda self: print("Default engine start logic")
        if not any('stop_engine' in base.__dict__ for base in bases):
            attrs['stop_engine'] = lambda self: print("Default engine stop logic")
        return super().__new__(cls, clsname, bases, attrs)
```

Here, we define the `HOPMeta` metaclass. In the `__new__` method, we check if the `start_engine` and `stop_engine` methods already exist in any of the base classes. If not, we dynamically add default implementations for these methods to the class being created.

### Step 3: Create Vehicle Subclasses

```python
class Car(Vehicle, metaclass=HOPMeta):
    def start_engine(self):
        print("Car engine started")

class Truck(Vehicle, metaclass=HOPMeta):
    def start_engine(self):
        print("Truck engine started")
```

In this step, we create `Car` and `Truck` subclasses of `Vehicle` and apply the `HOPMeta` metaclass. We provide specific implementations for `start_engine` method in these subclasses.

### Step 4: Using the Vehicle Subclasses

```python
car = Car("Red")
truck = Truck("Blue")

car.start_engine()  # Output: Car engine started
truck.start_engine()  # Output: Truck engine started

car.stop_engine()  # Output: Default engine stop logic
truck.stop_engine()  # Output: Default engine stop logic
```

Finally, we demonstrate the usage of `Car` and `Truck` subclasses. As we can see, the `start_engine` method uses the specific implementation defined in each subclass, while the `stop_engine` method falls back to the default implementation provided by the `Vehicle` base class.

## Conclusion

The Half-Object + Protocol metaclass pattern in Python allows us to provide default behavior for methods in a base class while still allowing subclasses to provide specific implementations. This pattern helps to enforce a consistent interface across related objects and promotes code reuse. By applying this pattern, we can build flexible and extensible systems in Python.