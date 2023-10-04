---
layout: post
title: "Extracting numbers from text using regular expressions"
description: " "
date: 2023-09-28
tags: [regex]
comments: true
share: true
---

Have you ever encountered a situation where you needed to extract numeric values from a piece of text? Whether you are working with a large dataset or just trying to extract a specific number from a string, regular expressions can be a powerful tool for accomplishing this task efficiently.

## What are regular expressions?

Regular expressions, often abbreviated as regex or regexp, are sequences of characters that define a search pattern. They are useful for manipulating and extracting data from strings based on patterns or rules. Regex patterns can be used to match and extract specific types of information, such as numbers, from text.

## Extracting numbers with regular expressions

In order to extract numeric values from text using regular expressions, you need to define a pattern that matches the desired format of the numbers you are looking for. Here's an example of how you can extract numbers with Python using the `re` module:

```python
import re

text = "The price is $10.99 and the quantity is 25."

numbers = re.findall(r'\d+\.\d+|\d+', text)

for number in numbers:
    print(number)
```

In the above code snippet, we start by importing the `re` module, which provides support for regular expressions in Python. We define a string `text` that contains the text from which we want to extract numbers.

The `re.findall()` function is used to find all occurrences of the pattern specified within the text. In this case, the regular expression `r'\d+\.\d+|\d+'` matches decimal numbers as well as whole numbers. The `\d` represents any digit, and the `+` means one or more occurrences.

The pattern `'\d+\.\d+|\d+'` specifically looks for either decimal numbers (e.g., 10.99) or whole numbers (e.g., 25).

Finally, we iterate over the `numbers` list and print each extracted number.

## Conclusion

Regular expressions are a powerful tool for extracting specific data, like numbers, from text. By defining a pattern that matches the desired format, you can efficiently extract numeric values using the `re` module in Python.

#python #regex