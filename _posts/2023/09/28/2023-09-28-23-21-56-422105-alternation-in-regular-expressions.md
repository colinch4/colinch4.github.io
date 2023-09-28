---
layout: post
title: "Alternation in regular expressions"
description: " "
date: 2023-09-28
tags: []
comments: true
share: true
---

Alternation allows you to specify multiple patterns to match against, separated by the pipe symbol (`|`). It basically says "match this pattern OR that pattern". The regular expression engine will try to match the patterns in the order they are specified until a match is found.

Here's a simple example to illustrate the concept of alternation:

```python
import re

pattern = r"cat|dog"
text = "I love my cat and dog"

matches = re.findall(pattern, text)
print(matches)
```

In this example, we have a pattern `cat|dog` that will match either the word "cat" or the word "dog". The `re.findall()` function returns all non-overlapping matches as a list.

When we run this code, the output will be:

```
['cat', 'dog']
```

The regular expression engine found both "cat" and "dog" in the given text because they are present in the string.

You can also use alternation when replacing text using the `re.sub()` function:

```python
import re

pattern = r"cat|dog"
text = "I love my cat and dog"

replaced_text = re.sub(pattern, "animal", text)
print(replaced_text)
```

In this example, we substituted both "cat" and "dog" with the word "animal" using `re.sub()`. The output will be:

```
I love my animal and animal
```

Note that the alternation operator `|` has a higher precedence than most other regular expression operators. So, if you want to match a group of characters as part of an alternation, be sure to use parentheses to create a group:

```python
import re

pattern = r"(cat|dog) food"
text = "I have cat food and dog food"

matches = re.findall(pattern, text)
print(matches)
```

In this example, `(cat|dog)` is a group that matches either "cat" or "dog", followed by a space and the word "food". The output will be:

```
['cat', 'dog']
```

In conclusion, alternation in regular expressions allows you to search for multiple patterns or replace them with different values. Understanding this concept and using it effectively can greatly enhance your text manipulation capabilities.