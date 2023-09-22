---
layout: post
title: "Using if statement to check for non-empty values in Python"
description: " "
date: 2023-09-21
tags: [ConditionalStatements]
comments: true
share: true
---

In Python, you can use an `if` statement to check if a value is empty or not. To determine if a value is non-empty, you can use the `not` keyword along with the `is` or `!=` operator. Here's an example:

```python
name = input("Enter your name: ")

if not name.strip():
    print("Name cannot be empty.")
else:
    print(f"Welcome, {name}!")
```

In the above code, we first prompt the user to enter their name using the `input()` function. Then, we use the `strip()` method to remove any leading or trailing whitespace from the input.

Next, we use the `if` statement to check if the value of `name` is empty or not. The `not name.strip()` expression evaluates to `True` if `name` is an empty string, and `False` otherwise.

If `name` is empty, the code inside the `if` block will execute and print the message "Name cannot be empty." Otherwise, the code inside the `else` block will execute, welcoming the user by printing their name.

By using the `not` keyword and checking for an empty string, you can easily determine if a value is non-empty or not in Python.

Remember to sanitize and validate user input, as the above code only checks for an empty string. Depending on your use case, you may need to perform additional checks and validations.

#Python #ConditionalStatements