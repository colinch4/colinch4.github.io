---
layout: post
title: "__add__ and __sub__ methods in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

Python is a versatile and powerful programming language that offers a wide range of functionality through its rich standard library and extensive third-party packages. When it comes to working with numerical data, Python provides built-in methods for performing mathematical operations, including addition and subtraction.

In Python, the `__add__` and `__sub__` methods are special methods that allow objects to define their behavior when they are involved in addition or subtraction operations. By implementing these methods, you can customize how instances of your class interact with the `+` and `-` operators.

### The `__add__` Method

The `__add__` method is called when the `+` operator is used to add two objects together. It allows you to define how instances of your class should be added to other objects. Here's an example implementation:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        else:
            raise TypeError("Unsupported operand type for +")

num1 = Number(5)
num2 = Number(10)

result = num1 + num2
print(result.value)  # Output: 15

result = num1 + 2
print(result.value)  # Output: 7
```

In the above example, the `Number` class defines the `__add__` method to handle addition operations involving instances of the class. It checks the type of the `other` operand and performs the corresponding addition operation. If the `other` operand is not of a supported type, a `TypeError` is raised.

### The `__sub__` Method

Similarly, the `__sub__` method is called when the `-` operator is used to subtract two objects. It allows you to define the behavior of instances of your class during subtraction operations. Here's an example implementation:

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value - other)
        else:
            raise TypeError("Unsupported operand type for -")

num1 = Number(10)
num2 = Number(5)

result = num1 - num2
print(result.value)  # Output: 5

result = num1 - 2
print(result.value)  # Output: 8
```

In the example above, the `Number` class implements the `__sub__` method to handle subtraction operations involving instances of the class. The method checks the type of the `other` operand and performs the corresponding subtraction operation. If the `other` operand is not of a supported type, a `TypeError` is raised.

By implementing the `__add__` and `__sub__` methods in your classes, you can customize how objects of your class behave during addition and subtraction operations. This flexibility allows you to create more intuitive and expressive code.

So next time you need to perform addition or subtraction operations on your custom objects in Python, consider implementing the `__add__` and `__sub__` methods to define their behavior.

#python #oop