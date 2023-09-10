---
layout: post
title: "[Python] Namespaces and variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, a **namespace** is a mapping between names and objects. It acts as a container for storing variables, functions, classes, and other objects.

## Understanding Namespaces

Each Python program has several namespaces, including the **global namespace**, **local namespace**, and **built-in namespace**.

- **Global Namespace**: It stores names that are defined at the top level of a module or declared as global within a function. These names can be accessed from anywhere in the program.

- **Local Namespace**: It stores names that are defined within a function or a method. These names are only accessible within the function or method where they are defined.

- **Built-in Namespace**: It contains the predefined names that are automatically available in Python. These names refer to functions and types like print(), len(), str(), etc.

## Variables in Namespaces

**Variables** are names that refer to a value or an object. They are created when a value is assigned to a name.

Here's an example to illustrate variables in different namespaces:

```python
# Global namespace
global_var = 10

def my_function():
    # Local namespace
    local_var = 20
    print("Local variable:", local_var)

    # Accessing global variable within a function
    print("Global variable within function:", global_var)

my_function()
print("Global variable in main program:", global_var)
```

Output:

```
Local variable: 20
Global variable within function: 10
Global variable in main program: 10
```

In the code above, `global_var` is a global variable defined outside any functions. Inside `my_function()`, a local variable `local_var` is defined. The `print()` statements access both the local and global variables.

## Modifying Variables

Variables in different namespaces can be modified using the `global` keyword to reference a global variable within a function. However, modifying a global variable inside a function is generally not recommended as it can lead to code confusion and side effects.

```python
global_var = 10

def modify_variable():
    global global_var
    global_var = 20

print("Global variable before modification:", global_var)
modify_variable()
print("Global variable after modification:", global_var)
```

Output:

```
Global variable before modification: 10
Global variable after modification: 20
```

In the above example, the `modify_variable()` function uses the `global` keyword to indicate that it wants to modify the `global_var` variable. As a result, the global variable `global_var` is changed to 20.

## Conclusion

Understanding namespaces and variables in Python is essential for writing clean and maintainable code. Remember that variable scope is important, and modifying global variables within functions should be used sparingly.