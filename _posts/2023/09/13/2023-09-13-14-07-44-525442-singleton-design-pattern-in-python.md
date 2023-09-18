---
layout: post
title: "Singleton design pattern in Python"
description: " "
date: 2023-09-13
tags: [designpatterns]
comments: true
share: true
---

In software engineering, the **Singleton Design Pattern** is a creational design pattern that restricts the instantiation of a class to a single instance and provides a global point of access to it. This pattern is commonly used in scenarios where there is a need for only one instance of a class, such as database connections, logging systems, or thread pools.

To implement the Singleton pattern in Python, we can make use of the class mechanism and Python's module system. Here's an example:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
```

In the above code, the `Singleton` class has a private class variable `_instance` which holds the reference to the single instance of the class. The `__new__` method is overridden to create and return the instance only if `_instance` is `None`, ensuring that only one instance is created.

To use the Singleton class, simply create instances of it, which will always refer to the same object:

```python
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
```

In the above code, `singleton1` and `singleton2` are both instances of the Singleton class, but they refer to the same object. The output of the comparison `singleton1 is singleton2` is `True`.

The Singleton pattern provides a global point of access to the single instance, eliminating the need to pass around the instance to different parts of the code. It also ensures that a class has only one instance throughout the application's lifecycle.

By using the Singleton pattern, you can enforce the uniqueness of objects in your Python programs and simplify the management of shared resources.

#python #designpatterns

---

References:
- [Singleton Pattern - Wikipedia](https://en.wikipedia.org/wiki/Singleton_pattern)
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)