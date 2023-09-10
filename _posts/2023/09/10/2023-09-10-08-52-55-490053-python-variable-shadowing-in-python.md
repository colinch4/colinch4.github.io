---
layout: post
title: "[Python] Variable shadowing in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, variable shadowing occurs when a variable in an inner scope has the same name as a variable in an outer scope. This means that the inner variable "shadows" or takes precedence over the outer variable, preventing access to the outer variable within the inner scope.

Variable shadowing can lead to confusion and unexpected behavior in your code. It's essential to understand how it works and how to avoid it.

## Example of Variable Shadowing

Let's look at an example to illustrate variable shadowing:

```python
x = 5

def my_function():
    x = 10
    print(x)

my_function()
print(x)
```

In this example, we have a global variable `x` with a value of 5. Inside the `my_function` function, we declare a local variable `x` with a value of 10. When we call `my_function`, it prints the value of the local `x`, which is 10. 

After calling `my_function`, we print the global `x` value, which is still 5. The local variable `x` inside `my_function` does not affect the value of the global `x` variable.

## The Scope Hierarchy in Python

Python follows a particular scope hierarchy to resolve variable names. It first searches for the variable in the innermost scope, moving outward until it finds a variable with the given name. If no variable is found, a `NameError` is raised.

The scope hierarchy follows this order:

1. Local Variables: Variables defined within a function.
2. Enclosing Function Variables: Variables defined in the immediate enclosing function, if any.
3. Global Variables: Variables defined in the global scope or at the module level.
4. Built-in Variables: Predefined variables in Python like `print`, `range`, `len`, etc.

## Avoiding Variable Shadowing

To avoid variable shadowing and maintain code clarity, consider the following best practices:

1. Use distinct and descriptive variable names: Choosing meaningful names for your variables can help prevent shadowing issues.
2. Limit the use of global variables: Minimize the use of global variables and use them only when necessary.
3. Avoid reusing variable names within a scope: Reusing variable names can lead to confusion and bugs. Use different names for variables in different scopes.
4. Be cautious with function arguments: Be mindful of using the same variable name as a function argument and a global variable.

By adhering to these best practices, you can reduce the chances of variable shadowing and ensure code clarity and maintainability.

## Conclusion

Variable shadowing in Python can introduce confusion and unexpected behavior in your code. Understanding how variable resolution works and following best practices can help you avoid shadowing issues and write more readable and maintainable code.

Remember to use distinct and descriptive variable names, limit the use of global variables, and be cautious when reusing variable names within a scope. By following these guidelines, you can prevent variable shadowing and write cleaner code.