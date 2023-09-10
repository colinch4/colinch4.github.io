---
layout: post
title: "[Python] Reflection and variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, *reflection* refers to the ability of a program to examine its own structure and properties at runtime. It allows you to access information about modules, classes, functions, and objects, and perform operations dynamically based on that information. One important aspect of reflection is the ability to work with variables dynamically.

## Accessing variable names as strings

To access the name of a variable as a string, you can use the `globals()` or `locals()` functions, which return a dictionary of global and local variable names respectively. By iterating through the dictionary, you can access the variable names as strings.

```python
var_name = 'example'

def get_variable_name(var_value):
    for name, value in globals().items():
        if value is var_value:
            return name
    return None

print(get_variable_name(example))  # Output: 'var_name'
```

In the example above, the `get_variable_name()` function takes a variable value and checks against all global variables. If a match is found, it returns the corresponding variable name as a string. In this case, it would return "var_name", which is the name of the variable assigned to the "example" value.

## Dynamically creating variables

Python also allows you to *dynamically create variables* using reflection. You can achieve this by using the `exec()` function, which executes a string of code as Python code.

```python
var_name = 'example'
var_value = 10

exec(f'{var_name} = {var_value}')

print(example)  # Output: 10
```

In the example above, the `exec()` function creates a variable with the name specified in the `var_name` variable and assigns it the value of `var_value`. After executing the code, we can access the dynamically created variable `example` and print its value, which is 10.

## Modifying variables dynamically

Using reflection, you can also *modify variables dynamically* by accessing and updating their values at runtime.

```python
var_name = 'example'
example = 10

# Get the value of the variable using reflection
var_value = globals()[var_name]

# Modify the value of the variable dynamically
globals()[var_name] = 20

print(example)  # Output: 20
```

In the example above, we first retrieve the value of the `example` variable using reflection by accessing the `globals()` dictionary with the `var_name` as the key. We then modify the value of the variable by assigning a new value to it using the `globals()` dictionary.

Reflection and working with variables dynamically can be powerful tools in Python, allowing you to write more flexible and adaptable code. However, it is important to use them judiciously and appropriately for the specific problem at hand.