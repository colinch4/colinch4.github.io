---
layout: post
title: "[Python] Using variables in regular expressions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Using Variables in Regular Expressions

### 1. Basic Variable Usage

One way to use variables in regular expressions is by simply incorporating them directly into the pattern. You can do this by concatenating the variable with the rest of the regular expression string. Here's an example:

```python
import re

pattern = "apple"
fruit_regex = re.compile(pattern)

text = "I love apple pie"
matches = fruit_regex.findall(text)

print(matches)
```

In the above code, we define a regular expression pattern using the variable `pattern`. We then compile the pattern into a regular expression object `fruit_regex`. Finally, we use the `findall()` method to search for all occurrences of the pattern in the given text. The output will be `['apple']` as the pattern matches the word "apple" in the text.

### 2. Using Variables with Special Characters

Sometimes, your regular expression pattern may contain special characters that need to be escaped. To incorporate variables with special characters, you can use the `re.escape()` function. This function escapes any special characters present in the variable's value. Here's an example:

```python
import re

fruit = "apple"
pattern = re.escape(fruit)
fruit_regex = re.compile(pattern)

text = "I love apple pie"
matches = fruit_regex.findall(text)

print(matches)
```

In the above code, we use the `re.escape()` function to escape any special characters in the variable `fruit`. This ensures that the variable's value is treated as a literal string in the regular expression pattern. The output will be the same as the previous example: `['apple']`.

### 3. Using Variables with Modifier Flags

Modifier flags in regular expressions allow you to change the behavior of the pattern matching. You can use variables to specify these flags dynamically. Here's an example:

```python
import re

fruit = "apple"
pattern = f"(?i){fruit}"
fruit_regex = re.compile(pattern)

text = "I love APPLE pie"
matches = fruit_regex.findall(text)

print(matches)
```

In the above code, we use an f-string to embed the variable `fruit` into the regular expression pattern. We prepend `(?i)` to make the pattern case-insensitive. The output will be `['APPLE']` as the pattern matches the word "APPLE" in the text.

### 4. Using Variables with Quantifiers

Quantifiers in regular expressions specify the number of occurrences of a pattern that should be matched. You can use variables to customize these quantifiers. Here's an example:

```python
{% raw %}
import re

fruit = "apple"
occurrences = 3
pattern = f"{fruit}{{0,{occurrences}}}"
fruit_regex = re.compile(pattern)

text = "I love apples, apple pie, and apple cider."
matches = fruit_regex.findall(text)

print(matches)
{% endraw %}
```

In the above code, we use an f-string to embed the variable `fruit` and `occurrences` into the regular expression pattern. We use the `{}` syntax to specify that the pattern should match between 0 and `occurrences` number of occurrences of the word "apple". The output will be `['apple', 'apple', 'apple']` as the pattern matches the word "apple" three times in the text.

## Conclusion

In this blog post, we explored how to use variables in regular expressions in Python. We saw that by incorporating variables into the regular expression pattern, we can make our patterns dynamic and flexible. Whether you need to match a specific word, escape special characters, specify modifier flags, or customize quantifiers, using variables in regular expressions can greatly enhance the power and versatility of your code.