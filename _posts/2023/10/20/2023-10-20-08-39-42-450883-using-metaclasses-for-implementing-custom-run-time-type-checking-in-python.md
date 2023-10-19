---
layout: post
title: "Using metaclasses for implementing custom run-time type checking in Python"
description: " "
date: 2023-10-20
tags: [metaclasses]
comments: true
share: true
---

Python is a dynamic and duck-typed programming language, which means that variables do not have fixed types and polymorphism is supported. While this flexibility is often beneficial, there are scenarios where we may want to enforce strict type checking at runtime.

In Python, one way to implement custom run-time type checking is by using metaclasses. Metaclasses allow us to customize the behavior of class creation, giving us the ability to override how classes are defined and instances are created.

To enforce type checking, we can define a metaclass that validates the types of the attributes in a class. Let's look at an example:

```python
class TypeCheckedMeta(type):
    def __new__(cls, clsname, bases, attrs):
        for name, value in attrs.items():
            if isinstance(value, (int, str, list)):
                attrs[name] = value
            else:
                raise TypeError(f"Invalid type for attribute '{name}'")

        return super().__new__(cls, clsname, bases, attrs)

class MyClass(metaclass=TypeCheckedMeta):
    name = "John"      # Valid attribute (str)
    age = 30           # Valid attribute (int)
    hobbies = [ "coding", "reading" ]  # Valid attribute (list)
    score = 95.5       # Invalid attribute (TypeError)

# Creating an instance of MyClass
my_object = MyClass()
```

In this example, we define a metaclass called `TypeCheckedMeta` which extends the `type` metaclass. The `__new__` method of the metaclass is overridden to perform our custom type checking logic.

Inside the `__new__` method, we iterate over the attributes of the class being defined (`attrs`). For each attribute, we check if its type is either `int`, `str`, or `list`. If the type is valid, we keep the attribute as it is. Otherwise, we raise a `TypeError` with a descriptive error message.

Using the `TypeCheckedMeta` as the metaclass of `MyClass` ensures that all attributes defined in `MyClass` will be type checked. If any invalid attributes are found, a `TypeError` will be raised during class creation.

Finally, we create an instance of `MyClass` and assign it to `my_object`.

By utilizing metaclasses, we can implement custom run-time type checking in Python, allowing us to enforce stricter type constraints and catch potential errors at runtime.

**References:**

- [Python Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
- [Understanding Python Metaclasses](https://realpython.com/python-metaclasses/)
- [Metaclasses in Python](https://stackabuse.com/metaclasses-in-python/)