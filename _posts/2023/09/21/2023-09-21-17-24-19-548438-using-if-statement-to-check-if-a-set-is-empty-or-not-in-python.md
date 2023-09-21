---
layout: post
title: "Using if statement to check if a set is empty or not in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here's an example:

```python
# Create an empty set
my_set = set()

# Check if the set is empty
if not my_set:
    print("The set is empty")
else:
    print("The set is not empty")
```

In this example, we create an empty set called `my_set`. We then use an `if` statement to check if `my_set` is empty. If the set is empty, the condition `not my_set` evaluates to `True`, and the code inside the `if` block will be executed, which prints "The set is empty". If the set is not empty, the code inside the `else` block will be executed, which prints "The set is not empty".

Remember, when working with sets in Python, you can use the `not` keyword followed by the set name to check if the set is empty or not.