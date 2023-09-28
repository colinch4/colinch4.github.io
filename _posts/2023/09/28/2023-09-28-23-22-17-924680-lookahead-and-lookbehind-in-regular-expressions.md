---
layout: post
title: "Lookahead and lookbehind in regular expressions"
description: " "
date: 2023-09-28
tags: [regex, lookahead]
comments: true
share: true
---

Regular expressions are powerful tools for pattern matching and text manipulation. They allow us to search for specific patterns within strings of text. In some cases, we may want to match a pattern only if it is followed by or preceded by another specific pattern. This is where lookahead and lookbehind assertions come into play.

## Lookahead (?=)

Lookahead assertion, represented by the `(?=)` syntax, allows us to match a pattern only if it is followed by another specific pattern. Consider the following example:

```python
import re

text = "I like apples and oranges"
matches = re.findall("apples(?= and)", text)

print(matches)
```

Output: `['apples']`

In the example above, we are using a lookahead to find the word "apples" only if it is followed by the word "and". The `(?= and)` ensures that the pattern "apples" is matched only if it is followed by " and".

## Lookbehind (?<=)

Lookbehind assertion, represented by the `(?<=)` syntax, allows us to match a pattern only if it is preceded by another specific pattern. Let's take a look at an example:

```python
import re

text = "I like apples and oranges"
matches = re.findall("(?<=like )apples", text)

print(matches)
```

Output: `['apples']`

Here, we are using a lookbehind to find the word "apples" only if it is preceded by the phrase "like ". The `(?<=like )` ensures that the pattern "apples" is matched only if it is preceded by "like ".

## Conclusion

Lookahead and lookbehind assertions are powerful techniques in regular expressions that allow us to match patterns based on what comes before or after them. They give us finer control when searching for specific patterns within text. By incorporating these assertions into our regular expressions, we can achieve more precise and accurate pattern matching.

#regex #lookahead #lookbehind