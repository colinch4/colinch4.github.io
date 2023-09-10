---
layout: post
title: "[Python] Nonlocal keyword in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, the `nonlocal` keyword is used to access variables defined in the nearest enclosing scope that is not global. While `global` keyword allows us to modify a global variable from within a nested scope, `nonlocal` allows us to modify a variable from an outer nested scope. 

By default, when we assign a value to a variable inside a function, Python considers it as a local variable. However, sometimes we may want to modify variables defined in an outer scope. This is where the `nonlocal` keyword comes in handy.

To demonstrate the usage of `nonlocal`, let's consider an example where we have a nested function and we want to modify a variable defined in the outer function.

```python
def outer_function():
    x = "outer"  # variable defined in the outer function
    
    def inner_function():
        nonlocal x
        x = "inner"  # modifying the variable defined in outer function
    
    inner_function()
    print(x)  # output: "inner"

outer_function()
```

In the above example, we have an `outer_function` that defines a variable `x`. Inside the `inner_function`, we use the `nonlocal` keyword to indicate that we want to modify the `x` defined in the outer function scope. After modifying the value of `x` to `"inner"`, when we print `x` in the outer function, it will give us the updated value.

It's important to note that the `nonlocal` keyword will only work if there is an enclosing scope where the variable is defined. If there is no outer scope with the defined variable, Python will raise a `SyntaxError`.

```python
def outer_function():
    def inner_function():
        nonlocal x  # Raises SyntaxError: no binding for nonlocal 'x' found
        
    inner_function()
    
outer_function()
```

In this case, since there is no `x` defined in the enclosing scope, Python raises a `SyntaxError` stating that there is no binding for the nonlocal variable `x`.

The `nonlocal` keyword is a powerful tool when working with nested functions in Python. It allows us to modify variables in outer scopes, providing flexibility and control over our code.