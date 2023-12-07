---
layout: post
title: "[c++] 가상 함수와 컴파일 타임 다형성(compile-time polymorphism)"
description: " "
date: 2023-12-07
tags: [c++]
comments: true
share: true
---

가상 함수는 하위 클래스에서 재정의(override)될 수 있는 멤버 함수입니다. 따라서 기본 클래스에서 정의된 가상 함수를 하위 클래스에서 다시 정의할 수 있으며, 이는 객체지향 프로그래밍의 다형성 원칙에 기반합니다.

한편 컴파일 타임 다형성은 실행 시간이 아닌 컴파일 시간에 결정되는 다형성을 의미합니다. 이는 템플릿 및 함수 오버로딩과 연관이 있으며, 컴파일러가 코드를 생성하는 시점에서 다양한 타입으로 동일한 코드를 처리할 수 있도록 합니다.

컴파일 타임 다형성을 구현하는 데 가장 일반적으로 사용되는 방법은 템플릿 메타프로그래밍(template metaprogramming)입니다. 템플릿을 사용하여 컴파일 시간에 다양한 타입을 처리하고 특화된 코드를 생성할 수 있습니다.

```c++
template <typename T>
T add(T a, T b) {
    return a + b;
}
```

위의 코드에서 `add` 함수는 템플릿을 사용하여 컴파일 타임 다형성을 구현하고 있습니다. 컴파일 타임에 `add<int>(3, 4)`는 `int` 타입에 대한 덧셈 함수로, `add<double>(3.5, 2.8)`은 `double` 타입에 대한 덧셈 함수로 특화됩니다.

참고문헌 :  
- Stroustrup, B. (2013). The C++ Programming Language, 4th Edition, Addison-Wesley.  
- Vandevoorde, D., & Josuttis, N. M. (2017). C++ Templates: The Complete Guide, 2nd Edition, Addison-Wesley.  
- Vandevoorde, D. (2002). C++ Solutions: Companion to the C++ Programming Language, Addison-Wesley.  
- https://en.cppreference.com/w/cpp/language/template_specialization