---
layout: post
title: "Using if statement to check if a string is a valid IP address in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

Here's an example of how you can implement this check using an `if` statement and the `re` module in Python:

```python
import re

def is_valid_ip(ip_address):
    # Regular expression pattern for validating IP address
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    # Use regular expression to match against the IP address
    match = re.match(pattern, ip_address)

    # If there is a match and all octets are valid (0-255), return True
    if match:
        octets = match.groups()
        return all(0 <= int(octet) <= 255 for octet in octets)
    
    return False

# Example usage
ip = "192.168.0.1"
if is_valid_ip(ip):
    print(f"{ip} is a valid IP address")
else:
    print(f"{ip} is not a valid IP address")
```

In the above code:

- The `is_valid_ip` function takes an `ip_address` parameter and uses a regular expression pattern to match against the input string.
- The pattern `r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'` matches four groups of 1-3 digits separated by periods. Each group represents an octet in the IP address.
- If there is a match, we extract the octets using the `groups()` method of the `match` object and check if each octet is within the valid range (0-255).
- Finally, we return `True` if all the octets are valid, and `False` otherwise.

You can use this method to check if a string is a valid IP address before further processing or validation.