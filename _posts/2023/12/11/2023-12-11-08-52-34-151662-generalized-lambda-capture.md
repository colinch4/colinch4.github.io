---
layout: post
title: "[c++] Generalized lambda capture"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, lambda expressions provide a convenient way to define anonymous functions. They can capture variables from their enclosing scope using a capture list. With the introduction of C++14, generalized lambda capture was added, allowing for more flexibility in capturing variables.

## Lambda Capture

In a lambda expression, the capture list allows you to specify which variables from the enclosing scope are accessible within the lambda function. There are two ways to capture variables: by value or by reference.

```c++
int x = 5;
auto func = [x]() { /*...*/ };   // Capture by value
auto func2 = [&x]() { /*...*/ };  // Capture by reference
```

## Generalized Lambda Capture

Prior to C++14, the capture list could only capture variables by value or by reference. However, with generalized lambda capture, you can capture variables by moving them or by initializing them with arbitrary expressions.

### Capture by Move

In C++14, you can capture a variable by moving it from the enclosing scope into the lambda function. This is achieved by using the move capture specifier `in place of value or reference capture.

```c++
std::unique_ptr<int> ptr = std::make_unique<int>(10);
auto func = [ptr = std::move(ptr)]() { /*...*/ };  // Capture by move
```

### Capture by Initialization

Generalized lambda capture also allows you to capture variables by initializing them with arbitrary expressions. This provides the flexibility to perform computations or execute functions during the capture.

```c++
int a = 5;
int b = 10;
auto func = [result = a + b]() { /*...*/ };  // Capture by initialization
```

## Benefits

The introduction of generalized lambda capture in C++14 provides more flexibility in capturing variables within lambda expressions. It enables the use of move semantics and arbitrary expressions during the capture process, allowing for improved resource management and enhanced expressive power in lambda functions.

In summary, generalized lambda capture expands the capabilities of lambda expressions in C++, enabling more versatile and expressive capture of variables from the enclosing scope.

References:
- [C++14 Standard Draft](https://github.com/cplusplus/draft/blob/master/papers/n3797.pdf)
- [cppreference - Lambda expressions](https://en.cppreference.com/w/cpp/language/lambda)