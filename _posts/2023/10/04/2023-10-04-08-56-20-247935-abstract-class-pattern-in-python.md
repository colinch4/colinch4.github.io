---
layout: post
title: "Abstract Class pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In object-oriented programming, an abstract class is a class that cannot be instantiated itself, but can only be subclassed. It serves as a blueprint for other classes, defining common attributes and methods that the subclasses must implement.

Python does not have a built-in implementation of abstract classes like some other programming languages. However, we can make use of the `abc` module from the Python standard library to create abstract classes.

## Creating an Abstract Class

To define an abstract class in Python, follow these steps:

1. Import the `abc` module:
    ```python
    import abc
    ```

2. Create a class and inherit from `abc.ABC` or one of its subclasses like `abc.ABCMeta` or `abc.ABC`.

3. Decorate the methods that you want to make abstract with the `@abc.abstractmethod` decorator.

Here's an example illustrating the implementation of an abstract class with an abstract method in Python:

```python
import abc

class AbstractClassExample(abc.ABC):

    @abc.abstractmethod
    def abstract_method(self):
        pass

    def concrete_method(self):
        print("This is a concrete method.")

class SubClassExample(AbstractClassExample):

    def abstract_method(self):
        print("This is the implementation of the abstract method.")

# Attempting to instantiate an abstract class raises an error
# abstract = AbstractClassExample()  # Raises TypeError

# Creating an instance of the subclass
sub = SubClassExample()
sub.abstract_method()  # Output: This is the implementation of the abstract method.
sub.concrete_method()  # Output: This is a concrete method.
```

In the above example, `AbstractClassExample` is an abstract class with one abstract method `abstract_method()`. The `SubClassExample` is a subclass of `AbstractClassExample` and implements the abstract method.

## Benefits of Using Abstract Classes

Abstract classes provide several benefits in software development:

1. **Code Reusability**: Abstract classes can define common methods and attributes that can be shared by multiple subclasses, promoting code reusability.

2. **Enforces Method Implementations**: Abstract classes ensure that the subclasses implement particular methods, enforcing a certain structure in the derived classes.

3. **Polymorphism**: Abstract classes allow objects to be referenced by their abstract class type, promoting polymorphism and flexibility in the code.

Abstract classes are a powerful tool in object-oriented programming, helping to organize and structure code efficiently by defining common characteristics and behaviors that subclasses must adhere to.