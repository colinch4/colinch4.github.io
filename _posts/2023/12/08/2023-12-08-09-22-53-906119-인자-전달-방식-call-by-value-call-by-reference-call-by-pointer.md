---
layout: post
title: "[c++] 인자 전달 방식 (call by value, call by reference, call by pointer)"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

프로그래밍 언어에서 함수에 값을 전달하는 방식은 크게 세 가지가 있습니다. 이 글에서는 C++ 언어의 함수에서 사용되는 **인자 전달 방식**에 대해 설명하겠습니다.

## Call by Value (값에 의한 호출)

**Call by Value**는 함수에 인자를 전달할 때, 해당 인자의 값만을 복사하여 전달하는 방식입니다. 즉, 함수 내에서 전달된 값의 변경이 있더라도 호출자에 영향을 미치지 않는다는 특징이 있습니다.

```c++
void changeValue(int x) {
    x = 10;
}

int main() {
    int num = 5;
    changeValue(num);
    // 여전히 num은 5입니다.
}
```

## Call by Reference (참조에 의한 호출)

**Call by Reference**는 함수에 변수의 참조(주소)를 전달하여, 함수 내에서 해당 참조를 통해 변수의 값을 변경할 수 있는 방식입니다.

```c++
void changeValue(int& x) {
    x = 10;
}

int main() {
    int num = 5;
    changeValue(num);
    // num은 이제 10입니다.
}
```

## Call by Pointer (포인터에 의한 호출)

**Call by Pointer**는 함수에 변수의 주소(포인터)를 전달하여, 함수 내에서 해당 주소를 통해 변수의 값을 변경할 수 있는 방식입니다.

```c++
void changeValue(int* x) {
    *x = 10;
}

int main() {
    int num = 5;
    changeValue(&num);
    // num은 이제 10입니다.
}
```

각각의 인자 전달 방식에는 장단점과 사용 시 주의할 점이 있으므로, 상황에 맞게 적절히 선택하여 사용해야 합니다.

## 참고 자료

- [C++ Reference - Function parameters](https://en.cppreference.com/w/cpp/language/parameters)