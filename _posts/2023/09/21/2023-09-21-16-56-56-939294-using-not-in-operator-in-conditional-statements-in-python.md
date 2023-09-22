---
layout: post
title: "Using not in operator in conditional statements in Python"
description: " "
date: 2023-09-21
tags: [operators]
comments: true
share: true
---

In Python, the `not` operator is a logical operator that is used to negate the result of a boolean expression. It flips the value of a boolean variable, transforming `True` to `False` and `False` to `True`. 

The `not` operator is commonly used in conditional statements to check if a condition is **not** true. This allows us to control the flow of our program based on the negation of a particular condition.

## Basic Syntax

The basic syntax of using the `not` operator in conditional statements is as follows:

```python
if not condition:
    # Code to be executed if the condition is not true
else:
    # Code to be executed if the condition is true
```

Here, `condition` is the boolean expression that we want to negate using the `not` operator. The code under the `if` block will be executed if the condition is not true, while the code under the `else` block will be executed if the condition is true.

## Example

Let's consider an example where we want to determine if a number is **not** divisible by 2. We can use the `not` operator in combination with the modulo operator `%` to achieve this.

```python
number = 5

if not number % 2 == 0:
    print("The number is not divisible by 2")
else:
    print("The number is divisible by 2")
```

In this example, if the remainder of `number` divided by 2 is not equal to 0, it means the number is not divisible by 2. The `not` operator negates this condition, so the code under the `if` block is executed, resulting in the output `"The number is not divisible by 2"`.

## Conclusion

The `not` operator in Python allows us to negate boolean expressions and control the flow of our program based on the result. It is commonly used in conditional statements to check if a condition is **not** true. By understanding how to use the `not` operator effectively, we can write more expressive and flexible code in Python. 

#python #operators