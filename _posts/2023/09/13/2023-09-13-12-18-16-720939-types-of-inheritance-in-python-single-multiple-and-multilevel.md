---
layout: post
title: "Types of inheritance in Python: single, multiple, and multilevel"
description: " "
date: 2023-09-13
tags: [python]
comments: true
share: true
---

1. Single Inheritance:
   Single inheritance is the simplest and most commonly used type of inheritance. It involves creating a new class (derived class) based on an existing class (base class). The derived class inherits all the attributes and methods of the base class, allowing us to reuse the code without duplicating it.

   ```python
   class BaseClass:
       def base_method(self):
           print("This is a base class method.")
   
   class DerivedClass(BaseClass):
       def derived_method(self):
           print("This is a derived class method.")
   
   obj = DerivedClass()
   obj.base_method()  # Output: This is a base class method.
   obj.derived_method()  # Output: This is a derived class method.
   ```

2. Multiple Inheritance:
   Multiple inheritance allows a derived class to inherit attributes and methods from more than one base class. This type of inheritance promotes code reuse and allows us to combine the characteristics of multiple classes in a single derived class. However, it can lead to name clashes and create complexity if not used carefully.

   ```python
   class BaseClass1:
       def method1(self):
           print("Method from BaseClass1.")
   
   class BaseClass2:
       def method2(self):
           print("Method from BaseClass2.")
   
   class DerivedClass(BaseClass1, BaseClass2):
       def derived_method(self):
           print("Method in DerivedClass.")
   
   obj = DerivedClass()
   obj.method1()  # Output: Method from BaseClass1.
   obj.method2()  # Output: Method from BaseClass2.
   obj.derived_method()  # Output: Method in DerivedClass.
   ```

3. Multilevel Inheritance:
   Multilevel inheritance involves creating a chain of derived classes where each derived class becomes the base class for the next level. It allows us to inherit attributes and methods from multiple classes and build a hierarchy of classes with different levels of specialization.

   ```python
   class BaseClass:
       def base_method(self):
           print("Method from BaseClass.")
   
   class DerivedClass1(BaseClass):
       def derived_method1(self):
           print("Method from DerivedClass1.")
   
   class DerivedClass2(DerivedClass1):
       def derived_method2(self):
           print("Method from DerivedClass2.")
   
   obj = DerivedClass2()
   obj.base_method()  # Output: Method from BaseClass.
   obj.derived_method1()  # Output: Method from DerivedClass1.
   obj.derived_method2()  # Output: Method from DerivedClass2.
   ```

Understanding the different types of inheritance in Python allows us to design our codebase more effectively and create robust and flexible class hierarchies. By utilizing inheritance, we can save time and effort in writing repetitive code, enhance code readability, and make our programs more modular and scalable.