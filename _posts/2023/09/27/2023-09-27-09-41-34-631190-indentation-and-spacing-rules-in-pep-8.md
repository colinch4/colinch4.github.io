---
layout: post
title: "Indentation and spacing rules in PEP 8"
description: " "
date: 2023-09-27
tags: [coding, PEP8]
comments: true
share: true
---

PEP 8 is a style guide for Python code, and it provides guidelines on how to format your code to make it more readable and consistent. One important aspect of code formatting is indentation and spacing. In this blog post, we will explore the rules outlined in PEP 8 for indentation and spacing in Python code.

## Indentation

Indentation refers to the number of spaces or tabs used to visually separate blocks of code. PEP 8 recommends using **4 spaces** for indentation. It explicitly suggests **avoiding** the use of tabs, as mixing tabs and spaces can lead to inconsistent formatting.

Here is an example of proper indentation according to PEP 8:

```python
def my_function():
    if condition:
        print("Condition is true.")
        print("Another statement.")

    for i in range(5):
        print(i)
```

## Use of Spaces

PEP 8 also provides guidelines on using spaces within your code. Here are the key rules:

### 1. Indentation after a colon

After a colon (`:`), there should be a **single space** before starting a new block of code.

```python
if condition:
    # code block
```

### 2. No spaces at the beginning or end of a line

Avoid using spaces at the **beginning** or **end** of a line.

```python
x = 5  # Correct
y = 10      # Incorrect

result = a + b  # Correct
result = a + b    # Incorrect
```

### 3. Operators and assignments

For **binary operators** (e.g., `+`, `-`, `*`, `/`), there should be **spaces** before and after the operator.

```python
x = 10
y = 5
z = x + y
```

For **assignments** (`=`, `+=`, `-=`), there should be a **single space** before and after the operator.

```python
x = 10
y += 5
```

### 4. Method arguments and parameters

There should be **no space** between the name of a function and the opening parenthesis, but there should be a **single space** after the comma separating arguments.

```python
def my_function(arg1, arg2):
    # code block
```

### 5. Line length and line breaks

PEP 8 recommends limiting lines to a maximum of **79 characters**. If a line exceeds this limit, it is recommended to break it into multiple lines using parentheses. The line continuation should be indented **4 spaces** from the normal indentation level.

```python
result = (long_variable_name1 + long_variable_name2 +
          long_variable_name3)
```

## Conclusion

Following the indentation and spacing rules outlined in PEP 8 helps to maintain a consistent and readable codebase. Adhering to these guidelines not only makes your code easier to understand but also promotes collaboration and maintainability.

#coding #PEP8