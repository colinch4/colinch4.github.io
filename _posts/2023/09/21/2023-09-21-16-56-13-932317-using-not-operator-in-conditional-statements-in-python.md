---
layout: post
title: "Using not operator in conditional statements in Python"
description: " "
date: 2023-09-21
tags: [python, conditional]
comments: true
share: true
---

Conditional statements are an essential part of programming as they help control the flow of the code based on certain conditions. Python provides several logical operators, including the `not` operator, which allows you to negate the outcome of a condition.

The `not` operator returns the opposite of a boolean value. It is often used to check if a condition is **not** true. By using the `not` operator, you can modify the behavior of conditional statements to execute specific code when a condition is false.

Here's an example of using the `not` operator in a conditional statement:

```python
user_logged_in = False

if not user_logged_in:
    print("Please log in to continue.")
else:
    print("Welcome!")
```

In the above example, we have a boolean variable `user_logged_in` set to `False`. The `not` operator is used to invert the value of `user_logged_in` in the `if` statement. If the condition is true (i.e., `user_logged_in` is **not** true), then the code inside the `if` block will be executed, which in this case will print "Please log in to continue." Otherwise, if the condition is false, the code inside the `else` block will execute, printing "Welcome!".

You can also use the `not` operator in combination with other logical operators, such as `and` and `or`, to create more complex conditions. Here's an example:

```python
is_weekend = True
is_raining = False

if not (is_weekend or is_raining):
    print("Enjoy your outdoor activity!")
else:
    print("Stay indoors and relax.")
```

In this example, the `not` operator is used to negate the combined condition `(is_weekend or is_raining)`. If the combined condition is true (i.e., it is **not** true that it is the weekend or raining), then the code inside the `if` block will be executed, printing "Enjoy your outdoor activity!". Otherwise, if the condition is false, the code inside the `else` block will execute, printing "Stay indoors and relax.".

Using the `not` operator in conditional statements allows you to easily invert the outcomes of conditions, providing more flexibility and control over your code's logic.

#python #conditional-statements