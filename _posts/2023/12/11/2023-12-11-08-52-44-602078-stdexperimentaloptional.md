---
layout: post
title: "[c++] std::experimental::optional"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

The `std::experimental::optional` is a template class introduced in the C++17 standard library. It is part of the C++17 Library Fundamentals Technical Specification 2 (TS2) and provides a way to represent optional (nullable) objects.

## Introduction to std::experimental::optional

The `std::experimental::optional` is a container that may or may not hold a value. It is useful for scenarios where a value might not be available, and it eliminates the need for null pointers or sentinel values.

## Syntax

To use `std::experimental::optional`, include the `<optional>` header file and declare an optional object with the desired type.

```cpp
#include <optional>
std::experimental::optional<int> optInt;
```

## Operations

- **`std::experimental::optional::value()`**: Returns the contained value or throws an exception if no value is present.
- **`std::experimental::optional::value_or()`**: Returns the contained value or a default value if no value is present.
- **`std::experimental::optional::has_value()`**: Returns true if a value is present, false otherwise.
- **`std::experimental::optional::emplace()`**: Constructs the contained value in place.

## Example Usage

```cpp
#include <optional>
#include <iostream>

int main() {
  std::experimental::optional<int> optInt;
  
  if (optInt.has_value()) {
    std::cout << "Value is present: " << optInt.value() << std::endl;
  } else {
    optInt = 42;
    std::cout << "Value is now present: " << optInt.value() << std::endl;
  }
  
  int val = optInt.value_or(-1);
  std::cout << "Value or default: " << val << std::endl;
  return 0;
}
```

## Conclusion

`std::experimental::optional` provides a safer and more expressive way to represent optional values in C++. It eliminates many of the pitfalls associated with using null pointers, making code more robust and easier to maintain.

For further information and examples, please refer to the C++17 standard and relevant documentation.

For more information, refer to the [C++ Reference for std::experimental::optional](https://en.cppreference.com/w/cpp/experimental/optional)