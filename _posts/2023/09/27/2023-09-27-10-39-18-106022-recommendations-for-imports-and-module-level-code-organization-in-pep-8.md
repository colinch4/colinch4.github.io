---
layout: post
title: "Recommendations for imports and module-level code organization in PEP 8"
description: " "
date: 2023-09-27
tags: []
comments: true
share: true
---

1. Import order:
   - **Standard library imports** should be listed first. These are Python's built-in modules such as `os`, `sys`, or `datetime`. Group them alphabetically and separate them from third-party imports with a blank line.
    
     ```python
     import os
     import sys

     import requests
     import numpy as np
     ```

   - **Third-party library imports** should come after the standard library imports and also be grouped alphabetically. Again, separate them from the local or project-specific imports with a blank line.
    
     ```python
     import requests
     import numpy as np

     from my_package import utils
     ```

   - Finally, **local or project-specific imports** should be placed after third-party imports and also separated by a blank line.
    
     ```python
     from my_package import utils
     from my_package.models import User
     ```

2. Preventing wildcard imports:
   - PEP 8 discourages the use of wildcard imports (`from module import *`). They make it harder to understand where a specific object or function is coming from and can lead to naming collisions. Instead, import specific objects or functions explicitly.
    
     ```python
     # Wrong way
     from math import *
     print(sqrt(4))

     # Preferred way
     from math import sqrt
     print(sqrt(4))
     ```

3. Module-level code organization:
   - Place **constants** (variables that don't change throughout the execution) at the top of the module, using uppercase snake_case naming convention. Make sure to include a comment documenting their purpose and usage if necessary.
    
     ```python
     API_KEY = 'my-api-key'  # Used for the API authentication
     MAX_RETRIES = 3  # Maximum number of retries for network requests
     ```

   - After constants, declare **functions** and **classes**. Functions should be separated by two blank lines, while classes should be separated by a single blank line. Make sure to add proper docstrings for all functions and classes, following the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#381-docstrings) or another appropriate style guide.
    
     ```python
     def get_data(url):
         """Fetches data from the specified URL."""
         ...


     class User:
         """Represents a user."""
         ...
     ```

   - At the end of the module, include a **main execution guard** using `if __name__ == "__main__":`. This allows the code within it to only run when the module is executed as a standalone script, not when imported as a module.
    
     ```python
     if __name__ == "__main__":
         # Code to run when executing the module as a script
         ...
     ```

Remember to periodically run a linter, like `flake8`, on your codebase to ensure it remains compliant with PEP 8 guidelines.