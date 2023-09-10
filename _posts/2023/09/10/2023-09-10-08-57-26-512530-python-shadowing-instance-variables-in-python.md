---
layout: post
title: "[Python] Shadowing instance variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In object-oriented programming, instance variables are attributes that hold values specific to each instance of a class. However, there might be scenarios where we may want to override or shadow an instance variable within a class or its subclass. 

Shadowing an instance variable means creating a new variable with the same name as an existing instance variable, effectively hiding the original variable. This can lead to unexpected behavior if not handled carefully.

Let's explore how shadowing instance variables works in Python and how to deal with it effectively.

## Shadowing instance variables in Python

To shadow an instance variable in Python, we simply create a new variable with the same name within a method or a subclass. When this new variable is accessed, it takes precedence over the original instance variable.

```python
class Car:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print("Original color:", self.color)

    def change_color(self, color):
        self.color = color


class ElectricCar(Car):
    def __init__(self, color, battery_level):
        super().__init__(color)
        self.battery_level = battery_level

    def print_color(self):
        print("Modified color:", self.color)


car = ElectricCar("Blue", 80)
car.print_color()  # Output: Modified color: Blue
```

In the above example, we have a base class `Car` with an instance variable `color`. The `ElectricCar` class is a subclass of `Car` and also has its own instance variable `color`. 

When the `print_color` method is called on an instance of `ElectricCar`, it will print "Modified color" because the method is shadowing the `color` instance variable defined in the base class.

## Avoiding shadowing instance variables

Shadowing instance variables can make code harder to understand and maintain, leading to bugs. To avoid this, it's recommended to use different variable names for instance variables and local variables within a class.

If you need to differentiate between the instance variable and the local variable, you can use the `self` keyword to refer to the instance variable explicitly.

```python
class Car:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        print("Original color:", self.color)

    def change_color(self, color):
        self.color = color


class ElectricCar(Car):
    def __init__(self, color, battery_level):
        super().__init__(color)
        self.battery_level = battery_level

    def print_color(self):
        print("Modified color:", self.color)

    def print_battery_level(self):
        battery_level = 100  # Local variable
        print("Battery level:", battery_level)
        print("Original battery level:", self.battery_level)

car = ElectricCar("Blue", 80)
car.print_color()  # Output: Modified color: Blue
car.print_battery_level()
```

In the updated example, we explicitly refer to the instance variable using `self`, making it clear that we are accessing the instance variable and not a local variable.

## Conclusion

Shadowing instance variables can be a useful technique in certain situations, but it can also lead to confusion and bugs. It's important to be aware of the potential implications and use proper naming conventions to avoid accidental shadowing.

By following good coding practices and naming convention, we can write clean and maintainable code that is less prone to errors.

Happy coding!