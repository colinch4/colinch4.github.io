---
layout: post
title: "Using if statement to check if a string is a valid phone number in Python"
description: " "
date: 2023-09-21
tags: [python, phonenumber, validation]
comments: true
share: true
---

When working with strings in Python, it's often necessary to validate whether a particular string represents a valid phone number. In this blog post, we'll explore how to use the `if` statement to check if a given string is a valid phone number in Python.

### Approach

A simple approach to validate a phone number is by using regular expressions, which can help identify the pattern of a valid phone number. Let's consider the following criteria for a valid phone number:

- The phone number must have 10 digits.
- It may contain optional dashes (-) or spaces.
- It should not start with a country code.

### Regular expression pattern

To check the validity of a phone number, we can use the built-in `re` module in Python along with a regular expression pattern. Here's an example pattern that matches the criteria mentioned above:

```python
import re

def is_valid_phone_number(phone_number):
    pattern = r"^[2-9]\d{2}[-\s]?\d{3}[-\s]?\d{4}$"
    return re.match(pattern, phone_number) is not None
```

The regular expression pattern, `^[2-9]\d{2}[-\s]?\d{3}[-\s]?\d{4}$`, breaks down as follows:
- `^[2-9]`: Matches a digit from 2 to 9 at the start of the string.
- `\d{2}`: Matches any two digits.
- `[-\s]?`: Matches an optional dash (-) or space.
- `\d{3}`: Matches any three digits.
- `[-\s]?`: Matches an optional dash or space.
- `\d{4}$`: Matches any four digits at the end of the string.

We use the `re.match()` function to check if the phone number matches the pattern. If it does, the function will return a match object; otherwise, it will return `None`.

### Using the `if` statement to check validity

To utilize the `is_valid_phone_number()` function and check if a given string is a valid phone number, we can incorporate the `if` statement as shown below:

```python
def check_phone_number(phone_number):
    if is_valid_phone_number(phone_number):
        print(f"{phone_number} is a valid phone number.")
    else:
        print(f"{phone_number} is not a valid phone number.")

# Example usage
check_phone_number("123-456-7890")  # Invalid phone number
check_phone_number("5551234567")    # Valid phone number
```

The `check_phone_number()` function utilizes the `is_valid_phone_number()` function to determine if the provided phone number is valid. Based on the result, an appropriate message is printed.

### Conclusion

Validating a phone number is a common task in many applications. Using the `if` statement along with regular expressions in Python, we can easily check whether a given string represents a valid phone number. By implementing the approach discussed in this blog post, you can efficiently validate phone numbers in your own Python projects.

#python #phonenumber #validation