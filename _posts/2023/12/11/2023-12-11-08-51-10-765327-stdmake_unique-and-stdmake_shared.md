---
layout: post
title: "[c++] std::make_unique and std::make_shared"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In modern C++, smart pointers are essential for managing dynamic memory and preventing memory leaks. `std::unique_ptr` and `std::shared_ptr` are two smart pointer types introduced in C++11 to facilitate this. In this article, we'll focus on two important functions: `std::make_unique` and `std::make_shared`, which are used to create objects managed by smart pointers. 

## 1. std::make_unique
`std::make_unique` is a utility function introduced in C++14 that allows us to create an instance of an object and wrap it in a `std::unique_ptr`. Here's an example of how to use `std::make_unique`:

```c++
#include <memory>

int main() {
    auto ptr = std::make_unique<int>(42);
    // Do something with ptr
    return 0;
}
```

By using `std::make_unique`, we don't need to explicitly mention the type of the object being created, as the type is automatically deduced from the arguments provided. Also, memory for the object is allocated at the same time, reducing the chances of resource leaks.

## 2. std::make_shared
`std::make_shared` is another utility function introduced in C++11 that creates an instance of an object and wraps it in a `std::shared_ptr`. Here's an example:

```c++
#include <memory>

int main() {
    auto ptr = std::make_shared<int>(42);
    // Do something with ptr
    return 0;
}
```

Similar to `std::make_unique`, using `std::make_shared` allows automatic type deduction, and it also performs a single allocation for both the control block (to manage the shared reference count) and the object itself, potentially improving performance and reducing memory fragmentation.

## 3. Conclusion
In summary, `std::make_unique` and `std::make_shared` are convenient utility functions for creating objects managed by smart pointers in C++. They simplify the process of memory allocation and object creation, while also reducing the chances of memory leaks and improving performance.

If you're working with C++ code, consider using `std::make_unique` and `std::make_shared` for managing dynamic memory and ensuring safe and efficient memory management.

References:
- [std::make_unique - cppreference.com](https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique)
- [std::make_shared - cppreference.com](https://en.cppreference.com/w/cpp/memory/shared_ptr/make_shared)