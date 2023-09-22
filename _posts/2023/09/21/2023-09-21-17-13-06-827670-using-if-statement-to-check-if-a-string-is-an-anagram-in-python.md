---
layout: post
title: "Using if statement to check if a string is an anagram in Python"
description: " "
date: 2023-09-21
tags: [Anagram]
comments: true
share: true
---

An anagram is a word or phrase formed by rearranging the letters of another word or phrase. In this blog post, we'll explore how to use an `if` statement to check if a string is an anagram in Python.

## Approach

To check if two strings are anagrams, we can compare their sorted versions. If the sorted versions of both strings are equal, then the strings are anagrams.

## Example Code

Below is an example code snippet that demonstrates this approach:

```python
def is_anagram(str1, str2):
    # Remove any whitespace and convert the strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the strings and compare them
    return sorted(str1) == sorted(str2)

# Test cases
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("aabb", "abab"))      # False
```

In the above code, the `is_anagram()` function takes two strings as arguments. It removes any whitespace and converts both strings to lowercase. Then, it sorts the characters of each string and compares them using the `==` operator. The function returns `True` if the strings are anagrams, and `False` otherwise.

## Conclusion

By using an `if` statement in combination with string sorting, we can easily check if two strings are anagrams in Python. This approach provides a simple and efficient solution for solving anagram-related problems.

#Python #Anagram