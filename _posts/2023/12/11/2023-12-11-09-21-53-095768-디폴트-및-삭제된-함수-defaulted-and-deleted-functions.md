---
layout: post
title: "[c++] 디폴트 및 삭제된 함수 (Defaulted and deleted functions)"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

C++에서 디폴트 및 삭제된 함수(defaulted and deleted functions)는 클래스 멤버 함수의 특별한 형태를 말합니다. 이러한 함수들은 클래스의 기본 동작을 수정하고 클래스의 행동을 명확하게 지정하는 데 유용합니다.

## 디폴트 함수(Default Functions)

디폴트 함수는 명시적으로 정의되지 않은 멤버 함수를 가리킵니다. 즉, 컴파일러가 자동으로 그 함수를 생성합니다. 주로 디폴트 생성자, 복사 생성자, 이동 생성자, 복사 할당 연산자, 이동 할당 연산자가 있습니다.

```cpp
class MyClass {
public:
    MyClass() = default;  // 디폴트 생성자
    MyClass(const MyClass&) = default;  // 복사 생성자
    MyClass(MyClass&&) = default;  // 이동 생성자
    MyClass& operator=(const MyClass&) = default;  // 복사 할당 연산자
    MyClass& operator=(MyClass&&) = default;  // 이동 할당 연산자
};
```

위와 같이 `= default`를 사용하여 디폴트 함수를 명시할 수 있습니다. 

## 삭제된 함수(Deleted Functions)

삭제된 함수는 호출을 제한하는 데 쓰입니다. 특정 함수를 사용할 수 없도록 하려는 경우에 삭제된 함수를 사용할 수 있습니다.

```cpp
class MyClass {
public: 
    void doSomething() = delete;  // doSomething 함수의 사용을 삭제
};
```

위와 같이 `= delete`를 사용하여 함수를 삭제할 수 있습니다.

이러한 디폴트 및 삭제된 함수는 C++11부터 도입되었으며, 코드의 가독성과 유지 보수성을 향상시키는 데 도움을 줍니다.

디폴트 및 삭제된 함수에 대한 자세한 내용은 [cppreference](https://en.cppreference.com/w/)에서 참고할 수 있습니다.