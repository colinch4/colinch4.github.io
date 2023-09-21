---
layout: post
title: "Multiple conditions in an if statement in Python"
description: " "
date: 2023-09-21
tags: [Python, IfStatement, LogicalOperators]
comments: true
share: true
---

Here's an example that demonstrates how to use multiple conditions in an `if` statement in Python:

```python
x = 5
y = 10

if x > 0 and y > 0:
    print("Both x and y are greater than 0")
elif x > 0 or y > 0:
    print("Either x or y is greater than 0")
else:
    print("Both x and y are not greater than 0")
```

In the above code, we have two variables `x` and `y`, and we are checking their values using multiple conditions. 

The first `if` statement checks if both `x` and `y` are greater than 0 using the `and` operator. If the condition is `True`, it prints "Both x and y are greater than 0".

If the first condition is `False`, the `elif` statement checks if at least one of the variables is greater than 0 using the `or` operator. If the condition is `True`, it prints "Either x or y is greater than 0".

If both the conditions are `False`, the `else` statement is executed, which prints "Both x and y are not greater than 0".

Using multiple conditions in an `if` statement allows you to create more complex logic to control the flow of your program based on different situations. Just make sure to use the correct logical operators (`and`, `or`) to combine the conditions effectively.

#Python #IfStatement #LogicalOperators