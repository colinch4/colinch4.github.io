---
layout: post
title: "[Python] Variable annotations in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Variable annotations provide a way to add type hints to your code, making it more readable and easier to understand. They also help catch potential type-related errors during development.

To annotate a variable in Python, you can use the colon (:) followed by the type of the variable. Here's an example:

```python
name: str = "John"
age: int = 25
height: float = 1.75
```

In the above code, we have three variables (`name`, `age`, and `height`) annotated with their respective types (`str`, `int`, and `float`). By doing this, you explicitly indicate the type of data that each variable is expected to hold.

Variable annotations are not enforced at runtime, meaning that Python will not raise any type errors if a variable's value does not match its annotation. However, you can use tools like *mypy* to perform static type checking and validate your code against the annotations.

Annotations can also be used with function parameters and return types. Here's a simple example:

```python
def greet(name: str) -> str:
    return "Hello, " + name

message: str = greet("Alice")
print(message)  # Output: Hello, Alice
```

In the above code, the `greet` function has an annotated parameter `name` of type `str` and an annotated return type of `str`. This helps make it clear what the function expects as input and what it returns.

Variable annotations can also be used in class definitions. Here's an example:

```python
class Circle:
    radius: float
    circumference: float

    def __init__(self, radius: float):
        self.radius = radius
        self.circumference = 2 * 3.14 * radius
```

In this example, the `Circle` class has variables `radius` and `circumference` annotated with the `float` type. This makes it easier to understand the data types used in the class.

Variable annotations are a great addition to Python, providing clearer code documentation and improving code quality. However, remember that they are optional and not enforced by the Python interpreter. It's always recommended to use static type checking tools like *mypy* to validate your code against the annotations.

I hope you found this blog post helpful in understanding variable annotations in Python. Happy coding!