---
layout: post
title: "[c++] std::exchange and std::exchange_if_not"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

In C++, `std::exchange` and `std::exchange_if_not` are utility functions provided by the standard library to simplify the process of value exchange. These functions are particularly useful in scenarios where you need to conditionally set a new value while simultaneously retrieving the old value. Let's delve into the details of these utility functions.

## `std::exchange`

The `std::exchange` function is defined as follows:

```cpp
template <class T, class U = T>
T exchange(T& obj, U&& new_value);
```

### Purpose
The purpose of `std::exchange` is to atomically store `new_value` into the object `obj`, and return the previous value of `obj`.

### Parameters
- `obj`: A reference to the object whose value needs to be exchanged.
- `new_value`: The new value that is to be stored in `obj`.

### Return Value
The previous value of `obj`.

### Example
```cpp
#include <iostream>
#include <utility>

int main() {
    int x = 1;
    int old_value = std::exchange(x, 10);
    std::cout << "Old value: " << old_value << std::endl;  // Output: Old value: 1
    std::cout << "New value: " << x << std::endl;          // Output: New value: 10
    return 0;
}
```

In the example above, `std::exchange` updates the value of `x` to 10 and returns the old value, which is 1.

## `std::exchange_if_not`

The `std::exchange_if_not` function is a customization point that conditionally exchanges the value of the object, similar to `std::exchange`. However, it allows for a conditional exchange based on a provided predicate.

### Purpose
The purpose of `std::exchange_if_not` is to conditionally store `new_value` into the object `obj` based on a provided predicate, and return the previous value of `obj`.

While `std::exchange` unconditionally swaps the values, `std::exchange_if_not` allows for an exchange only if a given predicate is true. 

### Parameters
- `obj`: A reference to the object whose value needs to be exchanged.
- `new_value`: The new value that is to be stored in `obj`.
- `predicate`: A function or callable object that determines whether the exchange should occur.

### Return Value
The previous value of `obj`.

### Example
```cpp
#include <iostream>
#include <utility>

bool should_exchange(int old_value, int new_value) {
    return new_value > old_value;
}

int main() {
    int x = 5;
    int old_value = std::exchange_if_not(x, 3, should_exchange);
    std::cout << "Old value: " << old_value << std::endl;  // Output: Old value: 5
    std::cout << "New value: " << x << std::endl;          // Output: New value: 5
    return 0;
}
```

In the example above, the exchange does not occur because the `should_exchange` predicate returns false.

## Conclusion

`std::exchange` and `std::exchange_if_not` are powerful utilities for simplifying object value exchange, providing cleaner and more readable code. They promote code safety and clarity, making them valuable tools to have in your C++ toolkit.

References:
- [std::exchange (C++ reference)](https://en.cppreference.com/w/cpp/utility/exchange)
- [std::exchange_if_not (C++ reference)](https://en.cppreference.com/w/cpp/utility/exchange_if_not)