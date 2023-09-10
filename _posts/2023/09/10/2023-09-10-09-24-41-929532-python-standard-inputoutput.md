---
layout: post
title: "[Python] Standard input/output"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Reading input from the user

The `input()` function allows us to read user input from the command line. It prompts the user for input and returns a string.

```python
name = input("Enter your name: ")
print("Hello", name)
```

In the above example, we use the `input()` function to prompt the user to enter their name. The entered value is then stored in the `name` variable. Finally, we use the `print()` function to display a personalized greeting.

## Writing output to the console

The `print()` function is used to display output on the console. It can display strings, numbers, and variables.

```python
age = 25
print("Your age is", age)
```

In the above example, we use the `print()` function to display the text "Your age is" followed by the value of the `age` variable.

## Formatting output with `print()`

The `print()` function can also format output using various techniques like **string concatenation**, **string interpolation**, or **formatted strings**.

### 1. String concatenation:

```python
name = "John"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")
```

### 2. String interpolation using `%` operator:

```python
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))
```

### 3. Formatted strings (f-strings):

```python
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

All three approaches will produce the same output.

These are the basics of standard input/output in Python. Understanding how to read input from the user and display output is essential for developing interactive command-line applications.