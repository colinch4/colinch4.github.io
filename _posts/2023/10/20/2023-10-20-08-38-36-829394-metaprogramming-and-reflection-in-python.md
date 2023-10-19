---
layout: post
title: "Metaprogramming and reflection in Python"
description: " "
date: 2023-10-20
tags: []
comments: true
share: true
---

In Python, metaprogramming refers to the ability to write code that manipulates other code at runtime. This powerful capability allows developers to dynamically create classes, modify existing classes, and even alter the behavior of functions and methods.

Reflection, on the other hand, is the ability of a program to examine and modify its own structure and behavior at runtime.

Both metaprogramming and reflection are often used in advanced programming scenarios, such as framework development, dynamic code generation, and debugging.

## 1. Metaclasses: The Power Behind Metaprogramming

In Python, class objects are instances of metaclasses, which are responsible for creating and initializing the class objects. By defining a custom metaclass, you can control the creation and behavior of classes.

```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Manipulate the class definition before it is created
        attrs['x'] = 10
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.x)  # Output: 10
```

In the above example, the `MyMeta` metaclass is defined by subclassing `type`. The `__new__` method allows modifications to class attributes before creating the class. In this case, we add a new attribute `x` with a value of `10` to the `MyClass` definition.

## 2. Decorators: Dynamically Modifying Functions and Methods

Decorators are a popular technique in Python to dynamically modify functions and methods. They allow you to wrap existing functions with additional behavior without directly modifying their source code.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned from {func.__name__}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(2, 3))  # Output: Calling add \n Returned from add \n 5
```

In the example above, the `debug` decorator prints debug information before and after calling the `add` function. The `@debug` syntax is used to apply the decorator to the function.

## 3. Built-in Reflection: Exploring the Structure of Objects

Python provides built-in functions and attributes that allow you to inspect and manipulate objects at runtime.

```python
class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()

print(hasattr(obj, 'x'))  # Output: True
print(getattr(obj, 'x'))  # Output: 10
setattr(obj, 'y', 20)
print(obj.y)  # Output: 20
```

In the above example, the `hasattr` function checks if `obj` has an attribute named `x`. The `getattr` function retrieves the value of attribute `x`, and `setattr` sets a new attribute `y` with a value of `20`.

## Conclusion

Metaprogramming and reflection are powerful techniques that allow developers to write more flexible and dynamic code in Python. By leveraging metaclasses, decorators, and built-in reflection, you can achieve advanced functionalities and modify the behavior of your programs at runtime.

# References

1. [Python Metaprogramming: A Guide](https://realpython.com/python-metaclasses/)
2. [Python Decorators: A Step-By-Step Introduction](https://realpython.com/primer-on-python-decorators/)
3. [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html)