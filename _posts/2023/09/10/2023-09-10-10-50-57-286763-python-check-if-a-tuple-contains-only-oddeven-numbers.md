---
layout: post
title: "[Python] Check if a Tuple Contains Only Odd/Even Numbers"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In this tutorial, we will learn how to check if a tuple in Python contains only odd or only even numbers. We will be using a simple approach to solve this problem.

## Checking if a Tuple Contains Only Odd Numbers

To check if a tuple contains only odd numbers, we can iterate over each element of the tuple and use the modulo operator `%` to check if the number is odd or even. If we find at least one even number, we can conclude that the tuple contains both odd and even numbers.

Here's an example code snippet to demonstrate the approach:

```python
def contains_only_odd_numbers(tuple):
    for num in tuple:
        if num % 2 == 0:
            return False
    return True

# Example usage
tuple1 = (1, 3, 5, 7, 9)
tuple2 = (1, 3, 5, 7, 8)

print(contains_only_odd_numbers(tuple1))  # Output: True
print(contains_only_odd_numbers(tuple2))  # Output: False
```

In the above code, the `contains_only_odd_numbers()` function takes a tuple as input and iterates over each element. If any element is divisible by 2 (i.e., it is even), the function returns `False`. Otherwise, if no even number is found, the function returns `True`.

## Checking if a Tuple Contains Only Even Numbers

To check if a tuple contains only even numbers, we can apply a similar approach as above. We would iterate over each element of the tuple and check if it is divisible by 2. If we find at least one odd number, we can conclude that the tuple contains both odd and even numbers.

Here's an example code snippet to demonstrate the approach:

```python
def contains_only_even_numbers(tuple):
    for num in tuple:
        if num % 2 != 0:
            return False
    return True

# Example usage
tuple3 = (2, 4, 6, 8, 10)
tuple4 = (2, 4, 6, 8, 9)

print(contains_only_even_numbers(tuple3))  # Output: True
print(contains_only_even_numbers(tuple4))  # Output: False
```

In the above code, the `contains_only_even_numbers()` function takes a tuple as input and iterates over each element. If any element is not divisible by 2 (i.e., it is odd), the function returns `False`. Otherwise, if no odd number is found, the function returns `True`.

## Conclusion

In this tutorial, we learned how to check if a tuple in Python contains only odd or even numbers. We used a simple iteration approach and the modulo operator `%` to determine the divisibility of each number. Remember, these functions can be easily modified to work with other data types or containers such as lists or sets.