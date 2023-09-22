---
layout: post
title: "Conditional statement with multiple conditions in Python"
description: " "
date: 2023-09-21
tags: [programming]
comments: true
share: true
---

When writing code in Python, you may often come across situations where you need to check multiple conditions before executing a certain block of code. In such cases, you can make use of conditional statements with multiple conditions.

## Using the `if-elif-else` statement

The `if-elif-else` statement in Python allows you to test multiple conditions and execute different blocks of code based on the result of each condition. 

Here's an example that demonstrates the use of a `if-elif-else` statement with multiple conditions:

```python
x = 10

if x > 10:
    print("x is greater than 10")
    
elif x < 10:
    print("x is less than 10")
    
else:
    print("x is equal to 10")
```

In this example, the code checks the value of `x` and prints a corresponding message based on the condition. If `x` is greater than 10, it prints `"x is greater than 10"`. If `x` is less than 10, it prints `"x is less than 10"`. If neither condition is true, it executes the code inside the `else` block and prints `"x is equal to 10"`.

## Using logical operators

You can also use logical operators such as `and` and `or` to combine multiple conditions in a single `if` statement. This allows you to test for multiple conditions simultaneously.

Here's an example that demonstrates the use of logical operators in a conditional statement:

```python
x = 5
y = 7

if x > 0 and y < 10:
    print("Both conditions are true")
    
elif x > 0 or y > 10:
    print("At least one condition is true")
    
else:
    print("None of the conditions are true")
```

In this example, the code checks two conditions using the logical operators `and` and `or`. If both conditions are true, it prints `"Both conditions are true"`. If at least one condition is true, it prints `"At least one condition is true"`. If none of the conditions are true, it executes the code inside the `else` block and prints `"None of the conditions are true"`.

## Conclusion

Conditional statements with multiple conditions are essential for writing flexible and efficient code in Python. By using `if-elif-else` statements or logical operators, you can easily handle different scenarios and execute the appropriate code based on the conditions being satisfied.

#python #programming