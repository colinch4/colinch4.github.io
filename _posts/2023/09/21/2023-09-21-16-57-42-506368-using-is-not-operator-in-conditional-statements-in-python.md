---
layout: post
title: "Using is not operator in conditional statements in Python"
description: " "
date: 2023-09-21
tags: [Python, ConditionalStatements]
comments: true
share: true
---

Conditional statements allow us to control the flow of our programs by checking if certain conditions are met. In Python, we can use the `not` operator to negate the result of a conditional expression.

The `not` operator is a logical operator that returns `True` if a condition is `False`, and `False` if the condition is `True`. This can be useful when we want to reverse the outcome of a conditional statement.

Let's look at an example to see how we can use the `not` operator in conditional statements:

```python
user_authenticated = False

if not user_authenticated:
    print("Please login to continue.")
else:
    print("Welcome, user!")
```

In the above code, we have a variable `user_authenticated` set to `False`. Using the `not` operator before the `user_authenticated` variable inside the `if` statement negates its value. So, if `user_authenticated` is `False`, the `if` condition evaluates to `True` and the message "Please login to continue." is printed. Otherwise, if `user_authenticated` is `True`, the `else` block is executed and the message "Welcome, user!" is printed.

We can also use the `not` operator with other conditional operators such as `==`, `!=`, `<`, `>`, `<=`, `>=`, and with logical operators such as `and`, `or`. Here is an example that demonstrates its usage:

```python
x = 10

if not (x == 5 or x > 10):
    print("x is either less than 5 or not greater than 10.")
else:
    print("x is either equal to 5 or greater than 10.")
```

In the above code, we have nested the condition inside parentheses to explicitly define the order of operations. The `not` operator negates the outcome of the condition. If the negated condition evaluates to `True`, the first message is printed; otherwise, the second message is printed.

By using the `not` operator in conditional statements, we can easily reverse the result of a condition, allowing us to write more concise and readable code.

#Python #ConditionalStatements