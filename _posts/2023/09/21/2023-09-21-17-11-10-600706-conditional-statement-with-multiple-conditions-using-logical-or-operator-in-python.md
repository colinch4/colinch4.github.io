---
layout: post
title: "Conditional statement with multiple conditions using logical OR operator in Python"
description: " "
date: 2023-09-21
tags: [LogicalOperators]
comments: true
share: true
---

The logical OR operator returns `True` if at least one of the conditions is true, and `False` otherwise. Here is an example of how you can use the logical OR operator in a conditional statement:

```python
x = 5
y = 10
z = 3

if x > 10 or y < 5 or z == 3:
    print("At least one condition is true")
else:
    print("None of the conditions are true")
```

In this example, the `or` operator is used to check if any of the conditions `x > 10`, `y < 5`, or `z == 3` evaluate to `True`. Since `z` is indeed equal to `3`, the first condition is true, and the message "At least one condition is true" will be printed.

If none of the conditions were true, the message "None of the conditions are true" would be printed instead.

Remember to use parentheses to group the conditions inside the `if` statement if you have complex conditions. This will ensure that the logical OR operator is applied correctly.

Using the logical OR operator with multiple conditions can help you create more versatile and flexible code, allowing you to handle different scenarios based on various conditions.

#Python #LogicalOperators