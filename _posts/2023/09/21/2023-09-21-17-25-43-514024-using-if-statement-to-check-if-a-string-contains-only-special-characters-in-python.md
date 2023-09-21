---
layout: post
title: "Using if statement to check if a string contains only special characters in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---
title: Using if statement to check if a string contains only special characters in Python
date: 2021-10-15
tags: python, if statement
---

# Using if statement to check if a string contains only special characters in Python

In Python, you can use an `if` statement to check if a string contains only special characters. This can be useful when you want to validate user input or perform specific tasks on strings that meet this criteria. In this blog post, we will explore how to accomplish this.

## Solution

Here's an example code snippet that demonstrates how to perform this check using an `if` statement in Python:

```python
def contains_only_special_characters(string):
    special_characters = "!@#$%^&*()_+=-{}[]|\:;"'<>,.?/"
    for char in string:
        if char.isalpha() or char.isdigit() or char.isspace():
            return False
    return True

# Example usage
input_string = "!@#$%^&*"
if contains_only_special_characters(input_string):
    print(f"The string '{input_string}' contains only special characters.")
else:
    print(f"The string '{input_string}' does not contain only special characters.")
```

In the above code, we define a function `contains_only_special_characters` that takes a string as input. We iterate over each character in the string and check if it is either an alphabetic character (`isalpha()`), a digit (`isdigit()`), or whitespace (`isspace()`). If any of these conditions are true, we immediately return `False` indicating that the string does not contain only special characters. If none of the conditions are true, we return `True` indicating that the string contains only special characters.

We then provide an example usage of the function. In this example, the input string is `!@#$%^&*`. The `if` statement checks if the string contains only special characters using the `contains_only_special_characters` function. If the condition is true, we print a message indicating that the string contains only special characters. If the condition is false, we print a message indicating that the string does not contain only special characters.

## Conclusion

By using an `if` statement in Python, you can easily check if a given string contains only special characters. This can be helpful in various scenarios, such as input validation or string manipulation. Feel free to modify the code snippet provided to suit your specific requirements.