---
layout: post
title: "[Python] Local keyword in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, the `local` keyword is used to declare a variable as local within a function. When we declare a variable inside a function, it is by default considered a local variable, meaning its scope is limited to that particular function.

## Scope in Python

Scope refers to the accessibility or visibility of variables, functions, and objects in some particular part of your code during runtime. In Python, there are three types of scope:

1. Local scope: Variables defined inside a function can only be accessed within that function.
2. Global scope: Variables defined outside of any function or class can be accessed from anywhere in the code.
3. Enclosing scope: Variables defined within nested functions can be accessed from the innermost nested function to the outermost function.

## Using the local keyword

Let's see an example to understand how the `local` keyword works:

```python
def my_function():
    local_var = 5
    print(local_var)

my_function()
print(local_var)  # Raises NameError
```

In the code above, we have a function called `my_function()` in which we define a variable `local_var` and assign it a value of 5. Inside the function, we print the value of `local_var`. If we call `my_function()`, it will print `5` as expected.

However, if we try to access `local_var` outside the function, as shown in the second `print` statement, it will raise a `NameError` because the variable is not defined in the global scope.

Note that using the `local` keyword explicitly is not necessary in Python. By default, any variable defined within a function is treated as a local variable.

## Benefits of using the local keyword

Explicitly declaring a variable as `local` within a function can be useful in scenarios where there is a need to distinguish between a local and a global variable with the same name. By doing so, we avoid potential conflicts and ensure that the intended variable is being used.

```python
my_var = 10

def my_function():
    my_var = 5
    print(my_var)  # Prints 5

my_function()
print(my_var)  # Prints 10
```

In the code snippet above, we have a global variable `my_var` with a value of `10`. Inside the function `my_function()`, we declare a local variable with the same name `my_var` and assign it a value of `5`. When we call `my_function()` and print `my_var` within the function, it will print `5`. However, `print(my_var)` outside the function will print `10` since it refers to the global variable.

Using the `local` keyword in such situations helps to avoid confusion and ensures that we are working with the intended variable.

## Conclusion

The `local` keyword in Python is not a separate keyword but rather a default behavior when defining variables within a function. Understanding the concept of local scope and using it appropriately can help write cleaner and more readable code by minimizing variable name clashes and improving code organization.