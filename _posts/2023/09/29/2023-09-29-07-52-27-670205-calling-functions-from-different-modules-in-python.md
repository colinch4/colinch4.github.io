---
layout: post
title: "Calling functions from different modules in Python"
description: " "
date: 2023-09-29
tags: [Python, Functions]
comments: true
share: true
---

## Importing a module

To import a module in Python, you can use the `import` keyword followed by the module name. For example, if you have a module called `math_functions.py`, you can import it like this:

```python
import math_functions
```

## Calling functions from another module

Once you have imported the module, you can access its functions using the dot notation. Suppose the `math_functions.py` module has a function called `add_numbers`. You can call this function as follows:

```python
import math_functions

result = math_functions.add_numbers(10, 5)
print(result)
```

In the above code, we import the `math_functions` module and then call the `add_numbers` function from that module. The result returned by the function is stored in the `result` variable and then printed to the console.

## Importing specific functions

Instead of importing the entire module, you can also import specific functions using the `from` keyword. This allows you to directly access those functions without specifying the module name.

```python
from math_functions import add_numbers, multiply_numbers

result1 = add_numbers(10, 5)
result2 = multiply_numbers(10, 5)

print(result1, result2)
```

In the above code, we import only the `add_numbers` and `multiply_numbers` functions from the `math_functions` module. This allows us to call these functions directly without using the module name as a prefix.

## Aliasing module names

If your module name is long or conflicts with other names in your code, you can use an alias to make it shorter and easier to use. To do this, use the `as` keyword followed by the alias name.

```python
import math_functions as mf

result = mf.add_numbers(10, 5)
print(result)
```

Here, we import the `math_functions` module and assign it an alias `mf`. Now, we can call functions from that module using the alias instead of the full module name.

## Conclusion

In Python, calling functions from different modules is straightforward. You just need to import the module and use the dot notation to access the functions. You can import the entire module or specific functions depending on your requirements. Additionally, you can use aliases to make module names shorter and easier to use. Understanding how to import and call functions from different modules is essential for building larger, modular Python applications.

#Python #Functions