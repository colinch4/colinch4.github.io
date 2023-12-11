---
layout: post
title: "[c++] Fixed deduced return type for normal functions"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In modern C++, the return type of a function can be deduced using `auto` keyword, which is known as *deduced return type*. This feature was initially available only for lambda functions and C++14 onwards brought the ability to use it for normal functions as well.

However, with deduced return types for normal functions, there were scenarios where the return type was incorrectly deduced leading to potential issues. To address this, C++20 introduced the capability to explicitly specify the deduced return type for normal functions using a trailing return type syntax.

## Problem with Deduced Return Type

Consider the following function:

```c++
auto add(int a, int b) {
    return a + b;
}
```

In this case, the return type for `add` function is deduced as `int` based on the return statement. However, if the logic inside the function changes, for example, to return a `double` instead, the return type will be incorrectly deduced, leading to unexpected behavior.

## Trailing Return Type to the Rescue

To overcome the limitations of deduced return types, C++20 offers the ability to explicitly specify the return type using a trailing return type syntax. Here's how the `add` function can be defined with an explicit return type:

```c++
auto add(int a, int b) -> int {
   return a + b;
}
```

By using the trailing return type syntax, the return type is explicitly set to `int`, ensuring that it remains consistent even if the implementation of the function changes.

## Benefits
- **Clarity**: Explicitly specifying the return type enhances code readability and makes it easier for other developers to understand the function signature.
- **Consistency**: By defining the return type explicitly, it prevents unintended changes in the return type when the logic inside the function is modified.
- **Compile-time Checking**: The explicit return type enables the compiler to perform type-checking at compile time, reducing the chances of runtime errors related to incorrect return types.

With the introduction of explicit return type syntax for normal functions in C++20, developers have more control over the return type deduction process, resulting in more robust and maintainable code.

For detailed information, you can refer to the [C++20 standard](https://isocpp.org).