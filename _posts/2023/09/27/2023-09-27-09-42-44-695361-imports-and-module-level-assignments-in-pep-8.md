---
layout: post
title: "Imports and module level assignments in PEP 8"
description: " "
date: 2023-09-27
tags: [PEP8]
comments: true
share: true
---

## Imports in PEP 8

When it comes to imports, PEP 8 recommends the following practices:

1. Place each import statement on a separate line.

   ```python
   import module1
   import module2
   ```

2. Group imports into three distinct sections, separated by a blank line:

   - Standard library imports
   - Third-party library imports
   - Local application imports

   ```python
   import os
   import sys

   import requests
   import numpy as np

   from myapp import module1, module2
   ```

## Module-Level Assignments in PEP 8

For module-level assignments, PEP 8 suggests the following conventions:

1. Use lowercase letters and underscores for variable names.

   ```python
   my_variable = 42
   ```

2. Avoid using the star (`*`) import, except in rare cases.

   ```python
   from my_module import my_function
   ```

3. If several module-level assignments are related, it is acceptable to align them with additional whitespace for improved readability.

   ```python
   x = 10
   y = 20
   result = x + y
   ```

By following these guidelines, Python code becomes more consistent and easier to read for yourself and other developers who might work on the same codebase.

#python #PEP8