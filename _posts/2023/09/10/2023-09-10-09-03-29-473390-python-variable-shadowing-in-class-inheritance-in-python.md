---
layout: post
title: "[Python] Variable shadowing in class inheritance in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, **variable shadowing** refers to the situation where a variable in a subclass has the same name as a variable in its parent class. This can lead to unexpected behavior when accessing or modifying the variable.

Let's consider a simple example to understand variable shadowing in class inheritance. Suppose we have a parent class called `Animal` with a variable `name` initialized to "Animal". We then create a subclass called `Dog` that also has a variable `name` initialized to "Dog".

```python
class Animal:
    def __init__(self):
        self.name = "Animal"

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"
```

Now, let's create an instance of `Dog` and access the `name` variable.

```python
dog = Dog()
print(dog.name)
```

The output will be:

```
Dog
```

In this example, the `name` variable in the `Dog` subclass shadows the `name` variable in the `Animal` parent class. So, when we access `dog.name`, it refers to the `name` variable defined in the `Dog` class, not in the `Animal` class.

However, what if we want to access the `name` variable from the parent class? We can use the `super()` function to access the parent class and retrieve the variable.

```python
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"
        self.parent_name = super().name

dog = Dog()
print(dog.parent_name)
```

The output will be:

```
Animal
```

By using `super().name`, we can access the `name` variable defined in the parent class.

To summarize, variable shadowing can occur in class inheritance when a variable in a subclass has the same name as a variable in its parent class. By using the `super()` function, we can access the parent class and retrieve the variable to avoid variable shadowing.

Be mindful of variable names when working with class inheritance in Python to ensure the desired behavior is achieved.