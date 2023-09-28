---
layout: post
title: "Extracting email addresses from HTML using regular expressions"
description: " "
date: 2023-09-28
tags: [webdevelopment, regex]
comments: true
share: true
---

In web scraping or data extraction tasks, we often come across the need to extract email addresses from HTML content. One way to achieve this is by using regular expressions (regex), which are powerful patterns that can match specific strings of text.

Let's dive into an example of how to extract email addresses from HTML using regex in Python:

```python
import re

def extract_emails_from_html(html_content):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(email_pattern, html_content)
    return emails

# Example usage
html_content = """
<html>
<body>
    <p>Contact us at: info@example.com or support@example.com</p>
    <p>For sales inquiries, email sales@example.com</p>
</body>
</html>
"""

emails = extract_emails_from_html(html_content)
print(emails)
```

In the above code, we define a function `extract_emails_from_html` that takes an HTML content string as input. It uses the `re.findall` function from the `re` module to search for all email addresses that match the specified pattern.

The regex pattern `r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'` represents the structure of a typical email address. It matches a word boundary (`\b`), followed by one or more alphanumeric characters, dots, underscores, percentage signs, and plus/minus signs. Then it matches the `@` symbol, followed by one or more alphanumeric characters, dots, and hyphens. Finally, it matches a dot followed by two or more alphabetic characters to represent the top-level domain.

Running the above code on the given `html_content` will output a list of email addresses: `['info@example.com', 'support@example.com', 'sales@example.com']`.

Remember that regular expressions have limitations and may not cover all possible email address formats. It's important to test and adapt the regex pattern based on the specific requirements and variations in the data you're working with.

# Conclusion

Regular expressions are handy for extracting email addresses from HTML or any other text content. By defining a well-structured regex pattern, we can efficiently extract email addresses from HTML and use them for further processing or analysis.

#webdevelopment #regex