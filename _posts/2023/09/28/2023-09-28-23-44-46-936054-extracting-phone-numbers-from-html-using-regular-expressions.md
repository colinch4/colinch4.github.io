---
layout: post
title: "Extracting phone numbers from HTML using regular expressions"
description: " "
date: 2023-09-28
tags: [webdevelopment, regularexpressions]
comments: true
share: true
---

In web scraping, it's often necessary to extract specific information from HTML documents. One typical task is extracting phone numbers from HTML. Regular expressions can be a powerful tool for this purpose.

Let's assume we have an HTML document and we want to extract all the phone numbers present in it. Here's an example of how you can achieve this using regular expressions in Python:

```python
import re

html = """
<html>
<body>
<h1>Contact Information</h1>
<p>Phone: 123-456-7890</p>
<p>Email: example@example.com</p>
<p>Phone: 987-654-3210</p>
</body>
</html>
"""

# Define the regular expression pattern for phone numbers
pattern = r"\d{3}-\d{3}-\d{4}"

# Extract phone numbers using the pattern
phone_numbers = re.findall(pattern, html)

# Print the extracted phone numbers
for phone_number in phone_numbers:
    print(phone_number)
```

In this example, we define the regular expression pattern `"\d{3}-\d{3}-\d{4}"`, which matches a phone number in the format `XXX-XXX-XXXX`, where X represents a digit.

The `re.findall()` function is then used to find all occurrences of the pattern in the HTML document and store them in a list called `phone_numbers`. Finally, we can iterate over the list and print each extracted phone number.

Remember to adjust the regular expression pattern according to the format of the phone numbers you expect to find in your HTML document.

By leveraging regular expressions, you can efficiently extract phone numbers from HTML, which can be useful in various web scraping and data analysis tasks.

#webdevelopment #regularexpressions