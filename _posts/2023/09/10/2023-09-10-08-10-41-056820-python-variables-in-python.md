---
layout: post
title: "[Python] Variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Variables are an essential concept in Python programming. They are used to store values that can be manipulated and used throughout your code. In this blog post, we will explore the basics of variables in Python and how to use them effectively.

## Declaring Variables

In Python, variables can be declared by simply assigning a value to them. Unlike some other programming languages, you don't need to specify the type of a variable explicitly. Python will automatically infer the type based on the value assigned to it.

Here's an example of declaring variables in Python:

```python
# Integer variable
age = 25

# String variable
name = "John Doe"

# Float variable
salary = 2500.00

# Boolean variable
is_student = True
```

In the example above, we declared four variables: `age`, `name`, `salary`, and `is_student`. Notice that we didn't specify any type explicitly.

## Variable Naming Rules

When naming variables in Python, you need to follow a few rules:

1. Variable names must start with a letter or an underscore (_).
2. Variable names can only contain letters, numbers, and underscores (_).
3. Variable names are case-sensitive, so `age` and `Age` are considered two different variables.
4. Avoid using reserved keywords as variable names. For example, you cannot use `if`, `else`, `while`, etc., as variable names.

## Variable Assignment and Re-assignment

In Python, you can assign a new value to a variable at any point in your code. This is known as variable re-assignment. The variable will take on the new value and its type will be inferred based on the new assigned value.

Here's an example of variable re-assignment:

```python
x = 10
print(x)  # Output: 10

x = "Hello"
print(x)  # Output: Hello
```

In the example above, the variable `x` is initially assigned the value 10. Later, it is re-assigned the value "Hello". Python automatically adjusts the type of the variable as needed.

## Using Variables in Operations

Variables are often used in mathematical or logical operations. You can use variables in expressions, calculations, or conditional statements.

Here's an example that demonstrates using variables in operations:

```python
a = 5
b = 10

sum = a + b
print(sum)  # Output: 15

is_greater = a > b
print(is_greater)  # Output: False
```

In the example above, we declare two variables `a` and `b`. We then use these variables to calculate their sum and determine if `a` is greater than `b`. The result of these operations is stored in the variables `sum` and `is_greater` respectively.

## Conclusion

Variables are an essential part of programming in Python. They allow you to store and manipulate data in your code. Understanding how to declare, name, and use variables effectively will help you write clean and readable code.

In this blog post, we covered the basics of variables in Python. We learned how to declare variables, the rules for naming variables, how to assign and re-assign values, and how to use variables in operations.

Stay tuned for more Python topics and happy coding!