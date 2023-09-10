---
layout: post
title: "[Python] Regular expressions"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Regular expressions are a powerful tool for pattern matching and text manipulation. In Python, the `re` module provides support for regular expressions. In this blog post, we will explore how to use regular expressions in Python.

## Overview of Regular Expressions

Regular expressions are sequences of characters that define a search pattern. They are mainly used for pattern matching within strings. Python's `re` module provides various functions for working with regular expressions.

## Basic Regular Expression Patterns

Let's start with some basic patterns that can be used in regular expressions.

- `.` : Matches any character except a newline.
- `^` : Matches the start of a string.
- `$` : Matches the end of a string.
- `[]` : Matches any character inside the square brackets.
- `[^]` : Matches any character not inside the square brackets.
- `*` : Matches zero or more occurrences of the preceding pattern.
- `+` : Matches one or more occurrences of the preceding pattern.
- `?` : Matches zero or one occurrence of the preceding pattern.

## Using the `re` module

To use regular expressions in Python, we need to import the `re` module. Here is an example of how to import the module:

```python
import re
```

### `re.search()`

The `re.search()` function searches the given pattern in the string and returns a match object if a match is found. Otherwise, it returns `None`. Let's see an example:

```python
import re

text = "Hello, world!"
pattern = "world"

result = re.search(pattern, text)

if result:
    print("Match found!")
else:
    print("No match found.")
```

Output:

```
Match found!
```

### `re.findall()`

The `re.findall()` function returns all non-overlapping matches of a pattern in the string, as a list of strings. Here is an example:

```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "[aeiou]"

result = re.findall(pattern, text)

print(result)
```

Output:

```
['e', 'u', 'i', 'o', 'o', 'u', 'o', 'e', 'a', 'o']
```

### `re.sub()`

The `re.sub()` function replaces occurrences of a pattern in a string with a specified replacement string. Let's see an example:

```python
import re

text = "Hello, world!"
pattern = "world"
replacement = "Python"

result = re.sub(pattern, replacement, text)

print(result)
```

Output:

```
Hello, Python!
```

## Conclusion

Regular expressions are a powerful tool for pattern matching and text manipulation in Python. The `re` module provides various functions to work with regular expressions. With regular expressions, you can match specific patterns, extract information, and modify strings easily. Experiment with different patterns and functions to explore the full potential of regular expressions in Python!