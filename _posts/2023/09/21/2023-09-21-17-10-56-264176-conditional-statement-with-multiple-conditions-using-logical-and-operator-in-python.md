---
layout: post
title: "Conditional statement with multiple conditions using logical AND operator in Python"
description: " "
date: 2023-09-21
tags: [python, logical]
comments: true
share: true
---

Here's an example of how you can use the logical AND operator in a conditional statement:

```python
x = 10
y = 5
z = 7

if x > y and y < z:
    print("Both conditions are True!")
else:
    print("At least one condition is False.")
```

In the example above, we have three variables `x`, `y`, and `z`. The condition `x > y` evaluates to `True` (since 10 is greater than 5) and the condition `y < z` also evaluates to `True` (since 5 is less than 7). Since both conditions are `True`, the print statement "Both conditions are True!" will be executed.

If at least one of the conditions is `False`, the `else` block will be executed instead. For example:

```python
x = 10
y = 5
z = 7

if x > y and y > z:
    print("Both conditions are True!")
else:
    print("At least one condition is False.")
```

In this case, the condition `y > z` is `False` (since 5 is not greater than 7), so the print statement "At least one condition is False." will be executed.

By using the logical AND operator, you can create more complex conditional statements with multiple conditions that must all be `True` for the code block to be executed. Make sure to use parentheses if you need to specify the order of operations within the conditional statement.

#python #logical-and