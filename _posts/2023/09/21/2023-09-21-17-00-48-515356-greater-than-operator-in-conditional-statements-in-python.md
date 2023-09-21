---
layout: post
title: "Greater than operator in conditional statements in Python"
description: " "
date: 2023-09-21
tags: [Python, ConditionalStatements]
comments: true
share: true
---

```python
# Example 1: Using the greater than operator in conditional statements
x = 5
y = 10

if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")
```

In this example, we assign the values 5 to `x` and 10 to `y`. We then use the greater than operator in the `if` statement to check if `x` is greater than `y`. Since `x` is not greater than `y`, the code block under the `else` statement is executed, and "y is greater than or equal to x" is printed.

The greater than operator can also be used with variables, expressions, or any valid Python value. Here's another example:

```python
# Example 2: Using the greater than operator with variables
a = 7
b = 3

result = a > b

print(result)  # Outputs True
```

In this case, we compare the values of `a` and `b` using the greater than operator and store the result in the `result` variable. We then print the value of `result`, which is `True` since `a` is indeed greater than `b`.

Remember that the greater than operator only checks for numerical or alphabetical comparison, depending on the data types being compared. If you're comparing strings, it will follow the lexicographical order.

That's it! You now have a good understanding of how to use the greater than operator in conditional statements in Python. Have fun coding!

**#Python #ConditionalStatements**