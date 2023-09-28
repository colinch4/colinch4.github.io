---
layout: post
title: "Matching phone numbers using regular expressions"
description: " "
date: 2023-09-28
tags: [regex, phonenumbers]
comments: true
share: true
---

In this blog post, we will explore how to use regular expressions to match phone numbers. Regular expressions, also known as regex, are a powerful tool for pattern matching in text. With the right regex pattern, we can easily identify and extract phone numbers from a given text.

## What is a phone number pattern?

Phone numbers can have different formats depending on the country or region. Some common phone number patterns include:

1. 10-digit format: (123) 456-7890
2. 11-digit format with country code: +1 (123) 456-7890
3. International format: +12 34567890

## Constructing a regex pattern for phone numbers

Let's start by constructing a regex pattern to match the 10-digit phone number format commonly used in the United States. The pattern can be defined as follows:

```python
import re

phone_number_pattern = r'\(\d{3}\) \d{3}-\d{4}'
```

Explanation of the pattern:

- `\(` and `\)` match the opening and closing parentheses, respectively.
- `\d{3}` matches exactly three digits.
- `\d{4}` matches exactly four digits.
- `\s` matches a whitespace character.

## Using the regex pattern to match phone numbers

Now that we have our regex pattern, we can use it to match and extract phone numbers from a given text using the `re` module in Python.

```python
text = "John's phone number is (123) 456-7890 and Jane's phone number is (987) 654-3210."

matches = re.findall(phone_number_pattern, text)

for match in matches:
    print(match)
```

Output:

```
(123) 456-7890
(987) 654-3210
```

## Customizing the regex pattern

If you want to match additional phone number formats, you can customize the regex pattern accordingly. For example, to include the 11-digit format with a country code (+1), you can modify the pattern as follows:

```python
phone_number_pattern = r'(\+\d{1,2} )?\(\d{3}\) \d{3}-\d{4}'
```

Explanation of the modified pattern:

- `(\+\d{1,2} )?` matches a country code (e.g., +1) followed by a space, appearing zero or one times.
- The rest of the pattern remains the same as the previous one.

By customizing the pattern, you can match different phone number formats based on your requirements.

## Conclusion

Regular expressions provide a powerful and flexible way to match phone numbers in text. By constructing an appropriate regex pattern, we can accurately extract phone numbers from a given text. Remember to customize the pattern as per specific requirements and country-specific formats.

#regex #phonenumbers