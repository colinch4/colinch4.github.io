---
layout: post
title: "Conditional statement with multiple composite conditions in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Let's say you have three variables: `x`, `y`, and `z`. You want to execute a certain block of code only if all three variables meet specific conditions.

Here's an example of a conditional statement with multiple composite conditions in Python:

```python
if x > 0 and y < 10 and z == "apple":
    # Execute code here if all conditions are met
    print("All conditions are met!")
else:
    # Execute code here if any of the conditions are not met
    print("Conditions not satisfied.")
```

In this example, the code inside the `if` block will only execute if `x` is greater than 0, `y` is less than 10, and `z` is equal to "apple". If any of the conditions are not met, the code inside the `else` block will execute.

You can also use the logical operator `or` to create composite conditions where at least one condition needs to be true. Here's an example:

```python
if x > 0 or y < 10 or z == "apple":
    # Execute code here if any of the conditions are met
    print("At least one condition is met!")
else:
    # Execute code here if none of the conditions are met
    print("No conditions satisfied.")
```

In this case, the code inside the `if` block will execute if at least one of the conditions is true.

By using logical operators `and` and `or`, you can create complex conditional statements with multiple composite conditions to accurately control the flow of your program.