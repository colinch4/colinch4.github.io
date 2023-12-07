---
layout: post
title: "[c++] RAII(Resource Acquisition Is Initialization) 패턴과 예외 처리"
description: " "
date: 2023-12-07
tags: [c++]
comments: true
share: true
---

RAII(Resource Acquisition Is Initialization) 패턴은 C++에서 자원을 획득(Acquire)하고 초기화(Initialization)하는 것을 객체의 생성자에서 처리하고, 자원을 해제(Release)하는 것을 소멸자에서 처리함으로써, 자원 누출이나 메모리 누수 등을 방지하는 프로그래밍 패턴입니다.

이 디자인 패턴은 자원을 획득할 때 예외가 발생하여도 안전하게 자원을 해제할 수 있도록 보장하며, 코드를 간결하게 유지할 수 있습니다. 주요 사용 사례는 파일 핸들, 뮤텍스, 소켓과 같은 시스템 리소스 및 메모리 할당과 관련된 자원들을 관리하는 데 사용됩니다.

## RAII 패턴 예제

다음은 파일을 다루는 예제 코드입니다.

```c++
#include <iostream>
#include <fstream>
#include <stdexcept>

class File {
public:
    File(const std::string& filename) : m_file(filename) {
        if (!m_file.is_open()) {
            throw std::runtime_error("File open failed");
        }
    }

    ~File() {
        if (m_file.is_open()) {
            m_file.close();
        }
    }

    void write(const std::string& data) {
        if (m_file.is_open()) {
            m_file << data;
        } else {
            throw std::runtime_error("File is not open");
        }
    }

private:
    std::ofstream m_file;
};

int main() {
    try {
        File file("example.txt");
        file.write("Hello, RAII pattern!");
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
}
```

위 예제는 RAII 패턴을 사용하여 파일 핸들을 안전하게 다루는 예시입니다. 파일 핸들을 생성자에서 획득하고, 소멸자에서 안전하게 파일을 닫습니다.

RAII 패턴을 사용하면 자원의 획득과 해제를 객체의 생명주기에 따라 자동으로 처리함으로써, 코드의 가독성과 안정성을 높일 수 있습니다.

## RAII 패턴과 예외 처리

RAII 패턴은 예외 처리와도 밀접한 관련이 있습니다. RAII 객체의 소멸자가 자원을 해제하므로, 예외가 발생하여도 소멸자가 호출되어 자원을 안전하게 해제할 수 있습니다. 이를 통해 메모리 누수와 같은 문제를 방지할 수 있습니다.

예를 들어, RAII를 사용하지 않고 리소스를 수동으로 할당하고 예외가 발생할 경우 리소스를 해제하지 않는다면, 메모리 누수가 발생하게 됩니다. 하지만 RAII 패턴을 사용하면 이러한 문제를 방지할 수 있습니다.

RAII 패턴을 사용하면 코드 중복을 피하고 예외 안전성을 보장하는 동시에 가독성을 향상시킬 수 있습니다.

RAII 패턴은 C++에서 자원 관리를 간소화하고 안전성을 높이는 강력한 도구입니다.

## 참고 자료
- https://en.cppreference.com/w/cpp/language/raii"RAII (Resource Acquisition Is Initialization)"
- https://www.geeksforgeeks.org/raii-in-c/"RAII in C++"
- https://www.learncpp.com/cpp-tutorial/10-2-b-resource-management-with-classes-using-raii/"Resource Management with Classes: RAII"