---
layout: post
title: "[c++] Relaxed restrictions on constexpr functions"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++20, the restrictions on `constexpr` functions have been relaxed, allowing for more flexibility and power in defining compile-time computable functions. 

## What are constexpr functions?

`constexpr` functions are functions that can be evaluated at compile time. They are used to perform computations and produce values that can be used in contexts requiring constant expressions. 

```c++
constexpr int square(int x) {
    return x * x;
}
```

In the above example, the `square` function is declared as `constexpr`, allowing it to be evaluated at compile time when called with constant expressions.

## Relaxed Restrictions

### Loosened Constraints

In C++20, the constraints on `constexpr` functions have been relaxed to allow more flexibility. Prior to C++20, `constexpr` functions were subject to several restrictions, including limitations on the use of control flow constructs like loops and conditional statements. In C++20, these constraints have been loosened, enabling more complex computations to be performed at compile time.

### Expanded Capabilities

C++20 allows `constexpr` functions to use a broader range of language features, including `if`, `switch`, `try`, `catch`, and other previously disallowed constructs. This expansion of capabilities provides developers with greater freedom in implementing compile-time computations and enables the use of more expressive and complex code within `constexpr` functions.

### Improved Usability

The relaxation of restrictions on `constexpr` functions improves the usability and practicality of compile-time computations. It promotes the use of `constexpr` functions for a wider range of scenarios, leading to more efficient code and increased opportunities for performance optimization.

## Example

```c++
constexpr int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}
```

In this example, the `factorial` function uses a conditional statement (`if`) within a `constexpr` function, which is now allowed in C++20.

## Conclusion

The relaxed restrictions on `constexpr` functions in C++20 expand the possibilities for compile-time computations and empower developers to leverage the full expressive power of the language within `constexpr` functions. This improvement in usability and flexibility contributes to a more versatile and efficient codebase, facilitating enhanced performance and more expressive compile-time operations.

## References

- C++20 Standard - [ISO/IEC 14882:2020](https://iso.org/standard/79358.html)
- C++ reference for [constexpr functions](https://en.cppreference.com/w/cpp/language/constexpr)