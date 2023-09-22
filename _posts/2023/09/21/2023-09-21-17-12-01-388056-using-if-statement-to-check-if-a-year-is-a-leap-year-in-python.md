---
layout: post
title: "Using if statement to check if a year is a leap year in Python"
description: " "
date: 2023-09-21
tags: [leapyear]
comments: true
share: true
---

In Python, you can use an `if` statement to check if a year is a leap year. A leap year is a year that is evenly divisible by 4, except for years that are evenly divisible by 100. However, years that are evenly divisible by 400 are still considered leap years.

Here is an example code snippet to check if a year is a leap year in Python:

```python
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2020
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

In this example, we define a function `is_leap_year` that takes a `year` as input and returns `True` if it is a leap year, and `False` otherwise.

The `if` statement is used to check if the `year` is evenly divisible by 4 using the modulo operator `%`. If it is, the code checks if it is also evenly divisible by 100. If it is, it further checks if it is divisible by 400. If all of these conditions are met, the function returns `True`, indicating that the year is a leap year. Otherwise, it returns `False`.

Finally, we call the `is_leap_year` function with the `year` we want to check and print the result accordingly.

Remember to replace the `year` variable in the example with the year you want to check.

#python #leapyear