---
layout: post
title: "Conditional statement with multiple nested if statements in Python"
description: " "
date: 2023-09-21
tags: [python, conditionalstatements]
comments: true
share: true
---

In Python, you can use nested if statements to create conditional statements with multiple levels of conditions. This is helpful when you need to check multiple conditions and perform different actions based on the results.

Here's an example of a nested if statement in Python:

```python
x = 10
y = 5

if x > y:
    print("x is greater than y")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")
elif x == y:
    print("x and y are equal")
else:
    print("x is less than y")
```

In this example, we have three levels of conditions. First, we check if x is greater than y using the outer if statement. If this condition is true, we print "x is greater than y". 

Inside the inner if statement, we check if x is greater than 0. If this condition is true, we print "x is positive". If it's false, we print "x is negative".

If the initial condition of x > y is false, we move to the next elif statement and check if x is equal to y. If this condition is true, we print "x and y are equal".

If both the initial and elif conditions are false, we move to the else statement and print "x is less than y".

Note that in this example, we've used the `print()` function to display the output. You can modify the actions inside each condition according to your requirements.

By using nested if statements, you can create complex conditional structures in Python to handle multiple cases based on different conditions.

#python #conditionalstatements