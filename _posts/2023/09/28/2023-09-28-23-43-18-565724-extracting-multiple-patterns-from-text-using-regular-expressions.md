---
layout: post
title: "Extracting multiple patterns from text using regular expressions"
description: " "
date: 2023-09-28
tags: [Regex, PatternMatching]
comments: true
share: true
---

Regular expressions (regex) are powerful tools for pattern matching and extracting specific information from a given text. In this blog post, we will explore how to use regex to extract multiple patterns from a text using Python.

## Getting Started

To begin, we need to install the `re` module, which provides support for regular expressions in Python. You can install it by running the following command:

```python
pip install re
```

## Example Usage

Let's say we have a text containing multiple email addresses and phone numbers, and we want to extract them separately. Here's an example text:

```
John's email address is john@example.com, and his phone number is (123) 456-7890. You can also reach him at john.doe@example.com or (987) 654-3210.
```

To extract the email addresses and phone numbers from this text, we can use regex patterns. Here's how we can do it:

```python
import re

text = "John's email address is john@example.com, and his phone number is (123) 456-7890. You can also reach him at john.doe@example.com or (987) 654-3210."

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phone_numbers = re.findall(phone_pattern, text)

print("Emails:", emails)
print("Phone Numbers:", phone_numbers)
```

**Output:**

```
Emails: ['john@example.com', 'john.doe@example.com']
Phone Numbers: ['(123) 456-7890', '(987) 654-3210']
```

## Explanation

In the example code above, we used the `re.findall()` function to find all matches of the specified patterns in the given text. 

- The `email_pattern` matches any valid email address. 
- The `phone_pattern` matches phone numbers in the format `(XXX) XXX-XXXX`.

By running `re.findall()` with the patterns and the input text, we extracted all the matches into separate lists.

## Conclusion

Regular expressions are useful for extracting specific patterns from text data. In this blog post, we demonstrated how to use regex to extract multiple patterns, such as email addresses and phone numbers, from a given text using Python. With a combination of pattern matching and the `re` module, you can efficiently extract and process important information from large amounts of text.

#Regex #PatternMatching