---
layout: post
title: "[Python] Global constants and variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, global constants and variables are used to store values that need to be accessed or modified throughout the entire program. These variables and constants have a global scope, meaning they can be accessed from any part of the code.

## Global Variables

Global variables are defined outside any function or class. They are accessible from any function within the program. To create a global variable, simply assign a value to a variable outside of any function or class definition.

```python
# Define a global variable
global_var = 10

def some_function():
    # Access the global variable
    print(f"The value of global_var is {global_var}")

some_function()  # Output: The value of global_var is 10
```

In the above example, we defined a global variable `global_var` and accessed it inside the `some_function()`.

If you need to modify the value of a global variable inside a function, use the `global` keyword to indicate that you are referring to the global variable and not creating a new local variable.

```python
# Define a global variable
global_var = 10

def modify_global_variable():
    global global_var
    global_var += 5

modify_global_variable()

print(global_var)  # Output: 15
```

In the above example, the `modify_global_variable()` function references the global variable `global_var` using the `global` keyword. By incrementing its value by 5, the global variable is modified.

## Global Constants

Global constants are similar to global variables but their values cannot be changed once they are assigned. Conventionally, the names of global constants are written in uppercase letters to distinguish them from variables.

```python
# Define a global constant
GLOBAL_CONSTANT = 3.14159

def calculate_area(radius):
    area = GLOBAL_CONSTANT * radius * radius
    return area

print(calculate_area(5))  # Output: 78.53975
```

In the above example, the `GLOBAL_CONSTANT` is assigned a value of pi (3.14159). It is used inside the `calculate_area()` function to calculate the area of a circle.

## Conclusion

Global constants and variables provide a way to store values that are accessible throughout the entire program. By defining global variables outside functions and classes, we can access and modify them from any part of the code. Global constants, on the other hand, contain values that remain constant throughout the execution of the program.

However, the use of global variables and constants should be minimized to avoid making the code difficult to understand and maintain. It is generally recommended to encapsulate data in classes and use class-level variables and constants instead.