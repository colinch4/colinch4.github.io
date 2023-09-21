---
layout: post
title: "Using if statement to check for lowercase letters in a string in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---
def check_lowercase_string(string):
    for char in string:
        if char.islower():
            return True
    return False

# Example usage
input_string = "Hello World"
result = check_lowercase_string(input_string)
print(result)  # Output: True

input_string = "HELLO WORLD"
result = check_lowercase_string(input_string)
print(result)  # Output: False
```

In this example, we create a function `check_lowercase_string` that takes a string as input. The function iterates through each character in the string and checks if it is lowercase using the `islower()` method. If any lowercase character is found, `True` is returned. If no lowercase character is found, `False` is returned.

We then demonstrate the usage of this function using two example strings. The first example string contains lowercase letters, so the output is `True`. The second example string contains only uppercase letters, so the output is `False`.

By using this code, you can easily check if a string contains any lowercase letters in Python.