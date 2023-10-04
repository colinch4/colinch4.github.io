---
layout: post
title: "Singleton pattern in Python"
description: " "
date: 2023-10-04
tags: [designpatterns]
comments: true
share: true
---

The Singleton pattern is a creational design pattern that ensures only one instance of a class is created and provides a global point of access to that instance. In Python, there are multiple ways to implement the Singleton pattern. In this blog post, we will explore two common approaches.

## 1. Classic Singleton

The classic Singleton implementation involves defining a class with a private constructor and a static method that returns the instance of the class. Here's an example:

```python
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton instance already exists!")
        Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
```

In the above implementation, the `__init__` method checks if an instance of the class already exists. If it does, an exception is raised. Otherwise, it assigns the instance to the `__instance` variable. The `get_instance` method is used to retrieve the singleton instance.

To use the Singleton class, you can simply call the `get_instance` method:

```python
singleton_instance = Singleton.get_instance()
```

This will create the instance if it doesn't exist or return the existing instance if it does.

## 2. Singleton as a Module

In Python, modules are singletons by default. So one simple way of implementing the Singleton pattern is to create a module to hold the shared state or functionality. Here's an example:

```python
# singleton.py
singleton_instance = None

def get_instance():
    global singleton_instance
    if singleton_instance is None:
        singleton_instance = Singleton()
    return singleton_instance

class Singleton:
    def __init__(self):
        # initialization code
```

In the above code, `singleton_instance` is a global variable that holds the singleton instance. The `get_instance` function is responsible for creating the instance if it doesn't exist or returning the existing instance.

To use the Singleton, you can import the module and call the `get_instance` function:

```python
from singleton import get_instance

singleton_instance = get_instance()
```

## Conclusion

The Singleton pattern ensures that only one instance of a class is created and provides a global point of access to that instance. In Python, the classic Singleton implementation and using a module as a Singleton are two common approaches. Choose the one that best fits your use case and enjoy the benefits of having a single globally accessible instance. #python #designpatterns