---
layout: post
title: "Conditional statement with multiple checks in Python"
description: " "
date: 2023-09-21
tags: [python, conditionalstatement, logicaloperators]
comments: true
share: true
---

In Python, conditional statements allow us to execute different blocks of code based on certain conditions. Often, we need to perform multiple checks before determining the appropriate action. In this blog post, we will explore how to write conditional statements with multiple checks using logical operators in Python.

## Logical Operators

Python provides three logical operators that can be used to combine multiple conditions:

1. `and`: Returns `True` if both conditions are true.
2. `or`: Returns `True` if at least one condition is true.
3. `not`: Returns the opposite boolean value of the condition.

These logical operators can be used to write conditional statements with multiple checks.

## Example: Checking Even or Divisible by 3

Let's consider an example where we want to check if a number is even and divisible by 3. We can use the logical `and` operator to combine these conditions in a single statement.

```python
number = 12

if number % 2 == 0 and number % 3 == 0:
    print("The number is even and divisible by 3.")
else:
    print("The number is not even and divisible by 3.")
```

In the above code, we first check if the number is divisible by 2 using the modulo operator `%`. If the remainder of the division is 0, it means the number is even. Then, we check if the number is divisible by 3 using the same modulo operator. If both conditions evaluate to `True`, the message "The number is even and divisible by 3." is printed. Otherwise, the else block is executed, and the message "The number is not even and divisible by 3." is printed.

## Example: Checking Temperature Range

Let's consider another example where we want to check if a temperature lies within a specific range. We can use the logical `and` operator to combine the lower and upper temperature bounds in a conditional statement.

```python
temperature = 25

if 20 <= temperature <= 30:
    print("The temperature is within the desired range.")
else:
    print("The temperature is outside the desired range.")
```

In the above code, we use the comparison operators `<=` to check if the temperature is greater than or equal to 20, and `<=` to check if the temperature is less than or equal to 30. If both conditions evaluate to `True`, the message "The temperature is within the desired range." is printed. Otherwise, the else block is executed, and the message "The temperature is outside the desired range." is printed.

## Conclusion

By using logical operators like `and`, `or`, and `not`, we can write conditional statements with multiple checks in Python. These operators allow us to combine conditions and perform actions based on the combined result. Whether it's checking multiple conditions or comparing ranges, these logical operators provide flexibility in writing expressive and efficient code.

#python #conditionalstatement #logicaloperators