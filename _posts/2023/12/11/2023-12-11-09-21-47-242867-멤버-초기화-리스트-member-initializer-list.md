---
layout: post
title: "[c++] 멤버 초기화 리스트 (Member initializer list)"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

보통 생성자는 생성된 객체의 상태를 초기화하기 위해 사용됩니다. 멤버 초기화 리스트를 사용하면 생성자의 본문이 실행하기 전에 멤버 변수가 초기화되므로 효율적인 초기화가 가능합니다.

멤버 초기화 리스트는 다음과 같이 클래스 생성자의 선언 부분의 끝에 콜론(:) 다음에 멤버 변수의 초기화 목록을 포함하여 작성됩니다.

```c++
class MyClass {
public:
    int myInt;

    MyClass(int x) : myInt(x) {
        // 생성자 본문
    }
};
```

위 예제에서 `myInt`는 멤버 초기화 리스트를 사용해서 생성자에서 초기화되었습니다.

멤버 초기화 리스트를 사용하면 객체의 멤버 변수가 효율적으로 초기화되어 불필요한 작업이 줄어들고 안정성과 성능을 향상시킬 수 있습니다.

더 많은 정보를 원하시면 C++ 공식 문서를 참고하시기 바랍니다. [Member initializer list - C++ Reference](https://en.cppreference.com/w/cpp/language/initializer_list)