---
layout: post
title: "Using if statement to check if a number is even or odd in Python"
description: " "
date: 2023-09-21
tags: []
comments: true
share: true
---

In Python, you can use an `if` statement to check if a given number is even or odd. The modulo operator `%` helps us determine if a number is divisible by 2. If the remainder is 0, then the number is even, otherwise it is odd.

Here's an example code snippet that demonstrates this:

```python
def check_even_odd(number):
    if number % 2 == 0:  # check if the number is divisible by 2
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage
check_even_odd(4)  # Outputs: 4 is even.
check_even_odd(7)  # Outputs: 7 is odd.
```

In the above code, the `check_even_odd` function takes a `number` parameter and checks if it's divisible by 2 using the modulo operator `%`. If the remainder is 0, it prints that the number is even, otherwise it prints that the number is odd.

By using this technique, you can easily determine whether a given number is even or odd in Python. This can be helpful in various scenarios where you need to perform different operations based on the parity of a number.