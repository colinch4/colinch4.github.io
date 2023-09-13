---
layout: post
title: "Method resolution order (MRO) in Python"
description: " "
date: 2023-09-13
tags: [Python]
comments: true
share: true
---

In object-oriented programming, inheritance allows a subclass to inherit the methods and attributes of its superclass. However, when a subclass inherits from multiple superclasses, it needs a mechanism to determine the order in which the inherited methods should be executed. This is where Method Resolution Order (MRO) comes into play.

## What is Method Resolution Order (MRO)?

MRO is a specific order in which a programming language resolves method calls in a class hierarchy. It determines the sequence in which the methods are searched and called when they are invoked from an instance of a class.

MRO is especially important in Python, as it supports multiple inheritance. Multiple inheritance refers to the ability of a class to inherit attributes and methods from more than one parent class. In such cases, MRO determines the order in which the parent classes are traversed to find the required method.

## How does MRO work in Python?

Python uses a depth-first, left-to-right approach to determine the MRO of a class. It follows a specific algorithm known as the C3 linearization algorithm. Let's look at an example:

```python
class A:
    def foo(self):
        print("A's foo()")

class B(A):
    def foo(self):
        print("B's foo()")

class C(A):
    def foo(self):
        print("C's foo()")

class D(B, C):
    pass

d = D()
d.foo()
```

In this example, class `D` inherits from classes `B` and `C`, both of which inherit from class `A`. When we call the `foo()` method on an instance of `D`, Python uses the MRO to determine which version of the method to execute.

The MRO for class `D` is determined by the C3 linearization algorithm, which results in the following order: `D`, `B`, `C`, `A`, `object`. Therefore, Python will first look for the `foo()` method in class `D`. If it doesn't find it, it will search in class `B`, then `C`, and finally in class `A`.

In this case, the output will be `"B's foo()"`, as class `B` overrides the `foo()` method defined in class `A`.

## Modifying MRO with super()

In Python, the `super()` function is commonly used to invoke a method from the superclass. By using `super()`, we can ensure that all the methods in the inheritance hierarchy are called correctly, as defined by the MRO.

```python
class A:
    def foo(self):
        print("A's foo()")

class B(A):
    def foo(self):
        super().foo()
        print("B's foo()")

class C(A):
    def foo(self):
        print("C's foo()")

class D(B, C):
    pass

d = D()
d.foo()
```

In this modified example, we have added `super().foo()` in the `foo()` method of class `B`. This allows class `B` to call the `foo()` method of its superclass, class `A`, before executing its own code.

The output of this code will be:

```
A's foo()
B's foo()
```

By using `super()`, we ensure that all classes in the hierarchy have the opportunity to execute their methods in the correct order defined by the MRO.

## Conclusion

Method Resolution Order (MRO) in Python is a crucial mechanism for resolving method calls in classes that inherit from multiple superclasses. With the help of the C3 linearization algorithm and the `super()` function, Python allows us to determine and control the order in which methods are executed. Understanding and utilizing MRO is essential for effectively managing inheritance and ensuring the correct execution of methods in complex class hierarchies. 

#Python #MRO