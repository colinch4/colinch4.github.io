---
layout: post
title: "Scope and lifetime of variables in Python functions"
description: " "
date: 2023-09-29
tags: []
comments: true
share: true
---

Understanding the scope and lifetime of variables is important when writing Python functions. Scope refers to the accessibility or visibility of variables within a program, while lifetime refers to the duration for which a variable exists in memory during program execution. 

Python has two types of scopes:
1. **Global scope**: Variables defined outside all functions or classes have global scope and can be accessed from anywhere in the program.
2. **Local scope**: Variables defined inside a function have local scope and can only be accessed within that function.

## Local Variables

Local variables are created when a function is called and are destroyed when the function completes execution or is exited. They cannot be accessed outside the function.

Let's look at an example:

```python
def my_function():
    x = 10
    print(x)

my_function()
```

In this example, `x` is a local variable defined within the `my_function()` function. It has a lifetime limited to the execution of the function. When the function is called, `x` is assigned the value of 10 and printed. Once the function completes, `x` will be destroyed.

## Global Variables

Global variables are accessible from any part of the program, including inside functions. However, if a local variable with the same name is defined within a function, it will take precedence over the global variable.

Let's see an example:

```python
x = 10

def my_function():
    x = 5
    print(x)

my_function()
print(x)
```

In this example, `x` is a global variable defined outside the function. Within the function `my_function()`, a local variable `x` is also defined. When we print the value of `x` inside the function, it will output 5, the value of the local variable. However, outside the function, the global variable `x` retains its value of 10.

## Using Global Keyword

If you want to modify a global variable within a function, you need to use the `global` keyword. This informs Python that the variable being modified is a global variable and not a local variable.

```python
x = 10

def my_function():
    global x
    x = 5
    print(x)

my_function()
print(x)
```

In this example, the `global` keyword is used to indicate that `x` inside the function is the global variable and not a local variable. Therefore, when the value of `x` is modified inside the function, it also affects the global variable `x` outside the function. Both print statements will output 5.

## Conclusion

Understanding the scope and lifetime of variables in Python functions is crucial for writing reliable and efficient code. By defining variables within the appropriate scope, you can ensure that your code behaves as expected and avoids any conflicts between global and local variables.