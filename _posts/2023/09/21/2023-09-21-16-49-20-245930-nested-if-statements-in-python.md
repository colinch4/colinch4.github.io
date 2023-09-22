---
layout: post
title: "Nested if statements in Python"
description: " "
date: 2023-09-21
tags: [Conditionals]
comments: true
share: true
---

When working with conditional statements in Python, it is sometimes necessary to have multiple levels of conditionals. One way to achieve this is by using nested if statements.

A nested if statement is an if statement placed inside another if statement. It allows you to check for multiple conditions and execute different blocks of code accordingly.

Here's an example to demonstrate the usage of nested if statements in Python:

```python
# User input
age = int(input("Enter your age: "))

# Check age range
if age >= 18:
    print("You are eligible to vote.")
    if age >= 65:
        print("You are also eligible for senior citizen benefits.")
    else:
        print("You are not eligible for senior citizen benefits.")
else:
    print("You are not eligible to vote.")
```

In the above code snippet, we first prompt the user to enter their age using the `input()` function. The value is then converted to an integer using the `int()` function.

Next, we have the first if statement to check if the age entered by the user is greater than or equal to 18. If the condition is true, the code inside the block is executed, which prints "You are eligible to vote."

Within this block, we have another if statement to check if the age is also greater than or equal to 65. If this condition is true, it prints "You are also eligible for senior citizen benefits." Otherwise, it prints "You are not eligible for senior citizen benefits."

If the initial condition of the first if statement is false, meaning the age is less than 18, the code inside the else block is executed, which prints "You are not eligible to vote."

Nested if statements can be used to create complex conditional logic by adding multiple levels of conditions. However, it is important to maintain readability and avoid excessive nesting, as it can make the code harder to understand and debug.

Remember to indent the code correctly to indicate which blocks belong to which if statement.

#Python #Conditionals