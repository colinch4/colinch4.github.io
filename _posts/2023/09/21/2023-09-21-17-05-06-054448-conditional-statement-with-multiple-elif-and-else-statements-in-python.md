---
layout: post
title: "Conditional statement with multiple elif and else statements in Python"
description: " "
date: 2023-09-21
tags: [ConditionalStatements]
comments: true
share: true
---

Here's an example of using multiple `elif` statements along with an `else` statement:

```python
# Get the user's age as input
age = int(input("Enter your age: "))

# Check different conditions using if-elif-else statement
if age < 18:
    print("You are underage.")
elif age >= 18 and age < 65:
    print("You are an adult.")
elif age >= 65 and age < 80:
    print("You are a senior citizen.")
else:
    print("You are an elder.")

# Output depends on the value of age
```

In the above code, we first take the user's age as input and convert it to an integer using the `int()` function. We then use the `if-elif-else` statement to check different conditions:

- If the age is less than 18, it prints "You are underage."
- If the age is greater than or equal to 18 and less than 65, it prints "You are an adult."
- If the age is greater than or equal to 65 and less than 80, it prints "You are a senior citizen."
- If the age is above 80 (or any other value not covered by the previous conditions), it prints "You are an elder."

By using multiple `elif` statements, we can handle multiple conditions, and the `else` statement covers any situation not explicitly handled by the preceding conditions.

Remember to consider the order of your conditions as Python evaluates them from top to bottom. So, make sure the conditions are in the right order to avoid unexpected results.

#Python #ConditionalStatements