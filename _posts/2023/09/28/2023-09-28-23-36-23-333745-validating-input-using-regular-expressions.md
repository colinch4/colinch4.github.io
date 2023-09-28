---
layout: post
title: "Validating input using regular expressions"
description: " "
date: 2023-09-28
tags: [regex, inputvalidation]
comments: true
share: true
---

In this blog post, we will explore how to use regular expressions to validate different types of input.

## Email Validation

Email validation is a common use case for regex. Let's say we want to validate if a given string is a valid email address.

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
```

In this example, we define a regex pattern that checks if the email string matches the following criteria:

- Starts with one or more alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens.
- Followed by the @ symbol.
- Followed by one or more alphanumeric characters, dots, or hyphens.
- Ends with a dot followed by two or more alphabetic characters.

The `re.match()` function is used to match the string against the pattern. If the match is successful, the function returns True indicating a valid email address, otherwise, it returns False.

## Phone Number Validation

Another common use case is validating a phone number. Let's say we want to validate if a given string is a valid phone number in the format `XXX-XXX-XXXX`.

```python
import re

def validate_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False
```

In this example, we define a regex pattern that checks if the phone number string matches the following criteria:

- Starts with three digits.
- Followed by a hyphen.
- Followed by three more digits.
- Followed by another hyphen.
- Ends with four digits.

The `re.match()` function is again used to match the string against the pattern. If the match is successful, the function returns True indicating a valid phone number, otherwise, it returns False.

## Conclusion

Regular expressions provide a flexible and powerful way to validate input using pattern matching. In this blog post, we explored two common examples: email and phone number validation. However, regular expressions can be used for many other types of input validation scenarios.

Using regular expressions for input validation ensures that the input data meets the expected format, enhancing the security and reliability of your applications.

#regex #inputvalidation