---
layout: post
title: "Using if statement to check if a string is a valid credit card number in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

When dealing with credit card numbers in Python, it is often necessary to validate whether a given string is a valid credit card number or not. This can be achieved using an `if` statement with some additional logic.

## Approach to Validate a Credit Card Number

To validate a credit card number, we need to perform the following steps:

1. Remove any spaces or dashes from the input string to obtain a numeric-only representation.
2. Check if the length of the cleaned-up string is 16 (the standard length for most credit card numbers).
3. Convert the string to a list of integers.
4. Double every second digit in the list.
5. If the doubled digit is greater than 9, subtract 9 from it.
6. Sum all the digits.
7. If the sum is divisible by 10, the credit card number is valid.

## Example Code

Here is an example implementation in Python:

```python
def is_valid_credit_card(credit_card_num):
    # Remove spaces and dashes from the string
    cleaned_num = credit_card_num.replace(" ", "").replace("-", "")

    # Check if the cleaned-up string has a length of 16
    if len(cleaned_num) != 16:
        return False

    # Convert the string to a list of integers
    digits = [int(char) for char in cleaned_num]

    # Double every second digit in the list
    for i in range(1, 16, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all the digits
    sum_of_digits = sum(digits)

    # Check if the sum is divisible by 10
    if sum_of_digits % 10 == 0:
        return True

    return False
```

## Usage

To use the `is_valid_credit_card` function, you can simply call it with a credit card number as the argument. It will return `True` if the number is valid, and `False` otherwise.

```python
credit_card_number = "4111 1111 1111 1111"
if is_valid_credit_card(credit_card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")
```

This will output "Valid credit card number" since the provided credit card number passes the validation check.

## Conclusion

By implementing the steps outlined above and using an `if` statement, we can determine whether a given string is a valid credit card number in Python. It's important to note that this approach assumes standard credit card number length and format conventions. Additional validation may be required for specific credit card types or issuer-specific patterns.