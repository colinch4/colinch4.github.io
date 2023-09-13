---
layout: post
title: "Visitor design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Visitor design pattern is a behavioral design pattern that allows adding new operations or behaviors to a group of objects without modifying their classes. It separates the algorithm from the objects on which it operates.

## When to use the Visitor design pattern?

You can use the Visitor design pattern when you have a group of objects and want to perform some operations on them without modifying their existing code. This pattern is especially useful when:

- You have a complex object structure and want to perform different operations on different subsets of objects.
- You want to add new behaviors to a group of objects without modifying their existing code.
- You want to keep related behavior in a single class rather than spreading them across multiple classes.

## Implementation in Python

To illustrate the Visitor design pattern, let's consider an example where we have a zoo and different animals. Each animal has a name and a method `accept_visitor`. We want to perform different operations or behaviors on these animals using visitor classes without modifying their existing code.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def accept_visitor(self, visitor):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def accept_visitor(self, visitor):
        visitor.visit_lion(self)

class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)

    def accept_visitor(self, visitor):
        visitor.visit_bear(self)

class Visitor(ABC):
    @abstractmethod
    def visit_lion(self, lion):
        pass

    @abstractmethod
    def visit_bear(self, bear):
        pass

class FeedVisitor(Visitor):
    def visit_lion(self, lion):
        print(f"Feeding {lion.name} the lion")

    def visit_bear(self, bear):
        print(f"Feeding {bear.name} the bear")

class LetOutVisitor(Visitor):
    def visit_lion(self, lion):
        print(f"Letting out {lion.name} the lion")

    def visit_bear(self, bear):
        print(f"Letting out {bear.name} the bear")

# Usage
lion = Lion("Simba")
bear = Bear("Baloo")

feed_visitor = FeedVisitor()
let_out_visitor = LetOutVisitor()

lion.accept_visitor(feed_visitor)
bear.accept_visitor(feed_visitor)

lion.accept_visitor(let_out_visitor)
bear.accept_visitor(let_out_visitor)
```

In the above code, we have defined the `Animal` class as an abstract base class (ABC) with a `accept_visitor` method. Then, we have concrete animal classes `Lion` and `Bear` which inherit from `Animal` class and implement the `accept_visitor` method.

We also have an abstract base class `Visitor` with abstract methods `visit_lion` and `visit_bear`. Then, we have concrete visitor classes `FeedVisitor` and `LetOutVisitor` which inherit from `Visitor` class and implement the visit methods for each animal.

In the usage section, we create an instance of `Lion` and `Bear`, along with instances of `FeedVisitor` and `LetOutVisitor`. We call the `accept_visitor` method on each animal and pass it the respective visitor instance.

## Benefits of the Visitor design pattern

1. **Separation of concerns:** With the Visitor design pattern, the logic for performing different operations on a group of objects is encapsulated in separate visitor classes. This keeps the concerns separated and makes the code more maintainable.
2. **Open/Closed Principle:** The Visitor pattern follows the Open/Closed principle by allowing the addition of new operations to existing objects without modifying their classes. This makes the code more extensible and avoids breaking existing functionality.
3. **Improved single responsibility:** The Visitor pattern allows each visitor class to have a single responsibility, encapsulating a particular behavior or operation. This makes the code easier to understand and maintain.

## Conclusion

The Visitor design pattern is a powerful pattern that allows adding new operations or behaviors to a group of objects without modifying their existing code. It promotes separation of concerns, follows the Open/Closed principle, and improves single responsibility. Implementing the Visitor pattern in Python can help make your code more modular, flexible, and extensible.