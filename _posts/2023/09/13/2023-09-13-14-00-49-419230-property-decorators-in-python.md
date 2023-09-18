---
layout: post
title: "Property decorators in Python"
description: " "
date: 2023-09-13
tags: [properties]
comments: true
share: true
---

In Python, property decorators provide a convenient way to define and manage properties of a class. Properties allow us to define getter and setter methods for accessing and modifying class attributes.

## Defining a Property

To define a property using decorators, we can use the `@property` decorator above the method that will act as the getter for the property. Here's an example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2
```

In the code above, we have defined a `Circle` class with a `radius` attribute. We have also defined a getter method called `area` using the `@property` decorator. This method calculates and returns the area of the circle using the formula `3.14 * radius**2`.

## Accessing the Property

To access the property, we can simply use it as if it were a regular attribute of the class:

```python
my_circle = Circle(5)
print(my_circle.area)  # Output: 78.5
```

In the example above, we create an instance of the `Circle` class with a radius of 5. We then access the `area` property which calls the getter method and retrieves the calculated area of the circle.

## Modifying the Property

To modify the property, we can define a setter method that is decorated with `@propertyname.setter`. Let's extend our `Circle` class to include a setter method for the `radius` property:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2

    @area.setter
    def area(self, new_radius):
        self.radius = new_radius
```

In the updated code, we added a `@area.setter` decorator above the `area` method. This method takes in a new radius value and updates the `radius` attribute of the class.

## Using the Setter Method

Now we can use the setter method to modify the `radius` attribute and automatically update the calculated area:

```python
my_circle = Circle(5)
print(my_circle.area)  # Output: 78.5

my_circle.area = 7
print(my_circle.area)  # Output: 153.86
```

In the code above, we first create an instance of the `Circle` class with a radius of 5. We then access the `area` property to get the calculated area. Next, we set the `area` property to 7, and when we retrieve the `area` property again, it automatically recalculates and returns the updated area.

## Conclusion

Property decorators in Python provide a powerful tool for defining and managing properties of a class. They allow us to create getter and setter methods that provide controlled access to class attributes. By using property decorators, we can encapsulate the logic and ensure consistent behavior when accessing and modifying properties in our code.

#python #properties