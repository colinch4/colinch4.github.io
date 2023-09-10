---
layout: post
title: "[Python] Local and global variable behavior in recursive functions in Python"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

When working with recursive functions in Python, it is important to understand how local and global variables behave within the scope of the function. In this blog post, we will explore the behavior of local and global variables in recursive functions and how they can affect the execution and output of our code.

## Local Variables in Recursive Functions

A local variable is defined within the scope of a function and is only accessible within that function. When a recursive function is called multiple times, each call creates a new instance of the local variables.

Let's take a look at an example to better understand this behavior:

```python
def recursive_function(n):
    if n > 0:
        local_variable = n
        print(f"Local variable: {local_variable}")
        
        recursive_function(n - 1)
```

In the above example, we have a recursive function called `recursive_function` that takes an integer `n` as an argument. Inside the function, we define a local variable `local_variable` and assign it the value of `n`. We then print the value of the `local_variable` before making the recursive call to `recursive_function` with `n - 1` as the argument.

When we execute this function with an integer value of `5`, it will create separate instances of the `local_variable` for each recursive call:

```
Local variable: 5
Local variable: 4
Local variable: 3
Local variable: 2
Local variable: 1
```

This demonstrates that each recursive call has its own separate instance of the local variable, and changing its value in one recursive call does not affect the value in other recursive calls.

## Global Variables in Recursive Functions

A global variable is accessible from any part of the code, including within recursive functions. However, modifying a global variable inside a recursive function can sometimes lead to unexpected results.

Consider the following example:

```python
global_variable = 0

def recursive_function(n):
    global global_variable
    
    if n > 0:
        global_variable += n
        print(f"Global variable: {global_variable}")
        
        recursive_function(n - 1)
```

In the above example, we have a global variable `global_variable` which is initialized to 0. Inside the `recursive_function`, we declare the variable as `global` to indicate that we are modifying the global variable rather than creating a new local variable with the same name. We increment the `global_variable` by `n` and print its value before making the recursive call.

When we execute this function with an integer value of `5`, we get the following output:

```
Global variable: 5
Global variable: 9
Global variable: 12
Global variable: 14
Global variable: 15
```

Notice that the value of the `global_variable` accumulates across all recursive calls. Each recursive call modifies the global variable, which affects its value in subsequent calls. This behavior may not always be desired and can lead to unexpected results if not properly handled.

## Conclusion

Understanding the behavior of local and global variables in recursive functions is important to ensure the correctness and predictability of your code. Local variables are created anew with each recursive call, while global variables can be accessed and modified across all recursive calls.

By keeping these behaviors in mind, you can write more effective and reliable recursive functions in Python.