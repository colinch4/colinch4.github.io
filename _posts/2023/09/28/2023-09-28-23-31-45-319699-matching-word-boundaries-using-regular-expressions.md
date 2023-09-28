---
layout: post
title: "Matching word boundaries using regular expressions"
description: " "
date: 2023-09-28
tags: [regex, wordboundaries]
comments: true
share: true
---

Regular expressions are powerful tools for pattern matching and manipulating text. One common requirement is to match a word boundary, which can be useful in tasks such as finding whole words or validating input.

In regular expressions, a word boundary represents the position between a word character and a non-word character. Word characters include letters, digits, and underscores.

To match a word boundary, you can use the `\b` escape sequence in your regular expression pattern. Here are a few examples:

- `\bword\b` matches the exact word "word" surrounded by word boundaries.
- `\b\d+\b` matches any sequence of digits that form a whole number.
- `\b[A-Za-z]+\b` matches any sequence of letters, representing a word.

Let's explore these examples in more detail:

```python
import re

text = "Hello, world! This is an example sentence."

# Match exact word "world"
matched_words = re.findall(r'\bworld\b', text)
print(matched_words)  # Output: ['world']

# Match whole numbers
numbers = "123 456 789"
matched_numbers = re.findall(r'\b\d+\b', numbers)
print(matched_numbers)  # Output: ['123', '456', '789']

# Match words with only letters
sentence = "This is a sentence with several words."
matched_words = re.findall(r'\b[A-Za-z]+\b', sentence)
print(matched_words)  # Output: ['This', 'is', 'a', 'sentence', 'with', 'several', 'words']
```

In each example, we use the `re.findall()` method to find all occurrences matching the given pattern. The `\b` word boundary ensures that only whole words are matched.

By using word boundaries in regular expressions, you can create more precise pattern matching and validation logic in your code. Remember to adjust the pattern to suit your specific needs.

#regex #wordboundaries