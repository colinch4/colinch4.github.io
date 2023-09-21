---
layout: post
title: "Using if statement to check for uppercase letters in a string in Python"
description: " "
date: 2023-09-21
tags: [python, string, uppercase]
comments: true
share: true
---

In Python, you can check if a string contains uppercase letters by using an `if` statement along with the `isupper()` method. The `isupper()` method returns `True` if all the characters in the string are uppercase and `False` otherwise.

Here's an example code that demonstrates how to check for uppercase letters in a string:

```python
# Function to check if a string contains uppercase letters
def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False

# Test the function
input_string = "Hello World"
if has_uppercase(input_string):
    print("The string contains uppercase letters.")
else:
    print("The string does not contain any uppercase letters.")
```

In the above code, we define a function `has_uppercase()` that takes a string as input and iterates over each character in the string. Inside the loop, we use the `isupper()` method to check if the character is uppercase. If we find any uppercase letter, we immediately return `True` from the function. If we reach the end of the loop without finding any uppercase letter, we return `False`.

We then test the function by passing the `input_string` variable to it. If the function returns `True`, we print a message indicating that the string contains uppercase letters. Otherwise, we print a message indicating that the string does not contain any uppercase letters.

This approach will work for any string, whether it contains only letters, digits, symbols, or a combination of them.

Remember to handle different edge cases and validate the input string according to your requirements.

#python #string #uppercase