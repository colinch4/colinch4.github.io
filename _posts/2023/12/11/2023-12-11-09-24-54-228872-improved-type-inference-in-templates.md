---
layout: post
title: "[c++] Improved type inference in templates"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

C++17부터는 템플릿에서의 타입 추론이 향상되었습니다. 이를 통해 코드를 더 간결하게 작성할 수 있으며, 에러 발생 가능성을 줄일 수 있습니다.

## 이전 방식

이전에는 템플릿 함수를 사용할 때, 타입을 명시적으로 지정해 주어야 했습니다. 이는 코드를 불필요하게 길게 만들고, 유지보수에 어려움을 초래할 수 있었습니다.

```c++
template <typename T, typename U>
void foo(T t, U u) {
    // 함수 내용
}

int main() {
    foo<int, double>(5, 3.14);
}
```

## C++17에서의 개선

C++17부터는 `auto` 키워드를 통해 함수 호출 시 타입을 추론할 수 있습니다. 이로써 코드가 간결해지고, 실수를 줄일 수 있습니다.

```c++
template <typename T, typename U>
void foo(T t, U u) {
    // 함수 내용
}

int main() {
    foo(5, 3.14);  // 타입 추론을 통해 간결하게 호출
}
```

이러한 변경으로 인해 코드의 가독성과 유지보수성이 향상되었습니다.

## 결론

C++17에서의 템플릿에서의 향상된 타입 추론은 코드 작성을 더 편리하고 안전하게 만들어 주었습니다. 기존 방식에 비해 간결하고 명확한 코드를 작성할 수 있으므로, 이를 적극적으로 활용하는 것이 좋습니다.

## 참고 자료

- [C++17 - Improved Type Inference for Templates](https://en.cppreference.com/w/cpp/language/decltype)