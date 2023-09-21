---
layout: post
title: "Using if statement to check if a number is positive, negative, or zero in Python"
description: " "
date: 2023-09-21
tags: [Python, IfStatement]
comments: true
share: true
---

Keywords: Python, if statement, positive, negative, zero

---

In Python, you can use an `if` statement to check if a given number is positive, negative, or zero. This is a common requirement when working with numerical data or performing mathematical calculations. In this article, we will explore how to implement this functionality in Python.

To check if a number is positive, we use the following code:

```python
num = 10

if num > 0:
    print("The number is positive")
```

Here, we assign the value `10` to the variable `num`. The `if` statement checks if `num` is greater than `0`. If the condition is true, which means `num` is positive, the message "The number is positive" is printed.

To check if a number is negative, we modify the above code as follows:

```python
num = -5

if num < 0:
    print("The number is negative")
```

Here, we assign the value `-5` to the variable `num`. The `if` statement checks if `num` is less than `0`. If the condition is true, which means `num` is negative, the message "The number is negative" is printed.

Lastly, to check if a number is zero, we modify the code again:

```python
num = 0

if num == 0:
    print("The number is zero")
```

Here, we assign the value `0` to the variable `num`. The `if` statement checks if `num` is equal to `0`. If the condition is true, which means `num` is zero, the message "The number is zero" is printed.

It's worth noting that the `if` statement can be combined with `elif` and `else` statements to handle more complex scenarios involving multiple conditions.

```python
num = -2

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

In the above example, if `num` is greater than `0`, the message "The number is positive" is printed. If `num` is less than `0`, the message "The number is negative" is printed. Otherwise, if none of the previous conditions are true, the message "The number is zero" is printed.

By using `if` statements, you can easily determine if a given number is positive, negative, or zero in Python. This is useful for various applications such as data analysis, mathematical calculations, or input validation.

**#Python #IfStatement**