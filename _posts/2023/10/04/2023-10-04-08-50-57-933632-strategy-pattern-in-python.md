---
layout: post
title: "Strategy pattern in Python"
description: " "
date: 2023-10-04
tags: [designpatterns]
comments: true
share: true
---

## Introduction
In software development, the **Strategy pattern** is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one as a separate class, and make them interchangeable at runtime. It enables the client to choose an algorithm dynamically without tightly coupling the client code to the specific implementation.

## Implementation

1. **Define the Strategy Interface**: Create an interface or abstract class that defines the contract for all the different strategies. This interface will declare the common methods that the strategies should implement.

   ```python
   from abc import ABC, abstractmethod

   class Strategy(ABC):
       @abstractmethod
       def execute(self):
           pass
   ```

2. **Implement Concrete Strategies**: Implement multiple concrete classes that inherit from the strategy interface and provide their own implementation of the methods.

   ```python
   class ConcreteStrategyA(Strategy):
       def execute(self):
           print("Executing strategy A")

   class ConcreteStrategyB(Strategy):
       def execute(self):
           print("Executing strategy B")

   class ConcreteStrategyC(Strategy):
       def execute(self):
           print("Executing strategy C")
   ```

3. **Create the Context Class**: The context class will be responsible for maintaining a reference to one of the strategy objects. It will also provide a method for the client to switch the strategy dynamically.

   ```python
   class Context:
       def __init__(self, strategy: Strategy):
           self._strategy = strategy

       def set_strategy(self, strategy: Strategy):
           self._strategy = strategy

       def execute_strategy(self):
           self._strategy.execute()
   ```

4. **Usage**: Now, let's put the strategy pattern into action.

   ```python
   strategy_a = ConcreteStrategyA()
   strategy_b = ConcreteStrategyB()
   strategy_c = ConcreteStrategyC()

   context = Context(strategy_a)
   context.execute_strategy()  # Output: Executing strategy A

   context.set_strategy(strategy_b)
   context.execute_strategy()  # Output: Executing strategy B

   context.set_strategy(strategy_c)
   context.execute_strategy()  # Output: Executing strategy C
   ```

## Benefits of Strategy Pattern

- **Flexibility**: The strategy pattern allows you to change the algorithm or strategy at runtime. You can easily swap one strategy with another without changing the client code.
- **Encapsulation**: Each strategy is encapsulated within its own object, making it easier to modify or add new strategies without impacting other parts of the codebase.
- **Simplification**: The strategy pattern simplifies complex conditional statements and reduces code duplication by providing a clean way to encapsulate different algorithms.

## Conclusion
The strategy pattern is a powerful tool for designing flexible and maintainable code. It promotes code reuse, extensibility, and separation of concerns. By implementing the strategy pattern, you can make your code more adaptable to changing requirements and improve its overall maintainability.

---
Tags: #python #designpatterns