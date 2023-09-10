---
layout: post
title: "[Python] Splitting a string into a list of words in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Method 1: Using the `split()` Method

The most straightforward way to split a string into words is by using the built-in `split()` method. This method splits a string into a list of substrings based on a specified delimiter.

```python
sentence = "Hello, world! Welcome to Python"
words = sentence.split()

print(words)
```

Output:
```
['Hello,', 'world!', 'Welcome', 'to', 'Python']
```

In the above example, we split the `sentence` string using the `split()` method without providing any delimiter. By default, `split()` splits the string at each occurrence of whitespace.

## Method 2: Using Regular Expressions

When dealing with more complex string splitting requirements, regular expressions can be a powerful tool. The `re` module in Python provides functions to work with regular expressions.

```python
import re

sentence = "Hello, world! Welcome to Python"
words = re.findall(r'\w+', sentence)

print(words)
```

Output:
```
['Hello', 'world', 'Welcome', 'to', 'Python']
```

In the above example, we use the `findall()` function from the `re` module to extract all the words from the `sentence` string. The regular expression `\w+` matches one or more word characters.

## Method 3: Using `split()` with Custom Delimiters

If you have a specific character or sequence of characters that you want to use as a delimiter, you can pass it as an argument to the `split()` method.

```python
sentence = "Hello, world! Welcome to Python"
words = sentence.split(", ")

print(words)
```

Output:
```
['Hello', 'world! Welcome to Python']
```

In the above example, we split the `sentence` string using the comma followed by a space as the delimiter.

## Conclusion

Spitting a string into a list of words in Python can be done using the `split()` method, regular expressions, or by specifying custom delimiters. The choice of method depends on the complexity of the splitting requirements. Now you have the knowledge to handle this common task in your Python code efficiently.