---
layout: post
title: "[Python] Default values for variables in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

## The Basics of Default Values

In Python, you can assign default values to function parameters. This means that if the function is called without providing a value for a specific parameter, the default value will be used. Consider the following example:

```python
def greet(name, message='Hello'):
    print(f"{message}, {name}!")

greet('John')   # Output: Hello, John!
greet('Jane', 'Nice to meet you')   # Output: Nice to meet you, Jane!
```

In the example above, the `greet` function takes two parameters - `name` and `message`. The `message` parameter has a default value of `'Hello'`. When calling the `greet` function without providing a value for `message`, it uses the default value.

## Setting Default Values for Variables

You can also set default values for variables outside of function parameters. This is useful when you want to assign a default value to a variable that might be updated later. Here's an example:

```python
username = None

def set_username(name):
    global username
    username = name

def display_username():
    print(f"Username: {username}")

display_username()   # Output: Username: None

set_username('John')
display_username()   # Output: Username: John
```

In the above example, we declare a variable `username` outside of any function. The initial value of `username` is `None`. Then, we define two functions - `set_username` and `display_username`. The `set_username` function updates the value of `username`, and the `display_username` function prints the value.

By setting a default value of `None` for `username`, we can check if it has been set or not. If it is still `None`, we know that it hasn't been updated yet.

## Default Values and Mutable Types

One important thing to note about default values is how they behave with mutable types such as lists or dictionaries. Consider the following example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item('Apple'))   # Output: ['Apple']
print(add_item('Orange'))   # Output: ['Apple', 'Orange']
```

In the example above, the `add_item` function takes two parameters - `item` and `items`, which has a default value of an empty list. When calling the function without providing a value for `items`, it uses the default list.

However, notice that when we call the function multiple times and append items to the list, the list seems to "remember" the items from previous calls. This is because the default value of `items` is created only once when the function is defined, and subsequent calls to the function use the same list.

To avoid this behavior, it's best to use a sentinel value as the default, such as `None`, and handle it appropriately within the function:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item('Apple'))   # Output: ['Apple']
print(add_item('Orange'))   # Output: ['Orange']
```

By assigning a new empty list to `items` if it is `None`, we ensure that each call to the function starts with a fresh list.

## Conclusion

In this blog post, we explored how to assign default values to variables in Python. We learned that default values can be set for function parameters, as well as for variables outside of function parameters. We also discussed how default values behave with mutable types and provided a solution to overcome undesired behavior.

Default values in Python are a powerful tool that can make your code more concise and flexible. Understanding how to use them effectively will enable you to write cleaner and more maintainable code.