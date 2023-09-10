---
layout: post
title: "[Python] Converting a list of strings to integers in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---
# Converting a list of strings to integers in Python

# Method 1: Using a for loop
string_list = ['1', '2', '3', '4', '5']

integer_list = []
for string in string_list:
    integer_list.append(int(string))

print(integer_list)
# Output: [1, 2, 3, 4, 5]


# Method 2: Using list comprehension
string_list = ['10', '20', '30', '40', '50']

integer_list = [int(string) for string in string_list]

print(integer_list)
# Output: [10, 20, 30, 40, 50]


# Method 3: Using the map() function
string_list = ['100', '200', '300', '400', '500']

integer_list = list(map(int, string_list))

print(integer_list)
# Output: [100, 200, 300, 400, 500]
```
When working with Python, you may encounter situations where you have a list of strings that need to be converted into integers. This can be useful, for example, when you're reading data from a file or receiving input from the user.

Python provides several ways to convert a list of strings to integers. You can use a for loop, list comprehension, or the map() function. Let's explore each method in more detail:

**Method 1: Using a for loop**
In this method, you iterate over each string in the list and use the `int()` function to convert it to an integer. Then, you add the converted integer to a new list called `integer_list`.

**Method 2: Using list comprehension**
List comprehension is a concise way to create lists in Python. In this method, you use a single line of code to iterate over each string in the `string_list` and convert it to an integer using the `int()` function. The resulting list of integers is assigned to the variable `integer_list`.

**Method 3: Using the map() function**
The `map()` function applies a given function (in this case, the `int()` function) to each element of an iterable (in this case, `string_list`). In this method, you convert the map object returned by the `map()` function to a list using the `list()` function. The resulting list of integers is assigned to the variable `integer_list`.

Each of these methods accomplishes the same task of converting a list of strings to integers. The method you choose will depend on the specific requirements of your program and your personal coding style.