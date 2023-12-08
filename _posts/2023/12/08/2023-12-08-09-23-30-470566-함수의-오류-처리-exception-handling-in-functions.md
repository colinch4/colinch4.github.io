---
layout: post
title: "[c++] 함수의 오류 처리 (exception handling in functions)"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

C++에서 함수를 작성할 때, 예외 상황을 처리하는 것은 매우 중요합니다. 함수 내에서 예외가 발생할 경우 이를 적절하게 처리하는 것이 프로그램의 안정성을 높이고, 사용자 경험을 향상시킵니다.

## 예외 처리란 무엇인가?

예외 처리는 프로그램 실행 중에 예기치 않은 상황이 발생했을 때, 이를 적절하게 처리하는 것을 말합니다. 이는 프로그램이 비정상적으로 종료되는 것을 방지하고, 오류에 대한 메시지를 출력하여 디버깅을 용이하게 하기 위한 것입니다.

## C++에서의 예외 처리

C++에서는 예외 처리를 위해 `try`, `catch`, `throw` 키워드를 제공합니다. 

예를 들어, 다음은 `divide`라는 함수에서 나눗셈 연산을 수행하고, 예외가 발생할 경우 이를 처리하는 코드입니다.

```c++
#include <iostream>
using namespace std;

double divide(int numerator, int denominator) {
    try {
        if (denominator == 0) {
            throw "Division by zero error";
        }
        return static_cast<double>(numerator) / denominator;
    } catch (const char* message) {
        cerr << "Error: " << message << endl;
        return 0;
    }
}

int main() {
    int a = 10, b = 0;
    cout << "Result: " << divide(a, b) << endl;
    return 0;
}
```

위의 코드에서 `try` 블록 내에서 예외가 발생하면 `throw` 키워드를 사용하여 예외를 발생시키고, 이를 `catch` 블록에서 적절하게 처리합니다.

## 함수에서의 예외 처리

함수에서도 예외를 처리할 수 있습니다. 함수에서 발생한 예외는 호출자에게 전파될 수 있으며, 호출자에서 이를 처리할 수 있습니다.

예를 들어, 다음은 함수에서 발생한 예외를 호출자에서 처리하는 코드입니다.

```c++
#include <iostream>
using namespace std;

void processFile() {
    // 파일 처리하는 코드
    if (errorCondition) {
        throw runtime_error("File processing error");
    }
}

int main() {
    try {
        processFile();
    } catch (const runtime_error& e) {
        cerr << "Error: " << e.what() << endl;
    }
    return 0;
}
```

위의 코드에서 `processFile` 함수에서 발생한 예외가 `main` 함수에서 `catch` 블록을 통해 처리되고 있음을 볼 수 있습니다.

알맞은 예외 처리를 통해 C++ 함수에서 발생하는 예외 상황을 유연하게 처리할 수 있습니다. 이는 안정성을 높이고, 코드의 가독성을 개선하여 유지 보수를 용이하게 합니다.

## 결론

C++에서 함수의 예외 처리는 프로그램의 안정성과 신뢰성을 높이는 데 중요한 역할을 합니다. 적절한 예외 처리를 통해 프로그램의 안정성을 높여보세요.

참고 문헌:
- https://www.learncpp.com/cpp-tutorial/15-exception-handling/
- https://en.cppreference.com/w/cpp/language/try_catch