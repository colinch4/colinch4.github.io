---
layout: post
title: "Python type annotations in MyPy"
description: " "
date: 2023-09-20
tags: [TypeAnnotations]
comments: true
share: true
---

Type annotations in Python provide a way to explicitly declare the type of variables, function parameters, and return values. This enables static type checking and allows tools like MyPy to analyze your code and flag potential type errors.

To start using type annotations in Python, you need Python 3.5 or higher. Let's begin by importing the `annotations` module from the typing module:

```python
from typing import annotations
```

Now, let's look at some examples of how type annotations work in Python:

### Basic Type Annotations

```python
name: str = "John"
age: int = 27
is_student: bool = True
```

In this example, we declare the `name` variable as a string, `age` as an integer, and `is_student` as a boolean.

### Function Annotations

```python
def greet(name: str) -> str:
    return "Hello, " + name
```

Here, we annotate both the `name` parameter and the return type of the function `greet` as strings.

### Type Annotations for Collection Types

```python
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5]
```

In this example, we use the `List` type from the typing module to specify that `numbers` is a list of integers.

### Optional Types

```python
from typing import Optional

def get_name(uppercase: Optional[bool] = False) -> str:
    name = "John"
    if uppercase:
        return name.upper()
    else:
        return name
```

The `Optional` type allows us to specify that a parameter can be `None` in addition to its declared type. Here, the `uppercase` parameter has a default value of `False`, but it can also be `None`.

### Type Annotations for Classes

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

In this example, we annotate the constructor of the `Person` class, specifying that the `name` parameter should be a string and the `age` parameter should be an integer.

To perform static type checking using MyPy, you can simply run the `mypy` command followed by the name of your Python file:

```
mypy myscript.py
```

Type annotations in Python bring the benefits of static typing while still maintaining the language's dynamic nature. They help catch errors early on, improve code readability, and enhance collaboration between developers.

So, why not start using type annotations and MyPy in your Python projects today? #Python #TypeAnnotations