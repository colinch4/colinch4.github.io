---
layout: post
title: "[Python] Accessing variables in Python functions"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

When writing functions in Python, it is common to need access to variables defined outside the function scope. In this blog post, we will explore the different ways to access variables in Python functions.

### Global Variables

Global variables are variables that are defined outside any functions and can be accessed from anywhere in the code. To access a global variable inside a function, you need to use the `global` keyword.

```python
count = 0

def increment_count():
    global count
    count += 1

print(count)  # Output: 0
increment_count()
print(count)  # Output: 1
```

In the above example, we have a global variable `count` defined outside the `increment_count()` function. Inside the function, we use the `global` keyword before the variable name to indicate that we want to access the global variable and modify its value.

### Parameters

Another way to access variables in Python functions is by passing them as parameters. Any values passed to a function as parameters can be accessed and used within the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

In the above example, the `greet()` function takes a `name` parameter. When we call the function and pass a value, that value is assigned to the `name` parameter within the function's scope.

### Return Statement

The return statement allows a function to send a result back to the caller. This can be used to access variables calculated or modified within the function.

```python
def square(number):
    return number ** 2

result = square(5)
print(result)  # Output: 25
```

In the above example, the `square()` function takes a `number` parameter and returns the square of that number. We can assign the return value to a variable (`result`) and then access that variable to get the calculated value.

### Closures and Nested Functions

In Python, functions can be defined inside other functions. These are called nested functions or closures. Nested functions can access variables defined in their enclosing scope.

```python
def outer_function():
    message = "Hello from outer function!"

    def inner_function():
        print(message)

    inner_function()

outer_function()  # Output: Hello from outer function!
```

In the above example, the `inner_function()` is defined inside the `outer_function()`. The inner function has access to the `message` variable defined in its enclosing scope (the outer function).

### Conclusion

Being able to access variables in Python functions is crucial for writing modular and reusable code. By understanding global variables, function parameters, return statements, and closures, you can effectively utilize and manipulate variables within your functions.