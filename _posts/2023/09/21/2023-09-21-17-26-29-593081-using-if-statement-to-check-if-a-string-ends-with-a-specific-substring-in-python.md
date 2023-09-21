---
layout: post
title: "Using if statement to check if a string ends with a specific substring in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here's an example code snippet that demonstrates how to use the `endswith()` function:

```python
# Define the main string
main_string = "Hello, world!"

# Define the substring to check
substring = "world!"

# Check if the main string ends with the substring
if main_string.endswith(substring):
    print("The string ends with the provided substring.")
else:
    print("The string does not end with the provided substring.")
```

In the above code, we assign the main string to the variable `main_string` and the substring to the variable `substring`. We then use the `endswith()` function to check if `main_string` ends with `substring`.

If the condition evaluates to `True`, it means that the string ends with the specified substring, and we print a corresponding message. Otherwise, if the condition is `False`, we print a different message indicating that the string does not end with the specified substring.

By using the `endswith()` function in conjunction with an `if` statement, you can easily determine whether a string ends with a specific substring in Python.