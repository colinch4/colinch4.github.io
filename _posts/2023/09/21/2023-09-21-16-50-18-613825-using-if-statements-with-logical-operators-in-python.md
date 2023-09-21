---
layout: post
title: "Using if statements with logical operators in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

When writing code in Python, you often encounter situations where you need to check multiple conditions before performing a certain action. In such cases, you can use if statements paired with logical operators to evaluate the conditions and decide whether to execute the code block.

## Logical Operators in Python

Python provides three logical operators to combine multiple conditions:

- **and**: Returns True if both conditions are True.
- **or**: Returns True if at least one condition is True.
- **not**: Reverses the result of the condition.

## Syntax of if Statement with Logical Operators

The basic syntax of an if statement with logical operators is as follows:

```python
if condition1 and condition2:
    # code block to be executed if both conditions are true

if condition1 or condition2:
    # code block to be executed if at least one condition is true

if not condition:
    # code block to be executed if the condition is not true
```

## Example: Using if statements with Logical Operators

Let's assume we have a program that checks whether a student is eligible for a scholarship based on their grade and attendance. We can use logical operators to implement this logic.

```python
grade = 85
attendance = 90

if grade >= 80 and attendance >= 80:
    print("Congratulations! You are eligible for a scholarship.")

if grade >= 90 or attendance >= 90:
    print("Wow! You are eligible for a special scholarship.")

if not (grade < 70):
    print("Good job! You passed the minimum grade requirement.")
```

In this example, the first if statement checks if the grade is greater than or equal to 80 and the attendance is greater than or equal to 80. If both conditions are true, it prints a message about being eligible for a scholarship. 

The second if statement checks if the grade is greater than or equal to 90 or the attendance is greater than or equal to 90. If either of these conditions is true, it prints a message about being eligible for a special scholarship.

Lastly, the third if statement uses the `not` logical operator to check if the grade is not less than 70. If the condition is true, it prints a message about passing the minimum grade requirement.

## Conclusion

Using if statements with logical operators allows you to evaluate multiple conditions and make decisions in your Python programs. By combining logical operators like `and`, `or`, and `not`, you can create complex conditions and execute specific code blocks based on the evaluation results.