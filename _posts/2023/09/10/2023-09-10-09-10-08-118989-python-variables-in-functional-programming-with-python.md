---
layout: post
title: "[Python] Variables in functional programming with Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In functional programming, the concept of variables differs slightly from traditional imperative programming. In this blog post, we will explore how variables are handled in functional programming using Python.

## Immutability of Variables

In functional programming, **variables are immutable**, meaning their value cannot be changed once they are assigned. This principle aligns with the functional programming paradigm, where functions produce new values instead of modifying existing ones.

Let's see an example:

```python
x = 5
x = x + 1
print(x)
```

Output:
```
6
```

In the above code snippet, even though we used the `=` operator to reassign a new value to `x`, we are not modifying its original value. Instead, a new value is created and assigned to `x`. The original value of `x` remains unchanged.

## Pure Functions

In functional programming, the best practice is to write **pure functions**. A pure function is a function that doesn't have any side effects and always produces the same output for the same input, regardless of the state of the program.

Pure functions should not rely on or modify external state, including variables outside the function scope. The output of the function should solely depend on the input parameters.

```python
def add(a, b):
    return a + b
```

The `add()` function above is an example of a pure function. It takes two input parameters `a` and `b` and returns their sum. It doesn't rely on any external variables or modify any state. Given the same inputs, it will always produce the same output.

## Variable Scope

In functional programming, variable scope should be limited to the smallest possible scope. Minimizing the scope of variables helps in writing pure functions and reduces the possibility of unintended side effects.

To limit the scope of variables, we can define them within the function or use **closure**. A closure is a function that remembers the values in its enclosing scope, even if they are not available in the current scope.

```python
def create_multiplier(multiplier):
    def multiply(num):
        return num * multiplier
    
    return multiply

double = create_multiplier(2)
print(double(5))
```

Output:
```
10
```

In the above example, the `create_multiplier()` function returns a closure `multiply()`. The closure remembers the value of `multiplier` even after the `create_multiplier()` function has finished executing. When we call `double(5)`, it multiplies the input `5` by the remembered `multiplier` value of `2`.

## Conclusion

Variables in functional programming are immutable, and the focus is on writing pure functions that do not have side effects. By limiting the scope of variables and using closures, we can effectively write functional code in Python.

Functional programming can provide many benefits such as improved code maintainability, testability, and concurrency. It encourages a declarative style of programming and can lead to elegant and concise code.