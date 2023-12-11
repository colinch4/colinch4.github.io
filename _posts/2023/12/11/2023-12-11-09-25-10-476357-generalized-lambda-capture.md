---
layout: post
title: "[c++] Generalized lambda capture"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, lambda functions are a powerful feature for creating anonymous functions within the scope of the function they are used in. Prior to C++14, lambda functions were limited in their ability to capture variables from their enclosing scope, particularly when it came to capturing by move semantics or capturing `this` by value. However, with the introduction of *generalized lambda capture* in C++14, these limitations were overcome.

## 1. Introduction to Lambda Capture

In C++ lambda functions, variables from the enclosing scope can be captured by value `[=]` or by reference `[&]` using the capture list. However, capturing by move semantics or capturing `this` by value used to be problematic prior to C++14.

## 2. Generalized Lambda Capture in C++14

C++14 introduced the ability to capture variables by move semantics and capture `this` by value in lambda functions. This is achieved by specifying the variable to be captured within square brackets and using the move capture syntax `name = std::move(varName)` for move capture, and `this` for capturing `this` by value.

Example:

``` c++
// Generalized Lambda Capture in C++14
auto func = [name = std::move(varName), this](){ /* lambda body */ };
```

In the above example, `name` is captured by move semantics and `this` is captured by value within the lambda function.

## 3. Benefits of Generalized Lambda Capture

Generalized lambda capture in C++14 provides more flexibility and expressiveness when working with lambda functions. It allows for capturing variables by move semantics, capturing `this` by value, and capturing multiple variables with different capture types in a single lambda function.

## 4. Conclusion

With the introduction of generalized lambda capture in C++14, lambda functions in C++ became more powerful and versatile, expanding their capabilities in capturing variables from the enclosing scope. This feature provides additional flexibility and expressiveness when using lambda functions in C++.

## References

- C++ Reference: [Lambda expressions](https://en.cppreference.com/w/cpp/language/lambda)
- Bjarne Stroustrup, "The C++ Programming Language, 4th Edition"

위치 => sample/coding/c++