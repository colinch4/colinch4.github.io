---
layout: post
title: "[Python] Convert a String into Tuple"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## Method 1: Using the `split()` method and tuple constructor

The simplest way to convert a string into a tuple is by using the `split()` method to split the string into a list of substrings, and then using the tuple constructor to convert the list into a tuple.

```python
string = "apple, banana, cherry"
tuple_1 = tuple(string.split(", "))
print(tuple_1)
```

Output:
```
('apple', 'banana', 'cherry')
```

In this example, the `split(", ")` method is used to split the string at each comma followed by a space, creating a list `['apple', 'banana', 'cherry']`. The tuple constructor `tuple()` is then applied to this list, converting it into a tuple.

## Method 2: Using list comprehension and tuple constructor

Alternatively, we can use list comprehension to create a new list of elements from the string, and then convert that list into a tuple using the tuple constructor.

```python
string = "1 2 3 4 5"
tuple_2 = tuple([int(x) for x in string.split()])
print(tuple_2)
```

Output:
```
(1, 2, 3, 4, 5)
```

In this example, the string `"1 2 3 4 5"` is split into a list of substrings using the `split()` method without any arguments. The list comprehension `[int(x) for x in string.split()]` is used to iterate over each substring in the list and convert it to an integer. Finally, the tuple constructor is used to convert the resulting list `[1, 2, 3, 4, 5]` into a tuple.

## Method 3: Using the `ast.literal_eval()` function

Another way to convert a string into a tuple is by using the `ast.literal_eval()` function from the `ast` module. This function safely evaluate an expression node or a string containing a Python literal or container, such as a tuple.

```python
import ast

string = "(5, 10, 'hello')"
tuple_3 = ast.literal_eval(string)
print(tuple_3)
```

Output:
```
(5, 10, 'hello')
```

In this example, the `ast.literal_eval()` function is used to safely evaluate the string `(5, 10, 'hello')` as a literal tuple without using `eval()` which may execute arbitrary code. The function returns the evaluated tuple.

## Conclusion

Converting a string into a tuple in Python can be achieved through multiple methods. Whether you choose to use the `split()` method and tuple constructor, list comprehension and tuple constructor, or the `ast.literal_eval()` function, you can easily transform strings into tuples to suit your specific needs.