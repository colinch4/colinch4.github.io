---
layout: post
title: "Singleton metaclass pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In object-oriented programming, the Singleton pattern restricts the instantiation of a class to a single object. This means that there is only one instance of the class, which can be accessed globally. In Python, one way to implement the Singleton pattern is using a metaclass.

## What is a Metaclass?

A metaclass is a class that defines the behavior of other classes. It is responsible for instantiating classes and defining their behavior at the class level. In Python, `type` is the metaclass for most classes. However, we can create custom metaclasses to implement specific behaviors, such as the Singleton pattern.

## Implementing Singleton using Metaclass

To implement the Singleton pattern using a metaclass, we need to define a metaclass that restricts the instantiation of a class to a single instance. Here's an example implementation:

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass
```

In this implementation, we define a `SingletonMeta` metaclass that keeps track of the instances of classes using a dictionary `_instances`. When a class is instantiated, the `__call__` method of the metaclass is called. It checks whether an instance of the class already exists. If not, it creates a new instance using `super().__call__` and stores it in the `_instances` dictionary.

We then define a `SingletonClass` class and set its metaclass to `SingletonMeta`. This ensures that only one instance of `SingletonClass` can be created.

## Using the Singleton Class

Now let's see how we can use the `SingletonClass`:

```python
instance1 = SingletonClass()
instance2 = SingletonClass()

print(instance1 is instance2)  # Output: True
```

In this example, both `instance1` and `instance2` are instances of the `SingletonClass`. Since the Singleton pattern ensures that there is only one instance of the class, `instance1` and `instance2` will refer to the same object. Therefore, the output of `instance1 is instance2` would be `True`.

## Conclusion

The Singleton pattern restricts the instantiation of a class to a single object. Using metaclasses in Python, we can implement the Singleton pattern and ensure that there is only one instance of a class. By defining a metaclass that keeps track of class instances, we can control the creation and access of objects.