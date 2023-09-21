---
layout: post
title: "Conditional statement with string comparison in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

In Python, you can use conditional statements to control the flow of your program based on specific conditions. One common scenario is comparing strings to perform different actions or execute different blocks of code.

### Using the `if` statement

The `if` statement in Python allows you to execute a block of code if a certain condition is true. When comparing strings, you can use various comparison operators such as `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), etc.

Here's an example that demonstrates how to use a conditional statement with string comparison:

```python
user_input = input("Enter your name: ")

if user_input == "John":
    print("Welcome, John!")
elif user_input == "Jane":
    print("Welcome, Jane!")
else:
    print("Hello, stranger!")
```

In this example, the program prompts the user to enter their name. It then compares the input string to different values using the `==` operator. If the input is equal to "John", it prints "Welcome, John!". If it's equal to "Jane", it prints "Welcome, Jane!". Otherwise, it prints "Hello, stranger!".

### Using the `in` operator for substring matching

You can also use the `in` operator to check if a substring exists within a given string. This can be useful when you want to perform actions based on whether a certain word or phrase is present in the input.

Here's an example:

```python
user_input = input("Enter a sentence: ")

if "apple" in user_input:
    print("The sentence contains the word 'apple'.")
else:
    print("No 'apple' found in the sentence.")
```

In this case, the program prompts the user to enter a sentence. It then checks if the word "apple" is present in the input string using the `in` operator. If it is, it prints "The sentence contains the word 'apple'." Otherwise, it prints "No 'apple' found in the sentence."

### Conclusion

Conditional statements with string comparison are a powerful tool in Python for making decisions based on specific conditions. By using comparison operators like `==` or `in`, you can create dynamic programs that react differently according to the input or the presence of specific substrings.