---
layout: post
title: "Conditional statement with multiple logical operators in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here's an example of a conditional statement with multiple logical operators in Python:

```python
x = 10
y = 5

if x > 5 and y < 10:
    print("Both conditions are True")

if x > 7 or y > 10:
    print("At least one condition is True")

if not x == y:
    print("The condition is True because x is not equal to y")
```

Let's break down each of these conditional statements:

1. The first conditional statement checks if both `x` is greater than 5 and `y` is less than 10. If both conditions are true, it prints "Both conditions are True".

2. The second conditional statement checks if either `x` is greater than 7 or `y` is greater than 10. If at least one of the conditions is true, it prints "At least one condition is True".

3. The third conditional statement uses the `not` operator to negate the condition. It checks if `x` is not equal to `y`. If the condition is true, it prints "The condition is True because x is not equal to y".

By using multiple logical operators, you can build complex conditions to make your code more flexible and adaptable. Just remember to use parentheses when needed to control the order of evaluation within the condition.