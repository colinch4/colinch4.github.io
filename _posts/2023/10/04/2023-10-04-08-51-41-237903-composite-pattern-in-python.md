---
layout: post
title: "Composite pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Composite Pattern is a structural design pattern that allows you to treat individual objects and their compositions uniformly. It composes objects into tree-like structures and lets clients treat individual objects and compositions uniformly.

In this blog post, we will explore the implementation of the Composite Pattern in Python. We will discuss the concept of the pattern, its use cases, and provide a code example to demonstrate its usage.

## Understanding the Composite Pattern

The Composite Pattern is useful when you have a hierarchy of objects and want to perform operations on both individual objects and collections of objects uniformly. The pattern allows you to treat the individual objects and collections as the same type of object.

The key components of the Composite Pattern are:

1. **Component**: This is the base interface or abstract class that defines the common operations for both leaf objects and composite objects.

2. **Leaf**: This represents the individual objects in the composition. Leaf objects do not have any children.

3. **Composite**: This represents the container object that can hold other child objects. It implements the operations defined by the Component interface and provides additional operations specific to composite objects.

## Use Cases of the Composite Pattern

The Composite Pattern is useful in the following scenarios:

- When you want to represent part-whole hierarchies of objects.
- When you want the client code to treat individual objects and compositions uniformly.
- When you want to add or remove objects dynamically without affecting the client code.

## Implementation Example

Let's consider a scenario where we have a company hierarchy consisting of employees and departments. Each department can have multiple employees, and departments can also have sub-departments.

Here's an example implementation of the Composite Pattern for this scenario:

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Developer(Employee):
    def __init__(self, name):
        self.name = name
    
    def get_details(self):
        return f"Developer: {self.name}"

class Department(Employee):
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee):
        self.employees.remove(employee)
    
    def get_details(self):
        details = f"Department: {self.name}\n"
        for employee in self.employees:
            details += employee.get_details() + "\n"
        return details

# Usage example
developer1 = Developer("John")
developer2 = Developer("Jane")
developer3 = Developer("Mike")
department1 = Department("Development")
department1.add_employee(developer1)
department1.add_employee(developer2)
department2 = Department("Marketing")
department2.add_employee(developer3)

company = Department("Company")
company.add_employee(department1)
company.add_employee(department2)

print(company.get_details())
```

In this example, we have two types of employees: `Developer` and `Department`. The `Developer` class represents an individual employee, while the `Department` class represents a container object that can hold other employees (either individual developers or sub-departments).

The `Department` class implements the `Employee` interface, allowing it to be treated as an employee. It also provides methods to add and remove employees from the department.

The `get_details` method is implemented in both the `Developer` and `Department` classes to return the details of the employee or the department along with its sub-employees.

## Conclusion

The Composite Pattern is a powerful design pattern that enables us to represent hierarchical structures of objects and perform operations uniformly on individual objects and compositions. It helps in building flexible and maintainable code by allowing the client code to treat both individual objects and collections of objects in a consistent manner.

By using the Composite Pattern, you can easily manage complex hierarchies, add or remove objects dynamically, and simplify the client code. It is particularly useful when dealing with tree-like structures or part-whole hierarchies.

So the next time you encounter a scenario where you have a hierarchical structure of objects, consider using the Composite Pattern to simplify your code and make it more flexible.