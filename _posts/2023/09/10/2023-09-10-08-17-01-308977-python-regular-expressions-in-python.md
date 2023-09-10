---
layout: post
title: "[Python] Regular expressions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

To use regular expressions in Python, you need to import the `re` module. Here are some common operations that you can perform using regular expressions:

### **Matching Patterns**

To check if a string matches a specific pattern, you can use the `match()` function from the `re` module. It searches for the pattern at the beginning of the string.

```python
import re

string = "Hello, World!"
pattern = r"Hello"

match = re.match(pattern, string)
if match:
    print("Pattern matched")
else:
    print("Pattern not found")
```

In the example above, the pattern `r"Hello"` is matched with the string `"Hello, World!"`, and it prints "Pattern matched".

### **Searching Patterns**

If you want to search for a pattern anywhere in a string, you can use the `search()` function. It returns the first occurrence of the pattern.

```python
import re

string = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"

match = re.search(pattern, string)
if match:
    print("Pattern found")
else:
    print("Pattern not found")
```

This code will match the pattern `r"fox"` with the string `"The quick brown fox jumps over the lazy dog."` and print "Pattern found".

### **Extracting Matches**

You can use regular expressions to extract specific parts of a string that match a pattern. The `findall()` function returns a list of all matches found.

```python
import re

string = "Email addresses: john@example.com, jane@example.com"
pattern = r"\w+@\w+\.\w+"

matches = re.findall(pattern, string)
print(matches)
```

The pattern `r"\w+@\w+\.\w+"` matches email addresses in the string. Running this code will print `["john@example.com", "jane@example.com"]`.

### **Replacing Matches**

Regular expressions also allow you to replace parts of a string that match a pattern. You can use the `sub()` function to perform the replacement.

```python
import re

string = "Hello, World!"
pattern = r"Hello"
replacement = "Hi"

new_string = re.sub(pattern, replacement, string)
print(new_string)
```

In the example above, the pattern `r"Hello"` is replaced with `"Hi"`, resulting in `"Hi, World!"` being printed.

### **Modifiers**

Regular expressions in Python support modifiers that control the behavior of the pattern matching. Some common modifiers are:

- **re.IGNORECASE**: Makes the matching case insensitive.
- **re.MULTILINE**: Allows ^ and $ to match the start and end of each line (instead of the whole string).

You can use these modifiers by passing them as the second argument in the matching functions.

Regular expressions in Python are a versatile tool for handling string manipulation. They can be used in various scenarios like data validation, text parsing, and data extraction. Knowing how to use regular expressions in Python can greatly enhance your coding capabilities.