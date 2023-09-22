---
layout: post
title: "Using if statements with range() function in Python"
description: " "
date: 2023-09-21
tags: [Range, IfStatements]
comments: true
share: true
---

In Python, the `range()` function is commonly used to generate a sequence of numbers. When combined with `if` statements, it becomes a powerful tool for controlling the flow of your code based on specific conditions.

The `range()` function generates a sequence of numbers starting from 0 (by default) and increments by 1 until the specified number. It can be used in various scenarios, like iterating over a loop or creating a list of numbers.

Let's see how we can use `if` statements with the `range()` function.

## Example: Checking if a Number is Even or Odd

Suppose we want to determine whether a given number is even or odd using `if` statements and the `range()` function. Here's an example:

```python
number = 6

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
```

In the above code, we use the modulus operator `%` to check if the number leaves a remainder of 0 when divided by 2. If the condition evaluates to `True`, we print that the number is even; otherwise, we print that the number is odd.

To check this code with different numbers, change the value of the `number` variable and run the code again.

## Example: Filtering Numbers Within a Range

Another common use case is filtering numbers within a range based on certain conditions. For example, let's say we want to print all the even numbers between 1 and 20:

```python
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
```

In the above code, we use a `for` loop to iterate through each number in the range from 1 to 20. The `if` statement checks if the number is even by applying the modulus operator. If the condition holds true, we print the number.

## Conclusion

Using `if` statements with the `range()` function in Python allows you to perform conditional checks and control the flow of your code based on specific conditions. Whether you want to determine if a number is even or odd, or filter numbers within a range, the combination of `if` statements and `range()` function is a powerful feature in Python.

#Python #Range #IfStatements