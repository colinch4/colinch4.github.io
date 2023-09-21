---
layout: post
title: "Conditional statement with boolean values in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

In Python, a conditional statement is used to execute a certain block of code based on a condition. The condition is usually a boolean value, which can either be `True` or `False`. Here is an example of how to use a conditional statement with boolean values in Python:

```python
# Define a boolean variable
is_sunny = True

# Check the condition using if statement
if is_sunny:
    print("It's a sunny day!")
else:
    print("It's not sunny today.")
```

In the above example, we have a boolean variable `is_sunny` which is set to `True`. We use an `if` statement to check the value of `is_sunny`. If the condition is `True`, it executes the block of code inside the `if` statement, which prints "It's a sunny day!". If the condition is `False`, it executes the block of code inside the `else` statement, which prints "It's not sunny today."

You can also use comparison operators to evaluate boolean conditions. For example:

```python
# Define two numeric variables
temperature = 30
threshold = 25

# Check the condition using if statement with comparison operator
if temperature > threshold:
    print("It's hot today!")
else:
    print("It's not that hot.")
```

In this example, we compare the values of `temperature` and `threshold`. If `temperature` is greater than `threshold`, it prints "It's hot today!". Otherwise, it prints "It's not that hot."

Remember to use a colon `:` after the `if` statement and the `else` statement, and indent the block of code that should be executed when the condition is `True` or `False`.

With boolean values and conditional statements, you can make your Python code more dynamic and responsive to different situations.