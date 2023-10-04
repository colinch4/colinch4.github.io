---
layout: post
title: "Command Query Separation pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In software development, the Command Query Separation (CQS) pattern is a principle that states that methods or functions should either be commands that perform an action and modify the system's state, or queries that return a result without modifying the state. This pattern helps to improve code clarity, maintainability, and separation of concerns.

## Implementing CQS in Python

Python is a versatile programming language that supports the implementation of the CQS pattern through the use of functions, classes, and decorators. Let's explore how we can apply this pattern in Python.

### Separating Commands and Queries

To begin, let's create a simple example of a class that demonstrates the CQS pattern:

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
```

In this example, the `add_item` method is a command that modifies the state of the `ShoppingCart` object by adding items to the `items` list. On the other hand, the `get_total` method is a query that returns the total price of all items in the cart without modifying the state.

### Applying Decorators

Python decorators provide a convenient way to separate commands and queries. Let's define two decorators, `@command` and `@query`, to enforce the separation for methods:

```python
def command(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        # Perform any additional command-side logic here
    return wrapper
    
def query(func):
    def wrapper(self, *args, **kwargs):
        # Perform any additional query-side logic here
        return func(self, *args, **kwargs)
    return wrapper
```

Now we can apply these decorators to methods within our class:

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    @command
    def add_item(self, item):
        self.items.append(item)

    @query
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
```

By decorating the `add_item` method with `@command` and the `get_total` method with `@query`, we explicitly indicate their respective roles as commands and queries.

### Benefits of CQS

The CQS pattern brings several benefits to your Python codebase:

1. **Improved Code Clarity**: Separating commands and queries helps to clarify the intent and purpose of each method, making your code easier to understand.
2. **Maintainability**: With clear separation, it becomes easier to modify or refactor methods without affecting other parts of the codebase.
3. **Testing**: CQS encourages testability, as queries can be easily tested for expected results without worrying about state changes.
4. **Reusability**: By separating commands and queries, you can reuse your queries in different contexts without worrying about unexpected side effects.

### Conclusion

The Command Query Separation pattern provides a useful guideline for designing clean and maintainable code in Python. By clearly separating commands that modify the system's state from queries that return results, you can improve code clarity, maintainability, and testability.