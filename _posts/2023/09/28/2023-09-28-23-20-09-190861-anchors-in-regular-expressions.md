---
layout: post
title: "Anchors in regular expressions"
description: " "
date: 2023-09-28
tags: []
comments: true
share: true
---

There are two main types of anchors: the caret (^) and the dollar sign ($).

The caret (^) anchor is used to match the beginning of a line or string. For example, the regular expression `^Hello` would match any line or string that begins with the word "Hello".

The dollar sign ($) anchor is used to match the end of a line or string. For example, the regular expression `World$` would match any line or string that ends with the word "World".

Here's an example in Python:

```python
import re

text = "Hello, World!"
pattern = r"^Hello"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
```

In this example, the caret anchor is used to match the beginning of the text. If the word "Hello" is found at the beginning of the text, it will display "Match found: Hello".

Similarly, you can use the dollar sign anchor to match the end of the text:

```python
import re

text = "Hello, World!"
pattern = r"World$"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
```

In this case, if the word "World" is found at the end of the text, it will display "Match found: World".

Anchors in regular expressions can be very useful when you need to match specific positions within a string. They provide a way to ensure that a pattern occurs at the beginning or end of a line or string.