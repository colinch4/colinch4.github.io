---
layout: post
title: "Using if statement to check if a string is a valid email address in Python"
description: " "
date: 2023-09-21
tags: [EmailValidation]
comments: true
share: true
---

Here's an example code snippet on how to check the validity of an email address using an `if` statement and regular expressions in Python:

```python
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email_address = input("Enter an email address: ")
if is_valid_email(email_address):
    print("Valid email address")
else:
    print("Invalid email address")
```

In the above code, we define a `is_valid_email` function that takes an email address as input. We define a regular expression pattern `r'^[\w\.-]+@[\w\.-]+\.\w+$'` that matches the standard email format. The `re.match()` function is then used to match the pattern against the email address string.

Inside the `if` statement, we check if `re.match()` returns a match object, indicating that the email address matches the pattern. If it does, we return `True`, indicating that the email is valid. Otherwise, we return `False`, indicating that the email is invalid.

Finally, we test the function by taking an email address from the user and calling the `is_valid_email` function. The result is printed based on the validity of the email address.

Using this simple `if` statement with regular expressions allows you to easily check if a string is a valid email address in Python. #Python #EmailValidation