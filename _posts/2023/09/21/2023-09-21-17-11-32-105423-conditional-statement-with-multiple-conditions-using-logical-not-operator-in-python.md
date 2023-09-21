---
layout: post
title: "Conditional statement with multiple conditions using logical NOT operator in Python"
description: " "
date: 2023-09-21
tags: [Python, Conditionals, LogicalOperators]
comments: true
share: true
---

In Python, you can use the logical NOT (`not`) operator to negate a boolean value or expression. This operator returns `True` if the operand is `False`, and `False` if the operand is `True`.

When dealing with conditional statements that involve multiple conditions, you can use the logical NOT operator to check if all the conditions are **not** true. In other words, if **any** of the conditions are true, the logical NOT operator will return `False`.

Let's see an example to understand this concept better:

```python
x = 5
y = 10

if not (x > 3 and y < 20):
    print("Condition is not true")
else:
    print("Condition is true")
```

In the above code, we have two conditions combined using the logical `and` operator: `x > 3` and `y < 20`. The `not` operator is used to negate the result of this combination.

If both `x > 3` and `y < 20` are true, the `not` operator will return `False`, and the code will print "Condition is not true".

If **any** of the conditions is `False`, the `not` operator will return `True`, and the code will print "Condition is true".

You can also use the logical NOT operator with other logical operators, such as `or`. For example:

```python
x = 5
y = 10

if not (x > 3 or y < 20):
    print("Condition is not true")
else:
    print("Condition is true")
```

In this case, the `not` operator is applied to the combination of `x > 3` **or** `y < 20`. If **any** of the conditions is `True`, the `not` operator will return `False`, and the code will print "Condition is not true".

As you can see, using the logical NOT operator allows you to create conditional statements with multiple conditions and negate the overall outcome based on your requirements.

#Python #Conditionals #LogicalOperators