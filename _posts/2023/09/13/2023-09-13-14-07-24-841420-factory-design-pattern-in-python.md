---
layout: post
title: "Factory design pattern in Python"
description: " "
date: 2023-09-13
tags: [Python, DesignPatterns]
comments: true
share: true
---

The **Factory Design Pattern** is a creational design pattern that provides an interface for creating objects, but allows subclasses to decide which class to instantiate. This pattern promotes loose coupling between classes, as it hides the creation logic from the client code.

## When to use the Factory Design Pattern?

Use the Factory Design Pattern in the following scenarios:
1. When the creation of objects needs to be centralized and abstracted from the client code.
2. When the client code should be decoupled from the specific classes of objects it needs to create.
3. When it is necessary to provide a common interface for creating multiple related objects.

## Example Implementation

Let's consider an example where we have an **Animal** class and its subclasses - **Dog** and **Cat**. We will implement a `AnimalFactory` class to create instances of `Dog` and `Cat` based on the user's input.

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

# Usage
factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.sound())  # Output: Woof!

cat = factory.create_animal("cat")
print(cat.sound())  # Output: Meow!
```

In the example above, we have an `Animal` base class with two subclasses `Dog` and `Cat`. The `AnimalFactory` class takes an `animal_type` parameter and returns an instance of the appropriate animal based on the input. The client code uses the factory to create instances of different animals without knowing which classes are involved in the creation process.

## Benefits of the Factory Design Pattern

- **Encapsulation**: The creation logic is encapsulated within the factory, and the client code is only responsible for how to use the objects.
- **Flexibility**: The factory can accommodate changes in object creation without affecting the client code.
- **Code Reusability**: The factory promotes reusability by providing a common interface for creating multiple related objects.

## Conclusion

The Factory Design Pattern is a powerful way to decouple object creation from the client code. It provides a centralized and flexible way to create objects based on specific requirements. By using this pattern, you can easily extend or modify the code without impacting other parts of your application.

#Python #DesignPatterns