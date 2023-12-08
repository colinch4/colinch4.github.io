---
layout: post
title: "[c++] C++ 11 이상에서의 unordered_map과 unordered_set 사용법"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

C++ 11부터 표준 라이브러리는 unordered_map과 unordered_set을 지원합니다. 이들은 각각 해시 테이블을 기반으로 하는 맵과 집합 자료 구조를 제공하여 검색, 삽입, 삭제 등의 연산을 평균 O(1)의 시간 복잡도로 수행할 수 있습니다.

## unordered_map 사용법

unordered_map은 key-value 쌍을 저장하는 자료 구조입니다. 다음은 unordered_map을 사용하는 간단한 예제입니다.

```c++
#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> myMap;
    
    // 삽입
    myMap["apple"] = 5;
    myMap["banana"] = 3;
    
    // 조회
    std::cout << "apple: " << myMap["apple"] << std::endl;
    
    // 삭제
    myMap.erase("banana");
    
    return 0;
}
```

## unordered_set 사용법

unordered_set은 중복을 허용하지 않는 집합 자료 구조입니다. 다음은 unordered_set을 사용하는 간단한 예제입니다.

```c++
#include <iostream>
#include <unordered_set>

int main() {
    std::unordered_set<int> mySet;
    
    // 삽입
    mySet.insert(5);
    mySet.insert(3);
    
    // 조회
    if (mySet.find(5) != mySet.end()) {
        std::cout << "5 exists in the set" << std::endl;
    }
    
    // 삭제
    mySet.erase(3);
    
    return 0;
}
```

unordered_map과 unordered_set은 각각 해시 함수를 사용하여 요소를 저장하므로, **검색, 삽입, 삭제** 연산의 시간 복잡도가 **상수 시간**에 가깝습니다. 이를 통해 대용량 데이터에 대한 효율적인 처리가 가능해집니다.

이상으로 C++ 11 이상에서의 unordered_map과 unordered_set 사용법에 대해 알아보았습니다. 자세한 내용은 [C++ 공식 문서](https://en.cppreference.com/w/cpp/container/unordered_map)를 참고해주세요.