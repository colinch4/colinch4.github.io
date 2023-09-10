---
layout: post
title: "[Python] Variable interpolation in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

1. **Using the `+` operator:**
The simplest way to interpolate variables into strings is by using the `+` operator to concatenate the variables and strings together. Let's say we have two variables `name` and `age`, and we want to create a string that includes these values.

```python
name = "John"
age = 30

message = "My name is " + name + " and I am " + str(age) + " years old."
print(message)
```

The output of this code will be `My name is John and I am 30 years old`.

2. **Using string formatting with `%`:**
Python also provides a string formatting syntax using `%` that allows us to interpolate variables into strings. This method is more concise and readable.

```python
name = "John"
age = 30

message = "My name is %s and I am %d years old." % (name, age)
print(message)
```

The `%s` is a placeholder for a string, and `%d` is a placeholder for an integer. The values specified in parentheses after the string are applied to the placeholders in the order they appear. The output will be the same as before.

3. **Using f-strings:**
Starting from Python 3.6, a new and preferred method for variable interpolation was introduced, called f-strings. F-strings make variable substitution even more straightforward by allowing you to embed expressions inside curly braces `{}`.

```python
name = "John"
age = 30

message = f"My name is {name} and I am {age} years old."
print(message)
```

In this example, the `{name}` and `{age}` expressions are evaluated and their values are inserted into the string. The output will be the same as in the previous examples.

Variable interpolation is a powerful feature in Python that allows you to create dynamic strings by embedding values of variables. Whether you choose to use the `+` operator, string formatting with `%`, or f-strings, the key is to choose the method that suits your coding style and requirements. These methods can greatly improve the readability and maintainability of your code.