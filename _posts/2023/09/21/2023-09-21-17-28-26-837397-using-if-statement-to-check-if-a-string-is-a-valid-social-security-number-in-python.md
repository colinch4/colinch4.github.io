---
layout: post
title: "Using if statement to check if a string is a valid Social Security number in Python"
description: " "
date: 2023-09-21
tags: [Validation]
comments: true
share: true
---

In this tech blog post, we will explore how to use an `if` statement to check if a given string is a valid Social Security Number (SSN) in the Python programming language.

## What is a Social Security Number?

A Social Security Number (SSN) is a unique nine-digit identification number that is issued to U.S. citizens, permanent residents, and temporary residents. It is used for various purposes, including tax tracking, government benefits, and employment eligibility verification.

## Valid SSN Format

A valid SSN follows a specific format: XXX-XX-XXXX, where each X represents a digit from 0 to 9. The first three digits represent the area number, the next two digits represent the group number, and the last four digits represent the serial number.

## Implementing the Validation Check

First, we need to define a function called `is_valid_ssn` that takes a string parameter as the SSN to validate. Inside the function, we will use an `if` statement to check if the given SSN follows the valid format.

```python
def is_valid_ssn(ssn):
    if len(ssn) != 11:
        return False
    if not ssn[0:3].isdigit() or not ssn[4:6].isdigit() or not ssn[7:11].isdigit():
        return False
    if ssn[3] != '-' or ssn[6] != '-':
        return False
    return True
```

Here's how the `is_valid_ssn` function works:

1. We first check if the length of the given SSN is equal to 11. If not, it cannot be a valid SSN, and the function immediately returns `False`.
2. Next, we use the `isdigit()` method to check if the characters at the corresponding positions (excluding the hyphens) are digits. If any of them are not digits, the function returns `False`.
3. After that, we check if the characters at positions 3 and 6 are hyphens ("-"). If not, the function returns `False`.
4. If all the above conditions pass, the function returns `True`, indicating that the given SSN is valid.

## Testing the Function

We can test our `is_valid_ssn` function by calling it with different SSN values.

```python
valid_ssn = "123-45-6789"
invalid_ssn = "abc-def-ghi"
non_digit_ssn = "12x-34-5678"

print(is_valid_ssn(valid_ssn))  # Output: True
print(is_valid_ssn(invalid_ssn))  # Output: False
print(is_valid_ssn(non_digit_ssn))  # Output: False
```

In the above example, the first SSN ("123-45-6789") is valid, so the function returns `True`. The second SSN ("abc-def-ghi") contains non-digit characters, so it is invalid and the function returns `False`. The third SSN ("12x-34-5678") is not properly formatted, so it is also invalid and the function returns `False`.

## Conclusion

By using the `if` statement and basic string manipulation techniques, we can easily check if a given string is a valid Social Security Number in Python. This can be useful in various applications where SSN validation is required, such as form input validation, data processing, and more.

#Python #SSN #Validation