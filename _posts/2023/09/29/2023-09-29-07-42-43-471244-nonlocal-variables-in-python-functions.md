---
layout: post
title: "Nonlocal variables in Python functions"
description: " "
date: 2023-09-29
tags: []
comments: true
share: true
---

In Python, nonlocal variables are used to refer to variables in the outer enclosing (non-global) scope of a nested function. It allows you to access and modify variables that are outside the immediate local scope of a function.

To better understand nonlocal variables, let's consider an example.

```python
def outer_function():
    x = "local"
    
    def inner_function():
        nonlocal x
        x = "nonlocal"
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()
```

In this example, we define an outer function called `outer_function` which has a nested function called `inner_function`. Inside `outer_function`, we define a variable `x` and assign it the value of `"local"`.

Now, inside `inner_function`, we want to modify the value of `x`. To do so, we use the `nonlocal` keyword before `x`. This tells Python that `x` is a nonlocal variable, and any modification to it should be reflected in the outer scope.

After modifying `x`, we print out its value within both functions. The output will be:

```
Inner function: nonlocal
Outer function: nonlocal
```

As you can see, the modification to `x` inside the inner function affects its value in the outer function as well. Without the use of `nonlocal`, `x` would be considered a local variable in `inner_function` and a separate local variable would be created in that scope.

It's important to note that the use of `nonlocal` is relevant only when there is a nested function involved. If the variable is in the global scope, you can directly modify it without using `nonlocal` or `global` keywords.

## Conclusion

Nonlocal variables provide a way to access and modify variables in the outer scope of a nested function. This allows for more flexible and dynamic programming within nested function structures. Just remember to use the `nonlocal` keyword when you want to modify a variable defined in an enclosing scope.