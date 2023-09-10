---
layout: post
title: "[Python] Error types in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, **errors** are a common occurrence during the development process. They are raised when there is an issue with the execution of the code, such as syntax errors, runtime errors, or logical errors. Understanding the different types of errors can help in debugging and resolving them more efficiently. This blog post will introduce you to some of the commonly encountered error types in Python.

## Syntax Errors
Syntax errors, also known as parsing errors, occur when the code violates the syntax rules of the Python language. These errors are raised by the Python interpreter when it encounters code that it cannot parse.

Example of a syntax error:
```python
def my_function()
    print("Hello, World!")
```

In this example, we are missing a colon `:` at the end of line 1, which causes a syntax error. The proper syntax for defining a function in Python is to use a colon after the function name.

## Runtime Errors (Exceptions)
Runtime errors, also known as exceptions, occur during the execution of a program. They are caused by various factors, such as invalid input, improper use of built-in functions or modules, or data type mismatches.

Some common runtime errors in Python include:

### NameError
A `NameError` is raised when a local or global name is not found. This usually occurs when a variable is referenced before being assigned a value.

Example:
```python
print(x)
```

In this example, if the variable `x` is not defined or assigned a value, a `NameError` will be raised.

### TypeError
A `TypeError` is raised when an operation or function is applied to an object of an inappropriate type.

Example:
```python
x = 5 + "10"
```

In this example, we are attempting to perform addition between an integer and a string, which results in a `TypeError`.

### ValueError
A `ValueError` is raised when a function receives an argument of the correct type but an inappropriate value.

Example:
```python
x = int("abc")
```

In this example, the `int()` function cannot convert the string "abc" to an integer, which raises a `ValueError`.

## Logical Errors
Logical errors are bugs in the code that do not cause any error messages or exceptions but result in incorrect output or unexpected behavior. These types of errors can be challenging to identify and fix.

Example:
```python
def calculate_average(num1, num2):
    average = (num1 + num2) / 3
    return average

result = calculate_average(10, 5)
print(result)
```

In this example, we are trying to calculate the average of two numbers by dividing their sum by 3. However, the correct calculation would be to divide by 2. This logical error will not raise any exceptions but will result in incorrect output.

## Conclusion
Understanding the different error types in Python is essential for effective debugging and writing robust code. Syntax errors occur during the parsing phase, while runtime errors are raised during program execution. Logical errors can be challenging to identify but can lead to incorrect outputs. By familiarizing yourself with these error types, you can become a more skilled Python programmer.

Keep coding and happy debugging!