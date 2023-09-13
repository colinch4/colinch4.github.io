---
layout: post
title: "SOLID principles of OOP in Python"
description: " "
date: 2023-09-13
tags: []
comments: true
share: true
---

When developing object-oriented programs in Python, it's essential to follow SOLID principles. SOLID is an acronym for five principles that help in designing maintainable and scalable code. These principles are:

## Single Responsibility Principle (SRP) [#SRP]
The SRP states that a class should have one single responsibility and one reason to change. In other words, a class should have only one job or task to perform. This principle promotes separation of concerns and ensures that a class remains focused on its core responsibility.

For example, if we have a `User` class, it should only be responsible for managing user data and not performing additional unrelated tasks like sending emails or generating reports. By adhering to SRP, it becomes easier to maintain and test our code as changes are isolated to specific classes.

## Open/Closed Principle (OCP) [#OCP]
The OCP states that software entities (classes, modules, functions) should be open for extension but closed for modification. This principle encourages using abstraction and interfaces to allow adding new functionality without modifying existing code.

To apply OCP, we can use inheritance and polymorphism in Python. Instead of modifying existing classes, we create new subclasses or implement new interfaces that extend the behavior. This allows our code to remain untouched while enabling us to introduce new features.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```

## Liskov Substitution Principle (LSP) [#LSP]
The LSP states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, any place that expects an object of a particular type should be able to work correctly with objects of any subtype of that type.

In Python, LSP can be achieved by adhering to the principle of duck typing. The code should rely on the behavior or methods of an object rather than its specific type. If a subclass can fulfill all the expectations of the superclass, it can be safely substituted.

## Interface Segregation Principle (ISP) [#ISP]
The ISP states that clients should not be forced to depend on interfaces they do not use. It is better to have smaller, focused interfaces rather than one large interface that encompasses all possible functionality.

In Python, we can achieve ISP by creating specific interfaces for each client. This allows clients to depend only on the methods they actually need, preventing unnecessary dependencies and potential code bloat.

## Dependency Inversion Principle (DIP) [#DIP]
The DIP states that high-level modules should not depend on low-level modules, but both should depend on abstractions. This promotes loose coupling and allows for easier code maintenance and extensibility.

In Python, we can achieve DIP by utilizing dependency injection. Instead of directly creating instances of other classes, we pass them as dependencies to the constructor or methods. This way, the high-level modules depend on abstractions (interfaces) rather than concrete implementations.

By following these SOLID principles, we can create more flexible, maintainable, and scalable OOP code in Python.

```python
class DatabaseConnector:
    def connect(self):
        pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        # Logic to connect to MySQL database

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        # Logic to connect to PostgreSQL database

class Application:
    def __init__(self, database_connector: DatabaseConnector):
        self.database_connector = database_connector
    
    def run(self):
        self.database_connector.connect()
        # Other application logic
```

#SRP #OCP #LSP #ISP #DIP