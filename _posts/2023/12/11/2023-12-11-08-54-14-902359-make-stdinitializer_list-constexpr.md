---
layout: post
title: "[c++] Make std::initializer_list constexpr"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

C++11부터 사용 가능한 `std::initializer_list`는 고정된 길이의 요소를 가진 초기화 목록을 나타내는데 사용됩니다. C++11 이후 C++에서 `constexpr`를 사용할 수 있게 되었지만, `std::initializer_list`의 요소를 `constexpr`로 만드는 것은 일반적으로 불가능했습니다. 그러나 C++20 이후로 `std::initializer_list`의 요소를 `constexpr`로 만들 수 있는 방법이 추가되었습니다.

## `std::initializer_list`의 요소를 `constexpr`로 만드는 방법

C++20에 추가된 변경을 통해 `std::initializer_list`의 요소를 `constexpr`로 만들기 위해 다음과 같이 사용할 수 있습니다.

```cpp
constexpr std::initializer_list<int> list = {1, 2, 3, 4, 5};
```

이것은 C++20에서 추가된 기능으로, 초기화 목록의 요소가 `constexpr`로 표시됩니다. 이제 `list`는 `constexpr`로 선언되는 것이 가능합니다.

## 예제

다음은 `std::initializer_list`의 요소를 `constexpr`로 만드는 예제입니다.

```cpp
#include <iostream>
#include <initializer_list>

int main() {
    constexpr std::initializer_list<int> list = {1, 2, 3, 4, 5};
    for (auto i : list) {
        std::cout << i << ' ';
    }
    return 0;
}
```

이 예제는 C++20에서 컴파일될 때 `list`가 `constexpr`로 선언된 것을 확인할 수 있습니다.

이제 C++20에서는 `std::initializer_list`의 요소를 `constexpr`로 만들어 사용할 수 있게 되었습니다.


### 참고 자료
- [cppreference - std::initializer_list](https://en.cppreference.com/w/cpp/utility/initializer_list)
- [cppreference - constexpr specifier](https://en.cppreference.com/w/cpp/language/constexpr)