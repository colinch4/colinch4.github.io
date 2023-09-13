---
layout: post
title: "Getter and setter methods in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

In object-oriented programming, getter and setter methods are used to access and modify the private instance variables of a class. By encapsulating the variables and providing controlled access to them, we can ensure data integrity and maintain the principle of data hiding.

## What are Getter and Setter methods?

Getter methods, also known as accessor methods, are used to retrieve the value of a private instance variable. They provide indirect access to the private variable and allow us to retrieve its value from outside the class.

Setter methods, also known as mutator methods, are used to modify the value of a private instance variable. They provide a controlled way to modify the private variable while ensuring data integrity and executing any necessary validation logic.

## How to define Getter and Setter methods?

In Python, we can define getter and setter methods by using the `@property` decorator for the getter method and the `@<variable_name>.setter` decorator for the setter method.

Here's an example that demonstrates how to define getter and setter methods in Python:

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private instance variable with underscore prefix
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty.")
```

In the above example, we have a `Person` class with a private instance variable `_name`. The getter method `name` retrieves the value of `_name`, and the setter method `name` sets the new value while checking for any conditions or validations.

## Accessing Getter and Setter methods

Once the getter and setter methods are defined, we can access them just like normal attributes of the class. 

```python
person = Person("John Doe")
print(person.name)  # Output: John Doe

person.name = "Jane Doe"
print(person.name)  # Output: Jane Doe
```

In the above code, we create an instance of the `Person` class and access the `name` attribute using the getter method. We can also modify the `name` attribute by assigning a new value to it using the setter method.

## Conclusion

Getter and setter methods provide a controlled and encapsulated way to access and modify the private instance variables of a class. They ensure data integrity and allow us to execute any necessary validation logic. By using the `@property` and `@<variable_name>.setter` decorators, we can easily define getter and setter methods in Python.