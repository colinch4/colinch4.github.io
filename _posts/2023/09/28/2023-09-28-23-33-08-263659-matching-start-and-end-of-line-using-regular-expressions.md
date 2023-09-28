---
layout: post
title: "Matching start and end of line using regular expressions"
description: " "
date: 2023-09-28
tags: [regex, programming]
comments: true
share: true
---

## JavaScript
```javascript
const text = `This is a sample text
With multiple lines
And different patterns`;

const regex = /^This.*patterns$/gm;
const matches = text.match(regex);

console.log(matches);
```

In JavaScript, we can use the `^` symbol to match the start of a line and the `$` symbol to match the end of a line. By adding the `m` flag at the end of the regular expression, we enable the multi-line mode, allowing the `^` and `$` to match the start and end of individual lines rather than the whole input string.

## Python
```python
import re

text = """This is a sample text
With multiple lines
And different patterns"""

regex = r"^This.*patterns$"
matches = re.findall(regex, text, re.MULTILINE)

print(matches)
```

In Python, we use the `re` module to work with regular expressions. The `^` and `$` symbols work similarly to JavaScript. We need to pass the `re.MULTILINE` flag to the `re.findall()` function to match the start and end of lines instead of the whole string.

## Ruby
```ruby
text = """This is a sample text
With multiple lines
And different patterns"""

regex = /^This.*patterns$/m
matches = text.scan(regex)

puts matches
```

In Ruby, regular expressions work in a similar way. By using the `/m` flag after the regular expression, we enable the multi-line mode and allow `^` and `$` to match line boundaries instead of the beginning and end of the entire string. We can use the `scan()` method to find all matches in the text.

## Conclusion
Matching the start and end of a line using regular expressions is a powerful technique for pattern matching and text manipulation. Whether you're working in JavaScript, Python, Ruby, or any other programming language with regex support, this knowledge will come in handy. Start experimenting with regular expressions and leverage their flexibility and power to suit your needs.

#regex #programming