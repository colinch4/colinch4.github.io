---
layout: post
title: "[Python] Global keyword in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, the `global` keyword is used to indicate that a variable inside a function should be considered as a global variable, rather than creating a new local variable.

When a variable is declared inside a function without using the `global` keyword, it is considered as a local variable. This means that any changes made to the variable will only affect the local scope of the function, and the global variable with the same name remains unaffected.

However, when we want to modify the value of a global variable from within a function, we need to use the `global` keyword. This informs Python that the variable is referring to the global scope, and any changes made to the variable will affect the global variable itself.

Let's look at a simple example to understand how the `global` keyword works:

```python
score = 10

def increase_score():
    global score
    score += 5

print(score)  # Output: 10
increase_score()
print(score)  # Output: 15
```

In the above code, we have a global variable `score` with an initial value of 10. Inside the `increase_score()` function, we use the `global` keyword to indicate that we want to modify the global variable `score`. The function increases the value of `score` by 5.

When we print the value of `score` both before and after calling the function, we can see that the value has been updated globally. If we had not used the `global` keyword inside the function, it would have created a new local variable `score` instead of modifying the global variable.

It's important to note that using global variables can sometimes lead to confusion and make the code harder to understand. It's generally recommended to minimize the use of global variables and instead pass variables as arguments to functions when possible.

In conclusion, the `global` keyword allows us to modify global variables from within a function in Python. It is used to differentiate between local variables and variables in the global scope.