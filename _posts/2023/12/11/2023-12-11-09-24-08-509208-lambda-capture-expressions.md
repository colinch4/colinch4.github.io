---
layout: post
title: "[c++] lambda capture expressions"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, lambda expressions provide a concise way to define a function object (also known as a functor) inline. They can capture variables from the surrounding scope using capture expressions.

## What are Capture Expressions?

A capture expression in a lambda allows you to specify which variables from the enclosing scope should be available inside the lambda body. There are two types of capture expressions:

- **By value:** `[=]` captures all non-static variables by value. For example:
  ```cpp
  int x = 5;
  auto func = [x]() { /* lambda body using x */ };
  ```

- **By reference:** `[&]` captures all non-static variables by reference. For example:
  ```cpp
  int y = 10;
  auto func = [&y]() { /* lambda body using y */ };
  ```

You can also capture specific variables individually:
- **Capture specific variables by value:** `[x, y]` captures `x` and `y` by value.
- **Capture specific variables by reference:** `[&x, &y]` captures `x` and `y` by reference.

## Examples

```cpp
#include <iostream>

int main() {
    int a = 5, b = 10;

    // Capture all variables by value
    auto func1 = [=]() { std::cout << a << " " << b << std::endl; };
    func1();  // Output: 5 10

    // Capture specific variables by reference
    auto func2 = [&a]() { a = 100; };
    func2();
    std::cout << a << std::endl;  // Output: 100

    return 0;
}
```

## Conclusion

Capture expressions in C++ lambda expressions provide flexibility in accessing variables from the enclosing scope. By understanding how to use capture expressions, you can effectively control which variables are accessible inside your lambda functions.

For more information, refer to the [C++ lambda expressions documentation](https://en.cppreference.com/w/cpp/language/lambda).