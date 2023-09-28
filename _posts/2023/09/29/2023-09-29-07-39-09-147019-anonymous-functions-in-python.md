---
layout: post
title: "Anonymous functions in Python"
description: " "
date: 2023-09-29
tags: [python, anonymousfunctions]
comments: true
share: true
---

In Python, an anonymous function is a function that is defined without a name. It is also known as a lambda function because it is defined using the `lambda` keyword. Anonymous functions are a useful and concise way to write small functions without the need for a formal definition.

Here's the general syntax of an anonymous function:

```python
lambda arguments: expression
```

Let's see some examples to better understand how anonymous functions work:

## Example 1: Adding two numbers

```python
add = lambda a, b: a + b
result = add(5, 3)
print(result)  # Output: 8
```

In this example, we define an anonymous function `add` that takes two arguments `a` and `b` and returns their sum. We then call the function with `5` and `3` as arguments and assign the result to the variable `result`. Finally, we print the result, which will be `8`.

## Example 2: Finding the square of a number

```python
square = lambda x: x ** 2
result = square(4)
print(result)  # Output: 16
```

In this example, we define an anonymous function `square` that takes one argument `x` and returns the square of `x`. We call the function with `4` as the argument and assign the result to the variable `result`. Finally, we print the result, which will be `16`.

## Example 3: Sorting a list of tuples

```python
students = [("Alice", 92), ("Bob", 85), ("Charlie", 88)]
students.sort(key=lambda student: student[1])
print(students)
```

In this example, we have a list of tuples representing students and their respective scores. We use the `sort` function with a key parameter that specifies a lambda function. The lambda function takes a student tuple as an argument and returns the second element of the tuple (the score). This allows us to sort the list of students based on their scores.

### Conclusion

Anonymous functions or lambda functions provide a concise way to define functions without requiring a formal definition. They are often used in situations where a small function is needed, such as in sorting or filtering operations. Understanding how to use anonymous functions can make your code more readable and expressive. #python #anonymousfunctions