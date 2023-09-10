---
layout: post
title: "[Python] List comprehension in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

In Python, **list comprehension** is a concise way to create lists based on existing lists, strings, or other sequences. It allows you to generate new lists by applying certain operations or conditions to the elements of an existing list.

List comprehensions in Python have a simple and expressive syntax, making them a powerful tool for working with lists. They can help you write more readable and efficient code.

## Syntax of List Comprehension

The basic syntax of a list comprehension in Python is:

```python
new_list = [expression for item in iterable if condition]
```

* `new_list`: The new list that will be created.
* `expression`: The operation or calculation to be performed on each item.
* `item`: The variable that represents each element of the iterable.
* `iterable`: The original list, string, or other sequence.
* `condition` (optional): A condition that filters the elements based on a certain criteria.

Let's look at some examples to understand how list comprehensions work.

## Example 1: Creating a new list

Suppose we have a list of numbers and we want to create a new list containing the squares of each number. We can achieve this using list comprehension as follows:

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

In this example, the expression `num ** 2` calculates the square of each number in the `numbers` list. The resulting squares are then added to the new list `squares`.

## Example 2: Filtering elements

List comprehensions can also include a condition to filter elements based on a specific criteria. Let's say we want to create a new list containing only the even numbers from the original list. We can add a condition to achieve this:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]
```

In this example, the condition `num % 2 == 0` checks if the number is divisible by 2, indicating that it's an even number. Only the even numbers satisfy this condition and are added to the new list `even_numbers`.

## Example 3: Manipulating strings

List comprehensions can also be used with strings. Let's say we have a string and we want to create a new list containing the uppercase letters from the string:

```python
text = "Hello, World!"
uppercase_letters = [letter for letter in text if letter.isupper()]
print(uppercase_letters)  # Output: ['H', 'W']
```

In this example, the condition `letter.isupper()` checks if each letter in the string is uppercase. Only the uppercase letters satisfy this condition and are added to the new list `uppercase_letters`.

## Conclusion

List comprehension is a powerful feature in Python that allows you to create new lists based on existing lists, strings, or other sequences. It provides a concise and readable way to perform operations or filter elements. By using list comprehension, you can write more efficient code and make your Python programs more expressive.