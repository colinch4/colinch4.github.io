---
layout: post
title: "Null Coalescing pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

In Python, there is no direct null coalescing operator like in some other programming languages. However, you can achieve the null coalescing pattern using a conditional expression.

## What is the null coalescing pattern?

The null coalescing pattern allows you to provide a default value when dealing with null or undefined variables. It helps to handle cases where you want to assign a fallback value in case a variable is null.

## Using the null coalescing pattern in Python

To apply the null coalescing pattern in Python, you can use the conditional expression (`if-else`) syntax. Here's an example code that demonstrates the null coalescing pattern:

```python
# Example 1: Assigning a default value to a variable
my_variable = None
fallback_value = "Default Value"

result = my_variable if my_variable is not None else fallback_value

print(result)  # Output: Default Value
```

In the above code, the variable `my_variable` is assigned a `None` value. We then use the null coalescing pattern to assign a fallback value to the variable `result`. If `my_variable` is not `None`, its value will be assigned to `result`. Otherwise, `fallback_value` will be assigned.

You can also use the null coalescing pattern with function arguments or return values. Consider the following example:

```python
# Example 2: Providing a default value for function arguments
def greet(name=None):
    name = name if name is not None else "Stranger"
    print(f"Hello, {name}!")

greet()  # Output: Hello, Stranger!
greet("John")  # Output: Hello, John!
```

In this example, the `greet` function takes an optional `name` argument. If the `name` argument is not provided or is `None`, the null coalescing pattern assigns the value `"Stranger"` to the `name` variable.

## Conclusion

Although Python doesn't have a direct null coalescing operator, you can achieve the same effect using a conditional expression. By incorporating the null coalescing pattern, you can write more robust code and handle null or undefined values gracefully.