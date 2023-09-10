---
layout: post
title: "[Python] Organizing variables using modules in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Have you ever found yourself in a situation where your Python script became cluttered with a large number of variables? Organizing your variables can greatly improve code readability and maintainability. This is where **modules** come into play.

## What is a module?

In Python, a module is a file containing Python definitions, statements, and functions. It acts as a container to store related variables and functions. By using modules, you can separate your code into logical units, making it easier to manage and reuse.

## Creating a module

To create a module, simply create a new Python file with a `.py` extension. For example, let's create a module called `variables.py`. Inside this file, you can define your variables:

```python
# variables.py

name = "John"
age = 25
height = 180
```

In the above example, we have defined three variables `name`, `age`, and `height` inside the `variables.py` module.

## Importing a module

To access the variables from the module, you need to import it into your Python script. There are a few ways to import a module:

1. Import the whole module:

```python
import variables

print(variables.name)
print(variables.age)
print(variables.height)
```

2. Import specific variables from a module:

```python
from variables import name, age

print(name)
print(age)
```

3. Import the whole module with an alias:

```python
import variables as var

print(var.name)
print(var.age)
```

Choose the import style that best fits your needs and coding style.

## Organizing variables using modules

By organizing your variables using modules, you can group related variables together. For example, let's create a module `user.py` to store variables related to users:

```python
# user.py

first_name = "John"
last_name = "Doe"
age = 25
email = "john@example.com"
```

Now, you can easily access these variables in your main script:

```python
import user

print(user.first_name)
print(user.last_name)
print(user.age)
print(user.email)
```

By using modules, you can easily separate and organize different sets of variables based on their functionality or purpose. This promotes code reusability and improves the overall maintainability of your codebase.

## Conclusion

In this blog post, we explored how to organize variables using modules in Python. By creating separate modules for different sets of variables, you can improve code readability, maintainability, and reusability. Start organizing your variables using modules and experience the benefits for yourself!