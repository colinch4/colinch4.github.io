---
layout: post
title: "Recommendations for using whitespace in function arguments and parameters in PEP 8"
description: " "
date: 2023-09-27
tags: [PEP8]
comments: true
share: true
---

Here are some important guidelines for using whitespace in function arguments and parameters:

1. **Parentheses**: Leave no whitespace directly inside the parentheses when defining a function or calling it.
```python
# Good
def foo(arg1, arg2):
    ...

result = foo(10, 20)

# Bad
def foo( arg1 , arg2 ):
    ...

result = foo( 10 , 20 )
```
2. **Commas**: Use a single space after each comma to separate function arguments.
```python
# Good
def foo(arg1, arg2, arg3):
    ...

# Bad
def foo(arg1,arg2,arg3):
    ...
```
3. **Indentation**: When wrapping function arguments onto multiple lines, use consistent indentation. Indent the arguments by four spaces to clearly distinguish them from the function name.
```python
# Good
result = some_function(
    long_argument1,
    long_argument2,
    long_argument3
)

# Bad
result = some_function(
long_argument1,
long_argument2,
long_argument3
)
```
4. **Multi-line Parameters**: If a function signature has multiple lines, align the parameters vertically. This enhances readability and helps identify each parameter easily.
```python
# Good
def some_function(
        argument1,
        argument2,
        argument3
):
    ...

# Bad
def some_function(argument1,
                  argument2,
                  argument3):
    ...
```

By following these whitespace guidelines, you can create clean and readable code that conforms to PEP 8 standards. Remember that consistent and clear code is easier to collaborate on and maintain in the long run.

#Python #PEP8