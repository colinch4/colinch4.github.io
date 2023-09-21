---
layout: post
title: "Conditional statement with multiple variables in Python"
description: " "
date: 2023-09-21
tags: [Python, ConditionalStatements]
comments: true
share: true
---

Let's consider a scenario where we have three variables `x`, `y`, and `z`, and we want to perform different actions based on their values. We can use the `if`, `elif`, and `else` keywords to create a conditional statement with multiple variables.

```python
# Define the variables
x = 5
y = 10
z = 7

# Conditional statement
if x > y and z < y:
    print("Condition 1: x > y and z < y is True")
elif x < y or z < y:
    print("Condition 2: x < y or z < y is True")
else:
    print("No conditions met")
```

In the above example, we have three conditions:

1. `x > y and z < y`: This condition evaluates to `False` since `x` is not greater than `y`. Therefore, it jumps to the `elif` block.

2. `x < y or z < y`: This condition evaluates to `True` because `x` is less than `y`. The first condition of the `elif` block is satisfied, so the corresponding code block will execute.

3. If none of the conditions are met, the `else` block will execute. In this case, since the second condition is met, the `else` block will not execute.

Output:
```
Condition 2: x < y or z < y is True
```

By using logical operators like `and` and `or`, we can combine multiple variables into a single conditional statement. This allows us to create more complex conditions and control the flow of our program based on those conditions.

#Python #ConditionalStatements