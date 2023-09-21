---
layout: post
title: "Using if statement to check if a number is a perfect square in Python"
description: " "
date: 2023-09-21
tags: [python, perfectsquare]
comments: true
share: true
---

Perfect squares are numbers that can be expressed as the product of an integer multiplied by itself. In Python, there are various ways to check if a given number is a perfect square using if statements. In this blog post, we will explore one such method.

```python
def is_perfect_square(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
```

In the code snippet above, we define a function called `is_perfect_square` that takes in a number `num` as an argument. The function first checks if the number is less than 0, as perfect squares cannot be negative. If `num` is 0, it is considered a perfect square.

For numbers greater than 0, we initialize a variable `i` to 1 and use a while loop to iterate until `i` squared is greater than `num`. Inside the loop, we check if `i` squared is equal to `num`. If it matches, we return `True` indicating that the number is a perfect square.

If the loop completes without finding a perfect square, we return `False`.

Let's test the function with some examples:

```python
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(25))  # Output: True
print(is_perfect_square(18))  # Output: False
print(is_perfect_square(-9))  # Output: False
```

In the example above, we call the `is_perfect_square` function with various numbers and print the output. The output confirms whether the respective number is a perfect square or not.

By using the if statement and a while loop, we have implemented a simple and efficient method to check if a number is a perfect square in Python.

#python #perfectsquare