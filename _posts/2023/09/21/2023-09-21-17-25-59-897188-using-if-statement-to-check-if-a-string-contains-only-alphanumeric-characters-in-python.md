---
layout: post
title: "Using if statement to check if a string contains only alphanumeric characters in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

In this blog post, we will discuss how to use an `if` statement to check if a string contains only alphanumeric characters in Python. 

Python provides several methods to perform this check, but using an `if` statement is one of the simplest approaches. We can iterate over each character in the string and use the `isalnum()` method to check if it is alphanumeric.

Here's an example of how to use an `if` statement to check if a string contains only alphanumeric characters in Python:

```python
def is_alphanumeric(string):
    for char in string:
        if not char.isalnum():
            return False
    return True

# Testing the function
test_string = "HelloWorld123"
if is_alphanumeric(test_string):
    print("The string contains only alphanumeric characters")
else:
    print("The string contains non-alphanumeric characters")
```

In the above code snippet, we define a function called `is_alphanumeric` which takes a string as input. We then iterate over each character in the string using a `for` loop and use the `isalnum()` method to check if the character is alphanumeric. If we find a non-alphanumeric character, we return `False`. If all characters in the string are alphanumeric, we return `True`.

Finally, we test the function by calling it with a test string, `HelloWorld123`. The `if` statement checks if the return value is `True` and prints an appropriate message accordingly.

Make sure to replace the `test_string` with the string you want to check for alphanumeric characters.

Now you can easily use an `if` statement to check if a string contains only alphanumeric characters in Python.