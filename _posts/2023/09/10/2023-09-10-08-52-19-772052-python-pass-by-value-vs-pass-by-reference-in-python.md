---
layout: post
title: "[Python] Pass by value vs pass by reference in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Let's dive deeper into understanding pass by value and pass by reference in Python.

## Pass by value
In pass by value, a copy of the value is made and passed to the function. Any changes made to the parameter within the function do not affect the original value. 

In Python, simple data types such as integers, floats, and strings are passed by value. This means that when you pass these types of arguments to a function, a new copy of the value is created inside the function.

Here's an example illustrating this behavior:

```python
def modify_value(num):
    num += 10

value = 5
modify_value(value)
print(value)  # Output: 5
```

In this example, we define a function `modify_value` that takes a parameter `num`. Inside the function, we update the variable `num` by adding 10 to its value. However, when we print `value` after calling the function, it remains unchanged. This is because the `num` parameter in the function is just a copy of the original value, and any modifications made within the function do not affect the original value outside the function.

## Pass by reference-like behavior
Although Python strictly follows pass by value, it can behave like pass by reference in some scenarios. This is because complex data types, such as lists and dictionaries, store references to the memory locations of their elements.

Take a look at this example:

```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```

In this case, we have a function `modify_list` that takes a list `lst` as a parameter. Inside the function, we append the value 4 to the list. When we print `my_list` after calling the function, we can see that the modification made within the function has affected the original list. This happens because `lst` is a reference to the memory location of `my_list`, and both variables are pointing to the same list object.

However, if we reassign the parameter `lst` inside the function, the reference will be lost, and the changes will only affect the local variable `lst`:

```python
def modify_list(lst):
    lst = [4, 5, 6]

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3]
```

In this updated example, when we assign a new list `[4, 5, 6]` to `lst` inside the function, it creates a new list object and breaks the reference to the original `my_list`. Consequently, the original list remains unchanged.

To summarize, Python uses pass by value for simple data types, where a new copy of the value is created. For complex data types, it may exhibit pass by reference-like behavior because they store references to memory locations. Understanding this distinction is crucial for accurately predicting how modifications to function arguments affect the original values.