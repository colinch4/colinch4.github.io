---
layout: post
title: "Else statement in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here is the general syntax of an `if-else` statement in Python:

```python
if condition:
    # code to execute if the condition is True
else:
    # code to execute if the condition is False
```

Example:

```python
age = 18

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")
```

In this example, if the `age` variable is greater than or equal to `18`, the first block of code will be executed and the message "You are eligible to vote!" will be printed. Otherwise, if the `age` is less than `18`, the second block of code will be executed and the message "You are not eligible to vote yet." will be printed.

The `else` statement provides an alternative set of actions to be executed when the condition in the `if` statement is `False`. It is a convenient way to handle situations where you want to perform different actions based on the outcome of a condition.