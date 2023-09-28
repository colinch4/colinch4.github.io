---
layout: post
title: "Extracting HTML tags with specific attributes using regular expressions"
description: " "
date: 2023-09-28
tags: []
comments: true
share: true
---

Regular expressions are powerful tools for pattern matching and searching within text. In the context of HTML, you can use regular expressions to extract specific HTML tags that have certain attributes. 

Let's say we want to extract all `<a>` tags that have a `href` attribute containing the word "example". Here's an example in Python using the `re` module:

```python
import re

html = """
<html>
<head>
<title>Example Page</title>
</head>
<body>
<a href="https://www.example.com">Home</a>
<a href="https://www.example.com/about">About</a>
<a href="https://www.google.com">Google</a>
<a href="https://www.examplepage.com">Example Page</a>
</body>
</html>
"""

pattern = r'<a\s+href="[^"]*example[^"]*"[^>]*>(.*?)</a>'
matches = re.findall(pattern, html, re.IGNORECASE)

for match in matches:
    print(match)
```
In this example, we define a regular expression pattern that matches the `<a>` tags with an `href` attribute containing the word "example". The `re.findall()` function is used to find all matches in the HTML string. The captured text within the parentheses `(.*?)` is printed as the output.

The regular expression `r'<a\s+href="[^"]*example[^"]*"[^>]*>(.*?)</a>'` can be broken down as follows:

- `<a\s+` matches the start of an `<a>` tag, allowing one or more whitespace characters before the `href` attribute.
- `href="` matches the literal string "href=".
- `[^"]*` matches any number of characters that are not a double quote, allowing for characters preceding the word "example" in the `href` attribute.
- `example` matches the exact word "example".
- `[^"]*` matches any number of characters that are not a double quote, allowing for characters following the word "example" in the `href` attribute.
- `"[^>]*>` matches the closing `"` of the `href` attribute and any additional attributes before the closing `>` of the opening tag.
- `(.*?)` captures the text between the opening and closing tags, non-greedily.
- `</a>` matches the closing `</a>` tag.

When running this code, the following output will be printed:
```
https://www.examplepage.com
```

Keep in mind that regular expressions may not be the ideal solution for parsing HTML. It's generally recommended to use proper HTML parsers like BeautifulSoup for more robust and reliable parsing of HTML documents.