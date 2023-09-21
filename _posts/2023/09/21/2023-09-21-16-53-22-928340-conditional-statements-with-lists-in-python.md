---
layout: post
title: "Conditional statements with lists in Python"
description: " "
date: 2023-09-21
tags: [python, conditional, programming]
comments: true
share: true
---

Let's start by understanding the basic structure of a conditional statement. In Python, we have the `if`, `elif` (short for else if), and `else` keywords to define different conditions and their corresponding code blocks.

Here's an example of a simple conditional statement:

```python
my_variable = 10

if my_variable > 5:
    print("The variable is greater than 5")
else:
    print("The variable is less than or equal to 5")
```

In the above code, we check if the value of `my_variable` is greater than 5. If it is, we print "The variable is greater than 5". Otherwise, we print "The variable is less than or equal to 5".

Now, let's see how we can use conditional statements with lists in Python. Suppose we have a list of numbers and we want to check if any of the numbers are greater than 10. We can use a `for` loop to iterate over each element in the list and apply a conditional statement to check if the current element satisfies our condition.

```python
numbers = [5, 10, 15, 20, 25]

for num in numbers:
    if num > 10:
        print(f"{num} is greater than 10")
    else:
        print(f"{num} is less than or equal to 10")
```

In the above code, we iterate over each element in the `numbers` list using the `for` loop. For each number, we apply the conditional statement to check if it is greater than 10. If it is, we print "<number> is greater than 10". Otherwise, we print "<number> is less than or equal to 10".

We can also combine multiple conditions using the `elif` keyword. Let's say we want to check if a number is less than 5, between 5 and 10, or greater than 10. We can use the following code:

```python
numbers = [2, 6, 12, 8, 3]

for num in numbers:
    if num < 5:
        print(f"{num} is less than 5")
    elif 5 <= num <= 10:
        print(f"{num} is between 5 and 10")
    else:
        print(f"{num} is greater than 10")
```

In this example, we use the `elif` keyword to specify the range of numbers between 5 and 10. If the number satisfies this condition, we print "<number> is between 5 and 10". Otherwise, we check if it is less than 5 or greater than 10 and print the corresponding message.

Using conditional statements with lists enables us to perform actions based on the elements present in the list. Whether it's filtering, transforming, or handling specific cases, conditional statements provide a powerful tool for handling lists in Python.

With the ability to combine conditional statements and list manipulation, you can now write more flexible and dynamic code that adapts to different scenarios. This will improve the functionality and efficiency of your Python programs.

#python #conditional-statements #programming