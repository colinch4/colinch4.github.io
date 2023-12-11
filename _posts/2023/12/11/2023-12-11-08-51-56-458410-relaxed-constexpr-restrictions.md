---
layout: post
title: "[c++] Relaxed constexpr restrictions"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

The `constexpr` keyword in C++ allows the evaluation of a function or object at compile time. However, prior to C++20, `constexpr` functions and constructors were subject to several restrictions, such as not being able to contain loops, or if statements or perform complex operations that were not possible to evaluate at compile time. C++20 introduced significant improvements to `constexpr` functions, relaxing many of these restrictions.

## What are the Changes in C++20?

### Loops and Branching

In C++20, `constexpr` functions and constructors are now allowed to contain loops and conditional statements. This means that code that iterates over a loop or uses if statements can be marked as `constexpr`, hence enabling more complex logic to be evaluated at compile time.

### Dynamic Memory Allocation

Prior to C++20, `constexpr` functions were not allowed to perform dynamic memory allocation. However, with the introduction of C++20, `constexpr` functions can now use `new`, `delete`, and `alloca` to allocate and deallocate dynamic memory.

### Virtual Functions

In C++20, `constexpr` functions can now be virtual, allowing for a wider range of classes and methods to benefit from compile-time evaluation.

### String Manipulation

C++20 relaxed the restrictions on string manipulation in `constexpr` functions, allowing for more flexibility in working with strings at compile time.

## Example

```c++
constexpr int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    constexpr int result = factorial(5); // evaluated at compile time
    // ...
}
```

In the example above, the `factorial` function is marked as `constexpr` and contains a loop, which is now allowed in C++20.

## Benefits

The relaxation of `constexpr` restrictions in C++20 allows for more performance-critical code to be evaluated at compile time, resulting in potential improvements in execution speed and memory usage. It also enables a wider range of code to be written in a way that ensures compile-time safety and efficiency.

## Conclusion

With the improvements introduced in C++20, the usage of `constexpr` has been significantly expanded, allowing for more complex expressions and computations to be evaluated at compile time, thereby enhancing the efficiency and safety of C++ programs.

## References
- C++ reference, "[constexpr specifier](https://en.cppreference.com/w/cpp/language/constexpr)"
- CppCon 2019: Ben Deane, "[Back to Basics: constexpr all the things](https://www.youtube.com/watch?v=uOUO3J4r2Bc)"
- Bjarne Stroustrup, "[The C++ Programming Language](https://www.amazon.com/C-Programming-Language-4th/dp/0321563840)"