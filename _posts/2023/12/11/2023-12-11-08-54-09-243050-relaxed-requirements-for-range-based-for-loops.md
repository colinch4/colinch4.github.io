---
layout: post
title: "[c++] Relaxed requirements for range-based for loops"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, range-based for loops provide a concise and readable way to iterate over a range of elements. However, traditional range-based for loops have some limitations in terms of the types they can iterate over. C++20 introduces relaxed requirements for range-based for loops, expanding the flexibility and usability of this feature.

## What are range-based for loops?

Range-based for loops were introduced in C++11 to simplify the process of iterating over a range of elements, such as arrays, containers, or any type that provides the necessary interface. The syntax is straightforward:

```cpp
for (auto &element : container) {
    // loop body
}
```

This loop iterates over each element in the `container`, and the variable `element` is bound to each value in the range in turn. This makes the code more readable and less error-prone by eliminating the need for manual indexing or iterator management.

## Traditional limitations

In C++11 through C++17, the range-based for loop had strict requirements on the container type. It could only handle iterables with `begin()` and `end()` member functions or free functions, and those member functions should return types that could be used in the loop.

These limitations made it difficult to use range-based for loops with existing code that did not conform to these requirements, including third-party libraries or custom types that did not expose the necessary interface.

## Relaxed requirements in C++20

In C++20, the requirements for range-based for loops have been relaxed, allowing for more flexibility in the types that can be iterated over. The new rules specify that the `begin()` and `end()` functions called during the iteration do not need to be member functions, but can instead be free functions, friend functions, or non-member functions found via argument-dependent lookup (ADL).

For example, a hypothetical `MyType` with `begin()` and `end()` implemented as free functions or as friend functions of `MyType` can now be used directly in a range-based for loop without modification.

## Example

```cpp
#include <iostream>
#include <vector>

template <typename T>
struct CustomContainer {
    T data[3] = {1, 2, 3};

    T* begin() { return std::begin(data); }
    T* end() { return std::end(data); }
};

int main() {
    CustomContainer<int> customContainer;
    for (auto& value : customContainer) {
        std::cout << value << " ";
    }
    return 0;
}
```

In this example, `CustomContainer` is a custom type that does not conform to the traditional requirements for range-based for loops. In C++20, using it in a range-based for loop is possible because its `begin()` and `end()` functions are defined as member functions.

## Conclusion

The relaxed requirements for range-based for loops in C++20 make the language more flexible, allowing for easier integration with existing code and custom types. This enhancement simplifies the process of adopting modern C++ features and provides more intuitive and concise syntax for iterating over different types of containers or ranges.

For more detailed information, refer to the [C++20 standard](https://isocpp.org/std/the-standard).