---
layout: post
title: "Extracting email addresses from text using regular expressions"
description: " "
date: 2023-09-28
tags: [EmailExtraction, RegularExpressions]
comments: true
share: true
---

When working with text data, it is a common task to extract email addresses. Regular expressions are a powerful tool for pattern matching and can be used to efficiently extract email addresses from a given text.

Here is an example code snippet in Python that demonstrates how to extract email addresses using regular expressions:

```python
import re

def extract_email_addresses(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

# Example usage
text = "Please contact me at john.doe@email.com or jane_smith123@gmail.com."
extracted_emails = extract_email_addresses(text)
print(extracted_emails)
```

In this code, we define the regular expression pattern `email_pattern` for matching email addresses. The pattern consists of three parts:
1. The username part, which allows alphanumeric characters, dots, underscores, and certain special characters.
2. The domain part, which allows alphanumeric characters, dots, and hyphens.
3. The top-level domain part, which allows two or more alphabetical characters.

The `re.findall()` function is then used to find all matches of the pattern in the given text and return them as a list of email addresses.

By using regular expressions, we can easily and efficiently extract email addresses from text without having to write custom parsing logic. This method is widely applicable in various scenarios, such as data processing and email scraping.

# #EmailExtraction #RegularExpressions