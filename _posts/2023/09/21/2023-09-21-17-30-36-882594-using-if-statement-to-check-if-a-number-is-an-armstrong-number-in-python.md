---
layout: post
title: "Using if statement to check if a number is an Armstrong number in Python"
description: " "
date: 2023-09-21
tags: [python, armstrongnumber]
comments: true
share: true
---

Armstrong numbers are special numbers where the sum of the cubes of its digits is equal to the number itself. For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

To determine if a given number is an Armstrong number, we can use an `if` statement in Python. Here's an example code snippet:

```python
# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    # Convert the number to a string to iterate over each digit
    string_number = str(number)

    # Initialize the sum variable
    armstrong_sum = 0

    # Iterate over each digit in the number
    for digit in string_number:
        # Add the cube of each digit to the sum
        armstrong_sum += int(digit) ** 3

    # Check if the sum is equal to the original number
    if armstrong_sum == number:
        return True
    else:
        return False

# Test the function
test_number = 153
if is_armstrong_number(test_number):
    print(f"{test_number} is an Armstrong number.")
else:
    print(f"{test_number} is not an Armstrong number.")
```

In this code, we define a function `is_armstrong_number()` that takes a number as an argument. We convert the number to a string to iterate over each digit. Then, we iterate over each digit and calculate the sum of the cubes of each digit using the `**` operator. Finally, we compare the sum with the original number and return `True` if they are equal, or `False` otherwise.

We can test the function with a sample number (in this case, 153) and display the result using an `if` statement.

**#python #armstrongnumber**