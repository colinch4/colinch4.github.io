---
layout: post
title: "Extracting URLs from JSON using regular expressions"
description: " "
date: 2023-09-28
tags: [python, json]
comments: true
share: true
---

URL extraction from JSON data using regular expressions can be a useful technique when working with web scraping or data parsing tasks. Regular expressions provide a powerful way to match and extract specific patterns from texts, including URLs.

In this blog post, we will explore how to extract URLs from JSON using regular expressions in Python.

## Using the re module

Python's `re` module provides a set of functions and methods for working with regular expressions. We can utilize this module to extract URLs from JSON data.

```python
import re

# JSON data containing URLs
json_data = {
    "id": 1,
    "name": "John Doe",
    "website": "https://example.com",
    "projects": [
        {
            "name": "Project 1",
            "link": "https://example.com/project1"
        },
        {
            "name": "Project 2",
            "link": "https://example.com/project2"
        }
    ]
}

# Regular expression pattern to match URLs
url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/(?:[-\w./]*(?:\?[\w./%&=]*)?))?"

# Extracting URLs from JSON
urls = re.findall(url_pattern, str(json_data))

# Printing the extracted URLs
for url in urls:
    print(url)
```

The code above demonstrates how to extract URLs from the given JSON data. We define a regular expression pattern to match URLs, using the `r` prefix to indicate a raw string. The `re.findall()` function is then used to find all matches of the URL pattern in the JSON data converted to a string.

## Conclusion

By using regular expressions, we can easily extract URLs from JSON data in a simple and efficient manner. This technique can be helpful when dealing with web scraping, data parsing, or any other scenarios where URLs need to be extracted from JSON.

Remember to handle exceptions and account for different URL formats to ensure accurate extraction. Regular expressions provide a powerful tool, but it's important to use them responsibly and handle edge cases appropriately.

#python #json #url #regex