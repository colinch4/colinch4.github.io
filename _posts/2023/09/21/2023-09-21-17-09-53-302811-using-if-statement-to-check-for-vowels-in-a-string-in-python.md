---
layout: post
title: "Using if statement to check for vowels in a string in Python"
description: " "
date: 2023-09-21
tags: [ifstatement, vowels]
comments: true
share: true
---
# Checking for vowels in a string using if statements in Python

def check_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char.lower() in vowels:
            return True
    return False

# Example usage
input_string = "Hello World"
if check_vowels(input_string):
    print("The string contains vowels.")
else:
    print("The string does not contain any vowels.")

```

#python #ifstatement #vowels