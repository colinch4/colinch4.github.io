---
layout: post
title: "Using if statement to check for a specific substring in a string in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here's an example code snippet that demonstrates how to check for a specific substring in a string:

```python
# String to be checked
my_string = "Hello, World!"

# Substring to search for
substring = "Hello"

# Check if substring is present in the string
if substring in my_string:
    print("Substring found in the string!")
else:
    print("Substring not found in the string.")
```

In the above code, we define a string called `my_string` and a substring called `substring`. We then use the `in` operator to check if the `substring` is present in `my_string`. If the `substring` is found in the `my_string`, it will print "Substring found in the string!"; otherwise, it will print "Substring not found in the string."

Note: The `in` operator is case-sensitive, so make sure the string and substring match exactly if you are searching for an exact match.

Using this approach, you can easily check for specific substrings in strings using the `if` statement in Python.