---
layout: post
title: "[c++] Delegating constructors"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

### 생성자 위임 예시
다음은 생성자 위임을 사용한 간단한 예시입니다.

```c++
#include <iostream>

class MyClass {
public:
    MyClass() : MyClass(0) {}
    MyClass(int value) : m_value(value) {}
    
    int getValue() const { return m_value; }
    
private:
    int m_value;
};

int main() {
    MyClass obj1;
    MyClass obj2(10);
    
    std::cout << obj1.getValue() << std::endl;  // 출력: 0
    std::cout << obj2.getValue() << std::endl;  // 출력: 10
    
    return 0;
}
```

위 예시에서, `MyClass`의 디폴트 생성자는 매개변수를 가진 생성자를 호출하여 중복 코드를 방지합니다. 이를 통해 코드를 간결하게 유지할 수 있습니다.

### 생성자 위임의 장점
- 중복 코드를 제거하여 유지보수와 가독성을 향상시킵니다.
- 새로운 생성자를 추가할 때 기존 생성자를 재활용할 수 있습니다.

생성자 위임은 C++에서 코드를 더 간결하고 유연하게 만드는 데 유용한 기능입니다. 관련 자세한 내용은 "Effective Modern C++"과 같은 C++ 책을 참고하시기 바랍니다.