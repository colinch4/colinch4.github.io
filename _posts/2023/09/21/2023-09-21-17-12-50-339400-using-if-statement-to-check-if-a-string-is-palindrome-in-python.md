---
layout: post
title: "Using if statement to check if a string is palindrome in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

A **palindrome** is a word, phrase, number, or other sequence that reads the same forward and backward. In this blog post, we will explore how to check if a string is a palindrome using an **if statement** in Python.

## Approach

To determine whether a string is a palindrome or not, we can compare the first character of the string with the last character, the second character with the second last character, and so on. If all the pairs of characters match, the string is a palindrome.

## Python Code

```python
def is_palindrome(string):
    # Remove any non-alphanumeric characters and convert to lowercase
    sanitized_string = ''.join(char.lower() for char in string if char.isalnum())

    # Check if the sanitized string is equal to its reverse
    if sanitized_string == sanitized_string[::-1]:
        return True
    else:
        return False

# Test the function
input_string = "A man, a plan, a canal, Panama!"
if is_palindrome(input_string):
    print("The string '{}' is a palindrome.".format(input_string))
else:
    print("The string '{}' is not a palindrome.".format(input_string))
```

## Explanation

In the code above, we define a function called `is_palindrome` that takes a string as input. To handle cases where the string may contain non-alphanumeric characters or have different cases (e.g., uppercase/lowercase), we create a sanitized version of the input string. 

We use a list comprehension to iterate over each character in the input string, filtering out non-alphanumeric characters using the `isalnum()` method, and converting each character to lowercase using the `lower()` method. The resulting sanitized string is stored in the `sanitized_string` variable.

Next, we use an **if statement** to compare the sanitized string with its reverse. The `[::-1]` syntax is used to create a reversed version of the string. If the sanitized string and its reverse are equal, we return `True`, indicating that the string is a palindrome. Otherwise, we return `False`.

Finally, we test the `is_palindrome` function by passing an example string and print the result accordingly.

## Conclusion

By using an **if statement** in Python, we can easily check whether a given string is a palindrome or not. Understanding how to manipulate strings and compare characters can be useful not just for checking palindromes, but also for various other string-related operations.