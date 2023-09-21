---
layout: post
title: "Using if statements with membership operators in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

If statements are a fundamental part of programming and allow us to control the flow of our code based on certain conditions. Python provides several operators that can be used within if statements to check for membership and make decisions accordingly.

## The `in` Operator

The `in` operator is used to check if a value exists in a sequence, such as a list, tuple, or string. It returns `True` if the value is found, and `False` otherwise.

```python
# Checking if a element exists in a list
fruits = ['apple', 'banana', 'mango']
if 'apple' in fruits:
    print("We have apples!")

# Checking if a character exists in a string
text = "Hello, World!"
if 'o' in text:
    print("'o' is present in the text.")
```

In the above examples, the code checks if the value `'apple'` exists in the `fruits` list and if the character `'o'` is present in the `text` string. If the condition is `True`, the corresponding message is printed.

## The `not in` Operator

Similar to the `in` operator, the `not in` operator checks if a value does **not** exist in a sequence. It returns `True` if the value is not found, and `False` if it is found.

```python
# Checking if an element does not exist in a list
cars = ['Toyota', 'Honda', 'Ford']
if 'Chevrolet' not in cars:
    print("Chevrolet is not one of our cars.")

# Checking if a character does not exist in a string
text = "Python is cool!"
if 'x' not in text:
    print("'x' is not present in the text.")
```

In the above examples, the code checks if the value `'Chevrolet'` does not exist in the `cars` list and if the character `'x'` is not present in the `text` string. If the condition is `True`, the corresponding message is printed.

## Combining with conditional statements

The membership operators can be combined with conditional statements, such as `if`, `elif`, and `else`, to create more complex decision-making structures.

```python
fruits = ['apple', 'banana', 'mango']
choice = input("Enter a fruit: ")

if choice in fruits:
    print("Yes, we have that fruit!")
elif choice == 'quit':
    print("Goodbye!")
else:
    print("Sorry, we don't have that fruit.")
```

In the above example, the code prompts the user to enter a fruit. If the entered fruit value is present in the `fruits` list, it prints a positive message. If the user enters `'quit'`, it prints a goodbye message. Otherwise, it informs the user that the fruit is not available.

By utilizing the `in` and `not in` operators with if statements, we can easily check for the presence or absence of values in sequences, allowing for more flexible decision-making within our Python programs.