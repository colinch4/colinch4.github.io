---
layout: post
title: "[c++] 정적 다형성(static polymorphism)과 동적 다형성(dynamic polymorphism)"
description: " "
date: 2023-12-07
tags: [c++]
comments: true
share: true
---

## 정적 다형성(static polymorphism)

정적 다형성은 컴파일 타임에 결정되는 다형성으로, **템플릿(template)과 오버로딩(overloading)**에 의해 구현됩니다. 템플릿은 컴파일 타임에 **특정 타입에 대해 코드를 생성**하므로, 각각의 다른 타입에 대해 특화된 코드를 생성할 수 있습니다. 오버로딩은 **함수의 이름을 동일하게 사용**하면서 매개변수의 타입 또는 개수를 다르게 함으로써 **여러 버전의 함수를 정의**할 수 있습니다. 컴파일러는 컴파일 타임에 이러한 정보를 바탕으로 함수 호출을 해석하고, **적절한 버전의 함수를 선택**합니다.

```cpp
// 템플릿을 사용한 정적 다형성의 예
template <typename T>
T add(T a, T b) {
    return a + b;
}
```

## 동적 다형성(dynamic polymorphism)

동적 다형성은 **런타임에 결정되는 다형성**으로, **가상 함수(virtual function)**와 **상속(inheritance)**에 의해 구현됩니다. 클래스들 간의 계층 구조를 만들고, 부모 클래스의 포인터나 참조를 사용하여 여러 타입의 객체를 동일하게 다룰 수 있습니다. 런타임에 객체의 실제 타입을 확인하고, 이에 맞는 가상 함수를 호출합니다.

```cpp
// 상속과 가상 함수를 사용한 동적 다형성의 예
class Animal {
public:
    virtual void makeSound() {
        std::cout << "Animal sound" << std::endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "Bark" << std::endl;
    }
};
```

정적 다형성과 동적 다형성은 각각 템플릿과 상속을 기반으로 하여 다른 시점에 다른 타입의 다형성을 구현합니다. 이러한 다형성을 적절히 활용하여 프로그램의 유연성을 높일 수 있습니다.

### 참고 자료
- [cplusplus.com - Polymorphism](https://www.cplusplus.com/doc/tutorial/polymorphism/)
- [GeeksforGeeks - Static and Dynamic Polymorphism in C++](https://www.geeksforgeeks.org/static-and-dynamic-polymorphism-in-cpp/)