---
layout: post
title: "Conditional statement with multiple operators in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

In Python, you can use multiple operators in a single conditional statement to create complex conditions. This allows you to evaluate multiple conditions at once and execute different code blocks based on the result.

### Example:

```python
number = 15

if number > 10 and number < 20:
    print("The number is between 10 and 20")
else:
    print("The number is not between 10 and 20")
```

In the above example, we have a variable `number` with a value of 15. The `if` statement checks if the `number` is **greater than 10** and **less than 20** using the `>` and `<` operators respectively. If both conditions are true, it will execute the code inside the if block, printing "The number is between 10 and 20". Otherwise, it will execute the code inside the else block, printing "The number is not between 10 and 20".

### Multiple Operators:

You can use various operators in combination to create complex conditions. Here are some commonly used operators:

- `and`: Returns `True` if both conditions are true
- `or`: Returns `True` if either of the conditions is true
- `not`: Negates the result of the condition

### Example:

```python
age = 25
grade = 'A'

if age > 18 and grade == 'A':
    print("You are eligible for the scholarship")
else:
    print("You are not eligible for the scholarship")
```

In the above example, the `if` statement checks if the `age` is greater than 18 **and** the `grade` is equal to 'A'. If both conditions are true, it will print "You are eligible for the scholarship". Otherwise, it will print "You are not eligible for the scholarship".

Using multiple operators in conditional statements allows you to create flexible and powerful logical conditions to control the flow of your program.