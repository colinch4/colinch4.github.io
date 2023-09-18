---
layout: post
title: "Multiple inheritance vs multiple levels of inheritance in Python"
description: " "
date: 2023-09-13
tags: [Inheritance, Programming]
comments: true
share: true
---

In Python, the concept of inheritance allows us to create new classes based on existing classes. It helps in code reusability and promotes the DRY (Don't Repeat Yourself) principle. There are two common approaches to using inheritance in Python: multiple inheritance and multiple levels of inheritance. 

## Multiple Inheritance
Multiple inheritance refers to a scenario where a subclass inherits from multiple parent classes. This means that the subclass can inherit attributes and methods from multiple sources.

```python
class Parent1:
    def method1(self):
        print("Method 1 from Parent 1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent 2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method 3 from Child")

c = Child()
c.method1()  # Output: Method 1 from Parent 1
c.method2()  # Output: Method 2 from Parent 2
c.method3()  # Output: Method 3 from Child
```
In the above example, `Child` inherits from both `Parent1` and `Parent2`. The `Child` class can access methods from both parent classes.

## Multiple Levels of Inheritance
Multiple levels of inheritance refers to a scenario where a subclass inherits from a parent class, which in turn, inherits from another parent class. This creates a hierarchical structure of classes.

```python
class GrandParent:
    def method1(self):
        print("Method 1 from GrandParent")

class Parent(GrandParent):
    def method2(self):
        print("Method 2 from Parent")

class Child(Parent):
    def method3(self):
        print("Method 3 from Child")

c = Child()
c.method1()  # Output: Method 1 from GrandParent
c.method2()  # Output: Method 2 from Parent
c.method3()  # Output: Method 3 from Child
```
In the above example, `GrandParent` is the parent of `Parent`, and `Parent` is the parent of `Child`. As a result, `Child` can inherit attributes and methods from both `Parent` and `GrandParent` classes.

## Comparison
Both multiple inheritance and multiple levels of inheritance offer different benefits and have their own use cases.

Multiple inheritance allows a class to inherit attributes and methods from multiple sources, which can be advantageous when reusing code from different classes. It provides more flexibility but can also lead to complex code and potential conflicts if not used carefully.

On the other hand, multiple levels of inheritance provide a more hierarchical structure and can be useful for organizing code and maintaining a clear class hierarchy. It promotes code modularity and can make the code easier to understand and maintain.

#Python #Inheritance #Programming