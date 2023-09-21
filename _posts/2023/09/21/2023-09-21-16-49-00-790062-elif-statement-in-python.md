---
layout: post
title: "Elif statement in Python"
description: " "
date: 2023-09-21
tags: [Python, Elif, PythonProgramming]
comments: true
share: true
---

In Python, the `elif` statement is short for "else if". It is used in control flow structures to add multiple conditions within an `if` statement.

## Syntax of the Elif Statement
The syntax of the `elif` statement is as follows:

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
elif condition3:
    # code to execute if condition3 is True
else:
    # code to execute if none of the conditions are True
```

## Usage of Elif Statement

The `elif` statement is useful when we have multiple conditions to check in a program. It allows us to execute different blocks of code based on different conditions.

```python
# Example: Checking the grade of a student
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")
```

In the example above, if `marks >= 90`, it will print "Grade A". If the condition is not met, it moves to the next condition `elif marks >= 80` and checks if it is True. If it is, it prints "Grade B". This process continues until a condition is satisfied, or if none of the conditions are True, the `else` block is executed.

## Conclusion

The `elif` statement is a powerful tool in Python that allows you to handle multiple conditions in a controlled manner. It provides flexibility and makes your code more readable and maintainable. Use it whenever you need to check multiple conditions within an `if` statement.

#Python #Elif #PythonProgramming