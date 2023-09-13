---
layout: post
title: "Accessing private methods and variables in Python"
description: " "
date: 2023-09-13
tags: [Python, Encapsulation]
comments: true
share: true
---

In Python, there are no strict rules for private methods and variables like some other programming languages. However, there is a convention to indicate that a method or variable is intended to be private and should not be accessed or modified directly by other parts of the code.

## Using Underscore Convention

In Python, the convention is to prefix the name of a method or variable with a single underscore (_) to indicate that it is intended to be a private member. However, it's important to note that this convention is purely a naming convention and does not provide any actual access control.

Here's an example:

```python
class MyClass:
    def __init__(self):
        self._private_variable = 10
    
    def _private_method(self):
        print("This is a private method.")
    
    def public_method(self):
        print("This is a public method.")
        self._private_method()
        print(self._private_variable)

obj = MyClass()
obj.public_method()
```

In the example above, `_private_variable` and `_private_method` are intended to be private. However, they can still be accessed and modified from outside the class. It's a matter of convention and best practice to treat them as private.

## Using Double Underscore Convention

Python provides another convention using double underscores (__) to indicate name mangling. When a name is prefixed with two underscores, the interpreter will modify the name to include the class name as a prefix. This can be used to make an attribute harder to access from outside the class.

Here's an example:

```python
class MyClass:
    def __init__(self):
        self.__private_variable = 10
    
    def __private_method(self):
        print("This is a private method.")
    
    def public_method(self):
        print("This is a public method.")
        self.__private_method()
        print(self.__private_variable)  # Accessing private variable using name mangling

obj = MyClass()
obj.public_method()
```

In this example, `__private_variable` and `__private_method` are intended to be private but can still be accessed using name mangling. The access is modified internally by prepending `_ClassName` to the variable or method name.

To access the private members outside of the class, you can use the name mangling syntax, but it is generally not recommended as it goes against the principle of encapsulation.

## Conclusion

Python does not provide strict access control mechanisms for private members like some other languages, but the naming conventions using a single underscore or name mangling can help indicate the intended privacy of methods and variables. However, it's important to remember that these conventions are not enforced by the language itself, and accessing private members is still possible. It's best to rely on proper encapsulation and only access the publicly exposed interface of the class. #Python #Encapsulation