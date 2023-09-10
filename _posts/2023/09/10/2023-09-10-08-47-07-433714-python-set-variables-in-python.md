---
layout: post
title: "[Python] Set variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

To set a variable in Python, you can use the assignment operator (`=`). The general syntax is as follows:

```python
variable_name = value
```

Here, `variable_name` is the name of the variable, and `value` is the data you want to assign to that variable. The variable name can consist of letters, numbers, or underscores (_), but it cannot start with a number.

Let's take a look at some examples to understand how to set variables in Python:

### Example 1: Setting a Variable

```python
name = "John Doe"
age = 25
height = 1.75
```

In this example, we have set three variables: `name`, `age`, and `height`. The variable `name` stores a string, `age` stores an integer value, and `height` stores a float value. Notice how we don't need to explicitly declare the type of the variable in Python.

### Example 2: Variables with Mathematical Expressions

```python
x = 5
y = 10
result = x + y
```

Here, we have set two variables `x` and `y` to hold integer values. We then set another variable `result` to store the sum of `x` and `y`. The variable `result` will be equal to 15.

### Example 3: Variables with User Input

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

In this example, we use the `input()` function to prompt the user for their name and age. The input is stored as strings, so we use the `int()` function to convert the age input to an integer.

### Example 4: Variables with Boolean Values

```python
is_student = True
has_license = False
```

In this case, we set two variables `is_student` and `has_license` to store boolean values. The `is_student` variable is set to `True`, while the `has_license` variable is set to `False`.

In conclusion, setting variables in Python is straightforward. You can assign any data type to a variable simply by using the assignment operator (`=`). Variables play a key role in storing and manipulating data, making them an essential concept in programming.

Remember, variable names should be meaningful and descriptive to make your code more readable and understandable. Happy coding!