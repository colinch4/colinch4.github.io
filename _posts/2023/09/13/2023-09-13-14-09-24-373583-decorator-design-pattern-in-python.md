---
layout: post
title: "Decorator design pattern in Python"
description: " "
date: 2023-09-13
tags: [Python, DecoratorPattern]
comments: true
share: true
---

The decorator design pattern is a structural pattern that allows behavior to be added to an object without changing its structure. It provides a flexible alternative to subclassing for extending functionality.

## How does it work?

In the decorator pattern, a decorator class wraps the original object and enhances its functionality by adding additional behavior. The decorator class implements the same interface as the original object, which allows it to be used interchangeably with the original object.

## Example

Let's consider a simple example where we have a `Coffee` class that represents a cup of coffee. We want to add extra ingredients, such as milk or sugar, to the coffee object using decorators.

```python
# Define the Coffee interface
class Coffee:
    def get_description(self):
        pass

    def get_cost(self):
        pass

# Implement the concrete Coffee class
class SimpleCoffee(Coffee):
    def get_description(self):
        return "Simple Coffee"
    
    def get_cost(self):
        return 1.0

# Decorator class for adding milk
class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description() + ", Milk"
    
    def get_cost(self):
        return self.coffee.get_cost() + 0.5

# Decorator class for adding sugar
class SugarDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_description(self):
        return self.coffee.get_description() + ", Sugar"
    
    def get_cost(self):
        return self.coffee.get_cost() + 0.25

# Create a simple coffee object
coffee = SimpleCoffee()

# Add milk to the coffee using MilkDecorator
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.get_description())  # Output: Simple Coffee, Milk
print(coffee_with_milk.get_cost())         # Output: 1.5

# Add sugar to the coffee using SugarDecorator
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_and_sugar.get_description())  # Output: Simple Coffee, Milk, Sugar
print(coffee_with_milk_and_sugar.get_cost())         # Output: 1.75
```

In the above example, the `MilkDecorator` and `SugarDecorator` classes wrap the `coffee` object and add the respective ingredients to its description and cost.

## Benefits of the Decorator Pattern

- Allows adding behavior to objects dynamically at runtime.
- Provides an alternative to subclassing for extending object functionality.
- Allows multiple decorators to wrap an object, providing more flexibility.

By using the decorator design pattern, we can enhance the functionality of objects without modifying their underlying implementation. It promotes code reusability and maintainability.

---

#Python #DecoratorPattern