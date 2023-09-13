---
layout: post
title: "Proxy design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The proxy design pattern is a structural design pattern that provides a surrogate or placeholder for another object in order to control access to it. It allows for the creation of a proxy object that has the same interface as the original object and can be used as a substitute for it. 

## When to use the Proxy Design Pattern
The proxy pattern is useful in scenarios where we want to provide controlled access to an object. It can be used in situations such as:

- Controlling access to sensitive information
- Delaying instantiation of an expensive object until it is actually needed
- Simplifying the interaction with a remote or distributed object
- Adding additional functionality to an existing object without modifying its code

## Example
Let's say we have a `RealImage` class that represents an image. The class has a method `display()` that displays the image on the screen. However, loading the image from disk can be time-consuming. To overcome this, we can use the proxy design pattern by introducing a `ProxyImage` class that acts as a proxy for the `RealImage` class.

```python
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()
    
    def load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")
    
    def display(self):
        print(f"Displaying image: {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage
image = ProxyImage("image.jpg")
# The image is not loaded from disk yet

# The first call to display will load the image from disk and display it
image.display()

# Subsequent calls to display will directly display the image
image.display()
```

In the example above, the `ProxyImage` class acts as a proxy for the `RealImage` class. When the `display` method is called on the `ProxyImage` object, it first checks if the `real_image` object is already created. If not, it creates a new instance of the `RealImage` class and delegates the `display` method call to it. This way, the image is only loaded from disk when it is actually needed.

Using the proxy pattern allows us to control the access to the `RealImage` object and add additional functionality if needed, without modifying the original `RealImage` class.

## Conclusion
The proxy design pattern provides a flexible way to control access to an object and add additional functionality. It helps in situations where we want to delay the instantiation of an object, add security checks, or simplify remote communication. By using the proxy pattern, we can effectively manage and control the usage of objects in our code.