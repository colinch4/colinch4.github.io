---
layout: post
title: "[Python] Variable scoping in nested functions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Global and local scope

In Python, variables have different scopes depending on where they are defined. The two main scopes are the **global** scope and the **local** scope. Variables defined outside of any function are considered global, meaning they can be accessed and modified from anywhere within the code. On the other hand, variables defined inside a function body are considered local to that function and can only be accessed within that function.

Here's an example to illustrate this concept:

```python
x = 10  # global variable

def foo():
    y = 20  # local variable
    print(x)  # accessing global variable
    print(y)  # accessing local variable

foo()
```

In this example, `x` is a global variable, so it is accessible within the `foo()` function. However, `y` is a local variable and can only be accessed within the `foo()` function. Running the code will output:
```
10
20
```

## Variable scoping in nested functions

Things get a bit more interesting when we introduce nested functions, which are functions defined inside other functions. In Python, nested functions have access to variables defined in the enclosing function's scope, as well as the global scope, but not vice versa.

Consider the following example:

```python
def outer():
    x = 10  # local variable

    def inner():
        y = 20  # local variable
        print(x)  # accessing variable from outer scope
        print(y)

    inner()

outer()
```

In this example, `inner()` is a nested function within `outer()`. The `inner()` function has access to the `x` variable defined in the `outer()` function's scope. Running the code will output:
```
10
20
```

However, if we try to access a variable defined inside the nested function from the outer function, we will encounter an error:

```python
def outer():
    def inner():
        y = 20  # local variable
        print(y)

    print(y)  # trying to access variable from inner scope

outer()
```

This code will result in a `NameError` because `y` is only defined within the `inner()` function's scope and is inaccessible outside of it.

## The `nonlocal` keyword

Now, what if we want to access a variable in the outer function and modify its value from within the nested function? This is where the `nonlocal` keyword comes into play. The `nonlocal` keyword allows us to indicate that a variable is not local to the nested function, but rather in the outer function's scope.

Let's modify our previous example to illustrate the use of the `nonlocal` keyword:

```python
def outer():
    x = 10  # local variable

    def inner():
        nonlocal x  # accessing variable from outer scope
        x += 5
        print(x)

    inner()
    print(x)  # modified value should reflect in outer scope

outer()
```

In this updated code, we use the `nonlocal` keyword to indicate that `x` is not a local variable, but rather in the outer function's scope. Running the code will output:
```
15
15
```

As you can see, the `x` variable in the outer function is successfully modified within the nested function.

## Best practices and recommendations

To avoid scoping-related issues in nested functions, it is recommended to follow these best practices:

1. **Avoid modifying global variables within nested functions:** Modifying global variables within nested functions can make code harder to understand and troubleshoot. Instead, consider passing variables as arguments to the nested functions and returning any modified values.

2. **Use separate names for local and global variables:** To avoid confusion between local and global variables, it is a good practice to use different names for them. This reduces the chance of accidental variable shadowing.

3. **Keep functions short and focused:** By keeping functions short and focused, you can minimize the need for nested functions and reduce the complexity of variable scoping.

By understanding how variable scoping works in nested functions and following these recommendations, you can effectively manage variable access and manipulation in your Python code.