---
layout: post
title: "[Python] Conditional statements in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Conditional statements are an essential part of any programming language, including Python. They allow us to make decisions and execute different blocks of code depending on specified conditions. In this blog post, we will explore the different types of conditional statements in Python and provide examples of their usage.

## 1. if statement

The `if` statement is the most basic type of conditional statement in Python. It allows us to execute a block of code if a certain condition is true. The syntax of the `if` statement is as follows:

```python
if condition:
    # code to be executed if the condition is true

# rest of the code
```

Here's an example that demonstrates the usage of the `if` statement:

```python
# Checking if a number is positive
num = 10

if num > 0:
    print("The number is positive")

print("End of the program")
```

In this example, if the condition `num > 0` evaluates to true, the message "The number is positive" will be printed. If the condition is false, the code block inside the `if` statement will be bypassed.

## 2. if-else statement

The `if-else` statement allows us to execute one block of code if a condition is true and a different block of code if the condition is false. The syntax of the `if-else` statement is as follows:

```python
if condition:
    # code to be executed if the condition is true
else:
    # code to be executed if the condition is false

# rest of the code
```

Here's an example that demonstrates the usage of the `if-else` statement:

```python
# Checking if a number is even or odd
num = 7

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("End of the program")
```

In this example, if the condition `num % 2 == 0` evaluates to true, the message "The number is even" will be printed. Otherwise, the message "The number is odd" will be printed.

## 3. if-elif-else statement

The `if-elif-else` statement allows us to test multiple conditions and execute different blocks of code depending on which condition is true. The syntax of the `if-elif-else` statement is as follows:

```python
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition2 is true
else:
    # code to be executed if neither condition1 nor condition2 is true

# rest of the code
```

Here's an example that demonstrates the usage of the `if-elif-else` statement:

```python
# Checking the grade based on percentage
percentage = 75

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Grade: D")

print("End of the program")
```

In this example, the code will check the percentage and print the corresponding grade based on the condition that evaluates to true. If none of the conditions are true, the code block inside the `else` statement will be executed.

Conditional statements provide a powerful way to control the flow of execution in a Python program. By using `if`, `if-else`, and `if-elif-else` statements, you can make your program more flexible and responsive to different situations.