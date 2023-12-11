---
layout: post
title: "[c++] SFINAE-friendly std::common_type"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, `std::common_type` is a type trait that determines a common type to which a set of types can be converted. However, it doesn't play nicely with SFINAE (Substitution Failure Is Not An Error) because it issues hard errors when the type deduction fails.

Fortunately, C++17 introduced a new feature to make `std::common_type` SFINAE-friendly, allowing it to be used in more scenarios without triggering hard errors.

## How to use SFINAE-friendly `std::common_type`

The SFINAE-friendly version of `std::common_type` is introduced in C++17 and can be used as follows:

```c++
#include <type_traits>

template <typename T, typename U, typename = std::void_t<>>
struct has_common_type : std::false_type {};

template <typename T, typename U>
struct has_common_type<T, U, std::void_t<std::common_type_t<T, U>>> : std::true_type {};
```

In the above code snippet, a custom type trait `has_common_type` is defined. It uses `std::void_t` to check for the existence of a common type between `T` and `U`. If a common type exists, the specialization of `has_common_type` will be set to `true_type`.

## Benefits of SFINAE-friendly `std::common_type`

The ability to use `std::common_type` in SFINAE scenarios provides greater flexibility and better error handling in template metaprogramming. It allows developers to create more generic and robust code that can handle a wider range of type deduction scenarios.

## Conclusion

The SFINAE-friendly `std::common_type` introduced in C++17 provides a more flexible and error-tolerant way to determine a common type between two types. This improvement enhances the usability and robustness of type deduction in C++ template metaprogramming.

For more details, you can refer to the [C++ reference for std::common_type](https://en.cppreference.com/w/cpp/types/common_type).