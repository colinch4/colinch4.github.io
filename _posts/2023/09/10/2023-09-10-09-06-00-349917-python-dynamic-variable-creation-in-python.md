---
layout: post
title: "[Python] Dynamic variable creation in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, you can dynamically create variables by using the `exec` function or by manipulating the `globals()` or `locals()` function. Let's explore each approach in more detail.

Using the `exec` function:
```python
var_name = "my_variable"
var_value = 10

exec(f"{var_name} = {var_value}")

print(my_variable) # Output: 10
```

In this example, we have a variable name stored in the `var_name` variable and a corresponding value stored in the `var_value` variable. We use f-strings (formatted strings) to dynamically generate the appropriate `exec` statement. The `exec` function then executes that statement, creating a variable with the name stored in `var_name` and assigning it the value stored in `var_value`.

Using the `globals()` or `locals()` function:
```python
var_name = "my_variable"
var_value = 10

globals()[var_name] = var_value

print(my_variable) # Output: 10
```

Here, we use the `globals()` function to access the global namespace of the Python program. We can then use square brackets to dynamically assign a value to a variable with the name stored in the `var_name` variable.

Similarly, we can use the `locals()` function to access the local namespace of a function. In this case, the variable will be only accessible within the scope of the function.

Dynamic variable creation can be a useful technique, but it's important to use it wisely and consider the implications on code readability and maintainability.