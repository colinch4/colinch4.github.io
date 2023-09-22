---
layout: post
title: "Using if statement to check if a number is a palindrome in Python"
description: " "
date: 2023-09-21
tags: [Palindrome]
comments: true
share: true
---

In this blog post, I will explain how to check if a given number is a palindrome using the `if` statement in Python. A palindrome is a number that reads the same forwards and backwards, like 121 or 1221. We will write a simple program that takes an input number and checks if it is a palindrome or not.

## Approach

The approach to solve this problem is quite simple. We will reverse the given number and check if it is equal to the original number. If it is, then the number is a palindrome.

## Example Code

Here is an example code snippet that demonstrates how to check if a number is a palindrome in Python:

```python
def is_palindrome(num):
    # Converting the number to a string for easy manipulation
    num_str = str(num)
    # Reversing the string
    reverse_str = num_str[::-1]

    if num_str == reverse_str:
        return True
    else:
        return False

# Testing the function
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
```

In this code, we define a function called `is_palindrome` which takes the number as a parameter. Inside the function, we convert the number to a string and reverse the string using slicing. Then, we compare the original string with the reversed string using the `==` operator. If they are equal, we return `True`, indicating that the number is a palindrome, otherwise `False`.

Finally, we test the function by passing the number `12321` to it and print the corresponding message based on the return value.

## Conclusion

In this blog post, we have learned how to check if a number is a palindrome using the `if` statement in Python. The code snippet provided demonstrates a simple approach to solve this problem. Remember to convert the number to a string and compare it with its reverse to determine if it is a palindrome. Happy coding! #Python #Palindrome