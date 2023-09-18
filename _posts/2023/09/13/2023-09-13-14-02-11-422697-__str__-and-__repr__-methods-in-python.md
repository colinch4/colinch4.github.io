---
layout: post
title: "__str__ and __repr__ methods in Python"
description: " "
date: 2023-09-13
tags: [objectrepresentation]
comments: true
share: true
---

## `__str__` Method

The `__str__` method is used to return a string representation of an object when the `str()` function is called on it or when it is used in string concatenation. This method is designed to provide a readable and informative representation for the end user.

Here's an example of implementing the `__str__` method in a Python class:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"{self.brand} {self.model}"

car = Car("Tesla", "Model S")
print(str(car))  # Output: Tesla Model S
```

In the above example, the `__str__` method is defined to return a formatted string representation of the car object, including its brand and model.

## `__repr__` Method

The `__repr__` method, short for "representation", is used to return a string representation of an object that can be used to recreate the object. It is mainly used for debugging and development purposes.

Here's an example of implementing the `__repr__` method in the same `Car` class:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}')"

car = Car("Tesla", "Model S")
print(repr(car))  # Output: Car(brand='Tesla', model='Model S')
```

In this example, the `__repr__` method returns a string representation that follows the syntax of a constructor call, making it possible to recreate the object using the `eval()` function or by copy-pasting the output.

## Differences between `__str__` and `__repr__`

The main difference between these two methods lies in their intended purpose and usage. The `__str__` method is meant to provide a human-readable representation of an object, while the `__repr__` method is aimed at providing a complete and unambiguous representation that can be used to recreate the object.

Another difference is in which contexts they are called. The `__str__` method is invoked by default when using the `print()` function or when an object is converted to a string implicitly, while the `__repr__` method is called when the `repr()` function is explicitly used or when the object is displayed in the interpreter.

## Conclusion

In this blog post, we learned about the `__str__` and `__repr__` methods in Python. We saw how they can be implemented in a class to provide string representations of objects. Understanding the differences between these two methods is crucial for effective debugging and providing useful information about your objects. So, make sure to consider implementing them in your Python classes.

#python #objectrepresentation