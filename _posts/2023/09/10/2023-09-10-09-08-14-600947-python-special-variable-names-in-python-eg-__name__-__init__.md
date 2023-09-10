---
layout: post
title: "[Python] Special variable names in Python (e.g., __name__, __init__)"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Python is a versatile and powerful programming language that allows developers to write clean and efficient code. One aspect that sets Python apart is its use of special variable names, which provide additional functionality and flexibility to the code.

In this blog post, we will explore two of the most commonly used special variable names in Python: `__name__` and `__init__`. We will discuss their purpose and how they can be utilized in different contexts.

## `__name__`

The `__name__` variable is a built-in variable in Python that is automatically created and assigned a value depending on how the Python script is executed. This variable is mainly used to identify whether the code is being run as a standalone script or imported as a module.

When a Python script is executed directly, the `__name__` variable is set to `"__main__"`. On the other hand, when the script is imported as a module into another script, the `__name__` variable is set to the name of the module.

```python
# main.py

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

In the example above, the `main()` function will only be executed if the script is run directly. This allows us to have specific code that should only run when the script is executed as the main entry point.

## `__init__`

The `__init__` method is a special method in Python classes that is automatically called when an object is created from a class. It is commonly used to initialize and set the initial state of the object.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Tesla", "Model 3", 2022)
print(my_car.make)  # Output: "Tesla"
```

In the example above, the `__init__` method is used to initialize the `Car` object with the specified make, model, and year. These values are then stored in instance variables (`self.make`, `self.model`, `self.year`) and can be accessed using dot notation.

The `__init__` method is especially useful when we need to perform some setup or initialization logic before using the object. It allows us to define and assign initial values to the object's attributes.

## Conclusion

Special variable names in Python like `__name__` and `__init__` enhance the functionality and flexibility of the code. These variables provide additional context and allow us to write code that is more modular and reusable.

Understanding and utilizing these special variable names can greatly improve the quality and maintainability of our Python code. So, the next time you come across `__name__` or `__init__`, you'll have a better understanding of their purpose and how to use them effectively.