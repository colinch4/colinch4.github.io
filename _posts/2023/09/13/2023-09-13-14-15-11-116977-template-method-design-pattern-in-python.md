---
layout: post
title: "Template method design pattern in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

The Template Method design pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class and allows subclasses to override specific steps of the algorithm without changing its structure. This pattern follows the "Don't call us, we'll call you" principle.

## Implementation

```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

class ConcreteClass(AbstractClass):

    def step_one(self):
        print("Step 1")

    def step_two(self):
        print("Step 2")

    def step_three(self):
        print("Step 3")

# Usage
if __name__ == "__main__":
    concrete_class = ConcreteClass()
    concrete_class.template_method()
```

In the example above, we have an abstract base class called `AbstractClass` that defines the template method `template_method()`, as well as several abstract methods that represent the steps of the algorithm.

The `ConcreteClass` is a subclass that inherits from `AbstractClass` and implements the abstract methods. This subclass can override any or all of the abstract methods while maintaining the structure of the algorithm.

The client code creates an instance of the `ConcreteClass` and calls the template method, which executes the algorithm by invoking the defined steps in the specified order.

## Benefits of the Template Method Design Pattern

- **Code reuse:** The template method defines the high-level algorithm and allows subclasses to reuse the common behavior while providing the flexibility to modify specific steps as needed.
- **Enforced structure:** The structure of the algorithm is defined by the base class, ensuring that all subclasses follow the same sequence of steps. This eliminates duplication and promotes code consistency.
- **Easy maintenance:** By encapsulating the algorithm's logic within a single method, any modifications or enhancements can be implemented in the base class without affecting the subclasses.

## Conclusion

The Template Method design pattern provides an efficient way to define an algorithm's structure in a base class while allowing subclasses to customize specific steps. By following this pattern, you can achieve code reuse, maintainability, and adherence to a predefined algorithm structure.