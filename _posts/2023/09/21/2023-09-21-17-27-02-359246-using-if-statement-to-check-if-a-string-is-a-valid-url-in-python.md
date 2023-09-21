---
layout: post
title: "Using if statement to check if a string is a valid URL in Python"
description: " "
date: 2023-09-21
tags: [python, URLvalidation]
comments: true
share: true
---

```python
import urllib.parse

def is_valid_url(url):
    # Check if the url is empty
    if not url.strip():
        return False

    # Parse the url
    parsed = urllib.parse.urlparse(url)

    # Check if the scheme and netloc are both non-empty
    if parsed.scheme and parsed.netloc:
        return True
    else:
        return False
```

In the code above, we define a function `is_valid_url` that takes a `url` as an argument. First, we strip the string to remove any leading or trailing whitespaces. 
Then, we use the `urlparse` function from the `urllib.parse` module to parse the URL. 
We check if both the `scheme` and `netloc` attributes of the parsed URL are non-empty to determine if the URL is valid.

Let's test the function with some examples:

```python
print(is_valid_url("https://www.example.com"))           # Output: True
print(is_valid_url("http://www.example.com"))            # Output: True
print(is_valid_url("www.example.com"))                   # Output: False
print(is_valid_url("example.com"))                       # Output: False
print(is_valid_url("http://localhost:8000"))             # Output: True
print(is_valid_url(""))                                  # Output: False
```

By using this `if` statement and the `urllib.parse` module, we can easily check if a string is a valid URL in Python.
#python #URLvalidation