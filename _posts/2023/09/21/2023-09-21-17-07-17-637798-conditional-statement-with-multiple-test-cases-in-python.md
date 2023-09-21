---
layout: post
title: "Conditional statement with multiple test cases in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

```python
# Example of a conditional statement with multiple test cases
x = 5

if x == 1:
    print("x is equal to 1")
    
elif x == 2:
    print("x is equal to 2")
    
elif x == 3:
    print("x is equal to 3")
    
elif x == 4:
    print("x is equal to 4")
    
else:
    print("x is not equal to 1, 2, 3, or 4")
```

In this example, we have a variable `x` set to 5. The code first checks if `x` is equal to 1 using the `if` statement. If the condition is true, it executes the corresponding block of code and prints "x is equal to 1". 

If the first condition is not true, the program moves to the next condition using the `elif` statement. It checks if `x` is equal to 2 and executes the block of code inside the `elif` statement if the condition is true, printing "x is equal to 2".

If none of the conditions in the `if` and `elif` statements are true, the `else` statement is executed, and it prints "x is not equal to 1, 2, 3, or 4".

You can add as many `elif` statements as needed to handle different test cases. The code will only execute the block of code corresponding to the first true condition. Once a true condition is found, no further conditions are evaluated.

Using conditional statements with multiple test cases in Python helps you handle different scenarios and make your code more versatile and responsive.