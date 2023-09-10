---
layout: post
title: "[Python] Deleting variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, variables can be deleted using the `del` keyword. This allows you to remove a variable and free up the memory occupied by its value. The `del` statement can be used on any type of variable, such as strings, numbers, lists, or even functions.

To delete a single variable, you can simply use the `del` keyword followed by the variable name:

```python
my_variable = 10
del my_variable
```

In the example above, the variable `my_variable` is created and assigned the value of `10`. After that, the `del` statement is used to delete the variable. Once the variable is deleted, trying to access it will result in a `NameError`.

You can also delete multiple variables at once by separating them with commas:

```python
var1 = 10
var2 = "Hello"
var3 = [1, 2, 3]

del var1, var2, var3
```

In this example, three variables (`var1`, `var2`, and `var3`) are created and assigned values. The `del` statement is then used to delete all three variables at once.

It's worth noting that deleting a variable does not delete the object it references. If an object has no other references, it will be garbage collected later by Python's automatic memory management.

In addition to deleting variables, you can also delete items from a list or keys from a dictionary using the `del` keyword. For example:

```python
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Removes the third item from the list
```

Similarly, you can delete a key-value pair from a dictionary:

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
del my_dict["age"]  # Removes the "age" key and its corresponding value
```

Deleting variables and other objects should be used with caution. It is generally recommended to let Python's automatic garbage collector handle memory management, as it is more efficient and less error-prone.