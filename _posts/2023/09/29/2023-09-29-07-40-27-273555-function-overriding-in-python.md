---
layout: post
title: "Function overriding in Python"
description: " "
date: 2023-09-29
tags: [FunctionOverriding]
comments: true
share: true
---

Function overriding is a concept in object-oriented programming where a derived class provides a different implementation of a method that is already defined in its base class. Python supports function overriding, allowing you to modify or extend the behavior of inherited methods.

To override a method in Python, you need to define a method with the same name in the derived class. The new method will take precedence over the method with the same name in the base class.

## Syntax of Function Overriding

```python
class BaseClass:
    def method_name(self, params):
        # implementation

class DerivedClass(BaseClass):
    def method_name(self, params):
        # overridden implementation
```

The derived class `DerivedClass` inherits from the base class `BaseClass` and overrides the `method_name` method.

## Example of Function Overriding

Let's take a look at an example to understand how function overriding works in Python:

```python
class Animal:
    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Create instances of the classes
animal = Animal()
dog = Dog()

# Call the make_sound method
animal.make_sound()  # Output: "Animal makes sound"
dog.make_sound()  # Output: "Dog barks"
```

In the example above, we have a base class `Animal` that defines the `make_sound` method. The derived class `Dog` inherits from `Animal` and overrides the `make_sound` method with its own implementation.

When we create an instance of `Animal` and call the `make_sound` method, it prints "Animal makes sound". However, when we create an instance of `Dog` and call the `make_sound` method, it prints "Dog barks", which is the overridden implementation in the `Dog` class.

## Conclusion

Function overriding allows you to modify or extend the behavior of inherited methods in Python. By defining a method with the same name in the derived class, you can override the implementation of the method in the base class. This feature helps in creating more flexible and customizable classes in object-oriented programming.

#Python #FunctionOverriding