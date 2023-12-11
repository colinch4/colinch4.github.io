---
layout: post
title: "[c++] std::is_constant_evaluated()"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

### Example
Here's an example of how you can use `std::is_constant_evaluated()` in your code:

```c++
#include <iostream>
#include <type_traits>

constexpr int square(int x) {
    if (std::is_constant_evaluated()) {
        return x * x;
    } else {
        return x + x;
    }
}

int main() {
    std::cout << square(5) << std::endl;  // Output will be 10 at runtime
    constexpr int res = square(5);  // Compile-time evaluation result is 25
    return 0;
}
```

In this example, `std::is_constant_evaluated()` is used to conditionally perform different computations based on whether the function is being evaluated at compile time or run time.

### References
- [cppreference - std::is_constant_evaluated](https://en.cppreference.com/w/cpp/types/is_constant_evaluated)