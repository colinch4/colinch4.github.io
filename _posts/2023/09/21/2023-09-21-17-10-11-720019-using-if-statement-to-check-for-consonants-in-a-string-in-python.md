---
layout: post
title: "Using if statement to check for consonants in a string in Python"
description: " "
date: 2023-09-21
tags: [StringManipulation]
comments: true
share: true
---

```python
def is_consonant(char):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return char.lower() in consonants

def check_consonants(string):
    consonant_count = 0

    for char in string:
        if is_consonant(char):
            consonant_count += 1

    return consonant_count

input_string = "Hello, World!"
total_consonants = check_consonants(input_string)

print(f'The total number of consonants in "{input_string}" is {total_consonants}.')
```

In the code snippet above, we first define a function `is_consonant()` that takes a character as input and checks if it is present in a string of consonants. We use the `.lower()` method to convert the character to lowercase before checking for a match. This is done to handle both uppercase and lowercase consonants.

Next, we define the `check_consonants()` function that takes a string as input. We initialize a variable `consonant_count` to keep track of the number of consonants encountered in the string. We iterate through each character in the string and check if it is a consonant using the `is_consonant()` function. If it is, we increment the `consonant_count` by 1.

Finally, we demonstrate the usage of the function by checking the number of consonants in the string "Hello, World!" and printing the result.

This simple example showcases how to use an `if` statement to check for consonants within a string in Python. By modifying the `consonants` string, you can easily customize the set of consonants to match your specific needs.

#Python #StringManipulation