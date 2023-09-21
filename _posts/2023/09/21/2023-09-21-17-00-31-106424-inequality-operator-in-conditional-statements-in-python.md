---
layout: post
title: "Inequality operator in conditional statements in Python"
description: " "
date: 2023-09-21
tags: [python, inequality]
comments: true
share: true
---

Let's take a look at an example:

```python
x = 5
y = 10

if x != y:
    print("x is not equal to y")

```

In the above code snippet, we have two variables `x` and `y`. The `!=` operator is used to compare their values. If `x` is not equal to `y`, the condition evaluates to True, and the code inside the if statement block will be executed. In our example, the output will be "x is not equal to y".

We can also use the inequality operator in more complex conditions:

```python
if x != y and x > 0:
    print("x is not equal to y and x is greater than 0")

```

In this case, the condition will only be True if both `x` is not equal to `y` and `x` is greater than 0.

It is important to note that the inequality operator `!=` checks for inequality of values, not the type of values. If you want to check for both inequality of values and types, you can use the `is not` operator.

In conclusion, the inequality operator (`!=`) in Python is used to check if two values are not equal to each other. It is commonly used in conditional statements to make decisions based on inequality conditions. #python #inequality