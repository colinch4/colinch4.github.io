---
layout: post
title: "Using if statement to check if a string contains only digits in Python"
description: " "
date: 2023-09-21
tags: [PythonProgramming, StringHandling]
comments: true
share: true
---

Hashtags: #PythonProgramming #StringHandling

With Python, you can easily check if a string contains only digits using an `if` statement. This can be particularly useful when dealing with user input or validating data. In this blog post, we will explore how to accomplish this task.

To check if a string contains only digits, we can iterate through each character of the string and check if it is a digit using the `isdigit()` method. Let's take a look at the code example below:

```python
def contains_only_digits(string):
    for char in string:
        if not char.isdigit():
            return False
    return True

# Testing the function
input_string = "12345"
if contains_only_digits(input_string):
    print("String contains only digits")
else:
    print("String does not contain only digits")
```

In the code snippet above, we define a function `contains_only_digits` that takes a string as input. We iterate through each character in the string using a `for` loop. Inside the loop, we use the `isdigit()` method to check if the character is a digit. If any character is found that is not a digit, we return `False`, indicating that the string does not contain only digits. If all characters are digits, we return `True`.

To test the function, we create a variable `input_string` and assign it a string value of "12345". We then use an `if` statement to check if the string contains only digits by calling the `contains_only_digits()` function. If the function returns `True`, we print "String contains only digits". Otherwise, we print "String does not contain only digits".

By using this method, you can easily check whether a string contains only digits in Python. This can be beneficial in scenarios where you need to validate user input or perform data analysis.